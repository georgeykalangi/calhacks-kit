---
name: hack-ship
description: Use in the last hours of a hackathon, before making a repo public, or before submitting to Devpost. Runs the pre-judging checklist (README, live URL or backup, demo account, sample data, value prop, architecture, track requirements, pitch roles, backup video), scans for leaked secrets, and drafts whatever is missing.
---

# Hack Ship

Make the project easy to run, easy to understand, and easy to trust before judges arrive.
Most judging losses are avoidable.

## No file access?
Ask the team to paste `HACK.md` and their README. Skip the commands and give them the checklist
and the secret-scan commands to run themselves.

## Steps

### 1. Secret scan first
Run this before anything else, and always before the repo is made public:

```bash
git ls-files | grep -E '(^|/)\.env$'
git grep -nE 'sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|AIza[0-9A-Za-z_-]{35}|xox[abprs]-[A-Za-z0-9-]{10,}'
git log -p --all | grep -nE 'sk-ant-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|AIza[0-9A-Za-z_-]{35}' | head
```

- A tracked `.env` file: remove it from git, add it to `.gitignore`, and keep `.env.example`.
- A key in the current files: move it to `.env`.
- A key anywhere in history that was ever pushed: **rotate the key now** at the provider.
  Rewriting history does not un-leak a pushed key.

Never print a found key in full. Show the file, line, and the first 6 characters.

### 2. Run the checklist
Verify each item with evidence (a file, a command that ran, a URL that loaded), not a teammate's
"yeah it's done". Mark `[x]` or `[ ]`.

| # | Item | How to verify | If missing |
|---|------|---------------|------------|
| 1 | README with setup | Follow it literally from a fresh clone in a temp dir | Draft it (see step 3) |
| 2 | Live URL or local backup | Open the URL in a private window | Deploy, or document local run plus video |
| 3 | Seeded demo account | Log in with the README credentials | Write a seed script; use fake data |
| 4 | Sample data ready | Journey works with the network API down or slow | Add a demo-mode fallback; disclose it |
| 5 | One-line value prop | It's at the top of the README | "<Product> helps <user> <do job> by <how>." |
| 6 | Architecture sketch | In README | Take it from HACK.md Stack |
| 7 | Track requirements verified | Each targeted track's rules checked | List gaps; fix or drop the track |
| 8 | Pitch roles assigned | Names in HACK.md Pitch | Run `/hack-pitch` |
| 9 | Backup video ready | A 60-90s recording of the journey exists | Screen-record the happy path now |

For the backup video, any screen recorder works. The `brag` and `hyperframes` repos in the
catalog can produce a polished one if there is time; a plain recording is enough.

### 3. Draft the README if missing
Sections: name and one-line value prop, demo link or video, the problem and user, how it works
(architecture sketch), setup in 5 steps or fewer, demo account, tech stack, what's mocked
(from HACK.md Honesty), team, and "Built at <event>" with the open-source and AI tools used.

### 4. Draft the submission
Fill the standard Devpost sections from HACK.md: Inspiration, What it does, How we built it,
Challenges we ran into, Accomplishments, What we learned, What's next. Disclose open-source
projects and AI coding tools used. Keep claims to what the demo actually shows.

### 5. Report
Show the checklist with `[x]`/`[ ]`, the secret-scan result, and the top three items to fix in
priority order. Add a Status log line to HACK.md.
