# Levi Mackay: Portfolio

**Live site: [levimackay.com](https://levimackay.com/)** · **[Resume (PDF)](https://levimackay.com/resume.pdf)**

Hey, I'm Levi. This repo is the deploy target for my portfolio site. It holds the built HTML, CSS and JavaScript plus the `CNAME` GitHub Pages serves from. It is not the buildable source. The source and its build tooling live in a separate private repo.

## What's here

- **Home** (`index.html`). A code editor that runs izvor, my own programming language, in the browser. Below it are five projects, more work, about and contact.
- **Project pages** (`work/<name>/index.html`). One each for izvor, Lydia, Proven Blue, tieout and McKay Jewelers. Each page has a table that puts every number next to the command that counted it.
- **Privacy** (`privacy/index.html`). The site collects nothing about visitors.
- **Sources** (`SOURCES.md`). Every figure on the site, the command that produced it and the date it was run.
- `projects/` and `about/` only forward to the home page. They were pages on the previous version of the site.

## Tech stack

- Static output from Astro. The JS and CSS bundles under `assets/` are hashed build output. There is no `package.json` or build step in this repo, so whatever is committed here is what ships.
- anime.js for the motion, plus a few React components for the headline, the large views of pictures and recordings, one chart and the pointer effects. On a phone they load only when the part that needs them is scrolled to. Under `prefers-reduced-motion` nothing animates.
- The editor runs the izvor interpreter as WebAssembly in a worker (`izvor/`). The code you type stays in your browser.
- Page changes use CSS view transitions.
- Fonts are self hosted: Mona Sans for headings and text and Monaspace Neon for labels and code. The font files are among the hashed files in `assets/` and their licenses are in `fonts/`. No Google Fonts.
- No cookies, no analytics scripts and nothing loaded from another host.

## Setup / running locally

This repo has no build step of its own. It is already built static output. To view it locally, serve the repo root with any static file server:

```bash
git clone https://github.com/levimackay/Portfolio.git
cd Portfolio
python3 -m http.server 8000
# then open http://localhost:8000
```

To change the site's content, layout or styling, edit it in the private source repo and redeploy. Editing the built files here directly will just get overwritten by the next deploy.

## Featured projects

In the order they appear on the home page:

| Project | What it is | Stack |
|---|---|---|
| [izvor](https://github.com/levimackay/izvor) | A typed programming language and its compiler, written from scratch in C. It interprets a program or compiles it through C to a native binary. | C |
| [Lydia](https://github.com/levimackay/lydia-cli) | A terminal coding agent that reads, edits and tests code on local models. By default nothing leaves the machine. | Python, Ollama |
| Proven Blue | Verified work portfolios for people in the trades. A contractor or teacher confirms the work someone posts. I built the backend and its security. Team project, so the source is private. | TypeScript, Supabase, PostgreSQL |
| [tieout](https://tieout-site-opal.vercel.app) | A tool for tax preparers that compares QuickBooks balances with a filed return and drafts correcting entries. Only run on sample files so far. | Python |
| [McKay Jewelers](https://mckayjewelersmagicvalley.com) | My first paying client, a jewelry store in Twin Falls. I wrote the contract, then designed, built and launched the site. | Next.js, TinaCMS, Cloudflare Workers |

## Repo layout

- **`index.html`, `work/`, `privacy/`, `404.html`**: the pages of the built site.
- **`assets/`**: hashed JS and CSS bundles, the fonts and the processed images. Build output, not meant to be edited by hand.
- **`media/`**: the screen recordings and their still frames.
- **`izvor/`**: the WebAssembly build of izvor and the worker that runs it.
- **`fonts/`**: the licenses of the two font families.
- **`.deploy-manifest`, `.deploy-kept`**: lists the deploy script keeps, so it only ever removes files it put here.

## Contributors

- Levi B Mackay ([@levimackay](https://github.com/levimackay)), sole author and maintainer.

## Connect

I'm always down to talk code, startups, or baseball. Find me on [LinkedIn](https://www.linkedin.com/in/levi-mackay-217380396/) or email me at levibmackay@gmail.com.

## License

MIT. See [LICENSE](LICENSE).
