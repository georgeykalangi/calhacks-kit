---
name: hack-scope
description: Use at the start of a hackathon, or whenever a team is debating ideas or adding features, to turn an idea into the smallest MVP they can build, demo, and defend before the deadline. Sets the deadline clock, asks the five problem questions, cuts scope to one end-to-end journey, and writes HACK.md.
---

# Hack Scope

Turn a raw idea into one end-to-end journey the team can finish. The output is `HACK.md` at the
repo root. Every other calhacks-kit skill reads it, so all teammates' sessions share one plan.

Be a direct mentor, not a cheerleader. A clear "cut that" now saves the team ten hours later.

## No file access?
If you are running as a pasted prompt in a chat, do every step below, then output the finished
`HACK.md` in one code block and tell the team to save it at the root of their repo.

## Steps

### 1. Load context
- If `HACK.md` already exists, read it and refine it. Never overwrite a teammate's plan silently.
- Copy `HACK.template.md` (next to this file) as the starting structure.
- If the team is at Cal Hacks, read `events/calhacks-13.md` (next to this file) and fill the
  Event section from it.

### 2. Start the clock
Ask for the submission deadline, the judging time, team size, and each person's strengths.
Compute hours remaining and propose a budget:

| Phase | Share | Goal |
|-------|-------|------|
| Build | 60% | the one journey works end to end, ugly is fine |
| Harden | 15% | happy path never breaks, seeded data, deploy |
| Demo prep | 15% | README, backup video, pitch rehearsal |
| Buffer | 10% | something will break |

If fewer than 12 hours remain, say so plainly and shrink the journey to 2-3 steps.

### 3. Ask the five questions
Ask one at a time. Push back on vague answers.
1. Who experiences this problem? ("Students" is vague. "First-years trying to find a study group
   in week two" is a user.)
2. Why is it worth solving? Ask for a number, a story, or personal experience.
3. What makes our approach different from what exists?
4. Can we demonstrate the value in two minutes?
5. What is the smallest version we can actually build?

### 4. Test the idea against the judging criteria
Run these four tests and report pass or fail with one line each:
- **Application**: can you name the user and the moment they would use it?
- **Functionality**: can the core journey run live without a teammate narrating around gaps?
- **Creativity**: is there one thing a judge has not seen ten times today?
- **Technical complexity**: is there a hard part beyond "we call an LLM API"? If not, suggest one
  that serves the user (a pipeline, real-time input, a tricky integration, an evaluation).

### 5. Cut to one journey
List every feature the team mentioned. Pick one journey of 3-5 user steps that ends in a visible
moment of value. Everything the demo does not touch goes on the Cut list with a one-line reason.
Login, settings, and onboarding screens are almost always cuts. Use a seeded demo account instead.

### 6. Check the rules
- If the team wants to continue a project they started before the event, stop and tell them most
  hackathons, including Cal Hacks, forbid it. Ideation beforehand is fine; implementation is not.
- Public libraries, APIs, and starter templates are normal, but record them so the submission
  can disclose them.

### 7. Write HACK.md
Fill in Event, Team, Problem, MVP, and Cut list. Leave Stack for `/hack-stack`. Add the first
Status log line with the time and "Scoped MVP".

Finish with: hours remaining, the one journey in a single sentence, and "Next: run /hack-stack".
