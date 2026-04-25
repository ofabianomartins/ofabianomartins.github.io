#!/usr/bin/env python3
"""
Post a short announcement for new Zola content to X (Twitter) and LinkedIn.
Assumes this repository uses Zola with optional multilingual index.LANG.md files.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

# --- git / zola path helpers


def get_changed_paths(repo: Path, before: str, after: str) -> list[str]:
    """List paths changed in the range [before, after], or the single commit on empty/initial before."""
    before = (before or "").strip()
    if not before or re.fullmatch(r"0{40,}", before):
        r = subprocess.run(
            ["git", "-C", str(repo), "show", "--name-only", "--pretty=format:", after],
            check=True,
            capture_output=True,
            text=True,
        )
    else:
        r = subprocess.run(
            ["git", "-C", str(repo), "diff", "--name-only", f"{before}..{after}"],
            check=True,
            capture_output=True,
            text=True,
        )
    return [l.strip() for l in r.stdout.splitlines() if l.strip()]


def content_post_dirs_from_paths(paths: list[str]) -> list[Path]:
    """
    Deduplicate content subdirs (skip _index*).
    e.g. content/porquerust/index.md -> content/porquerust
    """
    out: set[str] = set()
    for p in paths:
        p = p.replace(os.sep, "/")
        m = re.match(r"^content/([^/]+)/index\.", p, re.I)
        if m and not m.group(1).startswith("_"):
            out.add(f"content/{m.group(1)}")
    return [Path(s) for s in sorted(out)]


def parse_front_matter(path: Path) -> dict[str, Any] | None:
    raw = path.read_text(encoding="utf-8")
    if not raw.lstrip().startswith("+++"):
        return None
    m = re.match(
        r"^\+{3}\s*([\s\S]+?)\+{3}\s*",
        raw.lstrip(),
    )
    if not m:
        return None
    try:
        return tomllib.loads(m.group(1))
    except Exception:
        return None


def post_url(
    base: str,
    slug: str,
    file_path: str,
) -> str:
    """Zola: default language has no code prefix; index.LANG.md uses that language's code in path."""
    m = re.match(
        r"^content/[^/]+/index\.([a-z0-9-]+)\.md$",
        file_path.replace(os.sep, "/"),
        re.I,
    )
    if m and m.group(1).lower() not in ("md",):
        lang = m.group(1).lower()
        path = f"{lang}/{slug}/" if not slug.startswith(f"{lang}/") else f"{slug}/"
    else:
        path = f"{slug}/"
    return urljoin(base.rstrip("/") + "/", path)


def pick_representative_file_for_url(repo: Path, cdir: Path) -> tuple[Path, str]:
    """(path, slug) using first index*.md; slug from TOML or directory name."""
    cdirp = repo / cdir
    for name in ("index.md",):
        f = cdirp / name
        if f.is_file():
            fm = parse_front_matter(f) or {}
            return f, (fm.get("slug") or cdir.name) or cdir.name
    for f in sorted(cdirp.glob("index.*.md")):
        fm = parse_front_matter(f) or {}
        return f, (fm.get("slug") or cdir.name) or cdir.name
    return cdirp / "index.md", cdir.name


def build_public_url(
    base: str,
    repo: Path,
    cdir: Path,
) -> tuple[str, str]:
    """(url, title)"""
    rep, slug = pick_representative_file_for_url(repo, cdir)
    rel = str(rep.relative_to(repo))
    fm = parse_front_matter(rep) or {}
    title = (fm.get("title") or slug) or cdir.name
    url = post_url(base, str(slug).strip(), rel)
    return url, str(title).strip()


# --- X / Twitter


def post_twitter(
    text: str,
) -> None:
    import requests
    from requests_oauthlib import OAuth1

    key = os.environ.get("TWITTER_API_KEY", "").strip()
    key_secret = os.environ.get("TWITTER_API_KEY_SECRET", "").strip()
    token = os.environ.get("TWITTER_ACCESS_TOKEN", "").strip()
    token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET", "").strip()
    if not all([key, key_secret, token, token_secret]):
        print("announce_social: skipping X: missing one of TWITTER_* env vars", file=sys.stderr)
        return
    if len(text) > 250:
        text = text[:247] + "…"
    auth = OAuth1(key, key_secret, token, token_secret)
    r = requests.post(
        "https://api.twitter.com/2/tweets",
        json={"text": text},
        auth=auth,
        timeout=30,
    )
    r.raise_for_status()
    print("X: posted", r.json().get("data", {}).get("id", "?"))


# --- LinkedIn


def post_linkedin(
    text: str,
    article_url: str,
    title: str,
) -> None:
    import requests

    token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "").strip()
    author = os.environ.get("LINKEDIN_PERSON_URN", "").strip()
    if not token or not author:
        print(
            "announce_social: skipping LinkedIn: LINKEDIN_ACCESS_TOKEN or LINKEDIN_PERSON_URN not set",
            file=sys.stderr,
        )
        return
    if not author.startswith("urn:li:person:"):
        author = f"urn:li:person:{author}" if author.isdigit() else author
    # Member UGC: https://learn.microsoft.com/linkedin/consumer/integrations/self-serve/share-on-linkedin
    li_version = os.environ.get("LINKEDIN_VERSION", "202404")
    body = {
        "author": author,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text[:3000]},
                "shareMediaCategory": "ARTICLE",
                "media": [
                    {
                        "status": "READY",
                        "originalUrl": article_url,
                        "title": {"text": title[:200]},
                    }
                ],
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        },
    }
    r = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        json=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
            "Linkedin-Version": li_version,
        },
        timeout=30,
    )
    r.raise_for_status()
    print("LinkedIn: ok", r.headers.get("X-Restli-Id", "?"))


def main() -> int:
    before = os.environ.get("ANNOUNCE_GIT_BEFORE", "")
    after = os.environ.get("ANNOUNCE_GIT_SHA", os.environ.get("GITHUB_SHA", ""))
    if not after:
        print("announce_social: no GITHUB_SHA / ANNOUNCE_GIT_SHA; skip", file=sys.stderr)
        return 0
    base = (os.environ.get("SITE_BASE_URL", "") or "").strip()
    if not base:
        print("announce_social: SITE_BASE_URL not set; skip", file=sys.stderr)
        return 0

    repo = Path(
        os.environ.get("GITHUB_WORKSPACE")
        or subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
    )
    try:
        paths = get_changed_paths(repo, before, after)
    except subprocess.CalledProcessError as e:
        print("announce_social: git error:", e, file=sys.stderr)
        return 0
    cdirs = content_post_dirs_from_paths(paths)
    if not cdirs:
        print("announce_social: no new content/ post paths in this range; nothing to do")
        return 0
    for cdir in cdirs:
        if not (repo / cdir / "index.md").is_file() and not list(
            (repo / cdir).glob("index.*.md")
        ):
            continue
        url, title = build_public_url(base, repo, cdir)
        x_text = f"Novo post: {title}\n{url}"
        li_text = f"Novo no blog: {title} — {url}"
        try:
            post_twitter(x_text)
        except Exception as e:  # noqa: BLE001
            print("announce_social: X error:", e, file=sys.stderr)
        try:
            post_linkedin(li_text, url, title)
        except Exception as e:  # noqa: BLE001
            print("announce_social: LinkedIn error:", e, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
