# Saints Traditional English — New Testament (Greek NT)

> **Status:** `draft: true` — NKJV-Style (modern grammar + revered King James cadence), post-audit polished  
> **Current Coverage:** **4 of 27 Greek NT books complete** (89 chapters, 3,768 verses + 11 additional `unplaced` items, 411 translator notes (+ 11 additional notes)).  
> **Validation:** 100% validated against `Saints-Greek-Critical-Text` (Studio v9 Phase 2 / `50793ea`) with `validate_traditional_english.py --lang grc --strict` (`0` FAIL) and scholarly audit.

## Overview

This directory contains the **Saints Traditional English (NKJV-Style)** translation of the Greek NT New Testament, translated completely fresh from `Saints-Greek-Critical-Text` under the locked style policy ([`STYLE.md`](STYLE.md)) and shared term glossary ([`glossary.json`](glossary.json)).

- **Register & Method:** Complete formal equivalence in elevated, worship-ready modern grammar (`you`/`your`, modern verbs, American spelling, modern proper names, zero contractions, zero obsolete 1611 particles) with strict own-source fidelity (`κύριος` → `the Lord` (Title case, never all-caps `LORD`); never cross-harmonized).
- **Additional source verses (`unplaced`):** Additional source-edition verses absent from Saints.Bible numbering are preserved in book `json/*.json` (`unplaced` array) and chapter Markdown (`## Prologue` / `## Additional Verses (Not in Saints Numbering)`).
- **Companion Modern English edition:** [`../Modern-English-NT/`](../Modern-English-NT/README.md).

## Divisions

| Division | Status | Books | Chapters | Verses | Notes | Directory |
|---|---|---:|---:|---:|---:|---|
| **V. Salvation (Gospels)** | **Complete** | 4 / 4 | 89 | 3,768 (+11) | 411 | [`V-Salvation/`](V-Salvation/README.md) |
| **VI. Discipleship (Acts, Letters & General Epistles)** | In progress | 0 / 22 | — | — | — | — |
| **VII. Glory (Revelation)** | In progress | 0 / 1 | — | — | — | — |

## Division V. Salvation (4 / 4 Complete)

| # | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---:|---:|---:|---|---|
| 44 | Matthew | 28 | 1,068 (+3) | 122 | [`V-Salvation/markdown/44-matthew/`](V-Salvation/markdown/44-matthew/README.md) | [`44-matthew.json`](V-Salvation/json/44-matthew.json) |
| 45 | Mark | 16 | 673 (+5) | 70 | [`V-Salvation/markdown/45-mark/`](V-Salvation/markdown/45-mark/README.md) | [`45-mark.json`](V-Salvation/json/45-mark.json) |
| 46 | Luke | 24 | 1,149 (+2) | 117 | [`V-Salvation/markdown/46-luke/`](V-Salvation/markdown/46-luke/README.md) | [`46-luke.json`](V-Salvation/json/46-luke.json) |
| 47 | John | 21 | 878 (+1) | 102 | [`V-Salvation/markdown/47-john/`](V-Salvation/markdown/47-john/README.md) | [`47-john.json`](V-Salvation/json/47-john.json) |
