# Saints Modern English — Old Testament (Greek Septuagint)

> **Status:** `draft: true` — Post-audit polished  
> **Current Coverage:** **19 of 43 OT books complete** (332 chapters, 8,531 verses, 1,611 translator notes) — **Division I: Law (5/5 Pentateuch)** + **Division IV: Providence (14/16: complete Isaiah 66 ch, complete Daniel 12 ch, and all 12 Minor Prophets)** (combined with Complete 27/27 NT = **46 of 70 complete Greek books**).  
> **Validation:** 100% validated against `Saints-Greek-Critical-Text` with `validate_modern_english.py --strict` and programmatic/scholarly audits (`0` hard/soft failures).

## Overview

This directory contains the **Saints Modern English** translation of the Greek Old Testament (Septuagint / Theodotion Daniel), translated fresh from `Saints-Greek-Critical-Text` under the locked style policy ([`STYLE.md`](STYLE.md)) and shared term glossary ([`glossary.json`](glossary.json)).

- **Method:** Formal-equivalent (literal) Modern English smoothed for natural reading, with zero archaisms, own-source Greek fidelity (`κύριος` → `the Lord`), and original wording.
- **Saints.Bible versification:** Chapter and verse keys match `Saints-Greek-Critical-Text` and the Saints.Bible Parallel Reader.
- **Related directories:** Complete 27/27 NT in [`../Modern-English-NT/`](../Modern-English-NT/README.md); original reviewed pilot & projected layers in [`../Modern-English-Pilot/`](../Modern-English-Pilot/README.md).

## Divisions

| Division | Status | Books | Chapters | Verses | Notes | Directory |
|---|---|---:|---:|---:|---:|---|
| **I. Law (Pentateuch)** | **Complete** | 5 / 5 | 187 | 5,791 | 916 | [`I-Law/`](I-Law/README.md) |
| II. Judgement | Pending | 0 / 14 | — | — | — | — |
| III. Wisdom | In progress | 0 / 8 | — | — | — | — |
| **IV. Providence** | **14 / 16 Complete (Isaiah, Daniel, 12 Minor Prophets)** | 14 / 16 | 145 | 2,740 | 695 | [`IV-Providence/`](IV-Providence/README.md) |

## Division I: Law Books (5 / 5 Complete)

| # | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---:|---:|---:|---|---|
| 1 | Genesis | 50 | 1,530 | 237 | [`I-Law/markdown/01-genesis/`](I-Law/markdown/01-genesis/README.md) | [`01-genesis.json`](I-Law/json/01-genesis.json) |
| 2 | Exodus | 40 | 1,161 | 173 | [`I-Law/markdown/02-exodus/`](I-Law/markdown/02-exodus/README.md) | [`02-exodus.json`](I-Law/json/02-exodus.json) |
| 3 | Leviticus | 27 | 857 | 133 | [`I-Law/markdown/03-leviticus/`](I-Law/markdown/03-leviticus/README.md) | [`03-leviticus.json`](I-Law/json/03-leviticus.json) |
| 4 | Numbers | 36 | 1,285 | 206 | [`I-Law/markdown/04-numbers/`](I-Law/markdown/04-numbers/README.md) | [`04-numbers.json`](I-Law/json/04-numbers.json) |
| 5 | Deuteronomy | 34 | 958 | 167 | [`I-Law/markdown/05-deuteronomy/`](I-Law/markdown/05-deuteronomy/README.md) | [`05-deuteronomy.json`](I-Law/json/05-deuteronomy.json) |

## Division IV: Providence (14 / 16 Complete)

| # | Book | Section | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---|---:|---:|---:|---|---|
| 28 | Isaiah | Major Prophets | 66 | 1,289 | 309 | [`IV-Providence/markdown/28-isaiah/`](IV-Providence/markdown/28-isaiah/README.md) | [`28-isaiah.json`](IV-Providence/json/28-isaiah.json) |
| 31 | Daniel | Major Prophets (Theodotion) | 12 | 402 | 69 | [`IV-Providence/markdown/31-daniel/`](IV-Providence/markdown/31-daniel/README.md) | [`31-daniel.json`](IV-Providence/json/31-daniel.json) |
| 32 | Hosea | Minor Prophets | 14 | 197 | 65 | [`IV-Providence/markdown/32-hosea/`](IV-Providence/markdown/32-hosea/README.md) | [`32-hosea.json`](IV-Providence/json/32-hosea.json) |
| 33 | Joel | Minor Prophets | 4 | 73 | 18 | [`IV-Providence/markdown/33-joel/`](IV-Providence/markdown/33-joel/README.md) | [`33-joel.json`](IV-Providence/json/33-joel.json) |
| 34 | Amos | Minor Prophets | 9 | 145 | 44 | [`IV-Providence/markdown/34-amos/`](IV-Providence/markdown/34-amos/README.md) | [`34-amos.json`](IV-Providence/json/34-amos.json) |
| 35 | Obadiah | Minor Prophets | 1 | 21 | 5 | [`IV-Providence/markdown/35-obadiah/`](IV-Providence/markdown/35-obadiah/README.md) | [`35-obadiah.json`](IV-Providence/json/35-obadiah.json) |
| 36 | Jonah | Minor Prophets | 4 | 48 | 18 | [`IV-Providence/markdown/36-jonah/`](IV-Providence/markdown/36-jonah/README.md) | [`36-jonah.json`](IV-Providence/json/36-jonah.json) |
| 37 | Micah | Minor Prophets | 7 | 105 | 32 | [`IV-Providence/markdown/37-micah/`](IV-Providence/markdown/37-micah/README.md) | [`37-micah.json`](IV-Providence/json/37-micah.json) |
| 38 | Nahum | Minor Prophets | 3 | 47 | 15 | [`IV-Providence/markdown/38-nahum/`](IV-Providence/markdown/38-nahum/README.md) | [`38-nahum.json`](IV-Providence/json/38-nahum.json) |
| 39 | Habakkuk | Minor Prophets | 3 | 56 | 15 | [`IV-Providence/markdown/39-habakkuk/`](IV-Providence/markdown/39-habakkuk/README.md) | [`39-habakkuk.json`](IV-Providence/json/39-habakkuk.json) |
| 40 | Zephaniah | Minor Prophets | 3 | 53 | 15 | [`IV-Providence/markdown/40-zephaniah/`](IV-Providence/markdown/40-zephaniah/README.md) | [`40-zephaniah.json`](IV-Providence/json/40-zephaniah.json) |
| 41 | Haggai | Minor Prophets | 2 | 38 | 10 | [`IV-Providence/markdown/41-haggai/`](IV-Providence/markdown/41-haggai/README.md) | [`41-haggai.json`](IV-Providence/json/41-haggai.json) |
| 42 | Zechariah | Minor Prophets | 14 | 211 | 66 | [`IV-Providence/markdown/42-zechariah/`](IV-Providence/markdown/42-zechariah/README.md) | [`42-zechariah.json`](IV-Providence/json/42-zechariah.json) |
| 43 | Malachi | Minor Prophets | 3 | 55 | 14 | [`IV-Providence/markdown/43-malachi/`](IV-Providence/markdown/43-malachi/README.md) | [`43-malachi.json`](IV-Providence/json/43-malachi.json) |
