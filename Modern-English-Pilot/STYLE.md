# Saints Modern English — Style Policy & Pilot Specification

> Locked by the user (Swarm Board #65). All translators (`@greek-translator`, `@hebrew-translator`, `@latin-translator`), the verifier (`@translation-reviewer`), and the automated validator (`tools/validate_modern_english.py`) follow this specification strictly.

## 1. Register & Method
- **Literal (formal-equivalent) English smoothed for reading**, similar in approach to the **NASB 1995**.
- Follow the source text's wording, grammar (tense, aspect, voice, person, number, clauses), and word order wherever natural Modern English allows.
- Keep idioms literal when the meaning stays clear.
- Translate repeated key terms consistently within a passage and across books.
- Do **not** paraphrase, interpret, harmonize, or expand beyond the source wording.
- **Fully modern vocabulary**:
  - **No archaisms**: never use `thee`, `thou`, `thy`, `thine`, `ye`, `unto`, `hath`, `doth`, `spake`, `saith`, `shalt`, `wilt`, `hast`, `art`, `doeth`, `goeth`, `cometh`, `verily`, `begat`, `begot`, `brethren`, `firmament`, `wherefore`, `thereof`, `herein`, `therein`, `thereunto`, `whosoever`, `whatsoever`.
  - **No `"behold"`**: use `"look"`, `"see"`, `"now"`, or `"here is"` as context requires.

## 2. Copyright & Originality
- Translate **fresh from the Saints Critical Text**.
- **NEVER** reproduce the NASB, ESV, NRSV, KJV, NIV, Douay-Rheims, or any other published translation word for word, and **never** copy the existing Saints English / Hebrew–English / Latin–English columns.
- "NASB-like" describes the formal-equivalence **method**, not a text to imitate.

## 3. Own-Source Fidelity (Zero Cross-Language Harmonization)
- Translate **Greek** strictly from `pilot/source/grc/` (Saints Greek Critical Text).
- Translate **Hebrew/Aramaic** strictly from `pilot/source/heb/` (Saints Hebrew Critical Text — note Daniel 2:4b–49 is Biblical Aramaic).
- Translate **Latin** strictly from `pilot/source/lat/` (Saints Latin Critical Text, Clementine/Vulgate basis).
- **Never harmonize across languages.** Examples:
  - Genesis 1:1 Greek `ἐποίησεν τὸν οὐρανόν` → `"made heaven"` (singular);
  - Genesis 1:1 Hebrew `בָּרָא אֵת הַשָּׁמַיִם` → `"created the heavens"` (plural);
  - Genesis 1:1 Latin `creavit cælum` → `"created heaven"` (singular).
  - Genesis 3:15 Latin `ipsa conteret` → `"she will crush"` (note the Vulgate feminine pronoun in `notes`!).

## 4. Divine Names & Pronouns
- **Hebrew (`heb`)**:
  - `יְהוָה` / `יהוה` → **`the LORD`** (all-caps `LORD`, never `YHWH` or `Jehovah`).
  - `אֲדֹנָי יְהוָה` → **`the Lord GOD`**.
  - `אֱלֹהִים` → **`God`**.
- **Greek (`grc`) & Latin (`lat`)**:
  - `κύριος` / `Dominus` referring to God → **`the Lord`** (Title case, never all-caps `LORD` or `YHWH`).
  - `θεός` / `Deus` → **`God`**.
- **Pronouns referring to God**: Capitalize pronouns referring to God (**`He`, `Him`, `His`, `Himself`, `You`, `Your`, `Yours`, `Yourself`**).

## 5. Proper Names
- Use standard modern English spellings (see `glossary.json`): `Haran`, `Elijah`, `Solomon`, `Zion`, `Isaiah`, `Noah`, `Nebuchadnezzar`, `Moses`, `Judea`, `Capernaum`, etc.
- Keep a different proper-name form **only** where the source text itself genuinely has a different name (e.g., Septuagint-distinct or Hebrew-distinct place names), and **flag it in `notes`**.

## 6. Text-Critical Markers & Multi-Segment Verses
- **`⟦ ⟧` double brackets**: Preserve `⟦` and `⟧` **verbatim** around every bracketed verse (e.g., Greek John 7:53 and 8:1–11). Do not add `⟦ ⟧` where the source does not have them (e.g., Latin John 7:53–8:11 is unbracketed).
- **Hebrew Ketiv / Qere**: The Hebrew source shows written `ketiv` in `(parentheses)` followed by the read `qere` (e.g., Daniel 2 has 16 ketiv/qere verses). Always translate the **qere (read form)** and **never** emit raw ketiv parentheses `(...)` or `_` joiners.
- **Multi-segment verses**: Source verses already join multi-segment source spans into one string; produce one English verse per `"ch:v"` key.

## 7. Output Format & Per-Verse `notes`
- **Output directory**: `pilot/out/{grc,heb,lat}/` with **exact matching filenames** to `pilot/source/{grc,heb,lat}/`.
- **JSON shape**:
  ```json
  {
    "verses": {
      "1:1": "Plain-text Modern English verse here.",
      "1:2": "..."
    },
    "notes": {
      "1:2": "One or two plain sentences explaining a genuinely hard or debated source choice and why it was rendered this way."
    }
  }
  ```
- **Plain text only** in `verses`: no HTML, no Markdown, no italics, no line breaks (`\n`/`\r`).
- Modern American punctuation: double quotes (`"..."`) for direct speech, single quotes (`'...'`) for speech inside speech.
- Every source `"ch:v"` key MUST have exactly one non-empty English string.
- Include optional `notes` for genuinely difficult, debated, or edition-distinct translation choices (these may later feed the Concordance "why this wording" panel).

## 8. Pilot Passages (Saints Versification)
| Passage | File Name | `grc` | `heb` | `lat` | Notes |
|---|---|:---:|:---:|:---:|---|
| Genesis 1 | `01-genesis-1.json` | 31 | 31 | 31 | LXX `made heaven` vs MT `created the heavens` vs Lat `created heaven` |
| Genesis 2 | `01-genesis-2.json` | 25 | 25 | 25 | Creation of humanity, Eden rivers |
| Genesis 3 | `01-genesis-3.json` | 24 | 24 | 24 | Gen 3:15 (`αὐτός` vs `הוּא` vs `ipsa`) |
| Psalm 23 (= Gk/Lat Ps 22) | `21-psalms-22.json` | 6 | 6 | 6 | All 3 sources use Saints keys `22:1`–`22:6`; `heb` `src` maps to MT `23:1`–`23:6` |
| Isaiah 53 | `28-isaiah-53.json` | 12 | 12 | 12 | Distinct LXX vs MT vs Vulgate Servant Song wording |
| Daniel 2 | `31-daniel-2.json` | 49 | 49 | 49 | `grc` is Theodotion; `heb` is Hebrew `2:1–4a` + **Biblical Aramaic `2:4b–49`** (16 ketiv/qere) |
| John 1 | `47-john-1.json` | 51 | — | 51 | Prologue (`1:1c`, `1:18`), witness of John, first disciples |
| John 7:53–8:11 | `47-john-7-53-8-11.json` | 12 | — | 12 | `grc`: all 12 verses carry `⟦ ⟧`; `lat`: unbracketed |
| Romans 8 | `49-romans-8.json` | 39 | — | 39 | Life in the Spirit, `8:28`, `Abba` (`8:15`) |
| Romans 12 | `49-romans-12.json` | 21 | — | 21 | Benchmark chapter (`12:1–2` living sacrifice, renewal of the mind) |
| **Totals** | **26 files** | **270** | **147** | **270** | **687 pilot verse translations total** |

## 9. Validation Gate
Before handing off to `@translation-reviewer`, run:
```powershell
python "c:\Users\penna\Documents\Saints Website Repository\Saints-Modern-English\tools\validate_modern_english.py" --lang <grc|heb|lat>
```
Fix every `FAIL` line until the report shows `PASS` for every file.
