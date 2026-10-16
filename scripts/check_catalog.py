"""Validate skills/hack-stack/catalog.yaml and check each repo on GitHub.

Errors (exit 1): schema problems, duplicate repos, repos that are missing, archived, or forks.
Warnings: no detected license, no push in the last STALE_DAYS days.

Usage: GITHUB_TOKEN=... python scripts/check_catalog.py [--offline]
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

CATALOG_PATH = Path(__file__).resolve().parent.parent / "skills" / "hack-stack" / "catalog.yaml"
STALE_DAYS = 180
REQUIRED_FIELDS = {"repo", "category", "use_when", "setup_minutes", "needs_api_key", "license", "demo_value"}
OPTIONAL_FIELDS = {"install", "note"}
CATEGORIES = {
    "agent-workflow", "design-ui", "app-framework", "backend", "agents-data",
    "voice", "vision", "code-understanding", "demo-video", "presentation", "discovery",
}
API_KEY_LEVELS = {"none", "free-tier", "llm", "paid"}
DEMO_VALUES = {"low", "medium", "high"}


def validate_entry(entry: dict) -> list[str]:
    repo = entry.get("repo", "<missing repo>")
    errors = []
    missing = REQUIRED_FIELDS - entry.keys()
    unknown = entry.keys() - REQUIRED_FIELDS - OPTIONAL_FIELDS
    if missing:
        errors.append(f"{repo}: missing fields {sorted(missing)}")
    if unknown:
        errors.append(f"{repo}: unknown fields {sorted(unknown)}")
    if entry.get("category") not in CATEGORIES:
        errors.append(f"{repo}: category must be one of {sorted(CATEGORIES)}")
    if entry.get("needs_api_key") not in API_KEY_LEVELS:
        errors.append(f"{repo}: needs_api_key must be one of {sorted(API_KEY_LEVELS)}")
    if entry.get("demo_value") not in DEMO_VALUES:
        errors.append(f"{repo}: demo_value must be one of {sorted(DEMO_VALUES)}")
    if not isinstance(entry.get("setup_minutes"), int) or entry["setup_minutes"] < 0:
        errors.append(f"{repo}: setup_minutes must be a non-negative integer")
    if not isinstance(entry.get("repo"), str) or entry["repo"].count("/") != 1:
        errors.append(f"{repo}: repo must look like owner/name")
    return errors


def fetch_repo(repo: str, token: str | None) -> dict | None:
    request = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    request.add_header("Accept", "application/vnd.github+json")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def check_remote(repo: str, token: str | None) -> tuple[list[str], list[str]]:
    data = fetch_repo(repo, token)
    if data is None:
        return [f"{repo}: not found on GitHub"], []
    errors, warnings = [], []
    if data.get("archived"):
        errors.append(f"{repo}: archived upstream")
    if data.get("fork"):
        errors.append(f"{repo}: is a fork; link the original ({data['parent']['full_name']})")
    if not data.get("license"):
        warnings.append(f"{repo}: no license detected")
    pushed_at = datetime.fromisoformat(data["pushed_at"].replace("Z", "+00:00"))
    age_days = (datetime.now(timezone.utc) - pushed_at).days
    if age_days > STALE_DAYS:
        warnings.append(f"{repo}: no push in {age_days} days")
    return errors, warnings


def main() -> int:
    offline = "--offline" in sys.argv
    token = os.environ.get("GITHUB_TOKEN")
    catalog = yaml.safe_load(CATALOG_PATH.read_text())
    entries = catalog.get("entries", [])

    errors, warnings = [], []
    seen = set()
    for entry in entries:
        errors.extend(validate_entry(entry))
        repo = entry.get("repo")
        if repo in seen:
            errors.append(f"{repo}: duplicate entry")
        seen.add(repo)

    if not offline and not errors:
        for repo in sorted(seen):
            repo_errors, repo_warnings = check_remote(repo, token)
            errors.extend(repo_errors)
            warnings.extend(repo_warnings)

    for warning in warnings:
        print(f"WARN  {warning}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"{len(entries)} entries, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
