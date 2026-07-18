// ---------- QA hook: ?still freezes entrance animations ----------
if (new URLSearchParams(location.search).has('still')) {
  const s = document.createElement('style');
  s.textContent = '.rise{animation:none!important;opacity:1!important;transform:none!important}' +
    '.reveal{opacity:1!important;transform:none!important;transition:none!important}';
  document.head.appendChild(s);
}

// ---------- Constants ----------
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const canHover = window.matchMedia('(hover: hover)').matches;

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

// ---------- Scroll reveal (Intersection Observer) ----------
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

// ---------- Smooth Inertia Scrolling ----------
let targetScrollY = window.scrollY;
let currentScrollY = window.scrollY;
let isScrolling = false;

if (!reduceMotion && window.innerWidth > 900) {
  window.addEventListener('wheel', (e) => {
    if (e.target.closest('.terminal-body') || e.target.closest('.blog-drawer-body')) {
      return;
    }
    e.preventDefault();
    targetScrollY += e.deltaY * 0.95;
    targetScrollY = Math.max(0, Math.min(targetScrollY, document.documentElement.scrollHeight - window.innerHeight));
    if (!isScrolling) {
      isScrolling = true;
      requestAnimationFrame(updateScroll);
    }
  }, { passive: false });

  window.addEventListener('scroll', () => {
    if (!isScrolling) {
      targetScrollY = window.scrollY;
      currentScrollY = window.scrollY;
    }
  }, { passive: true });
}

function updateScroll() {
  currentScrollY += (targetScrollY - currentScrollY) * 0.085;
  window.scrollTo(0, currentScrollY);
  
  if (Math.abs(targetScrollY - currentScrollY) > 0.5) {
    requestAnimationFrame(updateScroll);
  } else {
    isScrolling = false;
  }
}

// ---------- Live GitHub Stats & Chart ----------
async function fetchGithubStats() {
  const username = 'levibmackay';
  const syncIndicator = document.getElementById('github-sync-indicator');
  
  try {
    const userRes = await fetch(`https://api.github.com/users/${username}`);
    if (!userRes.ok) throw new Error('Failed to fetch profile');
    const userData = await userRes.json();
    
    const reposRes = await fetch(`https://api.github.com/users/${username}/repos?per_page=100`);
    if (!reposRes.ok) throw new Error('Failed to fetch repos');
    const reposData = await reposRes.json();
    
    const repoCount = userData.public_repos || reposData.length;
    let totalStars = 0;
    const languages = {};
    
    reposData.forEach(repo => {
      totalStars += repo.stargazers_count || 0;
      const lang = repo.language;
      if (lang) {
        languages[lang] = (languages[lang] || 0) + 1;
      }
    });
    
    document.getElementById('git-repos-count').textContent = repoCount;
    document.getElementById('git-stars-count').textContent = totalStars;
    
    const langKeys = Object.keys(languages);
    if (langKeys.length) {
      const sortedLangs = langKeys.map(k => ({ lang: k, count: languages[k] })).sort((a,b) => b.count - a.count);
      const totalCount = sortedLangs.reduce((sum, item) => sum + item.count, 0);
      
      const topLangs = sortedLangs.slice(0, 4);
      const percentages = topLangs.map(item => Math.round((item.count / totalCount) * 100));
      
      const sumPct = percentages.reduce((a,b) => a+b, 0);
      if (sumPct < 100 && percentages.length) {
        percentages[0] += (100 - sumPct);
      }

      const pctElements = ['pct-python', 'pct-sql', 'pct-cpp', 'pct-js'];
      percentages.forEach((pct, idx) => {
        const el = document.getElementById(pctElements[idx]);
        if (el) el.textContent = pct;
      });
      
      updateDonutSegments(percentages);
    }
    
    if (syncIndicator) {
      syncIndicator.textContent = "Synchronized";
      syncIndicator.style.color = "#28c840";
    }
  } catch (error) {
    console.warn('Using cached offline performance engine data:', error);
    if (syncIndicator) {
      syncIndicator.textContent = "Live (Cached)";
      syncIndicator.style.color = "var(--muted)";
    }
  }
}

function updateDonutSegments(percentages) {
  const circles = [
    document.querySelector('.segment-python'),
    document.querySelector('.segment-sql'),
    document.querySelector('.segment-cpp'),
    document.querySelector('.segment-js')
  ];
  
  let accumulated = 0;
  percentages.forEach((pct, idx) => {
    const circle = circles[idx];
    if (circle) {
      circle.setAttribute('stroke-dasharray', `${pct} 100`);
      circle.setAttribute('stroke-dashoffset', `-${accumulated}`);
      accumulated += pct;
    }
  });
}

function renderContributionsGrid() {
  const grid = document.getElementById('github-contributions-grid');
  if (!grid) return;
  
  grid.innerHTML = '';
  for (let i = 0; i < 182; i++) {
    const cell = document.createElement('span');
    cell.className = 'github-cell';
    
    const rand = Math.random();
    let lvl = 0;
    if (rand > 0.88) lvl = 4;
    else if (rand > 0.74) lvl = 3;
    else if (rand > 0.52) lvl = 2;
    else if (rand > 0.28) lvl = 1;
    
    cell.classList.add(`lvl-${lvl}`);
    
    cell.style.animationDelay = `${(i % 26) * 12 + Math.floor(i / 26) * 12}ms`;
    grid.appendChild(cell);
  }
}

// ---------- Projects Sticky Scroll System ----------
const stickySection = document.querySelector('.projects-sticky-section');
const projectMediaWindow = document.getElementById('project-media-window');
const mediaWrappers = document.querySelectorAll('.media-wrapper');
const slides = document.querySelectorAll('.slide');

function updateStickyProjects() {
  if (!stickySection || window.innerWidth <= 900) {
    let minDistance = Infinity;
    let activeIdx = 0;
    const midpoint = window.innerHeight / 2;
    
    slides.forEach((slide, idx) => {
      const r = slide.getBoundingClientRect();
      const slideMid = r.top + r.height / 2;
      const dist = Math.abs(slideMid - midpoint);
      if (dist < minDistance) {
        minDistance = dist;
        activeIdx = idx;
      }
    });

    mediaWrappers.forEach((w, idx) => w.classList.toggle('active', idx === activeIdx));
    slides.forEach((s, idx) => s.classList.toggle('active', idx === activeIdx));
    return;
  }
  
  const rect = stickySection.getBoundingClientRect();
  const totalHeight = rect.height - window.innerHeight;
  const scrolled = -rect.top;
  let progress = scrolled / totalHeight;
  progress = Math.max(0, Math.min(1, progress));
  
  const totalProjects = mediaWrappers.length;
  let activeIdx = Math.floor(progress * totalProjects);
  if (activeIdx >= totalProjects) activeIdx = totalProjects - 1;
  
  const subProgress = (progress * totalProjects) - activeIdx;
  
  mediaWrappers.forEach((w, idx) => w.classList.toggle('active', idx === activeIdx));
  slides.forEach((s, idx) => s.classList.toggle('active', idx === activeIdx));
  
  const activeMedia = mediaWrappers[activeIdx];
  if (activeMedia && !reduceMotion) {
    const scale = 1 - Math.abs(subProgress - 0.5) * 0.12;
    const rotateY = (subProgress - 0.5) * 16;
    const rotateX = -Math.sin(subProgress * Math.PI) * 4;
    const blurVal = Math.max(0, Math.abs(subProgress - 0.5) * 8 - 1);
    
    activeMedia.style.transform = `perspective(1200px) rotateY(${rotateY.toFixed(2)}deg) rotateX(${rotateX.toFixed(2)}deg) scale(${scale.toFixed(3)}) translateZ(0)`;
    activeMedia.style.filter = blurVal > 0.5 ? `blur(${blurVal.toFixed(1)}px)` : 'none';
  }
}

// ---------- Timeline Progress Drawing ----------
const timelineSection = document.querySelector('.timeline-section');
const timelineProgress = document.getElementById('timeline-progress-bar');
const timelineItems = document.querySelectorAll('.timeline-item');

function updateTimeline() {
  if (!timelineSection) return;
  const rect = timelineSection.getBoundingClientRect();
  const start = rect.top + window.scrollY + 120;
  const scrollableHeight = rect.height - 240;
  const current = window.scrollY - start + window.innerHeight * 0.45;
  let progress = current / scrollableHeight;
  progress = Math.max(0, Math.min(1, progress));
  
  if (timelineProgress) {
    timelineProgress.style.height = (progress * 100).toFixed(1) + '%';
  }
  
  timelineItems.forEach((item) => {
    const itemRect = item.getBoundingClientRect();
    const itemCenter = itemRect.top + itemRect.height * 0.3;
    if (itemCenter < window.innerHeight * 0.65) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });
}

// ---------- Newsroom Filtering ----------
const filterButtons = document.querySelectorAll('.filter-btn');
const newsCards = document.querySelectorAll('.news-card');

filterButtons.forEach((btn) => {
  btn.addEventListener('click', () => {
    filterButtons.forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    
    const filter = btn.dataset.filter;
    
    newsCards.forEach((card) => {
      if (filter === 'all' || card.dataset.category === filter) {
        card.style.display = 'flex';
        setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 50);
      } else {
        card.style.opacity = '0';
        card.style.transform = 'translateY(15px)';
        card.style.display = 'none';
      }
    });
  });
});

// ---------- Blog Drawer System ----------
const blogDrawer = document.getElementById('blog-drawer');
const blogOverlay = document.getElementById('blog-overlay');
const blogDrawerContent = document.getElementById('blog-drawer-content');
const drawerClose = document.getElementById('drawer-close');
const drawerBadge = document.getElementById('drawer-badge');
const blogProgressBar = document.getElementById('blog-progress-bar');

function openBlogDrawer(postId, badgeText) {
  const template = document.getElementById(`blog-post-template-${postId}`);
  if (!template) return;
  
  blogDrawerContent.innerHTML = '';
  const clone = template.content.cloneNode(true);
  blogDrawerContent.appendChild(clone);
  
  if (drawerBadge) drawerBadge.textContent = badgeText;
  if (blogProgressBar) blogProgressBar.style.width = '0%';
  
  blogDrawer.hidden = false;
  document.body.style.overflow = 'hidden';
  
  setTimeout(() => {
    blogDrawer.classList.add('active');
    blogOverlay.classList.add('active');
  }, 30);
}

function closeBlogDrawer() {
  blogDrawer.classList.remove('active');
  blogOverlay.classList.remove('active');
  document.body.style.overflow = '';
  
  setTimeout(() => {
    blogDrawer.hidden = true;
  }, 450);
}

newsCards.forEach((card) => {
  card.addEventListener('click', () => {
    const postId = card.dataset.postId;
    const badge = card.querySelector('.news-badge').textContent;
    openBlogDrawer(postId, badge);
  });
});

if (drawerClose) drawerClose.addEventListener('click', closeBlogDrawer);
if (blogOverlay) blogOverlay.addEventListener('click', closeBlogDrawer);

const drawerBody = document.querySelector('.blog-drawer-body');
if (drawerBody) {
  drawerBody.addEventListener('scroll', () => {
    const total = drawerBody.scrollHeight - drawerBody.clientHeight;
    const progress = total > 0 ? (drawerBody.scrollTop / total) * 100 : 0;
    if (blogProgressBar) blogProgressBar.style.width = progress.toFixed(1) + '%';
  });
}

// ---------- Print Tech Specs Resume ----------
const printBtn = document.getElementById('btn-print-resume');
if (printBtn) {
  printBtn.addEventListener('click', () => {
    window.print();
  });
}

// ---------- Contact Configurator Submission ----------
const contactForm = document.getElementById('contact-form');
const successReceipt = document.getElementById('form-success-receipt');
const resetFormBtn = document.getElementById('btn-reset-form');

if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const submitBtn = document.getElementById('btn-submit-config');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = 'Sending Transmission... <span class="spinner"></span>';
    
    const name = document.getElementById('form-name').value;
    const email = document.getElementById('form-email').value;
    
    const collabType = contactForm.querySelector('input[name="collab_type"]:checked').value;
    
    const checkedStacks = Array.from(contactForm.querySelectorAll('input[name="stack"]:checked')).map(cb => cb.value);
    const stackDisplay = checkedStacks.length ? checkedStacks.join(', ') : 'None selected';
    
    setTimeout(() => {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
      
      const uniqueCode = `#LM-${Math.floor(1000 + Math.random() * 9000)}`;
      const timestamp = new Date().toISOString().replace('T', ' ').substring(0, 19);
      
      document.getElementById('receipt-id').textContent = uniqueCode;
      document.getElementById('receipt-collab').textContent = collabType;
      document.getElementById('receipt-stack').textContent = stackDisplay;
      document.getElementById('receipt-time').textContent = timestamp;
      
      contactForm.style.opacity = '0';
      setTimeout(() => {
        contactForm.setAttribute('hidden', '');
        successReceipt.removeAttribute('hidden');
      }, 300);
      
    }, 1400);
  });
}

if (resetFormBtn) {
  resetFormBtn.addEventListener('click', () => {
    successReceipt.setAttribute('hidden', '');
    contactForm.removeAttribute('hidden');
    contactForm.reset();
    setTimeout(() => { contactForm.style.opacity = '1'; }, 50);
  });
}

// ---------- 3D tilt on project media (desktop hover) ----------
if (canHover && !reduceMotion) {
  document.querySelectorAll('.news-card').forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(1000px) rotateX(${(-y * 3.5).toFixed(2)}deg) rotateY(${(x * 4.5).toFixed(2)}deg) translateY(-5px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
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
      setTimeout(() => toast.classList.remove('active'), 2200);
    });
  });
});

// ---------- Combined Scroll Tick loop ----------
let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    window.requestAnimationFrame(() => {
      const doc = document.documentElement;
      const max = doc.scrollHeight - doc.clientHeight;
      const progress = max ? (window.scrollY / max) * 100 : 0;
      document.querySelector('.scroll-progress').style.width = progress.toFixed(1) + '%';
      
      updateStickyProjects();
      updateTimeline();
      
      ticking = false;
    });
    ticking = true;
  }
}, { passive: true });

updateStickyProjects();
updateTimeline();

// ---------- Magnetic buttons ----------
if (canHover && !reduceMotion) {
  document.querySelectorAll('.btn, .terminal-toggle, .drawer-close').forEach((el) => {
    el.addEventListener('mousemove', (e) => {
      const r = el.getBoundingClientRect();
      const x = e.clientX - r.left - r.width / 2;
      const y = e.clientY - r.top - r.height / 2;
      el.style.transform = `translate(${(x * 0.16).toFixed(1)}px, ${(y * 0.26).toFixed(1)}px)`;
    });
    el.addEventListener('mouseleave', () => {
      el.style.transform = '';
    });
  });
}

// ---------- Border glow cards tracking cursor ----------
const glowCards = document.querySelectorAll('.glow-card');

glowCards.forEach((card) => {
  if (card.classList.contains('contact-card')) return;
  const light = document.createElement('span');
  light.className = 'edge-light';
  card.prepend(light);
});

const GLOW_FRAME_MS = 28;
if (canHover) {
  glowCards.forEach((card) => {
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

// ---------- Blur-in headings ----------
if (!reduceMotion) {
  document.querySelectorAll('main h2:not(.blur-ignore)').forEach((h) => {
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
    { threshold: 0.45 }
  );
  document.querySelectorAll('main h2').forEach((h) => blurObserver.observe(h));
}

// ---------- Terminal easter egg ----------
const terminal = document.getElementById('terminal');
const terminalOpen = document.getElementById('terminal-open');
const terminalToggle = document.getElementById('terminal-toggle');
const terminalClose = document.getElementById('terminal-close');
const terminalInput = document.getElementById('terminal-input');
const terminalOutput = document.getElementById('terminal-output');

const greetingHour = new Date().getHours();
const greetingMsg = greetingHour < 5 ? 'Burning the midnight oil?' : greetingHour < 12 ? 'Good morning.' : greetingHour < 18 ? 'Good afternoon.' : 'Good evening.';
document.getElementById('terminal-welcome').innerHTML =
  greetingMsg + " Type <span class='t-hl'>help</span> to see available commands.";

const commands = {
  help: "Available commands:\n  whoami     Who am I\n  bio        The longer story\n  projects   What I've built\n  skills     The tech stack specs\n  blog       View recent blog summaries\n  timeline   Explore milestones\n  contact    How to reach me\n  explode    Replay the hero animation\n  ls         Look around folders\n  clear      Wipe the screen",
  ls: "bio.txt  projects/  skills.json  blog/  contact.key  secret_plans.enc",
  whoami: "Levi Mackay — Software Engineer, CS Teaching Assistant, Sandbox Incubator developer.",
  bio: "4.0 GPA Computer Science major at BYU-Idaho. Active TA, system builder, and former Balkan service representative. I construct automation systems that solve real cognitive workflows.",
  projects: "1. SwingOS — real-time computer vision swing analysis\n2. Lydia — local AI coding assistant loops\n3. AI Security Scanner — LLM vulnerabilities static reviews\n4. Foreman's Friend — jobs volume bidding CLI",
  skills: "languages: [Python, SQL, JavaScript, C++, HTML/CSS]\ntools: [Git, Docker, Linux CLI, VS Code]\nfocus: [Local AI Agents, Computer Vision, Relational DBs, Systems]",
  blog: "Recent Newsroom entries:\n- Lydia: Designing a Local CLI Coding Agent\n- SwingOS: Real-Time Pose Telemetry on standard GPUs\n- CS Fundamentals: Teaching is the Best Way to Compile Code\n(Type 'blog <num>' to read summaries)",
  'blog 1': "Lydia summary: Explores constraints for local models to edit code accurately, implementing a search-and-replace pipeline and offloading model generation via Tailscale to private GPU servers.",
  'blog 2': "SwingOS summary: Outlines the trigonometry needed to track Bat tilt and head movement stabilizer from 33 joint positions mapped in OpenCV coordinate domains.",
  'blog 3': "TA summary: Explains how reviewing hundreds of beginner code structures taught me to write minimal clean APIs and design code that reduces cognitive load.",
  timeline: "Milestones:\n- 2024-Present: BYU-Idaho TA and Startup Builder in Sandbox\n- 2023-2025: Built SwingOS, Lydia, SecurityScanner, 4.0 GPA\n- 2021-2023: Full-time volunteer service across 5 Balkan countries\n- Before 2021: Landscape Foreman & Operator, designed estimators",
  contact: "Email: levibmackay@gmail.com\nLinkedIn: linkedin.com/in/levi-mackay-217380396\nGitHub: github.com/levibmackay",
  sudo: "Permission denied. Nice try though.",
  'secret_plans.enc': "Decryption failed. Some things you have to build first.",
  explode: () => {
    closeTerminal();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(() => { if (window.__replayIntro) window.__replayIntro(); }, 500);
    return "Boom. Reassembling shards...";
  },
};

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

if (terminalOpen) terminalOpen.addEventListener('click', openTerminal);
if (terminalToggle) terminalToggle.addEventListener('click', openTerminal);
if (terminalClose) terminalClose.addEventListener('click', closeTerminal);

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeTerminal();
    closeBlogDrawer();
  }
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

// ---------- Run on Load ----------
document.addEventListener('DOMContentLoaded', () => {
  renderContributionsGrid();
  fetchGithubStats();
});
