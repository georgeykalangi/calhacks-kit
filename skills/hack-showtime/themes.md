# Deck themes

Replace the THEME block in `deck-template.html` with one of these. Every theme uses fonts that are
already installed on macOS and Windows, so the deck renders offline on any laptop.

First choice: **match the product.** If the team's app has its own colors and font, build a theme
from them (see the last section). A deck that looks like the product makes the demo feel finished.

All text and background pairs below meet WCAG AA contrast (4.5:1 or better).

## Field Notes: editorial, calm, confident
Sage paper, black ink, condensed headlines, mono body. Works for almost any project.

```css
:root {
  --bg: #DCE5D3; --surface: #E9EFE3; --ink: #111111; --muted: #3B4A39;
  --accent: #1F3D2B; --accent-ink: #F4F7F0; --line: #111111;
  --band: #111111; --band-ink: #F4F7F0; --frame: 2px;
  --font-display: "Avenir Next Condensed", "Helvetica Neue", "Arial Narrow", Impact, sans-serif;
  --font-body: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --display-weight: 800; --display-case: uppercase;
}
```

## Night Shift: dev tools, infra, security, AI agents
Near-black, one electric accent. Looks good on dim stages and projectors.

```css
:root {
  --bg: #0E1116; --surface: #161B22; --ink: #F0F3F6; --muted: #A4AEB9;
  --accent: #C6F432; --accent-ink: #0E1116; --line: #3A434E;
  --band: #C6F432; --band-ink: #0E1116; --frame: 0px;
  --font-display: "SF Pro Display", "Segoe UI", system-ui, sans-serif;
  --font-body: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --display-weight: 800; --display-case: none;
}
```

## Paper and Ink: social impact, education, health, civic
Warm off-white, black type, a single red accent. Serious without being cold.

```css
:root {
  --bg: #F6F3EE; --surface: #FFFFFF; --ink: #161616; --muted: #4A4643;
  --accent: #C8102E; --accent-ink: #FFFFFF; --line: #161616;
  --band: #161616; --band-ink: #F6F3EE; --frame: 0px;
  --font-display: Georgia, "Times New Roman", serif;
  --font-body: "Helvetica Neue", Arial, sans-serif;
  --display-weight: 700; --display-case: none;
}
```

## Blueprint: hardware, robotics, data, climate
Deep blue with technical-drawing lines.

```css
:root {
  --bg: #0B2545; --surface: #12315C; --ink: #EEF4ED; --muted: #A9BCD0;
  --accent: #8DE4FF; --accent-ink: #0B2545; --line: #5C7CA3;
  --band: #EEF4ED; --band-ink: #0B2545; --frame: 2px;
  --font-display: "Avenir Next Condensed", "Helvetica Neue", "Arial Narrow", Impact, sans-serif;
  --font-body: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --display-weight: 700; --display-case: uppercase;
}
```

## Sunrise: consumer, social, creative, games
Cream with a warm orange. Friendly and energetic.

```css
:root {
  --bg: #FFF4E6; --surface: #FFFFFF; --ink: #1F1300; --muted: #5C4A33;
  --accent: #B83A00; --accent-ink: #FFFFFF; --line: #1F1300;
  --band: #1F1300; --band-ink: #FFF4E6; --frame: 0px;
  --font-display: "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --font-body: "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --display-weight: 800; --display-case: none;
}
```

## Build a theme from the product
1. Find the app's colors and font: `tailwind.config.*`, CSS variables in `globals.css` or
   `index.css`, or a theme file in the component library.
2. Map them: page background to `--bg`, card background to `--surface`, body text to `--ink`,
   secondary text to `--muted`, primary button color to `--accent`, its text to `--accent-ink`.
3. If the app uses a web font, put it first in the stack and keep system fallbacks after it.
   Do not load it from the network; the deck must work offline.
4. Check contrast of `--ink` on `--bg`, `--muted` on `--bg`, and `--accent-ink` on `--accent`
   (4.5:1 minimum). Darken or lighten until they pass.
