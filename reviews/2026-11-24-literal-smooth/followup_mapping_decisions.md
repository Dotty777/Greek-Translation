# Follow-Up Greek Verse Mapping & Note-Attachment Audit Ledger

**Date:** 2026-11-25  
**Auditor:** `@greek-mapper` (Greek-Translation follow-up audit; coordinated with `@latin-studio-mapper` on `versification.py` in `#115`–`#116`)  
**Scope:** All 70 Greek books (`34,198` adopted SGCT verses == `studio.db` Greek rows with `0` diffs; `34,154` placed + `42` unplaced ME entries; `6,202` translator notes).  
**Charter Wording Gate:** **0 English verse-text wording edits made** (`greek_wording_proposals.jsonl`: `0` entries). All repository changes are strictly verse-placement restoration (`unplaced` → `verses`), translator-note accuracy fixes, Markdown/README synchronization, and mapping metadata.

## 1. Corpus-Wide Status Partition (All 70 Greek Books — `34,198` Adopted Verses)

| Status | OT (43 books) | NT (27 books) | Total (70 books) | Definition |
|---|---:|---:|---:|---|
| `mapped_verified` | 25,965 | 7,942 | **33,907** | 1:1 monotone correspondence (`33,838` exact identity + `69` monotone shifted offset) |
| `split_or_merged` | 80 | 0 | **80** | Clause boundary split (1-to-many) or merge (many-to-1) within sequential progression |
| `reordered` | 178 | 0 | **178** | Transposed or non-monotone order (`160` Sirach 30:25–36:31 + `16` other OT loci) |
| `no_counterpart` | 15 | 18 | **33** | No Saints.Bible counterpart (`2 Kgs 25:10`, `14` Theodotion Daniel verses, `18` bracketed NT verses) |
| `unresolved` | 0 | 0 | **0** | None remaining |
| **Total Adopted Greek Verses** | **26,238** | **7,960** | **34,198** | **100% accounted for (`34,198 == 34,198`)** |

> **Modern English Reconciliation:** `34,198` adopted Greek verses `+ 1` separated Sirach Prologue (split out of SGCT `Sir 1:1`) `− 3` Sirach merged pairs in restored chapter order (`32:4+5→35:4`, `33:1+2→36:1`, `33:11+36:16→36:10`) `= 34,196` ME entries (`34,154` placed + `42` unplaced: `1` Sirach Prologue + `23` OT `no-site-verse` + `18` NT bracketed `⟦ ⟧`).

## 2. Priority Loci — Clause-by-Clause Content Verification

### 2.1 Native Greek `Exodus 39:14–21` (including `Exodus 39:15` & `39:21`)
- **Finding (Studio `versification.py`):** Pre-Stage-1 Swete had a corrupt `40:8` line in `Exod 39:15`; Stage 1 (`a0d022c1`) repaired `39:14–16`, restoring genuine `καὶ τὸ θυσιαστήριον καὶ πάντα τὰ σκεύη αὐτοῦ,` at `39:15` (= `Saints.Bible 39:15a`), while `versification.py` still carried stale `39:15 -` and `_DUPLICATE_OR_PLACEHOLDER`. Coordinated with `@latin-studio-mapper` (`#115` → `#116`): updated to `39:5-13 = 39:4-12`, `39:14 > 39:13-14`, `39:15` identity, `39:16 > 39:15-16` (with Hebrew `39:33 = 39:13` and Latin `39:32 = 39:13` guards).
- **Finding (`Greek-Translation`):** `02-exodus.json` already held correct English at `39:14`, `39:15`, and `39:16`, but `39:21` had been stranded in `unplaced` with a false `'no separate place'` note, leaving a gap between `39:20,` and `39:22`. Moved `39:21` verbatim into `verses['39:21']` (0 wording change), removed empty `unplaced`, and added Rule 2 versification notes at `39:14` and `39:21` (`1,163` verses, `176` notes).

### 2.2 Native Greek `Numbers 21:19–22` (including `Numbers 21:20`)
- **Finding (Studio `versification.py`):** Stage 1 repaired `Num 21:20–21`, so post-Stage-1 SGCT `21:20` (`Καὶ ἀπέστειλεν Μωυσῆς πρέσβεις...`) maps 1:1 to `Saints.Bible 21:21`, and `21:21` + `21:22` share `Saints.Bible 21:22`. Pre-Stage-1 `versification.py` still dropped `21:20` as a duplicate. Reconciled in `#115` → `#116` (`21:20 = 21:21`, `21:21 = 21:22`, removed `21:20` from `_DUPLICATE_OR_PLACEHOLDER`).
- **Finding (`Greek-Translation`):** `04-numbers.json` already placed `21:19–22` with 100% matching content; added Rule 2 versification note at `21:20` (`1,287` verses, `207` notes).

### 2.3 Native Greek `Sirach 1:1` + Prologue, `Sirach 41:22–24`, and `Sirach 51:11`
- **`Sirach 1:1` & Prologue (`split_or_merged`):** `studio.db` concatenates the ~144-word Greek Translator's Prologue with the 8-word maxim of `1:1` in entry `1:1`. `versification.py` intentionally keeps `sirach 1:1 -` so concordance indexing does not misfile Prologue tokens under `1:1`. `Modern-English-OT` (`27-sirach.json` / `chapter-01.md`) cleanly separates `unplaced:Prologue` (`## Prologue`, `Saints.Bible` chapter `0`) and `verses['1:1']` (`Saints.Bible 1:1`). Added explicit Rule 2 note at `1:1`.
- **`Sirach 41:22–24`:** Stage 1 repaired `41:23–24` so SGCT `41:22` spans `Saints.Bible 41:24–25`, `41:23` maps 1:1 to `41:26`, and `41:24` maps 1:1 to `41:27`. `versification.py` still dropped `41:23` as duplicate; reconciled in `#115` → `#116` (`41:23 = 41:26`, `41:24 = 41:27`, removed `41:23` from `_DUPLICATE_OR_PLACEHOLDER`, with Vulgate `42:1 > 41:24,41:23,42:1` guard). In `27-sirach.json`, moved `41:24` verbatim from `unplaced` into `verses['41:24']` (fixing dangling semicolon at `41:23;`) and replaced the false `'no separate place'` note with an accurate Rule 2 note at `41:24`.
- **`Sirach 51:11`:** Clause-verified against `Saints.Bible`: SGCT `51:11` spans `Saints.Bible 51:10b` (7 words; majority concordance target in `versification.py`) + `51:11a` (5 words), while `51:12` spans `51:11b–12`. Moved `51:11` verbatim from `unplaced` into `verses['51:11']` and replaced the false `'no separate place'` note with an accurate Rule 2 note at `51:11` (`27-sirach.json`: `1,354` verses, `240` notes, `1` unplaced [`Prologue` only]).

### 2.4 Documented `Sirach 30:25–36:31` Transpositions (All 160 Verses Audited)
- Verified **160/160** transposed native SGCT verses against `27-sirach.json` (`157` ME slots in restored `Saints.Bible` chapter order, incorporating the 3 documented merged pairs `32:4+5→35:4`, `33:1+2→36:1`, `33:11+36:16→36:10`) and against `sirach/verses.json`.
- Verified `Sir 32:18` cross-reference note `(compare 33:12)` is accurate (`ME 33:12` = SGCT `36:12` carries reflexive `πρὸς αὐτὸν`).
- Corrected **4 imprecise seam notes** (`35:12`, `35:21`, `35:24`, `36:18`) that falsely stated `Saints.Bible 35:11`, `35:23`, or `36:17` had `'no separate Greek GI line'` when those verses are in fact combined inside ME `35:12` (`SGCT 32:12`), `35:22` (`SGCT 32:19`), and `36:16` (`SGCT 36:22`), and appended explicit span clarifications to `33:32` (`SB 33:32–33`) and `36:26` (`SB 36:26–27`).

## 3. Additional Post-Stage-1 & Full-Corpus 70-Book Regression Findings

1. **`1 Chronicles 12:4–5`:** Stage 1 split `12:4` and `12:5` cleanly into 1:1 matches with `Saints.Bible 12:4` and `12:5`. Reconciled `versification.py` (`#115` → `#116`, removing stale `12:4 > 12:4-5`, `12:5 -`, and `_DUPLICATE_OR_PLACEHOLDER`). Moved `12:5` verbatim from `unplaced` into `verses['12:5']` in `13-1-chronicles.json` (removing dangling comma at `12:4,` and false `'no separate slot'` note; `930` verses, `155` notes, `0` unplaced).
2. **`Nehemiah 12:17–19`:** Stage 1 restored 1:1 alignment with `Saints.Bible 12:17–19`; reconciled `versification.py` (`#115` → `#116`, removing stale `12:17 > 12:17-18` and `12:18 = 12:19`). `16-nehemiah.json` already placed `12:17–19` cleanly.
3. **`Leviticus 8:19–29`:** Stage 1 moved the washing clause into `8:19`, so `8:19` spans `Saints.Bible 8:20` (majority) + `8:21a`. Reconciled `versification.py` (`#115` → `#116`: `8:19 > 8:20-21`, `8:20-29 = 8:21-30`, with Hebrew/Latin `8:20 = 8:20` guards).
4. **All other regression-check loci verified clean (`0` additional bugs):** `Deut 28:69/29:1–29`, `1 Chr 1:48–51, 6:54, 7:26`, `Num 27:3–7`, `1 Kgs 6:17–19`, `1 Kgs 11:5–8` (combined SB anchor), `Neh 12:8–9`, `Job 41:1–3`, `Ps 12:4–5` (already reconciled in `#43`), `Prov 24/30/31`, `Ezek 21:24–25`, `Jer 7:27–28` (combined SB anchor), `Jer 10:5/9`, `Jer 23:40`, `Jer 25:20`, `Jer 29:1`, `Dan 3–6` (including combined SB `5:26–28` and OG vs Theodotion), `Judg 5:13` (B vs A text), `Esther` Additions A–F, `2 Kgs 25:10` (`no_counterpart`), `Dan 6:16` (`no_counterpart`), and all `18` NT bracketed `unplaced` verses (`no_counterpart`).

## 4. Per-Book Non-Identity Summary (Books with Non-Identity Mappings)

| # | Book | Source | `mapped_verified` (id / shift) | `split_or_merged` | `reordered` | `no_counterpart` | `unresolved` | ME Placed + Unplaced |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Genesis | 1531 | 1529 (1529/0) | 2 | 0 | 0 | 0 | 1531 + 0 |
| 2 | Exodus | 1163 | 1155 (1145/10) | 8 | 0 | 0 | 0 | 1163 + 0 |
| 3 | Leviticus | 859 | 852 (844/8) | 7 | 0 | 0 | 0 | 859 + 0 |
| 4 | Numbers | 1288 | 1280 (1276/4) | 7 | 1 | 0 | 0 | 1287 + 1 |
| 5 | Deuteronomy | 958 | 956 (927/29) | 0 | 2 | 0 | 0 | 958 + 0 |
| 11 | 1 Kings | 755 | 749 (749/0) | 5 | 1 | 0 | 0 | 754 + 1 |
| 12 | 2 Kings | 719 | 717 (717/0) | 1 | 0 | 1 | 0 | 718 + 1 |
| 13 | 1 Chronicles | 930 | 928 (928/0) | 2 | 0 | 0 | 0 | 930 + 0 |
| 21 | Psalms | 2533 | 2530 (2527/3) | 3 | 0 | 0 | 0 | 2533 + 0 |
| 22 | Proverbs | 889 | 884 (882/2) | 5 | 0 | 0 | 0 | 889 + 0 |
| 26 | Wisdom of Solomon | 436 | 432 (421/11) | 4 | 0 | 0 | 0 | 435 + 1 |
| 27 | Sirach | 1357 | 1169 (1167/2) | 28 | 160 | 0 | 0 | 1354 + 1 |
| 29 | Jeremiah | 1296 | 1290 (1290/0) | 2 | 4 | 0 | 0 | 1295 + 1 |
| 30 | Ezekiel | 1265 | 1263 (1263/0) | 2 | 0 | 0 | 0 | 1265 + 0 |
| 31 | Daniel | 420 | 394 (394/0) | 2 | 10 | 14 | 0 | 402 + 18 |
| 34 | Amos | 146 | 144 (144/0) | 2 | 0 | 0 | 0 | 146 + 0 |
| 44 | Matthew | 1071 | 1068 (1068/0) | 0 | 0 | 3 | 0 | 1068 + 3 |
| 45 | Mark | 678 | 673 (673/0) | 0 | 0 | 5 | 0 | 673 + 5 |
| 46 | Luke | 1151 | 1149 (1149/0) | 0 | 0 | 2 | 0 | 1149 + 2 |
| 47 | John | 879 | 878 (878/0) | 0 | 0 | 1 | 0 | 878 + 1 |
| 48 | Acts | 1006 | 1002 (1002/0) | 0 | 0 | 4 | 0 | 1002 + 4 |
| 49 | Romans | 436 | 433 (433/0) | 0 | 0 | 3 | 0 | 433 + 3 |

*All remaining 48 books are 100% 1:1 `mapped_verified` identity across every verse (`0` splits, `0` reorders, `0` unplaced, `0` unresolved). Full 70-book machine-readable table: [`Modern-English-OT/parallel-verse-map.json`](../../Modern-English-OT/parallel-verse-map.json) and [`followup_mapping_decisions.jsonl`](followup_mapping_decisions.jsonl).*
