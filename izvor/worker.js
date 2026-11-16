// Runs izvor.wasm off the main thread, one request at a time. The module is
// compiled here, once per worker, so the page itself never compiles
// WebAssembly. Every request gets a fresh instance, so nothing one program
// leaves in memory can reach the next.
import { createWasi } from "./wasi.js";

// Characters kept per stream; a program that prints forever is cut off here.
const LIMIT = 1 << 20;
// Output is posted on every write until this much has gone to the page, then
// in batches of it. Nothing can run in the worker while the program does, so
// a time-based batch would lose whatever came just before a silent loop the
// page then stops; only a long run of output pays the batching.
const BATCH = 1 << 14;

let module;
const loaded = fetch(new URL("./izvor.wasm", import.meta.url))
  .then((response) => {
    if (!response.ok) throw new Error(`izvor.wasm returned HTTP ${response.status}`);
    return response.arrayBuffer();
  })
  .then((bytes) => WebAssembly.compile(bytes))
  .then(
    (compiled) => {
      module = compiled;
      postMessage({ type: "ready" });
    },
    (error) => postMessage({ type: "fail", message: error.message || String(error) })
  );

// Requests wait for the module, then each one runs start to finish without
// yielding, so two programs can never interleave.
onmessage = async ({ data }) => {
  await loaded;
  if (module) handle(data);
};

function handle({ id, mode, source }) {
  const decoders = [null, new TextDecoder(), new TextDecoder()];
  const pending = ["", "", ""];
  const kept = [0, 0, 0];
  let truncated = false;
  let sent = 0;

  // Output goes to the page while the program runs, so a run the page has to
  // stop still shows everything it printed before it went quiet.
  const flush = (extra) => {
    sent += pending[1].length + pending[2].length;
    postMessage({ id, out: pending[1], err: pending[2], ...extra });
    pending[1] = pending[2] = "";
  };

  const wasi = createWasi(["izvor", mode, "playground.iz"], source, (fd, bytes) => {
    if (kept[fd] >= LIMIT) {
      if (!truncated) flush();
      truncated = true;
      return;
    }
    const text = decoders[fd].decode(bytes, { stream: true });
    kept[fd] += text.length;
    pending[fd] += text;
    if (sent < BATCH || pending[1].length + pending[2].length >= BATCH) flush();
  });

  let code = 1;
  let trap = null;
  let ms = 0;
  try {
    const instance = new WebAssembly.Instance(module, wasi.imports);
    const started = performance.now();
    try {
      code = wasi.start(instance);
    } finally {
      ms = performance.now() - started;
    }
  } catch (error) {
    trap = { name: error.name, message: error.message };
  }
  pending[1] += decoders[1].decode();
  pending[2] += decoders[2].decode();
  flush({ done: true, code, trap, ms, truncated });
}
