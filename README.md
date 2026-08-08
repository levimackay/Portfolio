# Levi Mackay — Portfolio

**Live site → [levimackay.com](https://levimackay.com/)**

Hey, I'm Levi. This repo is what GitHub Pages serves for levimackay.com. It holds the compiled portfolio site — a Vite build committed as static output — plus source and write-ups for a few of the smaller projects I've built while working through my CS degree at BYU–Idaho: a mix of computer vision, AI tooling, data engineering, and automation.

## Features

- **Single-page portfolio** — hero, stats, about, project scrollytelling, more projects, skills, and contact sections, all in `index.html`.
- **WebGL hero animation** — a sphere of shards behind the page, built with Three.js. It's code-split into its own chunk (`assets/scene-*.js`) that only loads once the page is idle, and it's skipped entirely under `prefers-reduced-motion` or Save-Data.
- **Scroll-driven UI** — GSAP and ScrollTrigger drive the hero parallax, the word-by-word about reveal, the sticky project stage where four media layers cross-fade, the reveal-on-scroll sections, and the stat counters.
- **Lazy media** — project demo videos only fetch and play once their panel scrolls into view, and pause when it leaves.
- **Interactive terminal easter egg** — press `T` or click the terminal button to open a fake shell with commands `help`, `whoami`, `bio`, `projects`, `skills`, `contact`, `ls`, `explode` (replays the hero animation), and `clear`, plus a couple `help` doesn't list.
- **Project write-ups** — the projects that live in this repo have their own README under `projects/`.

## Tech stack

- **Vite build output** — the committed `index.html` loads hashed `assets/index-*.js` and `assets/index-*.css`. The source project isn't in this repo; only the compiled result is.
- **GSAP 3.15** with ScrollTrigger, bundled into the main JS chunk, for every scroll animation.
- **Three.js** (r185) for the hero scene, split into `assets/scene-*.js` and imported dynamically.
- **Tailwind CSS v4**, compiled into `assets/index-*.css`.
- Google Fonts (Inter) loaded non-blocking via `<link>`.
- Individual projects under `projects/` use their own stacks — Python, OpenCV, MediaPipe, MySQL, and Tkinter — see each project's README for specifics.

## Setup / running locally

The site here is already built, so there's nothing to install or compile in this repo. Asset paths are root-relative (`/assets/...`) for the custom domain, so opening `index.html` off the filesystem won't load anything — serve the repo root with a static file server instead:

```bash
git clone https://github.com/levimackay/Portfolio.git
cd Portfolio
python3 -m http.server 8000
# then open http://localhost:8000
```

Changing the site means rebuilding it in the source project and committing the new output here.

## Usage

- Browse the live site at the link above, or run it locally as described.
- Press **`T`** (or click the `>_ terminal` button in the footer) to open the interactive terminal and type `help` for the list of commands.
- Source and write-ups for the projects that live here are under `projects/`; the ones that live in their own repos link out from the site (Lydia, RexNest).

## Featured projects

These are the four the site leads with, plus the one of its secondary cards that has source in this repo.

| Project | What it is | Stack |
|---|---|---|
| [Lydia](https://github.com/levimackay/lydia-cli) | Local, terminal-based coding agent — no API keys, nothing sent to the cloud | Python, Ollama, Agents |
| [RexNest](https://rexburg-housing.vercel.app) | Student housing comparison site for BYU–Idaho renters, ranked by a weighted value score | Next.js, TypeScript, Supabase, PostgreSQL |
| Serbo-Croatian dictionary | 5,709 entries parsed and merged from a scanned book and two years of word sheets, then typeset | Python, Typst |
| canvas-risk | Risk model over the Canvas LMS API that scores students 0–100 to flag who's falling behind | Python, Canvas API, SQL |
| [SwingOS](projects/swing-analyzer) | Webcam prototype that flags when a batter's head drifts off a hand-set anchor line | Python, OpenCV, MediaPipe |

The site's other secondary cards — leetcoach, flipper-lab, and microplastics-idaho — live in their own repos and have nothing in this one. Three older projects have write-ups under `projects/` without being on the site: [baseball-database](projects/baseball-database), [flashcard-app](projects/flashcard-app), and [landscape-estimator](projects/landscape-estimator).

## Repo layout

- **`index.html`** — the built portfolio page, and the only HTML file served.
- **`assets/`** — the compiled JS and CSS bundles, the hero scene chunk, and the demo videos, posters, and OG image the page references.
- **`projects/`** — source code and READMEs for the projects that live in this repo.
- **`resume.pdf`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `CNAME`, `.nojekyll`** — the rest of what GitHub Pages serves for the custom domain.

Everything committed here is publicly reachable at levimackay.com whether or not the site links to it, so nothing goes in that I wouldn't want served.

## Contributors

- Levi B Mackay ([@levimackay](https://github.com/levimackay)) — sole author and maintainer.

## Connect

I'm always down to talk code, startups, or baseball. Find me on [LinkedIn](https://www.linkedin.com/in/levi-mackay-217380396/) or email me at levibmackay@gmail.com.

---

**Last updated:** 2026-08-08
