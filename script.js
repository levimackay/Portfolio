// ---------- QA hook: ?still freezes entrance animations ----------
if (new URLSearchParams(location.search).has('still')) {
  const s = document.createElement('style');
  s.textContent = '.rise{animation:none!important;opacity:1!important;transform:none!important}' +
    '.reveal{opacity:1!important;transform:none!important;transition:none!important}';
  document.head.appendChild(s);
}

// ---------- Footer year ----------
document.getElementById('year').textContent = new Date().getFullYear();

// ---------- Mobile nav ----------
const navToggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('nav');

navToggle.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', open);
});

nav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    nav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

// ---------- Scroll reveal ----------
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);

document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

// ---------- Animated stat counters ----------
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const counterObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      counterObserver.unobserve(entry.target);

      const el = entry.target;
      const target = parseFloat(el.dataset.count);
      const decimals = parseInt(el.dataset.decimals || '0', 10);

      if (reduceMotion) {
        el.textContent = target.toFixed(decimals);
        return;
      }

      const duration = 1400;
      const start = performance.now();
      const tick = (now) => {
        const t = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - t, 3);
        el.textContent = (target * eased).toFixed(decimals);
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  },
  { threshold: 0.6 }
);

document.querySelectorAll('[data-count]').forEach((el) => counterObserver.observe(el));

// ---------- 3D tilt on project media (desktop, pointer devices) ----------
if (window.matchMedia('(hover: hover)').matches && !reduceMotion) {
  document.querySelectorAll('.project-media').forEach((media) => {
    media.closest('.project').addEventListener('mousemove', (e) => {
      const rect = media.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      media.style.transform =
        `perspective(1000px) rotateX(${(-y * 4).toFixed(2)}deg) rotateY(${(x * 5).toFixed(2)}deg) translateY(-3px)`;
    });
    media.closest('.project').addEventListener('mouseleave', () => {
      media.style.transform = '';
    });
  });
}

// ---------- Copy email to clipboard ----------
const toast = document.querySelector('.toast');

document.querySelectorAll('[data-copy-email]').forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    const email = el.href.replace('mailto:', '');
    navigator.clipboard.writeText(email).then(() => {
      toast.classList.add('active');
      setTimeout(() => toast.classList.remove('active'), 2000);
    });
  });
});

// ---------- Terminal easter egg ----------
const terminal = document.getElementById('terminal');
const terminalOpen = document.getElementById('terminal-open');
const terminalClose = document.getElementById('terminal-close');
const terminalInput = document.getElementById('terminal-input');
const terminalOutput = document.getElementById('terminal-output');

const commands = {
  help: "Available commands: whoami, bio, projects, contact, ls, clear",
  ls: "bio.txt  projects/  contact.key",
  whoami: "Levi Mackay — CS student, TA, startup builder, problem solver.",
  bio: "4.0 GPA at BYU–Idaho. From plowing fields as a farm hand to building AI tools in the Sandbox incubator. Ski lift operator, landscape foreman, IT specialist. I build stuff that works.",
  projects: "1. SwingOS — real-time swing analysis (OpenCV + MediaPipe)\n2. AI Security Scanner — Gemini-powered vulnerability detection\n3. Foreman's Friend — job-site estimation CLI\n4. Baseball Analytics Engine — MySQL schema + advanced queries",
  contact: "email: levibmackay@gmail.com\nlinkedin: linkedin.com/in/levi-mackay-217380396",
};

function openTerminal() {
  terminal.hidden = false;
  terminalInput.focus();
}

function closeTerminal() {
  terminal.hidden = true;
}

terminalOpen.addEventListener('click', openTerminal);
terminalClose.addEventListener('click', closeTerminal);

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeTerminal();
  // Press "t" anywhere (outside an input) to open the terminal
  if (
    e.key.toLowerCase() === 't' &&
    !e.metaKey && !e.ctrlKey && !e.altKey &&
    document.activeElement.tagName !== 'INPUT' &&
    document.activeElement.tagName !== 'TEXTAREA'
  ) {
    e.preventDefault();
    openTerminal();
  }
});

terminalInput.addEventListener('keydown', (e) => {
  if (e.key !== 'Enter') return;

  const input = terminalInput.value.toLowerCase().trim();
  terminalInput.value = '';
  if (!input) return;

  if (input === 'clear') {
    terminalOutput.innerHTML = '';
    return;
  }

  const response = commands[input] || `command not found: ${input} — type 'help' for options.`;
  const row = document.createElement('div');

  const prompt = document.createElement('span');
  prompt.className = 't-hl';
  prompt.textContent = `> ${input}`;
  row.appendChild(prompt);
  row.appendChild(document.createElement('br'));
  row.appendChild(document.createTextNode(response));

  terminalOutput.appendChild(row);
  terminalOutput.scrollTop = terminalOutput.scrollHeight;
});
