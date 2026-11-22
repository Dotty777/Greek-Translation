# Saints Traditional English — Old Testament (Greek Septuagint)

> **Status:** `draft: true` — NKJV-Style (modern grammar + revered King James cadence), post-audit polished  
> **Current Coverage:** **9 of 43 Greek OT books complete** (216 chapters, 6,033 verses + 3 additional `unplaced` items, 991 translator notes (+ 1 additional note)).  
> **Validation:** 100% validated against `Saints-Greek-Critical-Text` (Studio v9 Phase 2 / `50793ea`) with `validate_traditional_english.py --lang grc --strict` (`0` FAIL) and scholarly audit.

## Overview

This directory contains the **Saints Traditional English (NKJV-Style)** translation of the Greek Septuagint Old Testament, translated completely fresh from `Saints-Greek-Critical-Text` under the locked style policy ([`STYLE.md`](STYLE.md)) and shared term glossary ([`glossary.json`](glossary.json)).

- **Register & Method:** Complete formal equivalence in elevated, worship-ready modern grammar (`you`/`your`, modern verbs, American spelling, modern proper names, zero contractions, zero obsolete 1611 particles) with strict own-source fidelity (`κύριος` → `the Lord` (Title case, never all-caps `LORD`); never cross-harmonized).
- **Additional source verses (`unplaced`):** Additional source-edition verses absent from Saints.Bible numbering are preserved in book `json/*.json` (`unplaced` array) and chapter Markdown (`## Prologue` / `## Additional Verses (Not in Saints Numbering)`).
- **Companion Modern English edition:** [`../Modern-English-OT/`](../Modern-English-OT/README.md).

## Divisions

| Division | Status | Books | Chapters | Verses | Notes | Directory |
|---|---|---:|---:|---:|---:|---|
| **I. Law (Pentateuch)** | In progress | 0 / 5 | — | — | — | — |
| **II. Judgement (Historical Books & Job)** | In progress (9/15) | 9 / 15 | 216 | 6,033 (+3) | 991 | [`II-Judgement/`](II-Judgement/README.md) |
| **III. Wisdom (Wisdom & Poetry)** | In progress | 0 / 7 | — | — | — | — |
| **IV. Providence (Prophets)** | In progress | 0 / 16 | — | — | — | — |

## Division II. Judgement (9 / 15)

| # | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---:|---:|---:|---|---|
| 6 | Joshua | 24 | 643 | 104 | [`II-Judgement/markdown/06-joshua/`](II-Judgement/markdown/06-joshua/README.md) | [`06-joshua.json`](II-Judgement/json/06-joshua.json) |
| 7 | Judges | 21 | 618 | 99 | [`II-Judgement/markdown/07-judges/`](II-Judgement/markdown/07-judges/README.md) | [`07-judges.json`](II-Judgement/json/07-judges.json) |
| 8 | Ruth | 4 | 85 | 16 | [`II-Judgement/markdown/08-ruth/`](II-Judgement/markdown/08-ruth/README.md) | [`08-ruth.json`](II-Judgement/json/08-ruth.json) |
| 9 | 1 Samuel | 31 | 772 (+1) | 142 | [`II-Judgement/markdown/09-1-samuel/`](II-Judgement/markdown/09-1-samuel/README.md) | [`09-1-samuel.json`](II-Judgement/json/09-1-samuel.json) |
| 10 | 2 Samuel | 24 | 694 | 109 | [`II-Judgement/markdown/10-2-samuel/`](II-Judgement/markdown/10-2-samuel/README.md) | [`10-2-samuel.json`](II-Judgement/json/10-2-samuel.json) |
| 11 | 1 Kings | 22 | 754 | 108 | [`II-Judgement/markdown/11-1-kings/`](II-Judgement/markdown/11-1-kings/README.md) | [`11-1-kings.json`](II-Judgement/json/11-1-kings.json) |
| 12 | 2 Kings | 25 | 718 (+1) | 116 | [`II-Judgement/markdown/12-2-kings/`](II-Judgement/markdown/12-2-kings/README.md) | [`12-2-kings.json`](II-Judgement/json/12-2-kings.json) |
| 13 | 1 Chronicles | 29 | 929 (+1) | 138 | [`II-Judgement/markdown/13-1-chronicles/`](II-Judgement/markdown/13-1-chronicles/README.md) | [`13-1-chronicles.json`](II-Judgement/json/13-1-chronicles.json) |
| 14 | 2 Chronicles | 36 | 820 | 159 | [`II-Judgement/markdown/14-2-chronicles/`](II-Judgement/markdown/14-2-chronicles/README.md) | [`14-2-chronicles.json`](II-Judgement/json/14-2-chronicles.json) |
