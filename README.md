# Levi Mackay — Portfolio

**Live site → [levimackay.com](https://levimackay.com/)**

Hey, I'm Levi. This repo is the deploy target for my portfolio site: it holds the built HTML/CSS/JS output plus the `CNAME` GitHub Pages serves from. It is not the buildable source — the source (and its build tooling) lives in a separate private repo. What's tracked here is three pages (home, about, projects) with a WebGL hero scene, GSAP/Lenis-driven scroll animations, and an interactive terminal.

## Features

- **Three pages** — `index.html` (hero, an inline terminal section, stat counters, contact), `about/index.html`, and `projects/index.html` (case studies for the featured projects, the Main Street Sites business section, an "also shipped" grid, and skills).
- **WebGL hero scene** — a Three.js scene, lazy-loaded from a separate chunk (`assets/scene-*.js`) after scroll settles. Under Data Saver, `prefers-reduced-motion`, or a software/no WebGL renderer (SwiftShader, llvmpipe), it loads a lighter 2D canvas fallback (`assets/scene2d-*.js`) instead — a still sphere, not skipped. A footer control ("animations") lets visitors override their system's reduced-motion setting either direction.
- **Scroll-driven UI** — GSAP with ScrollTrigger for reveals, a scrubbed project stage, and animated stat counters; Lenis for smooth scroll. Both fall back to instant, unanimated state under `prefers-reduced-motion`.
- **Interactive terminal** — press `T` (outside form fields) or use the on-page terminal control to open a command shell; `Escape` closes it, focus is trapped while it's open.
- **Copy-to-clipboard contact** and a mobile nav menu with focus handling.
- **Project write-ups** — case studies for the featured projects live in `projects/index.html`.

## Tech stack

- Built HTML/CSS/JS — the JS/CSS bundles under `assets/` (`main-*.js`, `main-*.css`, `scene-*.js`) are hashed build output, not hand-authored files. There's no `package.json` or build step in this repo; whatever's committed here is what ships.
- **Three.js** for the hero scene, **GSAP + ScrollTrigger** for scroll animation, **Lenis** for smooth scrolling — all bundled into the built JS, not loaded from a CDN.
- Fonts are self-hosted variable fonts (`fonts/`): Archivo for display and body text, Martian Mono for the terminal and technical labels. No Google Fonts.

## Setup / running locally

This repo has no build step of its own — it's already-built static output. To view it locally, serve the repo root with any static file server (opening `index.html` directly also works, but a local server avoids `file://` restrictions on things like fetch/video):

```bash
git clone https://github.com/levimackay/Portfolio.git
cd Portfolio
python3 -m http.server 8000
# then open http://localhost:8000
```

To change the site's actual content, layout, or styling, edit it in the private source repo and redeploy; editing the built files here directly will just get overwritten by the next deploy.

## Usage

- Browse the live site at the link above, or run it locally as described.
- Press **`T`** to open the interactive terminal and type `help` for the list of commands.

## Featured projects

Case studies on `/projects`, in the order they appear:

| Project | What it is | Stack |
|---|---|---|
| [izvor](https://github.com/levimackay/izvor) | A programming language built from scratch: lexer, recursive-descent parser, tree-walking interpreter, then a bytecode compiler and stack VM. Lexer and parser done; the interpreter runs arithmetic end to end. | C |
| [minidb](https://github.com/levimackay/minidb) | A single-file database engine: binary file formats, a pager, B-trees, cursors, a small SQL parser. Roadmap and Phase 0 scaffolding committed, implementation not started. | C |
| [FORGE](https://github.com/levimackay/forge) | A native iOS app turning long-term goals into adaptive daily missions. Phase 1 (core loop) in progress: Xcode project and package split in place, domain model and persistence next. | Swift 6, iOS 26 |
| [Lydia](https://github.com/levimackay/lydia-cli) | A local coding agent that reads, edits, tests, and drives git through a local Ollama model, nothing sent to the cloud | Python, Ollama |

Also shown on `/projects` under "Also shipped": a Serbo-Croatian dictionary project, [SwingOS](https://github.com/levimackay/swing-analyzer) (baseball swing pose tracking), [AI Security Scanner](https://github.com/levimackay/SecurityScanner), [RepoAnalyzer](https://github.com/levimackay/RepoVisualizer), [Canvas-Risk](https://github.com/levimackay/canvas-risk), [canvas-ta-tool](https://github.com/levimackay/canvas-ta-tool), [Bug Lab](https://github.com/levimackay/bug-lab), [Bug Hunt](https://github.com/levimackay/bug-hunt), [Swift Academy](https://github.com/levimackay/swift-academy), [C# DSA Academy](https://github.com/levimackay/csharp-dsa-academy), and [microplastics-idaho](https://github.com/levimackay/microplastics-idaho). The projects page also has a section on Main Street Sites, a web design business for local small businesses.

## Repo layout

- **`index.html`, `about/index.html`, `projects/index.html`** — the three pages of the built site.
- **`assets/`** — hashed JS/CSS bundles, demo videos, and screenshots. Not meant to be hand-edited; they're build output.
- **`fonts/`** — self-hosted Archivo and Martian Mono variable font files.
- **`projects/`** — holds `index.html`, the built projects page. All of its case-study content lives in that one file.

## Contributors

- Levi B Mackay ([@levimackay](https://github.com/levimackay)) — sole author and maintainer.

## Connect

I'm always down to talk code, startups, or baseball. Find me on [LinkedIn](https://www.linkedin.com/in/levi-mackay-217380396/) or email me at levibmackay@gmail.com.

## License

MIT — see [LICENSE](LICENSE).
