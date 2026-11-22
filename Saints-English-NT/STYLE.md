# Saints Traditional English — Style Policy & Trilingual Specification (NKJV-Style)

> Locked by the user (Swarm Board `#379`, refined to NKJV-register in `#389`). All translators (`@greek-translator`, `@hebrew-translator`, `@latin-translator`), reviewers (`@translation-reviewer`), and the automated validator (`tools/validate_traditional_english.py`) follow this specification strictly.
>
> **Canonical Critical Text Source (Zero Duplication):** Reads directly from the canonical `50793ea` (Studio v9 Phase 2) per-chapter source JSONs in `../Saints-Modern-English/full/source/{grc,heb,lat}/<NN-slug>/<ch:03d>.json`. Output translations live strictly inside `Saints-Traditional-English/full/out/{grc,heb,lat}/<NN-slug>/<ch:03d>.json` (never modifying `Saints-Modern-English/`).

## 1. Register: NKJV-Style (Modern Grammar + Revered King James Cadence)
- **Complete equivalence in elevated, worship-ready English**, following the approach of the **New King James Version (NKJV)**: effortless modern grammar paired with timeless, dignified, resonant King James rhythm.
- **Strictly Modern Pronouns & Modern Verbs EVERYWHERE:**
  - Use modern second-person pronouns: **`you` / `your` / `yours` / `yourself` / `yourselves`** (NEVER `thou`, `thee`, `thy`, `thine`, `thyself`, `ye`).
  - Use modern verb forms: **`are`, `have`, `has`, `do`, `does`, `say`, `says`, `spoke`, `will`, `shall`, `comes`, `goes`, `gives`, `makes`, `knows`, `loves`, `abides`, `dwells`** (NEVER `-est`/`-st`, `-eth`/`-th`, `art` [archaic verb], `hast`, `dost`, `wilt`, `shalt`, `wast`, `wert`, `didst`, `hadst`, `canst`, `mayest`, `hath`, `doth`, `saith`, `spake`).
  - **NEVER** use obsolete 1611 particles/forms: `unto`, `whosoever`, `whatsoever`, `whomsoever`, `wheresoever`, `whensoever`, `wherefore`, `thereof`, `herein`, `therein`, `thereunto`, `hereunto`, `whereunto`, `thereby`, `whereby`, `thereon`, `therewith`, `wherewith`, `therefrom`, `wherefrom`, `heretofore`, `verily`, `begat`, `begot`, `forasmuch`, `inasmuch`, `whence`, `whither`, `thither`, `hither`, `peradventure`, `howbeit`, `straitway`, `straightway`, `entreated`, `besought`.
  - **Zero modern colloquial contractions:** Never use `don't`, `won't`, `can't`, `isn't`, `aren't`, `haven't`, `hasn't`, `didn't`, `I'm`, `I've`, `I'll`, `it's`, `let's`, etc.
- **Dignified NKJV Heritage & Liturgical Cadence (Distinct from Flat Modern English):**
  - Retain resonant, majestic, crystal-clear traditional biblical vocabulary and stately formal-equivalent clause rhythm:
    - `Behold,` / `Thus says the LORD` (`heb`) / `Thus says the Lord` (`grc`/`lat`) / `Assuredly, I say to you` (`ἀμὴν λέγω ὑμῖν` / `amen dico vobis`)
    - `brethren`, `firmament` (where literally fitting), `dwell`, `abide`, `slay`/`slain`, `lest` (when smooth), `countenance`, `tabernacle`, `multitude`, `iniquity`, `transgression`, `lovingkindness`, `mercy`, `wrath`, `handmaid`, `forsook`/`forsaken`, `befall`, `hereafter`, `shall` for solemn promise/prophecy/command, `and it came to pass`.
  - Every verse must read smoothly aloud in public worship while remaining unmistakably traditional, solemn, and elevated.

## 2. Copyright & Fresh Originality
- Translate **completely fresh from the canonical Saints Critical Text**.
- **NEVER** copy or closely clone the **NKJV**, 1769 **KJV**, **ESV**, **NASB 1995**, **Douay-Rheims**, **ASV 1901**, or any other published translation word-for-word, especially on famous passages (`Gen 1`, `Ps 22/23`, `Isa 53`, `John 1`, `John 3:16`, `Rom 8`, `1 Cor 13`, `Rev 21–22`).
- "NKJV-style" defines the **method and elevated modern-grammar register**, not a text to copy.

## 3. Own-Source Fidelity (Zero Cross-Language Harmonization)
- **Greek (`grc`)**: Translate strictly from `../Saints-Modern-English/full/source/grc/` (Saints Greek Critical Text — Septuagint OT + NT). Never harmonize LXX OT to Hebrew MT.
  - Preserve `⟦` and `⟧` brackets verbatim **ONLY** on verses that carry them in the Greek source.
- **Hebrew & Biblical Aramaic (`heb`)**: Translate strictly from `../Saints-Modern-English/full/source/heb/` (Saints Hebrew Critical Text — Masoretic Hebrew + Biblical Aramaic in Ezra `4:8–6:18`, `7:12–26`; Jer `10:11`; Dan `2:4b–7:28`). Never harmonize to LXX or Vulgate.
  - **Ketiv / Qere discipline (STRICT):** Translate the **qere (read form)** cleanly. Never emit parentheses `(` `)`, underscores `_`, or leaked Hebrew/Aramaic characters in `verses` or `unplaced`. Note meaningful ketiv/qere variants concisely in `notes`.
  - Preserve `⟦` and `⟧` brackets verbatim **ONLY** where present in the Hebrew source (`Joshua 21:36–37`).
- **Latin (`lat`)**: Translate strictly from `../Saints-Modern-English/full/source/lat/` (Saints Latin Critical Text — Clementine Vulgate). Never harmonize to Greek or Hebrew.
  - Preserve distinctly Vulgate readings faithfully (e.g., `Gen 1:1` `creavit cælum` → `"created heaven"` [singular]; `Gen 3:15` `ipsa conteret` → `"she shall crush"` with note).
  - **ZERO** `⟦ ⟧` brackets in Latin (the Latin Critical Text has none).

## 4. Divine Names & Capitalized Divine Pronouns
- **Hebrew / Aramaic (`heb`):**
  - `יְהוָה` / `יהוה` / `יָהּ` → **`the LORD`** (all-caps `LORD`; NEVER `YHWH`, `Yahweh`, or `Jehovah`).
  - `אֲדֹנָי יֱהֹוִה` → **`the Lord GOD`**.
  - `יְהוָה אֲדֹנָי` → **`GOD the Lord`**.
  - `אֱלֹהִים` / `אֱלָהּ` → **`God`**; standalone `אֲדֹנָי` → **`the Lord`**.
- **Greek (`grc`) & Latin (`lat`):**
  - `κύριος` / `Dominus` referring to God or Christ → **`the Lord`** (Title case; **NEVER** all-caps `LORD`, `GOD`, `YHWH`, or `Jehovah`).
  - `θεός` / `Deus` → **`God`**; `κύριος ὁ θεός` / `Dominus Deus` → **`the Lord God`**.
- **Capitalize ALL Divine Pronouns Across All 3 Languages (NKJV Convention):**
  - `He`, `Him`, `His`, `Himself`, `You`, `Your`, `Yours`, `Yourself`, `Me`, `My`, `Mine`, `Myself`, `I` (and `Us`/`Our`/`Ourselves` where God speaks in divine plural, e.g. `Gen 1:26`).

## 5. Modern American Spelling, Proper Names & Formatting
- **Modern American English Spelling (STRICT):**
  - Use American spellings: `honor`, `favor`, `savior`, `armor`, `labor`, `color`, `neighbor`, `behavior`, `savor`, `vapor`, `odor`, `valor`, `splendor`, `show`/`showed`/`shows`/`showbread`, `music`, `public`, `traffic`, `scepter`, `sepulcher`, `center`, `plow`, `offense`, `defense`, `recompense`, `judgment`, `fulfill`, `skillful`, `willful`, `marvelous`, `counselor`, `worshiped`/`worshiper`.
  - **NEVER** use British or 1769-archaic spellings (`honour`, `favour`, `saviour`, `armour`, `labour`, `colour`, `neighbour`, `behaviour`, `savour`, `shew`, `shewed`, `musick`, `publick`, `traffick`, `sepulchre`, `sceptre`, `plough`, `offence`, `defence`, `recompence`, `judgement`, `fulfil`, `skilful`, `wilful`, `marvellous`, `counsellor`, `worshipped`).
- **Standard Modern Biblical Proper Names (see `glossary.json`):**
  - Use standard modern English biblical spellings: `Isaiah`, `Elijah`, `Elisha`, `Noah`, `Moses`, `Joshua`, `Jeremiah`, `Ezekiel`, `Hosea`, `Joel`, `Amos`, `Obadiah`, `Jonah`, `Micah`, `Habakkuk`, `Zephaniah`, `Haggai`, `Malachi`, `Hezekiah`, `Josiah`, `Solomon`, `Zion`, `Haran`, `Nebuchadnezzar`, `Pharaoh`, `Judea`, `Capernaum`, `Timothy`, `Luke`, `Mark`, `Korah`, `Hagar`, `Sarah`, `Rahab`, `Gomorrah`, `Sodom`.
  - **NEVER** use archaic KJV/Douay spellings (`Esaias`, `Isaias`, `Elias`, `Eliseus`, `Noe`, `Moyses`, `Josue`, `Jeremias`, `Jeremy`, `Ezechiel`, `Osee`, `Jonas`, `Pharao`, `Judaea`, `Capharnaum`, `Nabuchodonosor`, `Salomon`, `Sion` [except noted `Deut 4:48` Mount Sion], `Core`, `Timotheus`, `Lucas`, `Marcus`). Keep a genuinely distinct source name ONLY where the critical text itself has a different name, and explain it in `notes`.
- **Plain Text, ASCII Quotes & Spelled-Out Numbers:**
  - Plain text only in `verses` and `unplaced[].text`: **ZERO** HTML, **ZERO** Markdown, **ZERO** italics, **ZERO** line breaks (`\n`/`\r`), **ZERO** Arabic digits (`0`–`9` — spell out all numbers in words!).
  - Use straight ASCII American double quotes (`"..."`) for direct speech and straight single quotes (`'...'`) for speech within speech; balance straight double quotes within **each chapter** (`0` curly quotes `“`/`”`/`‘`/`’`).

## 6. Output JSON Schema & `unplaced` Support
- **File Path:** `Saints-Traditional-English/full/out/<lang>/<NN-slug>/<ch:03d>.json`
- **Schema:**
  ```json
  {
    "verses": {
      "1:1": "Plain-text NKJV-style Traditional English verse here."
    },
    "notes": {
      "1:1": "Optional concise 1-2 sentence translator note on a genuinely hard, debated, or edition-distinct reading."
    },
    "unplaced": [
      {
        "after": "0:0",
        "src": "Prologue",
        "reason": "prologue",
        "text": "Optional array matching source unplaced items in exact length and order.",
        "note": "Optional concise note."
      }
    ]
  }
  ```
  *(Omit `"unplaced"` when the source chapter has none.)*

## 7. Trilingual Pilot Scope (30 Chapter Files — Saints Versification)
| Passage | Book Dir & Chapters | `grc` | `heb` | `lat` | Key Checks |
|---|---|---:|---:|---:|---|
| Genesis 1–3 | `01-genesis` ch `001`–`003` | 80v | 80v | 80v | Own-source creation (`made heaven` / `created the heavens` / `created heaven`), `Gen 3:15` (`he` vs `she`), stately NKJV cadence |
| Psalm 22 (MT 23) | `21-psalms` ch `022` | 6v | 6v | 6v | Worship-ready lyrical cadence, `the Lord` (`grc`/`lat`) vs `the LORD` (`heb`), capitalized `He/His/You/Your` |
| Isaiah 53 | `28-isaiah` ch `053` | 12v | 12v | 12v | Distinct LXX vs MT vs Vulgate Servant Song, fresh originality |
| Daniel 2 | `31-daniel` ch `002` | 49v | 49v | 49v | `grc` Theodotion; `heb` Hebrew `2:1–4a` + Biblical Aramaic `2:4b–49` (16 ketiv/qere); `lat` Vulgate |
| John 1 | `47-john` ch `001` | 51v | — | 51v | Prologue (`1:1`, `1:14`, `1:18`), `"Assuredly, assuredly, I say to you"` |
| John 7:53 & 8:1–11 | `47-john` ch `007`–`008` *(partial)* | 12v | — | 12v | `grc`: `⟦ ⟧` verbatim on all 12 verses; `lat`: unbracketed |
| Romans 8 | `49-romans` ch `008` | 39v | — | 39v | Life in the Spirit, `Abba`, `8:28`, `8:38–39` |
| Romans 12 | `49-romans` ch `012` | 21v | — | 21v | Living sacrifice, `brethren`, renewal of the mind |
| Revelation 1 | `70-revelation` ch `001` | 20v | — | 20v | Majesty of the glorified Christ, `grc` `loosed us` vs `lat` `washed us` (`1:5`) |
| **Totals** | **30 files (26 full + 4 partial)** | **12 files** | **6 files** | **12 files** | **All 3 critical texts represented** |

## 8. Validation Gate
Before handing off for review, run:
```powershell
python "c:\Users\penna\Documents\Saints Website Repository\Saints-Traditional-English\tools\validate_traditional_english.py" --lang <grc|heb|lat> --partial-ok --strict
```
Fix every `FAIL` (and review any `WARN`) until every chapter passes cleanly.
