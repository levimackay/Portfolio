// The WASI preview1 calls izvor.wasm imports, and nothing else (checked with
// WebAssembly.Module.imports): args, stdin from a string, stdout and stderr
// handed to a callback, a clock, and exit. There is no file system, because
// the browser driver reads its program from stdin.
const encoder = new TextEncoder();

const EBADF = 8;
const ESPIPE = 70;

export class Exit {
  constructor(code) {
    this.code = code;
  }
}

export function createWasi(args, input, write) {
  const argv = args.map((arg) => encoder.encode(`${arg}\0`));
  const stdin = encoder.encode(input);
  let offset = 0;
  let memory;

  const view = () => new DataView(memory.buffer);
  const bytes = (address, length) => new Uint8Array(memory.buffer, address, length);

  // Calls fn on each buffer of an iovec array and adds up what it returns.
  function eachIov(iovs, count, fn) {
    const data = view();
    let total = 0;
    for (let i = 0; i < count; i++) {
      total += fn(
        bytes(data.getUint32(iovs + i * 8, true), data.getUint32(iovs + i * 8 + 4, true))
      );
    }
    return total;
  }

  const imports = {
    args_sizes_get(countOut, sizeOut) {
      const data = view();
      data.setUint32(countOut, argv.length, true);
      data.setUint32(
        sizeOut,
        argv.reduce((sum, arg) => sum + arg.length, 0),
        true
      );
      return 0;
    },
    args_get(pointers, buffer) {
      const data = view();
      for (const arg of argv) {
        data.setUint32(pointers, buffer, true);
        bytes(buffer, arg.length).set(arg);
        pointers += 4;
        buffer += arg.length;
      }
      return 0;
    },
    clock_time_get(_id, _precision, out) {
      view().setBigUint64(
        out,
        BigInt(Math.round((performance.timeOrigin + performance.now()) * 1e6)),
        true
      );
      return 0;
    },
    // The three standard streams look like a terminal: a character device
    // that cannot seek. wasi-libc then line-buffers stdout the way a
    // terminal would, so output printed before a crash is not lost.
    fd_fdstat_get(fd, out) {
      if (fd > 2) return EBADF;
      bytes(out, 24).fill(0);
      const data = view();
      data.setUint8(out, 2);
      data.setBigUint64(out + 8, 0x42n, true);
      return 0;
    },
    fd_read(fd, iovs, count, readOut) {
      if (fd !== 0) return EBADF;
      const read = eachIov(iovs, count, (target) => {
        const chunk = stdin.subarray(offset, offset + target.length);
        target.set(chunk);
        offset += chunk.length;
        return chunk.length;
      });
      view().setUint32(readOut, read, true);
      return 0;
    },
    fd_write(fd, iovs, count, writtenOut) {
      if (fd !== 1 && fd !== 2) return EBADF;
      const written = eachIov(iovs, count, (chunk) => {
        write(fd, chunk);
        return chunk.length;
      });
      view().setUint32(writtenOut, written, true);
      return 0;
    },
    fd_seek: () => ESPIPE,
    fd_close: () => 0,
    proc_exit(code) {
      throw new Exit(code);
    },
  };

  return {
    imports: { wasi_snapshot_preview1: imports },
    // Runs the module's _start and returns its exit status. Traps, such as
    // running out of stack, are thrown to the caller.
    start(instance) {
      memory = instance.exports.memory;
      try {
        instance.exports._start();
        return 0;
      } catch (error) {
        if (error instanceof Exit) return error.code;
        throw error;
      }
    },
  };
}
