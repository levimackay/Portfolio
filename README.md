# Levi Mackay — Portfolio

**Live site → [levibmackay.github.io/Portfolio](https://levibmackay.github.io/Portfolio/)**

Hey, I'm Levi. This repo is the central hub for the projects I've built while working through my CS degree at BYU–Idaho — a mix of computer vision, AI tooling, data engineering, and automation. It's also the source for my personal portfolio site: a single-page, no-build HTML/CSS/JS site with a WebGL hero scene, scroll animations, and a hidden interactive terminal easter egg.

## Features

- **Single-page portfolio** — hero, about, project case studies, skills, and contact sections, all in `index.html`.
- **WebGL hero animation** — a sphere of shards that assembles on load and reacts to scroll, built with Three.js (`scene.js`, vendored at `assets/vendor/three.min.js`).
- **Scroll-driven UI** — a scroll-progress bar, reveal-on-scroll sections, and an animated stat counter, all hand-rolled in `script.js` (no animation library).
- **Interactive terminal easter egg** — press `T` or click the terminal button to open a fake shell with commands like `whoami`, `bio`, `projects`, `skills`, `contact`, `ls`, and `explode` (replays the hero animation).
- **Copy-to-clipboard contact** — clicking the email button copies it and shows a toast confirmation.
- **Project write-ups** — each featured project has its own README under `projects/`.

## Tech stack

- **HTML / CSS / vanilla JavaScript** — no framework, no bundler, no build step for the site itself.
- **Three.js** (vendored `.js` file, loaded via `<script>` tag — not an npm dependency) for the hero WebGL scene.
- Google Fonts (Inter) loaded via `<link>`.
- Individual projects under `projects/` use their own stacks — Python, OpenCV, MediaPipe, MySQL, and Tkinter — see each project's README for specifics.

## Setup / running locally

There's no build step or package manager involved in the site itself — it's static files. To view it locally, serve the repo root with any static file server (opening `index.html` directly also works, but a local server avoids `file://` restrictions on things like fetch/video):

```bash
git clone https://github.com/levibmackay/Portfolio.git
cd Portfolio
python3 -m http.server 8000
# then open http://localhost:8000
```

## Usage

- Browse the live site at the link above, or run it locally as described.
- Press **`T`** (or click the `>_ terminal` link in the footer) to open the interactive terminal and type `help` for the list of commands.
- Project source code and write-ups live under `projects/`; each links out to a public GitHub repo where relevant (e.g. Lydia, AI Security Scanner).

## Featured projects

| Project | What it is | Stack |
|---|---|---|
| [SwingOS](projects/swing-analyzer) | Real-time biomechanical feedback for baseball swings using pose estimation | Python, OpenCV, MediaPipe |
| [Lydia](https://github.com/levibmackay/lydia-cli) | Local, Claude-Code-style coding agent — no API keys, nothing sent to the cloud | Python, Ollama, Agents |
| [AI Security Scanner](https://github.com/levibmackay/SecurityScanner) | AI-powered vulnerability detection with severity ratings and suggested fixes | Python, Gemini API |
| [Foreman's Friend](projects/landscape-estimator) | Job-site material and labor estimator, born from my time as a landscape foreman | Python, CLI |
| [Baseball Analytics Engine](projects/baseball-database) | Relational schema and layered queries for player performance trends | MySQL |
| [BCS Flashcards](projects/flashcard-app) | Vocabulary tool I built to study Bosnian, Croatian, and Serbian | Python, Tkinter |

## Repo layout

- **`index.html` / `styles.css` / `script.js` / `scene.js`** — the portfolio site itself.
- **`assets/`** — demo videos, screenshots, and the vendored Three.js library used by the site.
- **`projects/`** — source code and READMEs for the featured projects above.
- **`archive/`** — early coursework and experiments (Python and web dev assignments), kept out of the way of the main projects.
- **`byui_career_quest.html`** — a standalone browser mini-game, not linked from the main site.
- **`SiteRemodelTest/`** — a work-in-progress redesign experiment for the portfolio site, not yet live.
- **`dist/`** — a build output directory (git-ignored); not part of the tracked source.

## Contributors

- Levi B Mackay ([@levibmackay](https://github.com/levibmackay)) — sole author and maintainer.

## Connect

I'm always down to talk code, startups, or baseball. Find me on [LinkedIn](https://www.linkedin.com/in/levi-mackay-217380396/) or email me at levibmackay@gmail.com.

---
_Last updated: July 22, 2026_

---

Maintained by [Levi Mackay](https://github.com/levibmackay)

**Last updated:** 2026-07-27
