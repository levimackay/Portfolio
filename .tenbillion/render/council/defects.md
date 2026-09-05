# Measured defects

Target: .

## 1440

- [ ] #site-nav > div:nth-of-type(1) > a: text over imagery is under the WCAG floor (expected 4.5:1, got 1.06:1)
- [ ] #site-nav > div:nth-of-type(1) > nav > a:nth-of-type(1): text over imagery is under the WCAG floor (expected 4.5:1, got 1.06:1)
- [ ] #site-nav > div:nth-of-type(1) > nav > a:nth-of-type(2): text over imagery is under the WCAG floor (expected 4.5:1, got 1.06:1)
- [ ] #site-nav > div:nth-of-type(1) > nav > a:nth-of-type(3): text over imagery is under the WCAG floor (expected 4.5:1, got 1.09:1)

## 768

- [ ] #site-nav > div:nth-of-type(1) > a: text over imagery is under the WCAG floor (expected 4.5:1, got 1.07:1)
- [ ] #site-nav > div:nth-of-type(1) > nav > a:nth-of-type(1): text over imagery is under the WCAG floor (expected 4.5:1, got 1.07:1)
- [ ] #site-nav > div:nth-of-type(1) > nav > a:nth-of-type(2): text over imagery is under the WCAG floor (expected 4.5:1, got 1.06:1)
- [ ] #site-nav > div:nth-of-type(1) > nav > a:nth-of-type(3): text over imagery is under the WCAG floor (expected 4.5:1, got 1.13:1)
- [ ] #hero-heading > span: text over imagery is under the WCAG floor for large text (expected 3:1, got 1.13:1)

## 390

- [ ] #site-nav > div:nth-of-type(1) > a: text over imagery is under the WCAG floor (expected 4.5:1, got 1.08:1)
- [ ] #hero-heading > span: text over imagery is under the WCAG floor for large text (expected 3:1, got 1.07:1)

## reduced-motion

- [ ] div > div:nth-of-type(2) > div:nth-of-type(1) > span:nth-of-type(1) > button:nth-of-type(1) > span: left invisible once the animation is removed (opacity 0) (expected visible after load, got opacity 0)
- [ ] div > div:nth-of-type(2) > div:nth-of-type(1) > span:nth-of-type(1) > button:nth-of-type(2) > span: left invisible once the animation is removed (opacity 0) (expected visible after load, got opacity 0)
- [ ] div > div:nth-of-type(2) > div:nth-of-type(1) > span:nth-of-type(1) > button:nth-of-type(3) > span: left invisible once the animation is removed (opacity 0) (expected visible after load, got opacity 0)

## a11y

- [ ] .btn-primary[href$="projects/"]: color-contrast: Elements must meet minimum color contrast ratio thresholds (expected no serious or critical violations, got serious on 1 node)

## console

- none measured

---

# Critique (design judge, flagship dosage)

## 1440 viewport

What is on screen: near-black ground, a field of ~120 small grey and blue
triangular shards scattered evenly across the full 1440x900 frame, a fixed
transparent nav (wordmark left, four items right, last a pill), and a
vertically-centred hero of blue letterspaced eyebrow, three-line display
headline with the third line tinted, two-line subhead, three pills.

- [ ] hero composition (1440): eyebrow label + huge centred headline + one-line
      subhead + a row of pill buttons on the centre axis is the exact centred-hero
      pattern named in the anti-slop list; nothing sits off-axis, nothing is
      cropped, nothing is full-bleed. Expected at flagship dosage: one deliberate
      break in the axis or a full-bleed element. This is the single largest
      distinctiveness defect on the page.
- [ ] palette (site-wide): --color-ink #0a0a0c, --color-paper #f5f5f7,
      --color-accent #2997ff are apple.com's dark-mode ink, off-white and system
      blue to the hex. Swap the wordmark and this is an Apple product page. For a
      portfolio whose reviewers are Apple engineers this reads as imitation, not
      homage.
- [ ] --color-rim #c4844a (site-wide): the only second hue in the token set, used
      by exactly one rule (.stat-num) and zero HTML classes. The page therefore
      ships one accent hue at one intensity, which is a named tell. Expected: rim
      earns real territory or is deleted.
- [ ] shard field (1440): at scroll 0 the shards are dispersed uniformly over the
      whole viewport, not assembled. The comment in index.html promises "shard
      sphere assembles on load, explodes on scroll"; the assembled sphere is not
      visible in the first-paint frame, so the one set-piece on the home page
      reads as generic drifting particles. Expected: a legible sphere silhouette
      at rest.
- [ ] shard field contrast (1440): brightest shards measure roughly #2f6fd0 on
      #0a0a0c ground; at this exposure the field carries no shape and no depth,
      it reads as sensor noise. Deleting it costs the page nothing visible, which
      is the test it fails.
- [ ] eyebrow treatment (1440): hero eyebrow is Archivo 13px semibold uppercase
      at 0.28em in accent blue (inline classes), while every other section uses
      .eyebrow = Martian Mono 11px at 0.14em in paper/72. Two different eyebrow
      systems on one page. Expected: one.
- [ ] nav links over canvas (1440): measured 1.06:1 to 1.09:1 by tb measure. On
      this frame they read fine because the shards under them happen to be dark,
      but the field is animated and there is no scrim or backdrop on the nav at
      scroll 0, so a bright shard passing under "Work" is a real state, not a
      measurement artifact. Expected 4.5:1 in every frame; needs a scrim or a
      nav-safe exclusion zone in the scene.
- [ ] .btn-primary (1440, a11y serious): axe reports a color-contrast violation
      on the "See the work" button. The static pair #0a0a0c on #2997ff computes
      6.56:1, so the failure is axe resolving the background against the canvas
      through the reveal state. Either way it fails the audit an Apple reviewer
      would run.
- [ ] button radii (1440): all three hero pills, the nav Contact pill and the
      contact-section buttons use border-radius 9999px. One radius on every
      interactive element is a named tell.
- [ ] hero rag (1440): line 1 spans x 440-1000, line 2 spans x 353-1090, line 3
      spans x 412-1029. The rag is an unshaped trapezoid rather than a set one.
      Opinion, not breakage.

## 1440 full page (below the fold)

Correction to the viewport note above: in full-1440.png the shard sphere IS
assembled, a dense cloud of blue and grey triangles ringing the headline, and it
is the best thing on the site. The viewport capture at the same width shows it
dispersed. Both are true frames of the same page, which is the defect.

- [ ] hero scene timing (1440): 1440.png (viewport pass) shows the shards
      dispersed across the whole frame; full-1440.png shows them assembled into a
      sphere. The two captures were taken seconds apart, so the assembled state a
      visitor is meant to see is not reliably present in the first seconds.
      Expected: the silhouette readable within the first second of paint.
- [ ] terminal window (1440): .console-shell is height:360px fixed, holding one
      24px welcome line at the top and a 40px input row at the bottom, leaving
      roughly 296px of empty black in the middle. A live terminal that renders
      mostly void reads as broken, not as restraint. Expected: shell heights to
      content, or a seeded scrollback that fills it.
- [ ] two left rails (1440): the nav wordmark and the console copy sit on a
      144px left rail (max-w-1200 + px-6); "The work." and every work row sit on a
      244px rail (max-w-1000 + px-6). 100px of disagreement, visible as a step in
      the full-page view, with nothing on screen explaining it. Expected: one
      rail, or a difference large enough to read as intentional.
- [ ] stats row (1440): four numbers at fluid-3xl with 13px captions under them
      is the "row of three or four big numbers with small captions" tell,
      verbatim. Worse, one of the four is a GPA, which converts the section from
      evidence into an achievement counter, and one is "36 GitHub stars", a
      number too small to survive being set at 60px.
- [ ] stats colour (1440): --color-rim #c4844a appears on this page in exactly
      one place, the stat numerals. The only second hue in the system is spent on
      the most generic module on the page. Expected: the distinctive colour goes
      to the distinctive element.
- [ ] work list duplicate (1440): "Lydia" appears twice, row 3 linking
      /projects/#lydia and row 6 linking /projects/#more-projects, with two
      different one-line descriptions of the same project. Content bug, visible on
      screen. Expected: one Lydia row.
- [ ] work list rhythm (1440): seven rows, identical hairline, identical name
      size (clamp 1.35-1.9rem), identical 14px description column, identical row
      height. tinylang and Main Street Sites get the same weight. The list marches.
      Expected: the two or three rows that carry the argument set apart.
- [ ] hero and contact are the same composition (1440): both are eyebrow +
      centred display headline + centred subhead at max-w-44ch + a centred row of
      pills. Two of the page's five sections are the same picture, and they are
      the first and the last thing seen. Expected: the closing section answers the
      opening rather than repeating it.
- [ ] nothing full-bleed (1440): every content section lives inside max-w-1200 or
      max-w-1000. The only edge-to-edge element is the background canvas. Named
      tell: "every section in the same max-width container with nothing
      full-bleed".
- [ ] .console-shell box-shadow (1440): 0 30px 80px rgba(0,0,0,0.55) rendered on
      a #0a0a0c ground is invisible. Dead CSS carrying a named tell (drop shadows)
      for zero visual return.
- [ ] work-list-desc (1440): 14px at paper/55, measured 5.44:1. Passes AA, but
      14px is the browser's small-print size and this column carries the only
      description of each project on the home page. Opinion: it is undersold.

### What works at 1440
- Type is genuinely chosen, not defaulted: Archivo variable with the wdth axis
  driven by --display-stretch, Martian Mono for every technical label. No Inter,
  no Geist, no Space Grotesk, self-hosted, both preloaded.
- Section padding actually varies (--space-sm/md/lg, clamp 4-9rem), so the page
  does not march vertically the way the tell list describes.
- The assembled shard sphere in full-1440.png is a real set-piece with a real
  idea behind it, and it is the one memorable element on the page.
- The terminal is live rather than a decorative terminal mockup, which is the
  explicit inversion of a named tell.

## 768 viewport

Same centred stack, headline still breaking to three lines, three pills still in
one row. Shards dispersed rather than assembled, plus faint connector lines
crossing the frame diagonally.

- [ ] near-camera shard (768): a saturated blue triangle roughly 90x120px sits at
      the right edge, x 690-768 / y 380-500, immediately beside the word "use.",
      while every other shard in frame is 8-16px. The scale jump reads as a
      rendering fault rather than depth, and it is the exact object that drops
      #hero-heading > span to 1.13:1 (expected 3:1 for large text). Expected: a
      near-plane clip or a text-safe exclusion volume in front of the headline.
- [ ] second near-camera shard (768): a white triangle at x 680-696 / y 795-810
      is the brightest pixel in the lower half of the frame and pulls the eye off
      the CTA row. Same fix.
- [ ] connector lines (768): thin lines link the shards into a web across the
      whole frame. A constellation network on a dark ground is one of the most
      recognisable stock-tech backgrounds there is, and it fights the shard
      conceit rather than supporting it. Expected: shards or lines, not both.
- [ ] nav over canvas (768): measured 1.06-1.13:1 on all four nav items; the
      Contact pill sits directly over a grey shard in this frame, so this one is
      visible, not theoretical. Expected 4.5:1.
- [ ] hero dead zone (768): hero content ends at y 690 in a 1024-tall viewport,
      leaving 334px of empty field with no scroll cue of any kind. At flagship
      dosage the fold should tell the visitor there is more. Expected: a scroll
      affordance or content intruding into the bottom third.

## 390 viewport

Shards are now the dominant visual: 60-90px triangles crowd the top third,
directly behind and above the headline. Headline wraps to four lines. Three CTAs
wrap to two rows.

- [ ] hero headline rag (390): "I build software / people / actually use. / Not
      coursework." Line 2 is the single orphaned word "people" at roughly 100px
      wide against a 334px line 1. A one-word line in the middle of a display
      headline is a typographic failure, not a break. Expected: a balanced 3 or 4
      line set, or an explicit <br> break at 390.
- [ ] hero CTA row (390): three pills wrap to 2 + 1, leaving "GitHub" centred and
      alone on the second row. Mobile was stacked, not designed. Expected at 390:
      decide which CTA disappears, or full-width stacked buttons.
- [ ] .hero-scrim (390): the scrim is radial-gradient(58% 44% at 50% 47%), an
      ellipse sized for a 16:9 frame. At 390x844 that resolves to roughly
      226x371px centred at (195,397), so the top of the four-line headline at
      y=245 sits out in the 0.24-alpha falloff. Measured result: #hero-heading >
      span at 1.07:1 against 3:1. Expected: a scrim keyed to the text box rather
      than to the viewport.
- [ ] shard density not tuned per width (390): the same particle count reads as
      invisible noise at 1440 and as a crowded foreground at 390, where several
      triangles are 60-90px against a 390px frame. Expected: count and near-plane
      scaled by viewport.
- [ ] shards over the nav (390): dark blue triangles at roughly (215,40) and
      (130,60) sit under the wordmark and the hamburger; measured 1.08:1 on the
      wordmark. Expected 4.5:1.
- [ ] mobile subtraction (390): nothing is removed at 390. The same eyebrow, the
      same headline, the same subhead, the same three CTAs, the same particle
      count. Expected: a decision about what disappears, what grows and what stays
      dominant.

## 390 full page

- [ ] work list tail invisible (390): in full-390.png the "Main Street Sites" row
      renders at roughly 45% opacity, the duplicate "Lydia" row at roughly 20%,
      the "Serbo-Croatian dictionary" row is absent entirely, and both exits ("See
      the work in full", "Or read about me") never appear. .reveal-up starts at
      opacity:0 / translateY(56px) and is restored only by an IntersectionObserver
      callback. Whatever the capture reason, the page's primary exit to /projects/
      is at opacity 0 in the artifact a reviewer would screenshot. Expected: the
      exit CTA visible without depending on an observer callback.
- [ ] dead band before contact (390): roughly 260px of empty ground between the
      last work row and the CONTACT eyebrow, because the invisible exits occupy
      it. Expected: no gap larger than the section padding it sits in.
- [ ] contact CTA row (390): four pills wrap 1 / 2 / 1, leaving "LinkedIn" alone
      on the last row. Second orphaned-button instance on the page. Expected: a
      designed stack at 390.
- [ ] email pill (390): "levibmackay@gmail.com" fills its pill nearly edge to
      edge at 15px in a 390px column. No breathing room left in the button.
- [ ] stat counters (390): the capture reads 35 / 467 / 5609 / 3.91 mid-count
      against the true 36 / 475 / 5709 / 3.98. A count-up animation on a GPA means
      the page displays a false GPA for the duration of the animation. Expected:
      no count-up on a figure that is a fact about a person.
- [ ] terminal window (390): .console-shell drops to height:270px and still holds
      two lines of text, so roughly 190px of the box is empty. Same defect as
      1440, not fixed by the breakpoint.

### What works at 390
- The stats grid is a designed 2x2 rather than a 4-up squeeze, and the work list
  reflows to stacked name-over-description cleanly.
- Reduced motion is genuinely handled in CSS: .reveal-up and .scrub-text .word
  are forced to opacity 1 / transform none under prefers-reduced-motion, and
  #project-stage un-pins to static. That is the correct gentling behaviour, not
  deletion.

## reduced-motion (1440)

- [ ] hero scene deleted, not gentled (reduced-motion 1440): scene.js line 30
      does `if (!canvas || reduceMotion) { canvas.remove(); return; }`. Under
      prefers-reduced-motion the shard sphere is removed from the DOM and nothing
      replaces it, so the reduced-motion visitor gets a pure #0a0a0c field with
      centred white type and one blue pill. The page's only memorable element is
      gone and the remainder is indistinguishable from a default Tailwind hero.
      This breaks the review-animations reduced-motion standard directly (gentle,
      do not delete). Expected: a rendered still of the assembled sphere as a
      poster image, or a static CSS shard field.
- [ ] no WebGL fallback (all widths): the same `canvas.remove()` path runs in the
      `catch` around `new WebGLRenderer`. A visitor with WebGL blocked or
      unavailable gets the identical empty page, with no poster. Expected: the
      same still image serves both cases.
- [ ] three window-control buttons at opacity 0 under reduced motion (measured by
      tb measure): the terminal's close / minimize / zoom controls report opacity
      0 after the animation is removed. Their labels are aria-only, so the affected
      controls are invisible but still focusable. Expected: visible after load.

## projects page (markup and CSS, not rendered)

Structure: a sticky #project-stage holding four cross-fading .media-layer
windows, against four .panel articles that alternate left / right. Media 0 is a
4-line terminal transcript, media 1 is an 8-row roadmap table, media 2 and 3 are
inline SVG line diagrams. All four sit in the same .mac-window chrome.

Verdict on "one system or patched": the panel CARDS are one system and a good
one. The panel MEDIA is patched, and it is measurable.

- [ ] mac-window heights (projects, 1440): .mac-window is height:auto at
      max-width min(720px,50vw). At 1440 the four windows resolve to roughly
      139px (terminal, 4 lines), 392px (roadmap table, 9 rows), 446px (lydia SVG,
      viewBox 800x460) and 572px (forge SVG, viewBox 800x600). The frame that is
      supposed to be the constant across the four panels changes size by 4.1x and
      resizes visibly on every cross-fade. Expected: one window height, or a
      stated escalation.
- [ ] SVG grids do not agree (projects): the Lydia diagram uses five 132x100
      boxes in a left-to-right chain at viewBox 800x460 (aspect 1.74); the FORGE
      diagram uses seven 168x54 boxes in a ring at viewBox 800x600 (aspect 1.33).
      Two diagrams shown twenty seconds apart in the same frame share no box
      module, no aspect and no topology. This is the single clearest "patched"
      signal on the page. Expected: one box module and one aspect across both.
- [ ] SVG title separators disagree (projects): "Lydia · the loop" versus
      "FORGE — the recommendation loop". Different separator, and the FORGE one is
      an em dash, which the project's own copy rules ban. Expected: the same
      separator, and no em dash.
- [ ] mac-bar naming convention broken (projects): three titles name a file or a
      shell ("tinylang · zsh", "minidb · ROADMAP.md", "forge · PRODUCT.md") and
      the fourth names a concept ("lydia · agent loop"). The swapped panel did not
      adopt the convention it landed in. Expected: "lydia · <file>" or the whole
      set converted to concepts.
- [ ] SVG background tone mismatch (projects): both diagrams paint
      <rect width=800 height=460 fill="#0a0a0c"> as their ground, inside a
      .mac-window whose background is #101014. Panels 2 and 3 therefore have a
      visibly darker window interior than panels 0 and 1. Expected: #101014 in
      the SVG, or a transparent SVG ground.
- [ ] duplicate DOM id (projects): both inline SVGs declare
      <marker id="arrow">. Duplicate IDs in one document; every marker-end
      url(#arrow) in the FORGE diagram resolves to the Lydia diagram's marker.
      Invalid HTML and a latent rendering bug. Expected: arrow-lydia /
      arrow-forge.
- [ ] SVG has no max-height (projects): .mac-window img and .mac-window video get
      max-height:60vh; inline <svg> is not in that selector, so the FORGE diagram
      is unclamped inside a 100svh stage. Not visible at 1440x900, but it is one
      short viewport away from overflowing.
- [ ] container rails (site-wide): the three pages use max-w 1000, 1100, 1200 and
      640, and each page picks a different secondary. At 1440 that is left rails
      at 144px, 194px and 244px with nothing on screen explaining the difference.
      Expected: one rail plus one deliberate exception.
- [ ] no real product media anywhere (site-wide): index.html and
      projects/index.html contain zero <img> and zero <video>. The whole site
      carries exactly one photograph, the portrait on /about/. Meanwhile
      /assets holds lydia-demo.mp4, swingos-demo.mp4, dictionary-demo.mp4 and
      poster sets for canvas-risk, lydia, dictionary and rexnest, none of which
      is referenced by any HTML or by main-B6nW-T6g.js. The recordings exist and
      were dropped from the markup. This is the named tell "no real product demos
      (the tell that the page has nothing to show)", and it is self-inflicted.
- [ ] "Also shipped" cards (projects): Canvas-Risk, Serbo-Croatian dictionary and
      SwingOS each get a 15px heading and a 14px grey paragraph, while their
      poster images sit unused in /assets. Expected: the posters in the cards.

### What works on the projects page
- The four panel cards are a genuinely rigorous system: eyebrow in a fixed
  grammar (language · domain · status), display-sm title, two body paragraphs,
  a Challenge / Approach / Current state definition list, a tag row, a View
  source link, in that order, four times, with the card alternating left and
  right against the media.
- The copy is the strongest asset on the site. "Its implementation was written
  with heavy AI assistance and the README says so plainly" is the kind of
  disclosure that buys credibility, and every "Current state" is honest about
  what is scaffolded versus shipped.
- Real numbers with sources behind them: 475 tests across 56 files on Python
  3.11-3.13, two merged outside PRs, phase 0 task 0.2 green. No invented metric.

## motion

The review-animations skill is set disable-model-invocation and refused the
Skill tool, so this section is my own read of the shipped motion values, not
that skill's verdict. It still needs to be run by hand.

- [ ] hero-line-in animates clip-path (motion, all widths):
      @keyframes hero-line-in{0%{clip-path:inset(0 0 100%)} to{clip-path:inset(0
      0 0%)}} at 1.4s on cubic-bezier(.22,1,.36,1), applied to four staggered
      .hero-line elements at delays 0.15 / 0.27 / 0.39 / 0.51s. clip-path is not
      a compositor-only property; this repaints every frame. Breaks the
      transform-and-opacity-only standard. Expected: a transform-based mask or a
      translate under overflow hidden.
- [ ] LCP gated behind the reveal (motion, 390): the h1 is the LCP element and it
      starts at clip-path:inset(0 0 100%), fully hidden. With a 0.39s delay plus
      a 1.4s reveal the headline is not fully painted until 1.79s after the
      animation starts, on top of the WebGL boot. Measured mobile LCP 5459ms
      against the 2500ms ship floor, mobile performance 0.73 against 0.90.
      Expected: content never waits on decoration.
- [ ] reduced motion deletes rather than gentles (motion): scene.js line 30,
      `if (!canvas || reduceMotion) { canvas.remove(); return; }`. Breaks the
      reduced-motion standard outright. See the reduced-motion section above.
- [ ] every reveal is the same fade-up (motion): reveal-card-in and
      reveal-heading-in differ only in translateY distance (24px vs 56px) and
      duration (0.9s vs 1.2s). Every non-hero element on all three pages enters
      the same way. Named tell: "everything entering on the same
      fade-up-on-scroll". Expected: at least the set-piece sections enter
      differently.
- [ ] no transform-origin anywhere (motion): zero transform-origin declarations
      in the compiled CSS, so every scale and translate runs from the element
      centre rather than from the point that triggered it. Breaks the
      transform-origin-at-the-trigger standard.
- [ ] card reveal duration (motion): 0.9s on reveal-card-in, fired seven times
      down the home work list and again on every fact-card and skill-card. An
      element seen this often should be faster. Expected: 0.4-0.5s for repeated
      list items, keeping 1.2-1.4s for the once-per-visit hero.

### What works in the motion
- One orchestrated page load with real staggered delays (0.15 / 0.27 / 0.39 /
  0.51s) rather than scattered micro-interactions, which is exactly the brief.
- Easing is consistent and correct: cubic-bezier(.22,1,.36,1), an expo-out, on
  all five animated rules. No ease-in anywhere, no default `ease`.
- UI transitions are 0.15s to 0.45s with 0.3s the mode, so the sub-300ms UI
  standard is met or near-met throughout.
- CSS-only for a plain HTML site, with a .motion-failed escape hatch that forces
  opacity 1 and transform none if the JS never runs.

## anti-slop signature audit (no DESIGN.md exists; judged against the list)

Committed (tells the page DOES have):
1. Centred hero of eyebrow label, huge headline, one-line subhead, side-by-side
   buttons. Verbatim, and repeated in the contact section.
2. A row of four big numbers with small captions, one of which is a GPA.
3. Every section in the same max-width container, nothing full-bleed.
4. One accent hue (#2997ff) at one intensity everywhere; the only second hue
   (#c4844a) is used by one rule.
5. Everything entering on the same fade-up-on-scroll.
6. Drop shadows (0 30px 80px, 0 40px 90px, 0 24px 60px) rendered on near-black,
   where they do nothing.
7. The same radius on every pill (9999px) and near-same on every panel (14px
   window, 20px media, 24px card).
8. No real product demos or photography: zero <img> and zero <video> on the two
   main pages.
9. Em dashes in copy, including baked into an SVG title.

Refused (tells the page correctly avoids):
- No Inter, Geist, Space Grotesk, Roboto or system stack. Archivo variable with
  a driven wdth axis plus Martian Mono, self-hosted and preloaded.
- No gradient headline word, no radial orb behind the hero, no pure white
  background, no dot grid, no glass, no neon, no pastel, no purple-on-black.
- No three feature cards in a row, no bento, no pricing tiers, no colored left
  stripe, no checkmark bullets.
- No Lucide icons, no sparkles, no emoji, no animated arrows.
- The terminal is live, not a decorative terminal window. This is the page's
  best refusal.
- No fake testimonials, no invented metric. Every figure is checkable.
- Section padding genuinely varies (--space-sm/md/lg).

Count: 9 committed. Three or more is the threshold at which the page reads as
machine-made. The type and the terminal are what keep it from reading that way
anyway.

## Verdict

Rework. The type system, the copy and the terminal are premium-tier. The
composition around them is the default composition, the one set-piece is deleted
for reduced-motion visitors, the mobile ship floor fails on both performance and
LCP, and the page ships a visible duplicate row and orphaned demo footage that
would have answered its own biggest weakness.

## Removed since previous iteration

No previous iteration exists in this directory (iter numbering not in use, and
.tenbillion/render/council is the only render). Nothing can be marked removed.
