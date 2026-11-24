# Saints Modern English — Complete New Testament (Greek)

> **Status:** `draft: true` — Post-audit polished  
> **Coverage:** **Complete 27 of 27 New Testament books** (260 chapters, 7,942 verses, 1,122 translator notes) — all three NT divisions (**V. Salvation**, **VI. Discipleship**, **VII. Glory**) finished.  
> **Validation:** 100% validated against `Saints-Greek-Critical-Text` with `validate_modern_english.py --strict` and full programmatic & scholarly audit (`0` hard failures, `0` soft archaisms).

## Overview

This directory contains the complete **Saints Modern English** translation of the Greek New Testament, translated fresh from `Saints-Greek-Critical-Text` under the locked style policy ([`STYLE.md`](STYLE.md)) and shared term glossary ([`glossary.json`](glossary.json)).

- **Method:** Formal-equivalent (literal) Modern English smoothed for natural reading, with zero archaisms and original wording.
- **Text-critical fidelity:** Preserves double brackets `⟦ ⟧` verbatim wherever present in the Saints Greek Critical Text (including Matt 16:3, Mark 16:9–20, John 7:53–8:11, and Rom 16:24).
- **Additional critical-text verses (`unplaced`):** All **18 bracketed NT `no-site-verse` items** (Matt 17:21, 18:11, 23:14; Mark 7:16, 9:44, 9:46, 11:26, 15:28; Luke 17:36, 23:17; John 5:4; Acts 8:37, 15:34, 24:7, 28:29; Rom 14:24–26) are included in book `json/*.json` (`unplaced` array) and chapter Markdown (`## Additional Verses (Not in Saints Numbering)`).
- **Related directories:** Old Testament in [`../Modern-English-OT/`](../Modern-English-OT/README.md); original reviewed pilot & projected layers in [`../Modern-English-Pilot/`](../Modern-English-Pilot/README.md).

## Books Included (27 / 27 NT Books — Complete)

| # | Division | Book | Chapters | Verses | Notes | Reading Edition | Book JSON |
|---:|---|---|---:|---:|---:|---|---|
| 44 | V. Salvation | Matthew | 28 | 1,068 | 124 | [`markdown/44-matthew/`](markdown/44-matthew/README.md) | [`44-matthew.json`](json/44-matthew.json) |
| 45 | V. Salvation | Mark | 16 | 673 | 72 | [`markdown/45-mark/`](markdown/45-mark/README.md) | [`45-mark.json`](json/45-mark.json) |
| 46 | V. Salvation | Luke | 24 | 1,149 | 117 | [`markdown/46-luke/`](markdown/46-luke/README.md) | [`46-luke.json`](json/46-luke.json) |
| 47 | V. Salvation | John | 21 | 878 | 102 | [`markdown/47-john/`](markdown/47-john/README.md) | [`47-john.json`](json/47-john.json) |
| 48 | VI. Discipleship | Acts | 28 | 1,002 | 119 | [`markdown/48-acts/`](markdown/48-acts/README.md) | [`48-acts.json`](json/48-acts.json) |
| 49 | VI. Discipleship | Romans | 16 | 433 | 70 | [`markdown/49-romans/`](markdown/49-romans/README.md) | [`49-romans.json`](json/49-romans.json) |
| 50 | VI. Discipleship | 1 Corinthians | 16 | 437 | 62 | [`markdown/50-1-corinthians/`](markdown/50-1-corinthians/README.md) | [`50-1-corinthians.json`](json/50-1-corinthians.json) |
| 51 | VI. Discipleship | 2 Corinthians | 13 | 256 | 49 | [`markdown/51-2-corinthians/`](markdown/51-2-corinthians/README.md) | [`51-2-corinthians.json`](json/51-2-corinthians.json) |
| 52 | VI. Discipleship | Galatians | 6 | 149 | 25 | [`markdown/52-galatians/`](markdown/52-galatians/README.md) | [`52-galatians.json`](json/52-galatians.json) |
| 53 | VI. Discipleship | Ephesians | 6 | 155 | 28 | [`markdown/53-ephesians/`](markdown/53-ephesians/README.md) | [`53-ephesians.json`](json/53-ephesians.json) |
| 54 | VI. Discipleship | Philippians | 4 | 104 | 17 | [`markdown/54-philippians/`](markdown/54-philippians/README.md) | [`54-philippians.json`](json/54-philippians.json) |
| 55 | VI. Discipleship | Colossians | 4 | 95 | 18 | [`markdown/55-colossians/`](markdown/55-colossians/README.md) | [`55-colossians.json`](json/55-colossians.json) |
| 56 | VI. Discipleship | 1 Thessalonians | 5 | 89 | 17 | [`markdown/56-1-thessalonians/`](markdown/56-1-thessalonians/README.md) | [`56-1-thessalonians.json`](json/56-1-thessalonians.json) |
| 57 | VI. Discipleship | 2 Thessalonians | 3 | 47 | 11 | [`markdown/57-2-thessalonians/`](markdown/57-2-thessalonians/README.md) | [`57-2-thessalonians.json`](json/57-2-thessalonians.json) |
| 58 | VI. Discipleship | 1 Timothy | 6 | 113 | 23 | [`markdown/58-1-timothy/`](markdown/58-1-timothy/README.md) | [`58-1-timothy.json`](json/58-1-timothy.json) |
| 59 | VI. Discipleship | 2 Timothy | 4 | 83 | 14 | [`markdown/59-2-timothy/`](markdown/59-2-timothy/README.md) | [`59-2-timothy.json`](json/59-2-timothy.json) |
| 60 | VI. Discipleship | Titus | 3 | 46 | 9 | [`markdown/60-titus/`](markdown/60-titus/README.md) | [`60-titus.json`](json/60-titus.json) |
| 61 | VI. Discipleship | Philemon | 1 | 25 | 4 | [`markdown/61-philemon/`](markdown/61-philemon/README.md) | [`61-philemon.json`](json/61-philemon.json) |
| 62 | VI. Discipleship | Hebrews | 13 | 303 | 48 | [`markdown/62-hebrews/`](markdown/62-hebrews/README.md) | [`62-hebrews.json`](json/62-hebrews.json) |
| 63 | VI. Discipleship | James | 5 | 108 | 19 | [`markdown/63-james/`](markdown/63-james/README.md) | [`63-james.json`](json/63-james.json) |
| 64 | VI. Discipleship | 1 Peter | 5 | 105 | 19 | [`markdown/64-1-peter/`](markdown/64-1-peter/README.md) | [`64-1-peter.json`](json/64-1-peter.json) |
| 65 | VI. Discipleship | 2 Peter | 3 | 61 | 10 | [`markdown/65-2-peter/`](markdown/65-2-peter/README.md) | [`65-2-peter.json`](json/65-2-peter.json) |
| 66 | VI. Discipleship | 1 John | 5 | 105 | 19 | [`markdown/66-1-john/`](markdown/66-1-john/README.md) | [`66-1-john.json`](json/66-1-john.json) |
| 67 | VI. Discipleship | 2 John | 1 | 13 | 5 | [`markdown/67-2-john/`](markdown/67-2-john/README.md) | [`67-2-john.json`](json/67-2-john.json) |
| 68 | VI. Discipleship | 3 John | 1 | 15 | 4 | [`markdown/68-3-john/`](markdown/68-3-john/README.md) | [`68-3-john.json`](json/68-3-john.json) |
| 69 | VI. Discipleship | Jude | 1 | 25 | 4 | [`markdown/69-jude/`](markdown/69-jude/README.md) | [`69-jude.json`](json/69-jude.json) |
| 70 | VII. Glory | Revelation | 22 | 405 | 113 | [`markdown/70-revelation/`](markdown/70-revelation/README.md) | [`70-revelation.json`](json/70-revelation.json) |
