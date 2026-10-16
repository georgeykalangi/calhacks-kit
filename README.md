# calhacks-kit

Six Claude Code skills that take a hackathon team from idea to judged demo, plus a curated,
link-checked catalog of open-source repos worth using in a 36-hour build.

> **Unofficial.** Made by a Cal Hacks mentor for Cal Hacks 13.0 hackers. Not affiliated with or
> endorsed by Cal Hacks. When this kit and the organizers disagree, the organizers win.

## The skills

| Skill | When to run it | What you get |
|-------|----------------|--------------|
| `/hack-scope` | Hour 0-2 | The five problem questions, a deadline clock, one end-to-end journey, a cut list, and `HACK.md` |
| `/hack-stack` | Hour 1-3 | 3-5 picks from the [catalog](skills/hack-stack/catalog.yaml), the riskiest integration to spike, an architecture sketch |
| `/hack-check` | Every few hours | A score against the four judging criteria, scope-drift and honesty checks, rescue mode, feature freeze near the deadline |
| `/hack-ship` | Final hours | Secret scan, the pre-judging checklist verified with evidence, README and Devpost drafts |
| `/hack-pitch` | Before judging | A timed live-demo script, pitch roles, answers to likely judge questions |
| `/hack-showtime` | After the pitch is written | A short, themed HTML slide deck built around the live demo, checked for overflow, exported to PDF for Devpost |

![Slides from /hack-showtime for a fictional team, in three themes](examples/studysync/preview.png)

*`/hack-showtime` output for StudySync, a fictional team from the [dry-run scenario](evals/studysync.md).
Open [`examples/studysync/deck.html`](examples/studysync/deck.html) locally, press F for fullscreen and N for notes.*

Every skill reads and writes **`HACK.md`** at the root of your project. It is the team's shared
plan: commit it, and every teammate's Claude session works from the same scope, stack, and clock.

## Install

> **Install before you arrive.** Event wifi is slow with 2,000 people on it. Every teammate
> installs on their own laptop; the skills are plain Markdown, so there is nothing to build.

Pick the option that matches the tool you use:

| You use | Option | Command names |
|---------|--------|---------------|
| Claude Code | [A. Plugin](#a-claude-code-plugin-recommended) (recommended) | `/calhacks-kit:hack-scope` ... |
| Claude Code, want short names | [B. Copy the skills](#b-claude-code-short-names) | `/hack-scope` ... |
| Cursor, Codex, Windsurf, or another agent | [C. `npx skills`](#c-cursor-codex-and-other-agents) | depends on the agent |
| A chat window (free claude.ai, any LLM) | [D. Paste a prompt](#d-any-chat-no-install) | none |

### A. Claude Code plugin (recommended)

In Claude Code, send these as **two separate messages**:

```
/plugin marketplace add georgeykalangi/calhacks-kit
```
```
/plugin install calhacks-kit@calhacks-kit
```

Or run the same thing from your terminal:

```bash
claude plugin marketplace add georgeykalangi/calhacks-kit
claude plugin install calhacks-kit@calhacks-kit
```

Start a new Claude Code session, then check it worked:

```bash
claude plugin details calhacks-kit@calhacks-kit   # should list "Skills (6)"
```

Plugin skills are namespaced: type `/calhacks-kit:hack-scope`, `/calhacks-kit:hack-stack`, and so on.
You can also just describe what you need ("help us scope our idea") and Claude picks the right skill.
The kit adds about 500 tokens to each session until a skill runs.

### B. Claude Code, short names

```bash
git clone https://github.com/georgeykalangi/calhacks-kit
mkdir -p ~/.claude/skills
cp -r calhacks-kit/skills/* ~/.claude/skills/
```

Start a new session and type `/hack-scope`. To install for one project only, copy into
`<your-project>/.claude/skills/` instead.

### C. Cursor, Codex, and other agents

Needs Node.js. From your project folder:

```bash
npx skills add georgeykalangi/calhacks-kit
```

It asks which skills and which agents to install for. To skip the questions:

```bash
npx skills add georgeykalangi/calhacks-kit --skill '*' -a claude-code cursor codex -y
```

This writes the skills to `.agents/skills/` (read by Cursor and Codex) and links them into
`.claude/skills/`. Add `-g` to install for your user instead of this project.

### D. Any chat, no install

Each skill works as a pasted prompt. This copies one skill to your clipboard:

```bash
npx skills use georgeykalangi/calhacks-kit@hack-scope | pbcopy    # macOS
npx skills use georgeykalangi/calhacks-kit@hack-scope | clip      # Windows
npx skills use georgeykalangi/calhacks-kit@hack-scope | xclip -selection clipboard   # Linux
```

Paste it into the chat, then describe your project. Without Node.js, open the skill's
[`SKILL.md`](skills/hack-scope/SKILL.md) on GitHub, click **Raw**, and copy everything.
A chat cannot read your files, so the skill asks you to paste `HACK.md` in and gives you the
updated version to save back to your repo.

## Quick start

```bash
cd your-project
claude
```
```
/calhacks-kit:hack-scope We are 3 people, deadline is Sunday 2pm. Idea: <your idea>
```

It asks the five problem questions, cuts the idea to one journey, and writes `HACK.md`.
**Commit `HACK.md` and push it.** Teammates pull it, and their sessions now share the same plan.
Then follow the timeline below.

## Update and uninstall

| | Plugin (A) | Copied skills (B) | `npx skills` (C) |
|---|---|---|---|
| Update | `claude plugin marketplace update calhacks-kit` then `claude plugin update calhacks-kit@calhacks-kit` | `git pull` in the clone, copy again | `npx skills update` |
| Uninstall | `claude plugin uninstall calhacks-kit@calhacks-kit` | delete `~/.claude/skills/hack-*` | `npx skills remove` |

## Troubleshooting

- **`/hack-scope` isn't found after installing the plugin.** Plugin skills have a prefix:
  use `/calhacks-kit:hack-scope`, or install with option B for short names.
- **The skills don't show up at all.** Start a new session. Check with `claude plugin list`
  (plugin) or `ls ~/.claude/skills` (copied).
- **`npx skills add` asks a lot of questions.** Use the `-y` command in option C.
- **GitHub is unreachable on event wifi.** Get the folder from a teammate (AirDrop or USB) and use
  option B: the skills are plain files and work offline.
- **Before you trust any skill**, read it. They are short Markdown files in [`skills/`](skills/)
  and run with your agent's permissions.

## A 36-hour run

```
Hour 0   /hack-scope   -> HACK.md: user, problem, one journey, cut list
Hour 1   /hack-stack   -> stack picks, spike the riskiest integration
Hour 6   /hack-check   -> scores, drift, honesty
Hour 18  /hack-check   -> harden phase begins
Hour 24  /hack-check   -> feature freeze
Hour 30  /hack-ship    -> secret scan, checklist, README, submission draft
Hour 32  /hack-pitch   -> script, roles, Q&A
Hour 33  /hack-showtime -> deck.html + deck.pdf, then rehearse three times
```

## The rules still apply

Cal Hacks does not allow projects started before the event. This kit contains **no project
code**: only process, checklists, and links. Write your project during the event, and disclose
the open-source projects and AI tools you used in your submission.

AI can help you build faster, but your team must understand, review, and test what it writes.
Judges will ask.

## The catalog

[`skills/hack-stack/catalog.yaml`](skills/hack-stack/catalog.yaml) lists about 30 repos across
agent workflow, UI, app frameworks, backend, agents and data, voice, vision, code understanding,
and demo video. Each entry records when to use it, rough setup minutes, whether it needs an API
key, its license, and how much judges will see it.

Every link points to the original repo, not a fork. A weekly GitHub Action fails on repos that
disappear, get archived, or turn out to be forks, and warns on missing licenses and stale repos.
Review each repo's install steps, license, and permissions before you use it.

## Share what you build

- **Add a repo to the catalog**: see [CONTRIBUTING.md](CONTRIBUTING.md). Small PRs are welcome
  during the event.
- **Built something with the kit?** Add it to [SHOWCASE.md](SHOWCASE.md) after judging.
- **A skill gave bad advice?** [Open an issue](../../issues/new?template=bad-advice.md).

## Credits

Based on the *Cal Hacks 13.0: Build Something That Matters* hacker guide and the Cal Hacks
Winning Guide by [George Kalangi](https://github.com/georgeykalangi), Cal Hacks 12.0 mentor.
Catalog entries belong to their authors under their own licenses.

## License

[MIT](LICENSE)
