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

// ---------- Scroll reveal (fades back out when scrolled past in either direction) ----------
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      entry.target.classList.toggle('visible', entry.isIntersecting);
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

// ---------- Pause offscreen video (avoid decoding it for the whole scroll session) ----------
const projectVideos = document.querySelectorAll('.project-media video');
if (projectVideos.length) {
  const videoObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const v = entry.target;
        if (entry.isIntersecting) v.play().catch(() => {});
        else v.pause();
      });
    },
    { threshold: 0.1 }
  );
  projectVideos.forEach((v) => videoObserver.observe(v));
}

// ---------- Scroll progress + media parallax ----------
const progressBar = document.querySelector('.scroll-progress');
const canHover = window.matchMedia('(hover: hover)').matches;

const parallaxTargets = [];
if (canHover && !reduceMotion) {
  document.querySelectorAll('.project-media:not(.media-tile)').forEach((m) => {
    const el = m.querySelector('img, video');
    if (el) {
      el.style.transform = 'scale(1.1)';
      parallaxTargets.push(el);
    }
  });
}

let scrollTicking = false;
function onScroll() {
  if (scrollTicking) return;
  scrollTicking = true;
  requestAnimationFrame(() => {
    scrollTicking = false;
    const doc = document.documentElement;
    const max = doc.scrollHeight - doc.clientHeight;
    progressBar.style.width = (max ? (window.scrollY / max) * 100 : 0) + '%';

    const mid = window.innerHeight / 2;
    parallaxTargets.forEach((el) => {
      const r = el.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return;
      const offset = (r.top + r.height / 2 - mid) / mid; // -1 … 1
      el.style.transform = `scale(1.1) translateY(${(-offset * 16).toFixed(1)}px)`;
    });
  });
}
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// ---------- Nav scrollspy ----------
const spy = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      document.querySelectorAll('.nav a').forEach((a) => {
        a.classList.toggle('active', a.getAttribute('href') === '#' + entry.target.id);
      });
    });
  },
  { rootMargin: '-40% 0px -55% 0px' }
);
['about', 'projects', 'skills', 'contact'].forEach((id) => {
  const el = document.getElementById(id);
  if (el) spy.observe(el);
});

// ---------- Magnetic buttons ----------
if (canHover && !reduceMotion) {
  document.querySelectorAll('.btn, .terminal-toggle').forEach((el) => {
    el.addEventListener('mousemove', (e) => {
      const r = el.getBoundingClientRect();
      const x = e.clientX - r.left - r.width / 2;
      const y = e.clientY - r.top - r.height / 2;
      el.style.transform = `translate(${(x * 0.18).toFixed(1)}px, ${(y * 0.28).toFixed(1)}px)`;
    });
    el.addEventListener('mouseleave', () => {
      el.style.transform = '';
    });
  });
}

// ---------- Border glow cards (ported from React Bits' BorderGlow) ----------
// Pointer position near a card's edge lights a conic-masked gradient border,
// a soft fill, and an outer glow aimed at the cursor. All visuals live in CSS;
// this just feeds --cursor-angle and --edge-proximity per card.
const glowCards = document.querySelectorAll('.glow-card');

glowCards.forEach((card) => {
  const light = document.createElement('span');
  light.className = 'edge-light';
  card.prepend(light);
});

// Each --cursor-angle/--edge-proximity write forces the browser to repaint
// the card's layered gradient/mask background, which is expensive. Capping
// writes to ~30fps (instead of every pointermove event or every animation
// frame) keeps the effect visually smooth while cutting that repaint cost
// roughly in half to a third.
const GLOW_FRAME_MS = 32;

if (canHover) {
  glowCards.forEach((card) => {
    // The contact card is far larger than any other glow-card (~6-8x the
    // paint area), so per-pixel cursor tracking there was the actual source
    // of the page-wide hover lag. It gets a fixed-angle CSS-only :hover
    // glow instead (see styles.css) — same "wakes up" feel, no JS.
    if (card.classList.contains('contact-card')) return;

    let lastPaint = 0;
    card.addEventListener('pointermove', (e) => {
      const now = performance.now();
      if (now - lastPaint < GLOW_FRAME_MS) return;
      lastPaint = now;

      const r = card.getBoundingClientRect();
      const cx = r.width / 2;
      const cy = r.height / 2;
      const dx = e.clientX - r.left - cx;
      const dy = e.clientY - r.top - cy;
      const kx = dx === 0 ? Infinity : cx / Math.abs(dx);
      const ky = dy === 0 ? Infinity : cy / Math.abs(dy);
      const edge = Math.min(Math.max(1 / Math.min(kx, ky), 0), 1);
      let angle = Math.atan2(dy, dx) * (180 / Math.PI) + 90;
      if (angle < 0) angle += 360;
      card.style.setProperty('--edge-proximity', (edge * 100).toFixed(2));
      card.style.setProperty('--cursor-angle', angle.toFixed(2) + 'deg');
    });
  });
}

// Intro flourish: the contact card's border glows once when it first appears.
// This used to be a ~4s JS-driven sweep that rewrote --cursor-angle every
// animation frame — each write forced a repaint of the card's layered
// gradient/mask background, which measured at ~120ms per frame (worse than
// 8fps) and was the actual source of the whole-page jank. A single class
// toggle lets the existing CSS opacity transition (cheap, two paints total)
// do the same "the border wakes up" effect instead.
function glowSweep(card) {
  card.style.setProperty('--cursor-angle', '135deg');
  card.style.setProperty('--edge-proximity', '100');
  card.classList.add('sweep-active');
  setTimeout(() => card.classList.remove('sweep-active'), 2200);
}

if (!reduceMotion) {
  const contactCard = document.querySelector('.contact-card');
  if (contactCard) {
    const sweepObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          sweepObserver.unobserve(entry.target);
          setTimeout(() => glowSweep(entry.target), 350);
        });
      },
      { threshold: 0.5 }
    );
    sweepObserver.observe(contactCard);
  }
}

// ---------- Blur-in headings (React Bits BlurText style) ----------
if (!reduceMotion) {
  document.querySelectorAll('main h2').forEach((h) => {
    const nodes = Array.from(h.childNodes);
    let wordIndex = 0;
    h.textContent = '';
    nodes.forEach((node) => {
      if (node.nodeType !== Node.TEXT_NODE) {
        h.appendChild(node);
        return;
      }
      node.textContent.split(/(\s+)/).forEach((part) => {
        if (!part) return;
        if (/^\s+$/.test(part)) {
          h.appendChild(document.createTextNode(part));
          return;
        }
        const span = document.createElement('span');
        span.className = 'blur-word';
        span.style.setProperty('--wd', wordIndex++ * 70 + 'ms');
        span.textContent = part;
        h.appendChild(span);
      });
    });
  });

  const blurObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        entry.target.classList.toggle('blur-in', entry.isIntersecting);
      });
    },
    { threshold: 0.5 }
  );
  document.querySelectorAll('main h2').forEach((h) => blurObserver.observe(h));
}

// QA hook: ?glow forces every glow card fully lit
if (new URLSearchParams(location.search).has('glow')) {
  glowCards.forEach((card) => {
    card.classList.add('sweep-active');
    card.style.setProperty('--edge-proximity', '100');
    card.style.setProperty('--cursor-angle', '135deg');
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
const terminalToggle = document.getElementById('terminal-toggle');
const terminalClose = document.getElementById('terminal-close');
const terminalInput = document.getElementById('terminal-input');
const terminalOutput = document.getElementById('terminal-output');

// Time-aware greeting
const hour = new Date().getHours();
const greeting = hour < 5 ? 'Burning the midnight oil?' : hour < 12 ? 'Good morning.' : hour < 18 ? 'Good afternoon.' : 'Good evening.';
document.getElementById('terminal-welcome').innerHTML =
  greeting + " Type <span class='t-hl'>help</span> to see available commands.";

const commands = {
  help: "Available commands:\n  whoami     who am I\n  bio        the longer story\n  projects   what I've built\n  skills     the stack\n  contact    how to reach me\n  explode    replay the hero animation\n  ls         look around\n  clear      wipe the screen",
  ls: "bio.txt  projects/  skills.json  contact.key  secret_plans.enc",
  whoami: "Levi Mackay — CS student, TA, startup builder, problem solver.",
  bio: "4.0 GPA at BYU–Idaho. From plowing fields as a farm hand to building AI tools in the Sandbox incubator. Ski lift operator, landscape foreman, IT specialist. Two years in the Balkans. I build stuff that works.",
  projects: "1. SwingOS — real-time swing analysis (OpenCV + MediaPipe)\n2. AI Security Scanner — Gemini-powered vulnerability detection\n3. Foreman's Friend — job-site estimation CLI\n4. Baseball Analytics Engine — MySQL schema + advanced queries",
  skills: "languages: [Python, JavaScript, SQL, C++]\ntools: [Git, Linux, Docker]\nfocus: [AI & automation, computer vision, database design]\nhuman: [English, Bosnian, Croatian, Serbian]",
  contact: "email: levibmackay@gmail.com\nlinkedin: linkedin.com/in/levi-mackay-217380396",
  sudo: "Permission denied. Nice try though.",
  'secret_plans.enc': "Decryption failed. Some things you have to build first.",
  explode: () => {
    closeTerminal();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(() => { if (window.__replayIntro) window.__replayIntro(); }, 500);
    return "Boom. Rebuilding the sphere…";
  },
};

// Typewriter output
function typeOut(text) {
  const row = document.createElement('div');
  terminalOutput.appendChild(row);
  if (reduceMotion) {
    row.textContent = text;
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
    return;
  }
  let i = 0;
  (function step() {
    i += 2;
    row.textContent = text.slice(0, i);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
    if (i < text.length) setTimeout(step, 8);
  })();
}

function openTerminal() {
  terminal.hidden = false;
  terminalInput.focus();
}

function closeTerminal() {
  terminal.hidden = true;
}

terminalOpen.addEventListener('click', openTerminal);
terminalToggle.addEventListener('click', openTerminal);
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

  const cmd = commands[input];
  const response = typeof cmd === 'function' ? cmd() : cmd || `command not found: ${input} — type 'help' for options.`;

  const echo = document.createElement('div');
  const prompt = document.createElement('span');
  prompt.className = 't-hl';
  prompt.textContent = `> ${input}`;
  echo.appendChild(prompt);
  terminalOutput.appendChild(echo);

  typeOut(response);
});
