#!/usr/bin/env python3
"""Re-sync the governance ledgers (SUBMITTED.md, COMMUNITY_SUBMISSIONS.md)
from README.md, the source of truth.

The ledgers were written for an earlier, smaller version of the list
(94 / 99 entries) and never re-synced after the README grew to 112
distinct entries. This script regenerates their data sections from the
README so the three files agree. It preserves each ledger's prose
(intro, review rules, externally-accepted sections, related pages).

Usage: python3 scripts/sync_ledgers_from_readme.py [--check-only]
With --check-only, exits 1 if the ledgers disagree with the README.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SUBMITTED = ROOT / "SUBMITTED.md"
COMMUNITY = ROOT / "COMMUNITY_SUBMISSIONS.md"

CATEGORIES = [
    "Equalizers",
    "Synthesizers",
    "Compression",
    "Saturation / Distortion",
    "Reverb",
    "Delay",
    "Creative Effects",
    "Modulation",
    "Filters",
    "Utility / Metering",
    "Open-Source DSP Plugins",
    "Multi-Effect Bundles",
    "Plugin Frameworks",
    "DSP Resources",
]


def clean_desc(desc: str) -> str:
    """Strip the trailing 'Official site / repo' link from a description."""
    desc = re.sub(r"\s*[·-]?\s*\[Official site / repo\]\([^)]*\)\s*$", "", desc)
    return desc.strip()


def parse_readme(text: str):
    featured: list[tuple[str, str]] = []
    feat = text.split("## Featured ecosystem")[1].split("\n## ")[0]
    for name, desc in re.findall(
        r"\|\s*\[\*\*(.+?)\*\*\]\([^)]*\)\s*\|\s*(.+?)\s*\|", feat
    ):
        featured.append((name.strip(), clean_desc(desc)))

    cats: list[tuple[str, list[tuple[str, str]]]] = []
    for sec in CATEGORIES:
        part = text.split("## " + sec)
        assert len(part) == 2, f"section missing: {sec}"
        body = part[1].split("\n## ")[0]
        entries = []
        for m in re.finditer(
            r"^- \[?\*?\*?(.+?)\*?\*?\]?\([^)]*\)\s*[—–-]\s*(.+)$", body, re.M
        ):
            entries.append((m.group(1).strip().strip("*"), clean_desc(m.group(2))))
        assert entries, f"no entries parsed in section: {sec}"
        cats.append((sec, entries))

    packs: list[tuple[str, str]] = []
    packs_sec = text.split("## TizWildin FREE sample packs")[1].split("### ")[0]
    for name, desc in re.findall(
        r"\|\s*\[\*\*(.+?)\*\*\]\([^)]*\)\s*\|\s*(.+?)\s*\|", packs_sec
    ):
        packs.append((name.strip(), clean_desc(desc)))

    addl: list[tuple[str, str]] = []
    addl_sec = text.split("### Additional sources")[1].split("\n## ")[0]
    for m in re.finditer(
        r"^- \[?\*?\*?(.+?)\*?\*?\]?\([^)]*\)\s*[—–-]\s*(.+)$", addl_sec, re.M
    ):
        addl.append((m.group(1).strip().strip("*"), clean_desc(m.group(2))))

    related: list[tuple[str, str]] = []
    rel_sec = text.split("### Related audio projects")[1].split("\n## ")[0]
    for m in re.finditer(
        r"^- \[?\*?\*?(.+?)\*?\*?\]?\([^)]*\)\s*[—–-]\s*(.+)$", rel_sec, re.M
    ):
        related.append((m.group(1).strip().strip("*"), clean_desc(m.group(2))))

    return featured, cats, packs, addl, related


def distinct_count(featured, cats, packs, addl, related) -> int:
    names: set[str] = set()
    for n, _ in featured:
        names.add(n)
    for _, entries in cats:
        names.update(n for n, _ in entries)
    names.update(n for n, _ in packs)
    names.update(n for n, _ in addl)
    names.update(n for n, _ in related)
    return len(names)


def render_submitted(featured, cats, packs, addl, related, total: int) -> str:
    lines = [
        "## Approved and published in this repository",
        "",
        f"_Re-synced 2026-11-08 from README.md (was 94 entries — the ledger "
        f"predated the May 2026 README growth). Total distinct entries: "
        f"**{total}**._",
        "",
        f"### Featured ecosystem ({len(featured)})",
    ]
    for name, desc in featured:
        lines.append(f"- **{name}** — {desc}")
    for sec, entries in cats:
        lines.append("")
        lines.append(f"### {sec} ({len(entries)})")
        for name, _ in entries:
            lines.append(f"- **{name}**")
    lines.append("")
    lines.append(f"### Free Sample Packs ({len(packs)})")
    for name, _ in packs:
        lines.append(f"- **{name}**")
    lines.append("")
    lines.append(
        "> Note: the previous version of this ledger listed "
        "**TizWildin Drum Kit Vol. 1** here. It appears in no other file "
        "(not the README pack table, not the HUB packs manifest), so it is "
        "removed pending confirmation whether it is a real pack."
    )
    lines.append("")
    lines.append(f"### Additional sources ({len(addl)})")
    for name, _ in addl:
        lines.append(f"- **{name}**")
    lines.append("")
    lines.append(f"### Related audio projects ({len(related)})")
    for name, _ in related:
        lines.append(f"- **{name}**")
    lines.append(
        "_VF-PlexLab and PAP-Forge-Audio are also in Featured ecosystem "
        "(Experimental); Stickz is also in Creative Effects._"
    )
    lines.append("")
    return "\n".join(lines)


def render_community(featured, cats, packs, addl, related, total: int) -> str:
    lines = [f"### Featured Ecosystem — {len(featured)} entries", ""]
    lines.append("| Entry | Description |")
    lines.append("|-------|-------------|")
    for name, desc in featured:
        lines.append(f"| **{name}** | {desc} |")
    for sec, entries in cats:
        lines.append("")
        lines.append(f"### {sec} — {len(entries)} entries")
        lines.append("")
        lines.append("| Entry | Description |")
        lines.append("|-------|-------------|")
        for name, desc in entries:
            lines.append(f"| **{name}** | {desc} |")
    lines.append("")
    lines.append(f"### Free Sample Packs — {len(packs)} entries")
    lines.append("")
    lines.append("| Entry | Description |")
    lines.append("|-------|-------------|")
    for name, desc in packs:
        lines.append(f"| **{name}** | {desc} |")
    lines.append("")
    lines.append(f"### Additional sources — {len(addl)} entries")
    lines.append("")
    lines.append("| Entry | Description |")
    lines.append("|-------|-------------|")
    for name, desc in addl:
        lines.append(f"| **{name}** | {desc} |")
    lines.append("")
    lines.append(f"### Related audio projects — {len(related)} entries")
    lines.append("")
    lines.append("| Entry | Description |")
    lines.append("|-------|-------------|")
    for name, desc in related:
        lines.append(f"| **{name}** | {desc} |")
    lines.append("")
    lines.append(
        "_VF-PlexLab and PAP-Forge-Audio are also in Featured ecosystem "
        "(Experimental); Stickz is also in Creative Effects._"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**Total accepted entries: {total}**")
    lines.append("")
    return "\n".join(lines)


def splice(text: str, start_marker: str, end_marker: str, new: str) -> str:
    i = text.index(start_marker)
    j = text.index(end_marker, i)
    return text[:i] + new + text[j:]


def main() -> int:
    check_only = "--check-only" in sys.argv
    text = README.read_text(encoding="utf-8")
    featured, cats, packs, addl, related = parse_readme(text)
    total = distinct_count(featured, cats, packs, addl, related)
    print(f"README distinct entries: {total}")
    print(f"Featured: {len(featured)}; packs: {len(packs)}; "
          f"additional: {len(addl)}; related: {len(related)}")
    for sec, entries in cats:
        print(f"  {sec}: {len(entries)}")

    sub = SUBMITTED.read_text(encoding="utf-8")
    new_sub_body = render_submitted(featured, cats, packs, addl, related, total)
    new_sub = splice(
        sub,
        "## Approved and published in this repository",
        "## Externally accepted / approved elsewhere",
        new_sub_body,
    )
    new_sub = re.sub(
        r"Approved and published in this repository:\*\* \*\*\d+ entries\*\*",
        f"Approved and published in this repository:** **{total} entries**",
        new_sub,
        count=1,
    )

    com = COMMUNITY.read_text(encoding="utf-8")
    new_com_body = render_community(featured, cats, packs, addl, related, total)
    new_com = splice(
        com,
        "### Featured Ecosystem",
        "## Related pages",
        new_com_body,
    )

    if check_only:
        ok = (new_sub == sub) and (new_com == com)
        print("IN SYNC" if ok else "OUT OF SYNC")
        return 0 if ok else 1

    SUBMITTED.write_text(new_sub, encoding="utf-8")
    COMMUNITY.write_text(new_com, encoding="utf-8")
    print("Wrote SUBMITTED.md and COMMUNITY_SUBMISSIONS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
