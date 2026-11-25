# Follow-Up Revision-Pinned Greek Contextual-Review Ledger (Strict Honesty Audit)

**Date:** 2026-11-25  
**Auditor:** `@greek-mapper` (Greek-Translation only; built strictly from surviving committed reviewer logs, verdicts, blind-review packets, and reconciliation records)  
**Adopted Critical Text:** `Saints-Greek-Critical-Text` (`a0d022c1`, `34,198` verses across 70 books / 1,291 chapters)  
**Revision Chain Audited:** `df7abd10` → `278767fb` → `53ec61b9` → `1379708f` → `d307f8f7` → `4615526d` → `acef6069` → `fea550e4e94aed2bab37bd4a901e2d22987346fd` (0 English verse-text wording changes in follow-up commit)

## 1. Strict-Honesty Corpus Coverage Summary (All 70 Greek Books — `34,198` Verses)

> **Strict Honesty Rule:** ONLY individually documented verses or explicitly named verse/chapter ranges in surviving files are counted as `documented_contextual_read`. Aggregate-only claims without surviving chapter/verse IDs (`155 OT chapters`, `158/163 NT chapters / 4,839 NT verses`, deleted `helper_ot_notes.md`/`helper_nt_notes.md`, Claude's unlogged prose claim, and `351` automated global consistency batch rows) are strictly excluded and reported separately below.

| Metric | OT (43 books) | NT (27 books) | Total (70 books) | % of `source_total` |
|---|---:|---:|---:|---:|
| **`documented_contextual_read` (unique)** | **2,387** | **1,149** | **3,536** | **10.34%** |
| ↳ *of which Greek-source contextual read* | *1,714* | *609* | *2,323* | *6.79%* |
| ↳ *of which standalone English only (Pass 3)* | *673* | *540* | *1,213* | *3.55%* |
| **`automated_screening_only`** | **23,851** | **6,811** | **30,662** | **89.66%** |
| **`insufficient_evidence`** | **0** | **0** | **0** | **0.00%** |
| **`source_total` (exact invariant check)** | **26,238** | **7,960** | **34,198** | **100.00%** |

*Editorial status (strictly separate from contextual-read coverage; from `pass2_coverage.json`): `verified` = `34,036`, `disputed` / `awaiting_human_signoff` = `162` across `15` human-editor queue items (`GRC-HQ-001`–`GRC-HQ-015`).*

### Unique Documented Verses by Review Pass (`greek_contextual_ledger.jsonl`: 5,084 total read records)

| Pass | Reviewer | Source Rev | English Rev | Unique Verses |
|---|---|---|---|---:|
| `pre_stage2_claude_fidelity` | `claude-opus-5.5` | `pre-Stage1@df7abd10` | `df7abd10` | 1,554 |
| `pass1_grc_fidelity` | `grc-fidelity` | `a0d022c1` | `278767fb` | 1,181 |
| `pass2_grc_peer` | `grc-peer` | `a0d022c1` | `53ec61b9` | 295 |
| `pass3_grc_flow` *(standalone English)* | `grc-flow` | `null` | `1379708f` | 1,353 |
| `pass3_bounceback_grc_peer` | `grc-peer` | `a0d022c1` | `d307f8f7` | 6 |
| `pass35_blind_ai_peer_review` | `grc-p35-blind-ai-peer-reviewer` | `a0d022c1` | `d307f8f7` | 40 |
| `pass35_response_grc_peer` | `grc-peer` | `a0d022c1` | `acef6069` | 174 |
| `pass4_reconciliation` | `reconciliation-auditor` | `a0d022c1` | `acef6069` | 117 |

## 2. Unattributed Aggregate Claims (Reported Separately — `0` Verses Assigned)

1. **Claude Pre-Stage-2 Global Claim (`UNATTR-CLAUDE-01`):** `reviews/2026-11-24-ME-GREEK-FIDELITY/README.md` states every verse across all 70 books (`34,150` verses) was read, but no verse-level reading log survives for the ~32,700 unedited verses. In addition, **351** automated edition/division-wide consistency batch rows in `wording-changes.jsonl` (`NT-wide`, `OT-wide`, `Pentateuch-wide`, `Psalter-wide`, `1-2 Kings regnal formula`, `edition-wide`, `house style`) are strictly excluded from `documented_contextual_read`.
2. **Pass 1 OT Helper Aggregate Claim (`UNATTR-P1-OT-01`):** `pass1_coverage.json` claims `155` OT chapters read in context (per-book integers only), but `helper_ot_notes.md` was deleted prior to commit. Conservatively excludes even the 3 OT books where `context_chapters_read == chapters` (`Esther`, `Song of Songs`, `Jonah` = `329` verses).
3. **Pass 1 NT Helper Aggregate Claim (`UNATTR-P1-NT-01`):** `pass1_coverage.json` claims `158` NT chapters / `4,839` NT verses read in context (vs. `#61` assigning `160` and `#69` claiming `163`), and `helper_nt_notes.md` was deleted prior to commit. Conservatively excludes even the 17 short NT epistles where `context_chapters_read == chapters` (`1,594` verses).

## 3. Post-Edit Reread Audit (`df7abd10` / `278767fb` → Final Revision)

Across all commits after `df7abd10` / `278767fb`, **345** distinct adopted Greek verses had their verse text, placement, translator note, or immediate `±1` surrounding neighbor modified (plus `12` Stage-1-removed duplicate/phantom `unplaced` entries deleted in `53ec61b9`):

| Change Scope | Total Verses | Independently Reread After Last Text Edit | Independently Reread on Final Revision (`true`) | Not Independently Reread on Final Revision (`false`) |
|---|---:|---:|---:|---:|
| **Verse text edited (`53ec61b9`, `1379708f`, `d307f8f7`, `4615526d`)** | **92** | 13 (10 Greek-source) | **10** | **82** |
| **Placement moved verbatim (`unplaced`→`verses`, 0 wording change)** | **2** | n/a (0 wording change) | **0** | **2** |
| **Translator note changed only** | **122** | n/a | **34** | **88** |
| **Surrounding `±1` neighbor changed only** | **129** | n/a | **0** | **129** |

### Verse-Text-Changed Loci (`92` Verses) — Post-Edit Reread Breakdown
- **Key honest takeaway:** Of the **92** adopted Greek verses whose English text changed between `278767fb` and `acef6069` (`0` verse-text wording changes in the follow-up commit), **13** were independently reread in a subsequent pass after their last text edit (**10** against Greek, e.g. `Ezra 3:10` verified in Pass 4 `P4-REC-089` on `acef6069`), while **79** have NOT yet received an independent post-edit contextual reread (including Pass 3.5 edits `Neh 3:2` and `Ps 61:1`, Pass 3 bounce-back edits `Lev 25:55, 26:1, 26:46` and `Neh 12:9`, most Pass 3 mechanical edits, and Pass 2 Stage-1/fidelity edits not subsequently sampled in Pass 3 / 3.5 / 4). Full verse-by-verse SHA & evidence records are in [`followup_contextual_review_ledger.json`](followup_contextual_review_ledger.json).

## 4. Complete 70-Book Contextual-Read Coverage Table

| # | Book | Test. | Source Total | Documented Contextual Read | (Greek-Source / Eng-Only) | Automated Screening Only | Insufficient Evidence | Separate Editorial Disputed |
|---:|---|---|---:|---:|---|---:|---:|---:|
| 1 | Genesis | OT | 1531 | 89 (5.8%) | 62 / 27 | 1442 | 0 | 2 |
| 2 | Exodus | OT | 1163 | 109 (9.4%) | 109 / 0 | 1054 | 0 | 0 |
| 3 | Leviticus | OT | 859 | 193 (22.5%) | 100 / 93 | 666 | 0 | 0 |
| 4 | Numbers | OT | 1288 | 96 (7.5%) | 73 / 23 | 1192 | 0 | 0 |
| 5 | Deuteronomy | OT | 958 | 80 (8.3%) | 49 / 31 | 878 | 0 | 0 |
| 6 | Joshua | OT | 643 | 13 (2.0%) | 13 / 0 | 630 | 0 | 0 |
| 7 | Judges | OT | 618 | 16 (2.6%) | 16 / 0 | 602 | 0 | 0 |
| 8 | Ruth | OT | 85 | 26 (30.6%) | 5 / 21 | 59 | 0 | 0 |
| 9 | 1 Samuel | OT | 772 | 37 (4.8%) | 37 / 0 | 735 | 0 | 0 |
| 10 | 2 Samuel | OT | 694 | 57 (8.2%) | 29 / 28 | 637 | 0 | 0 |
| 11 | 1 Kings | OT | 755 | 33 (4.4%) | 33 / 0 | 722 | 0 | 0 |
| 12 | 2 Kings | OT | 719 | 40 (5.6%) | 40 / 0 | 679 | 0 | 0 |
| 13 | 1 Chronicles | OT | 930 | 50 (5.4%) | 48 / 2 | 880 | 0 | 11 |
| 14 | 2 Chronicles | OT | 820 | 29 (3.5%) | 29 / 0 | 791 | 0 | 0 |
| 15 | Ezra | OT | 280 | 9 (3.2%) | 9 / 0 | 271 | 0 | 0 |
| 16 | Nehemiah | OT | 388 | 32 (8.2%) | 32 / 0 | 356 | 0 | 0 |
| 17 | Esther | OT | 164 | 14 (8.5%) | 14 / 0 | 150 | 0 | 0 |
| 18 | 1 Maccabees | OT | 924 | 39 (4.2%) | 39 / 0 | 885 | 0 | 0 |
| 19 | 2 Maccabees | OT | 555 | 54 (9.7%) | 14 / 40 | 501 | 0 | 0 |
| 20 | Job | OT | 1068 | 125 (11.7%) | 41 / 84 | 943 | 0 | 1 |
| 21 | Psalms | OT | 2533 | 255 (10.1%) | 224 / 31 | 2278 | 0 | 104 |
| 22 | Proverbs | OT | 889 | 59 (6.6%) | 24 / 35 | 830 | 0 | 0 |
| 23 | Ecclesiastes | OT | 222 | 14 (6.3%) | 13 / 1 | 208 | 0 | 0 |
| 24 | Song of Songs | OT | 117 | 20 (17.1%) | 20 / 0 | 97 | 0 | 0 |
| 25 | Lamentations | OT | 150 | 11 (7.3%) | 11 / 0 | 139 | 0 | 1 |
| 26 | Wisdom of Solomon | OT | 436 | 46 (10.6%) | 22 / 24 | 390 | 0 | 0 |
| 27 | Sirach | OT | 1357 | 294 (21.7%) | 236 / 58 | 1063 | 0 | 0 |
| 28 | Isaiah | OT | 1289 | 124 (9.6%) | 86 / 38 | 1165 | 0 | 7 |
| 29 | Jeremiah | OT | 1296 | 72 (5.6%) | 70 / 2 | 1224 | 0 | 0 |
| 30 | Ezekiel | OT | 1265 | 97 (7.7%) | 61 / 36 | 1168 | 0 | 9 |
| 31 | Daniel | OT | 420 | 182 (43.3%) | 99 / 83 | 238 | 0 | 2 |
| 32 | Hosea | OT | 197 | 5 (2.5%) | 5 / 0 | 192 | 0 | 0 |
| 33 | Joel | OT | 73 | 4 (5.5%) | 4 / 0 | 69 | 0 | 0 |
| 34 | Amos | OT | 146 | 10 (6.8%) | 10 / 0 | 136 | 0 | 0 |
| 35 | Obadiah | OT | 21 | 0 (0.0%) | 0 / 0 | 21 | 0 | 0 |
| 36 | Jonah | OT | 48 | 19 (39.6%) | 3 / 16 | 29 | 0 | 0 |
| 37 | Micah | OT | 105 | 4 (3.8%) | 4 / 0 | 101 | 0 | 2 |
| 38 | Nahum | OT | 47 | 2 (4.3%) | 2 / 0 | 45 | 0 | 0 |
| 39 | Habakkuk | OT | 56 | 1 (1.8%) | 1 / 0 | 55 | 0 | 0 |
| 40 | Zephaniah | OT | 53 | 1 (1.9%) | 1 / 0 | 52 | 0 | 0 |
| 41 | Haggai | OT | 38 | 1 (2.6%) | 1 / 0 | 37 | 0 | 0 |
| 42 | Zechariah | OT | 211 | 18 (8.5%) | 18 / 0 | 193 | 0 | 2 |
| 43 | Malachi | OT | 55 | 7 (12.7%) | 7 / 0 | 48 | 0 | 0 |
| 44 | Matthew | NT | 1071 | 223 (20.8%) | 75 / 148 | 848 | 0 | 0 |
| 45 | Mark | NT | 678 | 64 (9.4%) | 46 / 18 | 614 | 0 | 0 |
| 46 | Luke | NT | 1151 | 76 (6.6%) | 46 / 30 | 1075 | 0 | 1 |
| 47 | John | NT | 879 | 222 (25.3%) | 68 / 154 | 657 | 0 | 3 |
| 48 | Acts | NT | 1006 | 99 (9.8%) | 69 / 30 | 907 | 0 | 4 |
| 49 | Romans | NT | 436 | 104 (23.9%) | 45 / 59 | 332 | 0 | 7 |
| 50 | 1 Corinthians | NT | 437 | 38 (8.7%) | 26 / 12 | 399 | 0 | 0 |
| 51 | 2 Corinthians | NT | 256 | 14 (5.5%) | 14 / 0 | 242 | 0 | 1 |
| 52 | Galatians | NT | 149 | 27 (18.1%) | 9 / 18 | 122 | 0 | 1 |
| 53 | Ephesians | NT | 155 | 12 (7.7%) | 12 / 0 | 143 | 0 | 0 |
| 54 | Philippians | NT | 104 | 2 (1.9%) | 2 / 0 | 102 | 0 | 0 |
| 55 | Colossians | NT | 95 | 10 (10.5%) | 10 / 0 | 85 | 0 | 0 |
| 56 | 1 Thessalonians | NT | 89 | 2 (2.2%) | 2 / 0 | 87 | 0 | 0 |
| 57 | 2 Thessalonians | NT | 47 | 4 (8.5%) | 4 / 0 | 43 | 0 | 0 |
| 58 | 1 Timothy | NT | 113 | 10 (8.8%) | 10 / 0 | 103 | 0 | 0 |
| 59 | 2 Timothy | NT | 83 | 4 (4.8%) | 4 / 0 | 79 | 0 | 1 |
| 60 | Titus | NT | 46 | 4 (8.7%) | 4 / 0 | 42 | 0 | 0 |
| 61 | Philemon | NT | 25 | 25 (100.0%) | 25 / 0 | 0 | 0 | 0 |
| 62 | Hebrews | NT | 303 | 32 (10.6%) | 19 / 13 | 271 | 0 | 1 |
| 63 | James | NT | 108 | 23 (21.3%) | 7 / 16 | 85 | 0 | 1 |
| 64 | 1 Peter | NT | 105 | 2 (1.9%) | 2 / 0 | 103 | 0 | 0 |
| 65 | 2 Peter | NT | 61 | 2 (3.3%) | 2 / 0 | 59 | 0 | 0 |
| 66 | 1 John | NT | 105 | 9 (8.6%) | 9 / 0 | 96 | 0 | 0 |
| 67 | 2 John | NT | 13 | 13 (100.0%) | 13 / 0 | 0 | 0 | 0 |
| 68 | 3 John | NT | 15 | 15 (100.0%) | 15 / 0 | 0 | 0 | 0 |
| 69 | Jude | NT | 25 | 6 (24.0%) | 6 / 0 | 19 | 0 | 0 |
| 70 | Revelation | NT | 405 | 107 (26.4%) | 65 / 42 | 298 | 0 | 1 |
