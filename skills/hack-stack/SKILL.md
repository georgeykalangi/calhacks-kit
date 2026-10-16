---
name: hack-stack
description: Use after the MVP is scoped, or when a hackathon team asks which framework, API, repo, or Claude skill to use. Recommends a small stack from a curated catalog of open-source repos based on the MVP, the team's skills, the hours left, and the sponsor tracks they target. Writes the Stack and architecture sketch into HACK.md.
---

# Hack Stack

Pick the fewest tools that get the one journey working. Every new dependency costs setup time
the team does not have.

## No file access?
If you are a pasted prompt, ask the team to paste their `HACK.md`. Use the catalog at
https://github.com/georgeykalangi/calhacks-kit/blob/main/skills/hack-stack/catalog.yaml if you can
browse; otherwise recommend from what you know and mark each pick "not from catalog, verify".

## Steps

### 1. Read the plan
Read `HACK.md`: the MVP journey, team strengths, hours remaining, tracks targeted. If there is no
`HACK.md`, tell the team to run `/hack-scope` first, or ask for those four facts directly.

### 2. Read the catalog
Read `catalog.yaml` next to this file. Each entry has `use_when`, `setup_minutes`,
`needs_api_key`, `license`, and `demo_value`. Treat setup times as rough estimates.

### 3. Recommend 3-5 picks
Rules:
- Prefer what the team already knows. A familiar framework beats a better unfamiliar one.
- Total setup time should stay under 10% of the hours remaining.
- Prefer tools with free tiers or no keys. Flag anything needing a paid key, a waitlist, or approval.
- Pick at most two agent-workflow skills. More skills means more context and slower sessions.
- Flag AGPL licenses if the team mentions continuing the project as a company.
- If a sponsor track requires a specific API, that API is part of the stack, not optional.
- You may suggest tools outside the catalog. Mark them "not in catalog, verify before relying on it".

For each pick give: what it does for this MVP, setup minutes, key needed, and the install command
only if you are sure of it. Otherwise point to the repo README.

### 4. Name the riskiest part
Pick the one thing most likely to sink the demo. It can be an integration (an API they have
never used, real-time audio, hardware, auth) or an assumption about results (will the model's
output be consistent enough to match, rank, or classify on?). Tell the team to spike it for
30 minutes with real inputs before building around it. If the spike fails, change the approach
now, not at hour 30.

### 5. Set up secrets safely
Before any key is used, make sure the repo has:
- `.env` listed in `.gitignore`
- `.env.example` with variable names and no values
Hackathon repos go public for judging. A key committed at hour 3 is leaked at hour 36.

### 6. Write HACK.md
Fill the Stack section: picks with one-line reasons, the riskiest integration, and a simple
architecture sketch (ASCII or Mermaid) of user -> frontend -> backend -> model/API/data.
`/hack-ship` and `/hack-pitch` reuse this sketch. Add a Status log line.

Finish with the stack in one line and "Next: spike <riskiest integration>, then build the journey".
