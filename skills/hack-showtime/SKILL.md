---
name: hack-showtime
description: Use when a hackathon team needs slides for judging, an expo table, a final stage demo, or their Devpost submission. Builds a short, beautiful, offline HTML slide deck from HACK.md and PITCH.md that supports the live demo instead of replacing it, then exports it to PDF.
---

# Hack Showtime

Build the deck that sits next to the live demo. Judges score the product, not the slides: the
deck's job is to make the problem, the hard part, and the value impossible to miss in a few
seconds each. Show, don't just tell.

Output: `showtime/deck.html` (one self-contained file, works offline, any projector) and
`showtime/deck.pdf` for Devpost and sharing.

## No file access?
Ask the team to paste `HACK.md` and `PITCH.md`. Fetch the template from
https://raw.githubusercontent.com/georgeykalangi/calhacks-kit/main/skills/hack-showtime/deck-template.html
if you can browse, fill it in, and return the whole file in one code block to save as `deck.html`.
If you cannot fetch it, write the slide text and speaker notes only, one slide per section.

## Steps

### 1. Read the story
Read `HACK.md` (user, problem, journey, stack, architecture, honesty, team) and `PITCH.md`
(script and Q&A). The deck follows the pitch order. If either file is missing, ask for: the
one-liner, the user, the moment of value, the hard technical part, and what's mocked.
Suggest `/hack-pitch` first if there is no script yet.

### 2. Collect real visuals
Screenshots of the working product are the most important visual in the deck.
- Ask for 2-4 screenshots of the journey's key steps, saved in `showtime/img/`, plus the backup
  video if it exists. If the app is running and you can drive a browser, capture them yourself.
- Never draw or generate a mockup of a screen that does not exist. A deck that shows features
  the demo cannot back up loses the judges' trust.

### 3. Pick a theme
Read `themes.md` next to this file. First choice: build a theme from the product's own colors
and font, so the deck and the app look like one thing. Otherwise pick the preset that fits the
project's tone. One theme, one accent color.

### 4. Outline 6-7 slides
Each main slide earns its place by answering a judging criterion:

| # | Slide | Layout | Criterion |
|---|-------|--------|-----------|
| 1 | Name + one-liner | `layout-title` | Application |
| 2 | Live demo cue + screenshot or video backup | `layout-media` | Functionality |
| 3 | The problem: user + evidence | `layout-statement` | Application |
| 4 | How it works: architecture with the hard part highlighted | flow (`.node.key`) | Technical Complexity |
| 5 | What's new | columns or stats | Creativity |
| 6 | Impact and what's next | `layout-statement` or columns | Application |
| 7 | Team + disclosure | team | Honesty |

The demo comes second. Judges should see the product within 20 seconds. Add up to 3 appendix
slides after the team slide for likely Q&A (deeper architecture, evaluation results, limits),
never in the main flow.

### 5. Write like a poster, not a document
- Headlines are claims, not labels: "First-years study alone for weeks", not "Problem".
- One idea per slide. At most 25 words of body text. At most 3 points per slide.
- Every number has a source in the speaker notes. No invented statistics.
- The spoken words go in `<aside class="notes">`; the slide holds the proof.
- The team slide's disclosure line lists open-source and AI tools used and everything in the
  Honesty section of `HACK.md`.
- No emoji, no stock photos, no decorative AI art.

### 6. Build the deck
- Copy `deck-template.html` (next to this file) to `showtime/deck.html`.
- Replace the THEME block with the chosen theme. Set `<title>` to `Project | Event`.
- Fill the slides between the SLIDES markers using the template's layout classes:
  `layout-title`, `layout-statement`, `layout-split`, `layout-media`, `.flow` with `.node`
  and `.node.key`, `.cols`, `.stats`, `.band`, `.team`, `.disclosure`.
- Do not edit the ENGINE section. It handles scaling to any screen, keyboard and click
  navigation, slide numbers, speaker notes, and print layout.
- Use relative image paths (`img/demo.png`). Give every `<img>` an `alt` describing what the
  screenshot shows. Use `<video src="img/demo.mp4" controls muted playsinline>` for video.

### 7. Check every slide
First the automatic check. Opening the deck with `?check` marks every slide whose content runs
into the footer or past the edge. With Chrome installed:

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Windows/Linux: chrome or google-chrome
"$CHROME" --headless --disable-gpu --window-size=1920,1080 --dump-dom \
  "file://$PWD/showtime/deck.html?check" | grep -oE '<section [^>]*data-overflow="true"'
```

No output means no overflow. Then render each slide and look at it:

```bash
for n in $(seq 1 7); do   # one number per slide
  "$CHROME" --headless --disable-gpu --hide-scrollbars --window-size=1920,1080 \
    --screenshot="showtime/check-$n.png" "file://$PWD/showtime/deck.html#$n"
done
```

Fix overflow, collisions, and anything hard to read from 3 meters away. Fix by cutting words,
not by shrinking text below 28px. Monospace body fonts run wider, so recheck after any theme
change. Delete the `check-*.png` files when done.

Without Chrome, open `deck.html?check` in any browser: overflowing slides get a red border.

### 8. Export and share
```bash
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="showtime/deck.pdf" "file://$PWD/showtime/deck.html"
```
Without Chrome: open the deck, Print, Save as PDF, landscape, margins none, background graphics on.

Tell the team how to present it: open `deck.html` in a browser, press F for fullscreen, use the
arrow keys or click, press N for speaker notes. Add the PDF to the Devpost submission and the
repo. Add a Status log line to `HACK.md`.

## Need a different format?
- PowerPoint or Google Slides file required: use Anthropic's `pptx` skill from
  https://github.com/anthropics/skills with the same outline and writing rules.
- Animated, more elaborate HTML decks: see `frontend-slides` in the `/hack-stack` catalog.
