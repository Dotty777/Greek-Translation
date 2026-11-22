# Saints Traditional English — Old Testament (Greek Septuagint)

> **Status:** `draft: true` — NKJV-Style (modern grammar + revered King James cadence), post-audit polished  
> **Current Coverage:** **33 of 43 Greek OT books complete** (747 chapters, 18,564 verses + 18 additional `unplaced` items, 3,191 translator notes (+ 6 additional notes)).  
> **Validation:** 100% validated against `Saints-Greek-Critical-Text` (Studio v9 Phase 2 / `50793ea`) with `validate_traditional_english.py --lang grc --strict` (`0` FAIL) and scholarly audit.

## Overview

This directory contains the **Saints Traditional English (NKJV-Style)** translation of the Greek Septuagint Old Testament, translated completely fresh from `Saints-Greek-Critical-Text` under the locked style policy ([`STYLE.md`](STYLE.md)) and shared term glossary ([`glossary.json`](glossary.json)).

- **Register & Method:** Complete formal equivalence in elevated, worship-ready modern grammar (`you`/`your`, modern verbs, American spelling, modern proper names, zero contractions, zero obsolete 1611 particles) with strict own-source fidelity (`κύριος` → `the Lord` (Title case, never all-caps `LORD`); never cross-harmonized).
- **Additional source verses (`unplaced`):** Additional source-edition verses absent from Saints.Bible numbering are preserved in book `json/*.json` (`unplaced` array) and chapter Markdown (`## Prologue` / `## Additional Verses (Not in Saints Numbering)`).
- **Companion Modern English edition:** [`../Modern-English-OT/`](../Modern-English-OT/README.md).

## Divisions

| Division | Status | Books | Chapters | Verses | Notes | Directory |
|---|---|---:|---:|---:|---:|---|
| **I. Law (Pentateuch)** | **Complete** | 5 / 5 | 187 | 5,791 (+3) | 824 | [`I-Law/`](I-Law/README.md) |
| **II. Judgement (Historical Books & Job)** | In progress (9/15) | 9 / 15 | 216 | 6,033 (+3) | 991 | [`II-Judgement/`](II-Judgement/README.md) |
| **III. Wisdom (Wisdom & Poetry)** | **Complete** | 7 / 7 | 277 | 5,691 (+12) | 1,096 | [`III-Wisdom/`](III-Wisdom/README.md) |
| **IV. Providence (Prophets)** | In progress (12/16) | 12 / 16 | 67 | 1,049 | 280 | [`IV-Providence/`](IV-Providence/README.md) |

## Division I. Law (5 / 5 Complete)

| # | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---:|---:|---:|---|---|
| 1 | Genesis | 50 | 1,530 | 220 | [`I-Law/markdown/01-genesis/`](I-Law/markdown/01-genesis/README.md) | [`01-genesis.json`](I-Law/json/01-genesis.json) |
| 2 | Exodus | 40 | 1,161 (+1) | 166 | [`I-Law/markdown/02-exodus/`](I-Law/markdown/02-exodus/README.md) | [`02-exodus.json`](I-Law/json/02-exodus.json) |
| 3 | Leviticus | 27 | 857 | 117 | [`I-Law/markdown/03-leviticus/`](I-Law/markdown/03-leviticus/README.md) | [`03-leviticus.json`](I-Law/json/03-leviticus.json) |
| 4 | Numbers | 36 | 1,285 (+2) | 172 | [`I-Law/markdown/04-numbers/`](I-Law/markdown/04-numbers/README.md) | [`04-numbers.json`](I-Law/json/04-numbers.json) |
| 5 | Deuteronomy | 34 | 958 | 149 | [`I-Law/markdown/05-deuteronomy/`](I-Law/markdown/05-deuteronomy/README.md) | [`05-deuteronomy.json`](I-Law/json/05-deuteronomy.json) |

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

## Division III. Wisdom (7 / 7 Complete)

| # | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---:|---:|---:|---|---|
| 21 | Psalms | 151 | 2,532 (+10) | 594 | [`III-Wisdom/markdown/21-psalms/`](III-Wisdom/markdown/21-psalms/README.md) | [`21-psalms.json`](III-Wisdom/json/21-psalms.json) |
| 22 | Proverbs | 31 | 887 | 132 | [`III-Wisdom/markdown/22-proverbs/`](III-Wisdom/markdown/22-proverbs/README.md) | [`22-proverbs.json`](III-Wisdom/json/22-proverbs.json) |
| 23 | Ecclesiastes | 12 | 222 | 49 | [`III-Wisdom/markdown/23-ecclesiastes/`](III-Wisdom/markdown/23-ecclesiastes/README.md) | [`23-ecclesiastes.json`](III-Wisdom/json/23-ecclesiastes.json) |
| 24 | Song of Songs | 8 | 117 | 36 | [`III-Wisdom/markdown/24-song-of-songs/`](III-Wisdom/markdown/24-song-of-songs/README.md) | [`24-song-of-songs.json`](III-Wisdom/json/24-song-of-songs.json) |
| 25 | Lamentations | 5 | 150 | 27 | [`III-Wisdom/markdown/25-lamentations/`](III-Wisdom/markdown/25-lamentations/README.md) | [`25-lamentations.json`](III-Wisdom/json/25-lamentations.json) |
| 26 | Wisdom of Solomon | 19 | 434 | 65 | [`III-Wisdom/markdown/26-wisdom-of-solomon/`](III-Wisdom/markdown/26-wisdom-of-solomon/README.md) | [`26-wisdom-of-solomon.json`](III-Wisdom/json/26-wisdom-of-solomon.json) |
| 27 | Sirach | 51 | 1,349 (+2) | 193 | [`III-Wisdom/markdown/27-sirach/`](III-Wisdom/markdown/27-sirach/README.md) | [`27-sirach.json`](III-Wisdom/json/27-sirach.json) |

## Division IV. Providence (12 / 16)

| # | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---:|---:|---:|---|---|
| 32 | Hosea | 14 | 197 | 53 | [`IV-Providence/markdown/32-hosea/`](IV-Providence/markdown/32-hosea/README.md) | [`32-hosea.json`](IV-Providence/json/32-hosea.json) |
| 33 | Joel | 4 | 73 | 17 | [`IV-Providence/markdown/33-joel/`](IV-Providence/markdown/33-joel/README.md) | [`33-joel.json`](IV-Providence/json/33-joel.json) |
| 34 | Amos | 9 | 145 | 43 | [`IV-Providence/markdown/34-amos/`](IV-Providence/markdown/34-amos/README.md) | [`34-amos.json`](IV-Providence/json/34-amos.json) |
| 35 | Obadiah | 1 | 21 | 5 | [`IV-Providence/markdown/35-obadiah/`](IV-Providence/markdown/35-obadiah/README.md) | [`35-obadiah.json`](IV-Providence/json/35-obadiah.json) |
| 36 | Jonah | 4 | 48 | 14 | [`IV-Providence/markdown/36-jonah/`](IV-Providence/markdown/36-jonah/README.md) | [`36-jonah.json`](IV-Providence/json/36-jonah.json) |
| 37 | Micah | 7 | 105 | 27 | [`IV-Providence/markdown/37-micah/`](IV-Providence/markdown/37-micah/README.md) | [`37-micah.json`](IV-Providence/json/37-micah.json) |
| 38 | Nahum | 3 | 47 | 13 | [`IV-Providence/markdown/38-nahum/`](IV-Providence/markdown/38-nahum/README.md) | [`38-nahum.json`](IV-Providence/json/38-nahum.json) |
| 39 | Habakkuk | 3 | 56 | 14 | [`IV-Providence/markdown/39-habakkuk/`](IV-Providence/markdown/39-habakkuk/README.md) | [`39-habakkuk.json`](IV-Providence/json/39-habakkuk.json) |
| 40 | Zephaniah | 3 | 53 | 12 | [`IV-Providence/markdown/40-zephaniah/`](IV-Providence/markdown/40-zephaniah/README.md) | [`40-zephaniah.json`](IV-Providence/json/40-zephaniah.json) |
| 41 | Haggai | 2 | 38 | 9 | [`IV-Providence/markdown/41-haggai/`](IV-Providence/markdown/41-haggai/README.md) | [`41-haggai.json`](IV-Providence/json/41-haggai.json) |
| 42 | Zechariah | 14 | 211 | 60 | [`IV-Providence/markdown/42-zechariah/`](IV-Providence/markdown/42-zechariah/README.md) | [`42-zechariah.json`](IV-Providence/json/42-zechariah.json) |
| 43 | Malachi | 3 | 55 | 13 | [`IV-Providence/markdown/43-malachi/`](IV-Providence/markdown/43-malachi/README.md) | [`43-malachi.json`](IV-Providence/json/43-malachi.json) |
