---
name: hack-check
description: Use every few hours during a hackathon, when a team is stuck on a blocker, or when they want to add a feature late. Scores the current build against the four judging criteria, flags scope drift and anything mocked that must be disclosed, and switches to rescue mode or feature-freeze mode when the clock demands it. Updates HACK.md.
---

# Hack Check

A progress check a mentor would give at the team's table: honest, short, and focused on what
raises the score before the deadline.

## No file access?
Ask the team to paste `HACK.md`, their recent commit messages, and what currently works.

## Steps

### 1. Gather evidence
- Read `HACK.md` for the deadline, MVP journey, and cut list.
- Read `git log --oneline -20` and skim what changed.
- If there is a run or test command, run it. Evidence beats the team's description.

### 2. Pick the phase from the clock
Get the current time with `date` and compare it with the deadline in `HACK.md`.

| Hours left | Phase | Behavior |
|------------|-------|----------|
| more than 12 | Build | Push to finish the journey end to end, even if rough. |
| 6 to 12 | Harden | No new features. Fix the happy path, seed data, deploy. |
| under 6 | Freeze | Refuse new features. Only demo-critical fixes, README, video, pitch. |

Finishing the MVP journey is never a "new feature". If the journey does not work end to end by
Harden or Freeze, it is the only priority: go straight to rescue mode (step 6) and shrink it
until it runs. A "new feature" is anything outside the journey or on the cut list.

In Harden or Freeze, if the team asks for a new feature, say no and name what to do instead.

### 3. Score the four criteria
Score each 1-5 with one line of evidence and one concrete action:

| Criterion | Score | Evidence | Next action |
|-----------|-------|----------|-------------|
| Application | | | |
| Functionality / Quality | | | |
| Creativity | | | |
| Technical Complexity | | | |

Name the weakest criterion and the single highest-leverage fix for it.

Also check each targeted track in `HACK.md`. If the build does not yet meet a track's
requirement (for example, the required API is never actually called), say so explicitly.

### 4. Check scope drift
Compare recent work against the MVP journey. If time went into items on the cut list, or into
things the demo never touches, say how many hours it cost and steer back.

### 5. Check honesty
- List anything mocked, hardcoded, or faked. It must appear in the Honesty section of `HACK.md`
  and be disclosed in the demo. Judges respect disclosure; they punish discovery.
- Ask the team three questions a judge would ask about the hard part. If no teammate can explain
  how the AI-generated code works, schedule 20 minutes for the team to walk through it together.
  Understanding the code is the team's job, not the assistant's.

### 6. Rescue mode
Use when the team says they are stuck, or one blocker has eaten more than 45 minutes.
Walk the options in this order and timebox the choice to 5 minutes:
1. **Cut**: can the journey work without this? Move it to the cut list.
2. **Swap**: is there a simpler library, API, or hosted service that does it?
3. **Fake with disclosure**: seed the data or stub the call so the demo works, and record it
   under Honesty.
Then set a timebox for the chosen path. If it fails, move to the next option.

### 7. Update HACK.md
Append a Status log line: time, phase, weakest criterion, next action. Update Honesty.

Keep the reply under 200 words plus the table. End with the one thing to do next.
