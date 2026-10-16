# Contributing

## Add a repo to the catalog

1. Edit [`skills/hack-stack/catalog.yaml`](skills/hack-stack/catalog.yaml) and add one entry under
   the right category. The field reference is at the top of the file.
2. Link the **original** repo, never a fork.
3. Write `use_when` as the situation a team is in, not a description of the tool:
   "Your agent has to operate real websites", not "A browser automation library".
4. Only add `install` if you copied the command from the repo's own README.
5. Open a PR. The `catalog-check` action validates the entry and checks the repo on GitHub.

A repo belongs here if a team could get value from it within a 36-hour hackathon:

- It has a license and was updated in the last six months.
- Setup to "hello world" takes under an hour.
- It does not require a paid plan, waitlist, or approval to try. Free tiers are fine; say so
  in `needs_api_key`.

To check locally:

```bash
pip install -r scripts/requirements.txt
GITHUB_TOKEN=$(gh auth token) python scripts/check_catalog.py
```

## Improve a skill

Skills live in `skills/<name>/SKILL.md`. Keep them short: a team reads the output at 3 a.m.
If you change behavior, describe in the PR a real team situation where the old version gave
worse advice.

## Add an event preset

Copy `skills/hack-scope/events/calhacks-13.md`, fill in facts from the event's official site,
note the date you checked, and mark anything unannounced as TBA.
