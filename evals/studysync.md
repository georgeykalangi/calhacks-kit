# Dry-run scenario: StudySync (over-scoped team)

Run each skill in order with these simulated answers. Each "Expect" line is what a correct run
must produce. Re-run after changing a skill.

## Team and clock
- Priya (React), Marcus (Python/FastAPI), Lin (first-timer, design + some JS)
- Now: Sat 08:00. Deadline: Sun 14:00. Judging: expo tables, 3 min, judges rotate.
- Track: Anthropic, "best use of Claude" (assume it requires the Claude API)

## /hack-scope
Pitch: "AI study buddy: matches study groups, summarizes notes, makes flashcards, has a voice
tutor, syncs Google Calendar." First answer to "who": "college students".

- Expect: pushback on "college students" until it becomes a specific user
  (e.g. first-years in an 800-person intro CS class, weeks 2-4).
- Expect: one journey of 3-5 steps (notes in -> stuck concepts -> matched group joined).
- Expect: summaries, flashcards, voice tutor, calendar sync, and login on the cut list.
- Expect: budget in clock times that accounts for sleep.

## /hack-stack
- Expect: picks the team already knows (React, FastAPI) over unfamiliar frameworks.
- Expect: the Anthropic SDK from the catalog, because the track requires it.
- Expect: no database beyond a seeded JSON file.
- Expect: the riskiest part named as consistency of concept labels across students, not only
  an API integration, with a 30-minute spike.

## Simulated build (commit these)
1. `api/main.py` with `/match` returning hardcoded concepts and matches, plus a committed `.env`
   containing `ANTHROPIC_API_KEY=sk-ant-api03-<fake>`
2. `web/src/Login.jsx` (Google OAuth), `web/src/Settings.jsx`
3. Remove `.env` from git, add it to `.gitignore`
4. `api/config.py` with `OPENAI_KEY = "sk-proj-<fake>"`, then delete it
5. `README.md` saying only `Run: npm start` (no package.json exists)

## /hack-check at Sun 04:00 (10h left). The team asks to add flashcards.
- Expect: phase Harden, flashcards refused.
- Expect: the unfinished journey treated as the only priority, not blocked as a "new feature".
- Expect: drift flagged (login and settings are on the cut list).
- Expect: hardcoded matches listed under Honesty.
- Expect: the Anthropic track flagged as unmet (Claude never called).
- Expect: Technical Complexity scored lowest.

## /hack-ship
- Expect: both fake keys found in history (the `sk-ant-` and `sk-proj-` keys), with "rotate now".
- Expect: current files clean, no tracked `.env`.
- Expect: README item fails on a fresh clone (`npm start` with no package.json).

## /hack-pitch
- Expect: a 3-minute script with the demo inside the first 20 seconds, plus a 30-second
  version for judges who arrive late, written to `PITCH.md`.
- Expect: the hardcoded parts disclosed in one plain sentence.

## /hack-showtime
Provide one screenshot of the match screen in `showtime/img/`.

- Expect: 7 slides in pitch order, demo second, team slide with the disclosure line.
- Expect: a theme built from the product's colors (first choice), not a random preset.
- Expect: no mockups of screens that do not exist; the real screenshot on the demo slide.
- Expect: `deck.html?check` reports no overflow in the chosen theme. The original slide 5 copy
  ("Matched on confusion, not calendars" plus longer column text) overflows in every theme and
  must be cut, not shrunk.
- Expect: `deck.pdf` has exactly 7 pages at 16:9.
