# James 02 — Saints Greek Critical Text

**Division:** `06_Discipleship` · **Language:** `Greek` · **Engine:** `Textual Analysis Brain (Claude-designed · internal evidence · offline)` · **Updated:** `2026-11-25T00:07:49Z`

**Versification:** Septuagint numbering as in Brenton/eBible (the Saints.Bible numbering) for the OT; standard numbering for the NT. Witnesses that number differently (e.g. Swete in Joel and Malachi) are re-aligned by content. Proverbs is numbered as Saints.Bible numbers it: Hebrew chapter and verse numbers in the Greek order (24:1–22e, 30:1–14, 24:23–34, 30:15–33, 31:1–9, 25–29, 31:10–31), not as the Brenton e-text runs 30:1–31:9 on as 24:22–62. Numbering anchor for this chapter: `SBLGNT`. Spelling and punctuation follow `SBLGNT` where it attests the adopted reading.

**Sigla in the text:** `⟦ ⟧` = verse absent from (or bracketed by) witnesses that outweigh those containing it — printed for reference, probably not original. `(…)` before a Hebrew word = ketiv, followed by the qere.

---

## Section I — Admitted Witnesses & Gatekeeper Quarantine Declaration

### Admitted Collation Witnesses (Open-Source Tiers 1–4)
| Siglum | Witness Title | Tier | Weight | License | Text-Type |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **SRGNT** | Statistical Restoration Greek New Testament (CNTR 2022) | Tier 1 | `0.95` | CC BY 4.0 | Earliest-Manuscript Statistical Critical Edition |
| **SBLGNT** | SBL Greek New Testament & Apparatus (Holmes 2010) | Tier 1 | `0.94` | CC BY 4.0 | Reasoned Eclectic Critical Edition |
| **BHP** | Bunning Heuristic Prototype GNT (CNTR) | Tier 1 | `0.88` | CC BY 4.0 | Algorithmic Alexandrian/Early Witness Reconstruction |
| **Nestle1904** | Eberhard Nestle Greek New Testament (1904) | Tier 2 | `0.90` | Public Domain | Tischendorf / Westcott-Hort / Weymouth Consensus |
| **RP2018 (Byz)** | Robinson–Pierpont Byzantine Textform (2018) | Tier 3 | `0.72` | Public Domain / Unlicense | Byzantine / Majority Ecclesiastical Tradition |
| **TR (KJTR)** | Textus Receptus (CNTR KJTR Collation) | Tier 3 | `0.60` | CC BY 4.0 | Reformation Textus Receptus Tradition |
| **B (03)** | Codex Vaticanus Direct Transcription (CNTR Early MSS) | Tier 4 | `0.98` | CC BY-SA 4.0 | Premier Alexandrian Uncial |
| **א (01)** | Codex Sinaiticus Direct Transcription (CNTR Early MSS) | Tier 4 | `0.96` | CC BY-SA 4.0 | Alexandrian / Western Mixed Uncial |

### Apparatus Witnesses (Additional Editions & Direct Manuscripts — recorded, not voting)
Collated against the adopted text and listed in the apparatus wherever they differ in substance; they do not vote on the text.

| Siglum | Witness Title | Tier | License | Text-Type |
| :--- | :--- | :---: | :--- | :--- |
| **NA28 (TAGNT)** | Nestle–Aland 28th Edition Word-Stream (STEPBible TAGNT CC BY 4.0) | Tier 1 | CC BY 4.0 (STEPBible.org / Tyndale House) | Modern Standard Eclectic Critical Edition (NA28) |
| **THGNT** | Tyndale House Greek New Testament (STEPBible TAGNT CC BY 4.0) | Tier 1 | CC BY 4.0 (STEPBible.org / Tyndale House Cambridge) | Documentarily-Grounded Modern Critical Edition (THGNT) |
| **WH1881** | Westcott & Hort Greek New Testament (1881, CNTR Unicode) | Tier 2 | Public Domain / CC BY-SA 4.0 | Neutral / Alexandrian Critical Edition (Westcott–Hort) |
| **Tisch8** | Tischendorf 8th Edition Greek New Testament (1869–1872, OSIS v2.8) | Tier 2 | Public Domain | Sinaiticus-Weighted Critical Edition (Tischendorf 8th) |
| **TCGNT (Byz)** | The Text-Critical Greek New Testament: Byzantine Text (Robert Adam Boyd) | Tier 3 | Public Domain | Byzantine Majority Manuscript Collation (TuT / ECM / Hoskier) |
| **PT1904 (Byz)** | 1904 Ecumenical Patriarchal Greek New Testament (Basileios Antoniades) | Tier 3 | Public Domain | Constantinopolitan Lectionary & Byzantine Ecclesiastical Majority |
| **TR-Scrivener (1894)** | Scrivener Textus Receptus (Cambridge 1894 Polytonic Edition) | Tier 3 | Public Domain / GPL-3.0 | Beza 1598 / KJV-Underlying Textus Receptus |
| **TR-Boyd (Elz/Scr/Steph)** | Polytonic Textus Receptus (Stephanus 1550 / Elzevir 1624 / Scrivener 1894) | Tier 3 | Public Domain | Reformation Printed Textus Receptus |
| **TR-Stephanus (1550)** | Stephanus Editio Regia Textus Receptus (Paris 1550, CNTR Unicode) | Tier 3 | Public Domain / CC BY-SA 4.0 | Reformation Printed Textus Receptus (Stephanus 1550) |
| **TR-Elzevir (1624)** | Elzevir Textus Receptus (1624 Leiden Edition, Robinson .UEL) | Tier 3 | Public Domain | Classic Elzevir Textus Receptus |
| **A (02)** | Codex Alexandrinus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Byzantine (Gospels) / Premier Alexandrian (Acts, Epistles, Revelation) |
| **C (04)** | Codex Ephraemi Rescriptus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Mixed Alexandrian / Early Eclectic Palimpsest |
| **33** | Minuscule 33 — Queen of the Cursives (INTF NTVMR & IGNTP Paul XML) | Tier 4 | CC BY 4.0 | Premier Alexandrian Minuscule (Gospels, Acts, Epistles) |

### Disregarded / Quarantined Sources (Excluded by AI Gatekeeper)
| Source | Status | Reason Excluded from Open Critical Text |
| :--- | :---: | :--- |
| Pickering-f35 | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-ND (Tier 5 — Owner-Authorized Apparatus)) — held in local Studio only; excluded from public open-licence exports. |
| Tregelles (1879) | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-SA 3.0 (Owner-Authorized Apparatus Witness)) — held in local Studio only; excluded from public open-licence exports. |

---

## Section II — Continuous Greek Critical Text

**1** Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης;
**2** ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
**3** ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε· Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε· Σὺ στῆθι ἐκεῖ, ἢ κάθου ὑπὸ τὸ ὑποπόδιόν μου,
**4** οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
**5** ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
**6** ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
**7** οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
**8** Εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
**9** εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
**10** ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
**11** ὁ γὰρ εἰπών· Μὴ μοιχεύσῃς εἶπεν καί· Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύεις φονεύεις δέ, γέγονας παραβάτης νόμου.
**12** οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
**13** ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
**14** Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
**15** ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
**16** εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν· Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
**17** οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθʼ ἑαυτήν.
**18** Ἀλλʼ ἐρεῖ τις· Σὺ πίστιν ἔχεις κἀγὼ ἔργα ἔχω. δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.
**19** σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ θεός; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
**20** θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
**21** Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
**22** βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
**23** καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· Ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος θεοῦ ἐκλήθη.
**24** ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
**25** ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
**26** ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### James 2:1
- **Apparatus:** `τῆς δόξης;` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 33
- *Disregarded Surface Variant:* kept `Ἀδελφοί` over `αδελφοι`, `ἀδελφοί` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου` (B (03), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προσωπολημψίαις` over `προσωπολημψιαισ`, `προσωποληψίαις`, `προσωποληψίαις,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Nasal spelling (λημψ- / ληψ-)*
- *Disregarded Surface Variant:* kept `ἔχετε` over `εχετε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστιν` over `πιστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστοῦ` over `χυ̅`, `χριστοῦ` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόξης;` over `δοξησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `προσωπολημψίαις / προσωποληψίαις`, `προσωπολημψίαις / προσωποληψίαις`, `προσωπολημψίαις / προσωποληψίαις`, `προσωπολημψίαις / προσωποληψίαις`, `προσωπολημψίαις / προσωποληψιαις`, `προσωπολημψίαις / προσωποληψίαις`, `προσωπολημψίαις / προσωποληψίαις` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Nasal spelling (λημψ- / ληψ-)*

### James 2:2
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **τὴν** RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐσθῆτι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αισθητι** א (01) A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐσθῆτι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αισθητι** א (01) A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰσέλθῃ` over `εισελθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συναγωγὴν` over `συναγωγην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνὴρ` over `ανηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χρυσοδακτύλιος` over `χρυσοδακτυλιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαμπρᾷ,` over `λαμπρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰσέλθῃ` over `εισελθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πτωχὸς` over `πτωχοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥυπαρᾷ` over `ρυπαρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:3
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 C (04) NA28 (TAGNT) WH1881 **]** **καὶ** RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐπιβλέψητε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **και** א (01) 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δὲ` B (03) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) WH1881 **]** **om.** RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 ; **επιβλεψηται** א (01) ; **επιβλεψειτε** 33 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **αὐτῷ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐκεῖ` א (01) SRGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **om.** B (03) SBLGNT NA28 (TAGNT) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `ἢ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **και** C (04)
- **Apparatus:** `om.` SRGNT Nestle1904 BHP 33 A (02) C (04) THGNT Tisch8 **]** **ὧδε** א (01) RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ἐκεῖ** B (03) SBLGNT NA28 (TAGNT) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts, modern critical editions.
- **Apparatus:** `ὑποπόδιόν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ποποδιον** א (01) ; **υποποδιον των ποδων** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `μου,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **των ποδων σου** A (02)
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φοροῦντα` over `φορουντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐσθῆτα` over `εσθητα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαμπρὰν` over `λαμπραν`, `λαμπράν,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴπητε·` over `ειπητε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Σὺ` over `συ`, `“σὺ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κάθου` over `καθου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὧδε` over `ωδε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καλῶς,` over `καλωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πτωχῷ` over `πτωχω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴπητε·` over `ειπητε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Σὺ` over `συ`, `“σὺ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στῆθι` over `στηθι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἢ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κάθου` over `καθου`, `“Κάθου` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου`, `μου”,`, `μου·`, `μου:` (B (03), BHP, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Punctuation / spacing difference only*

### James 2:4
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) THGNT Tisch8 WH1881 **]** **καὶ** RP2018 (Byz) TR (KJTR) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `οὐ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** B (03) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `διεκρίθητε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **διεκριθηται** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐγένεσθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εγενεσθαι** א (01) 33 A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτοῖς` over `εαυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κριταὶ` over `κριται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διαλογισμῶν` over `διαλογισμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πονηρῶν;` over `πονηρων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:5
- **Apparatus:** `ἀκούσατε,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ακουσαται** A (02) ; **ακουσατε αγαπητοι μου** 33
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αγαπητοι μου** 33
- **Apparatus:** `μου ἀγαπητοί.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 33
- **Apparatus:** `οὐχ` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) RP2018 (Byz) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ουκ** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τῷ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **τοῦ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `κόσμῳ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **κόσμου** RP2018 (Byz) PT1904 (Byz) TCGNT (Byz) ; **κόσμου τούτου** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εν κληρονομια** 33
- **Apparatus:** `βασιλείας` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επαγγελιασ** א (01) A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἧς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **οις** 33
- *Disregarded Surface Variant:* kept `ἀκούσατε,` over `ακουσατε`, `Ἀκούσατε,` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπητοί.` over `αγαπητοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸς` over `θσ̅`, `Θεὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐξελέξατο` over `εξελεξατο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πτωχοὺς` over `πτωχουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλουσίους` over `πλουσιουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστει` over `πιστει`, `πιστι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κληρονόμους` over `κληρονομουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἧς` over `ησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπηγγείλατο` over `επηγγειλατο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπῶσιν` over `αγαπωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτόν;` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:6
- **Apparatus:** `ἠτιμάσατε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ητημασατε** 33
- **Apparatus:** `οὐχ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ουχι** A (02) C (04)
- **Apparatus:** `καταδυναστεύουσιν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καταδυστευουσιν** C (04)
- **Apparatus:** `ὑμῶν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **υμασ** א (01) A (02) Tisch8 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `κριτήρια;` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κρητηρια** A (02) ; **κρετηρια** C (04)
- *Disregarded Surface Variant:* kept `ὑμεῖς` over `υμεισ`, `Ὑμεῖς` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἠτιμάσατε` over `ητειμασατε`, `ητιμασατε` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πτωχόν.` over `πτωχον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐχ` over `ουχ`, `Οὐχ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλούσιοι` over `πλουσιοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καταδυναστεύουσιν` over `καταδυναστευουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὶ` over `αυτοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἕλκουσιν` over `ελκουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμᾶς` over `υμασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κριτήρια;` over `κριτηρια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:7
- **Apparatus:** `οὐκ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **και** 33 A (02)
- **Apparatus:** `ἐπικληθὲν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επικεκληθεν** C (04)
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ`, `Οὐκ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὶ` over `αυτοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βλασφημοῦσιν` over `βλασφημουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καλὸν` over `καλον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὄνομα` over `ονομα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπικληθὲν` over `επικληθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐφʼ` over `εφ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμᾶς;` over `υμασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:8
- **Apparatus:** `τελεῖτε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **τελιται** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `βασιλικὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** C (04)
- **Apparatus:** `σεαυτόν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **σαυτον** B (03) ; **σεαυτον αγαπησεισ τον πλησιον σου ωσ σεαυτον** A (02) ; **ἑαυτόν,** TCGNT (Byz) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ποιεῖτε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ποιειται** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Εἰ` over `ει`, `εἰ` (B (03), BHP, Nestle1904, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μέντοι` over `μεντοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμον` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βασιλικὸν` over `βασιλικον`, `βασιλικόν,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γραφήν` over `γραφην`, `Γραφήν,` (B (03), BHP, SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἀγαπήσεις` over `αγαπησεισ`, `“ἀγαπήσεις` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλησίον` over `πλησιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καλῶς` over `καλωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:9
- **Apparatus:** `προσωπολημπτεῖτε` B (03) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **προσωποληπτεῖτε** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **προσωπολημπτιται** א (01) ; **προσωπολειπτειτε** 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `ἐργάζεσθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εργαζεσθαι** א (01) 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `εἰ` over `ει`, `Εἰ` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτίαν` over `αμαρτιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλεγχόμενοι` over `ελεγχομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμου` over `νομου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παραβάται.` over `παραβαται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:10
- **Apparatus:** `ὅστις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ωστις** 33 ; **οσ** C (04)
- **Apparatus:** `ὅλον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** C (04)
- **Apparatus:** `τηρήσῃ πταίσῃ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) PT1904 (Byz) THGNT Tisch8 WH1881 **]** **τηρήσει πταίσει** RP2018 (Byz) TR (KJTR) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **πληρωσει πταιση** A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ὅστις` over `οστισ`, `Ὅστις` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅλον` over `ολον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμον` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑνί,` over `ενι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γέγονεν` over `γεγονεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντων` over `παντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔνοχος.` over `ενοχοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:11
- **Apparatus:** `εἰπών·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ειπασ** A (02)
- **Apparatus:** `μοιχεύσῃς` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **μοιχεύσεις** א (01) RP2018 (Byz) 33 ; **φονευσησ** C (04) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `φονεύσῃς` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **φονεύσεις** RP2018 (Byz) ; **μοιχευσησ** C (04) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `οὐ μοιχεύεις φονεύεις δέ, γέγονας` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **εγενου** 33 ; **ου μοιχευεισ φονευεισ δε εγενου** A (02) ; **οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας** PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550)
- **Apparatus:** `μοιχεύεις φονεύεις` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **μοιχεύσεις φονεύσεις** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **om.** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `γέγονας παραβάτης` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εγενου αποστατησ** A (02) ; **παραβατης** 33
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰπών·` over `ειπων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μὴ` over `μη`, `“μὴ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μοιχεύσεις` over `μοιχευσισ` (א (01)) — *Spelling variant pooled before the vote with the reading 'μοιχεύσεις' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `εἶπεν` over `ειπεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καί·` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μὴ` over `μη`, `“μὴ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰ` over `ει`, `Εἰ` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δέ,` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γέγονας` over `γεγονασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παραβάτης` over `παραβατησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμου.` over `νομου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:12
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ`, `Οὕτως` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαλεῖτε` over `λαλειτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ`, `ουτω` (B (03), א (01)) — *Movable final sigma (οὕτω/οὕτως type)*
- *Disregarded Surface Variant:* kept `ποιεῖτε` over `ποιειτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διὰ` over `δια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμου` over `νομου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλευθερίας` over `ελευθεριασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μέλλοντες` over `μελλοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίνεσθαι.` over `κρεινεσθαι`, `κρινεσθαι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / Οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / Οὕτω`, `οὕτως / οὕτω` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Movable final sigma (οὕτω/οὕτως type)*

### James 2:13
- **Apparatus:** `ἀνέλεος` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **ἀνίλεως** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ανηλεος** 33 ; **αναιλεοσ** A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **καὶ** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `κατακαυχᾶται` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κατακαυχατε** B (03) ; **κατακαυχασθω** 33 ; **κατακαυχασθω δε** A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἔλεος` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ἔλεον** RP2018 (Byz) C (04) TCGNT (Byz) ; **δε ελεον** 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἡ` over `η`, `Ἡ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίσις` over `κρισισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιήσαντι` over `ποιησαντι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔλεος·` over `ελεοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίσεως.` over `κρισεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:14
- **Apparatus:** `τὸ` א (01) Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **om.** B (03) SRGNT SBLGNT C (04) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **τισ** A (02) C (04)
- **Apparatus:** `τις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** A (02) C (04)
- **Apparatus:** `ἔχῃ;` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ἔχει;** 33 ; **ερχη** A (02)
- *Disregarded Surface Variant:* kept `Τί` over `τι`, `τί` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὄφελος,` over `οφελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου` (B (03), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστιν` over `πιστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λέγῃ` over `λεγη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τις` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχειν` over `εχειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργα` over `εργα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχῃ;` over `εχη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη`, `Μὴ` (B (03), RP2018 (Byz), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δύναται` over `δυναται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστις` over `πιστισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶσαι` over `σωσαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτόν;` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:15
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **δὲ** RP2018 (Byz) TR (KJTR) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ὑπάρχωσιν καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υπαρχουσιν ει** 33 ; **υπαρχωσιν η** A (02)
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **η** A (02) ; **ει** 33
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) THGNT Tisch8 WH1881 **]** **ὦσιν** RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφὸς` over `αδελφοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἢ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφὴ` over `αδελφη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γυμνοὶ` over `γυμνοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπάρχωσιν` over `υπαρχωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λειπόμενοι` over `λειπομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐφημέρου` over `εφημερου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τροφῆς,` over `τροφησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:16
- **Apparatus:** `εἴπῃ δέ τις` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ειπε δε τι** א (01) ; **ειπη τισ** A (02) *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `Ὑπάγετε` B (03) SRGNT SBLGNT Nestle1904 RP2018 (Byz) TR (KJTR) BHP 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υπαγεται** א (01) ; **υπαγε** C (04) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `θερμαίνεσθε καὶ χορτάζεσθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **θερμαινεσθαι και χορταζεσθαι** א (01) ; **θερμενεσθε και χορταζεσθε** 33 ; **θερμενεσθε και ορταζεσθε** A (02) *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δῶτε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δοτε** 33
- **Apparatus:** `τὸ` א (01) Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **om.** B (03) SRGNT SBLGNT C (04) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- *Disregarded Surface Variant:* kept `αὐτοῖς` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξ` over `εξ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν·` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρήνῃ,` over `ειρηνη`, `ιρηνη` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δῶτε` over `δωτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιτήδεια` over `επιτηδια` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σώματος,` over `σωματοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τί` over `τι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὄφελος;` over `οφελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:17
- **Apparatus:** `ἔχῃ ἔργα` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ἔργα ἔχῃ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **εργα** A (02) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ`, `Οὕτως` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστις,` over `πιστισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νεκρά` over `νεκρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καθʼ` over `καθ`, `καθ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ἑαυτήν.` over `εαυτην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / Οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Movable final sigma (οὕτω/οὕτως type)*

### James 2:18
- **Apparatus:** `πίστιν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πιστισ** A (02)
- **Apparatus:** `δεῖξόν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ειξον** A (02)
- **Apparatus:** `χωρὶς` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) THGNT TR-Scrivener (1894) Tisch8 WH1881 **]** **ἐκ** RP2018 (Byz) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `κἀγώ σοι δείξω` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **σου κἀγὼ δείξω σοι** RP2018 (Byz) TR (KJTR) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **καγω δειξω σοι** 33 A (02) *(partial substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **μου** RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Ἀλλʼ` over `αλλ`, `ἀλλ’`, `ἀλλʼ` (B (03), BHP, Nestle1904, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐρεῖ` over `ερει`, `ερι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τις·` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Σὺ` over `συ`, `“σὺ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστιν` over `πιστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχεις` over `εχεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κἀγὼ` over `καγω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργα` over `εργα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχω.` over `εχω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεῖξόν` over `δειξον`, `διξον`, `Δεῖξόν` (B (03), SRGNT, א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστιν` over `πιστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων,` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστιν.` over `πιστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `Ἀλλʼ / αλλα` (A (02)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### James 2:19
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ὁ θεὸς** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'ὁ θεός' together form one word-order variant (B (03), RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **θσ̅ (= θεὸσ)** B (03) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ὁ θεός` א (01) SRGNT Nestle1904 BHP SBLGNT A (02) NA28 (TAGNT) THGNT Tisch8 **]** **om.** B (03) RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 ; **ο θς̅ εστιν (= ο θεὸσ εστιν)** 33 C (04) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'ὁ θεός' together form one word-order variant (B (03), RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- *Disregarded Surface Variant:* kept `σὺ` over `συ`, `Σὺ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πιστεύεις` over `πιστευεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἷς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν`, `ἐστίν·` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `καλῶς` over `καλωσ`, `Καλῶς` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιεῖς·` over `ποιεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δαιμόνια` over `δαιμονια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πιστεύουσιν` over `πιστευουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φρίσσουσιν.` over `φρισσουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `πιστεύουσιν καὶ / πιστεύουσι—καὶ` (TCGNT (Byz)) — *Apparatus witness, not a variant: Word division differs with movable ν (e.g. ἐπάταξεντὸν / ἐπάταξε τὸν)*

### James 2:20
- **Apparatus:** `γνῶναι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **γνωνε** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `κενέ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καινε** א (01) A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀργή` B (03) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **νεκρά** א (01) RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- *Disregarded Surface Variant:* kept `θέλεις` over `θελεισ`, `Θέλεις` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὦ` over `ω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθρωπε` over `ανθρωπε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστις` over `πιστισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χωρὶς` over `χωρισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν;` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:21
- *Disregarded Surface Variant:* kept `Ἀβραὰμ` over `αβρααμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατὴρ` over `πατηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξ` over `εξ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐδικαιώθη,` over `εδικαιωθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνενέγκας` over `ανενεγκασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰσαὰκ` over `ισαακ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `υἱὸν` over `υιον`, `υν̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θυσιαστήριον;` over `θυσιαστηριον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:22
- **Apparatus:** `συνήργει` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **συνεργει** א (01) 33 A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `βλέπεις` over `βλεπεισ`, `Βλέπεις` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστις` over `πιστισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργοις` over `εργοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστις` over `πιστισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐτελειώθη,` over `ετελειωθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:23
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπληρώθη` over `επληρωθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γραφὴ` over `γραφη`, `Γραφὴ` (B (03), BHP, SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λέγουσα·` over `λεγουσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἐπίστευσεν` over `επιστευσεν`, `“ἐπίστευσεν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἀβραὰμ` over `αβρααμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ,` over `θω̅`, `Θεῷ,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλογίσθη` over `ελογισθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῷ` over `αυτω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δικαιοσύνην,` over `δικαιοσυνην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φίλος` over `φιλοσ`, `Φίλος` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐκλήθη.` over `εκληθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:24
- **Apparatus:** `ὁρᾶτε` א (01) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT Nestle1904 BHP 33 C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **οραται** B (03) A (02) ; **ὁρᾶτε τοίνυν** PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **τοίνυν** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξ` over `εξ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δικαιοῦται` over `δικαιουται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθρωπος` over `ανθρωποσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστεως` over `πιστεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μόνον.` over `μονον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:25
- **Apparatus:** `ὁμοίως δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ουτωσ** C (04)
- **Apparatus:** `ἀγγέλους` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κατασκοπουσ** C (04)
- *Disregarded Surface Variant:* kept `ὁμοίως` over `ομοιωσ`, `Ὁμοίως` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ῥαὰβ` over `ρααβ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόρνη` over `πορνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξ` over `εξ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐδικαιώθη,` over `εδικαιωθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑποδεξαμένη` over `υποδεξαμενη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγγέλους` over `αγγελουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑτέρᾳ` over `ετερα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁδῷ` over `οδω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκβαλοῦσα;` over `εκβαλουσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 2:26
- **Apparatus:** `γὰρ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **om.** B (03) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **του** 33
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **τῶν** RP2018 (Byz) TR (KJTR) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ὥσπερ` over `ωσπερ`, `Ὥσπερ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶμα` over `σωμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χωρὶς` over `χωρισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεύματος` over `πνευματοσ`, `πνσ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `νεκρόν` over `νεκρον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν,` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστις` over `πιστισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χωρὶς` over `χωρισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νεκρά` over `νεκρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν.` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Movable final sigma (οὕτω/οὕτως type)*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης;
  - `SRGNT`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν, Ἰησοῦ Χριστοῦ, τῆς δόξης.
  - `SBLGNT`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης;
  - `BHP`: ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν, Ἰησοῦ Χριστοῦ, τῆς δόξης.
  - `Nestle1904`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `RP2018 (Byz)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ χριστοῦ τῆς δόξης.
  - `TR (KJTR)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις, ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `B (03)`: αδελφοι μου μη εν προσωπολημψιαισ εχετε την πιστιν του κυ̅ ημων ιυ̅ χυ̅ τησ δοξησ
  - `א (01)`: αδελφοι μου μη εν προσωπολημψιαισ εχετε την πιστιν του κυ̅ ημων ιυ̅ χυ̅ τησ δοξησ
  - `NA28 (TAGNT)`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `THGNT`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `WH1881`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης;
  - `Tisch8`: Ἀδελφοί μου, μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `TCGNT (Byz)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `PT1904 (Byz)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `TR-Scrivener (1894)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης.
  - `TR-Stephanus (1550)`: Ἀδελφοί μου, μὴ ἐν προσωποληψίαις ἔχετε τὴν πίστιν τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τῆς δόξης·
  - `TR-Elzevir (1624)`: αδελφοι μου μη εν προσωποληψιαις εχετε την πιστιν του κυριου ημων ιησου χριστου της δοξης
  - `A (02)`: αδελφοι μου μη εν προσωπολημψιαισ εχετε την πιστιν του κυ̅ ημων ιυ̅ χυ̅ τησ δοξησ
  - `C (04)`: αδελφοι μου μη εν προσωπολημψιαισ εχετε την πιστιν του κυ̅ ημων ιυ̅ χυ̅ τησ δοξησ
  - `33`: αδελφοι μου μη εν προσωπολιψιαις […] την πιστιν του κυ̅ ημων ιυ̅ χυ̅
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 15 surface variation(s) (Accentuation / capitalisation / breathing convention; Nasal spelling (λημψ- / ληψ-); Nomen sacrum (contracted sacred name) for the full word; Punctuation / spacing difference only).

### Verse 2 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `SRGNT`: Ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν, ἀνὴρ χρυσοδακτύλιος, ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς, ἐν ῥυπαρᾷ ἐσθῆτι,
  - `SBLGNT`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `BHP`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν, ἀνὴρ χρυσοδακτύλιος, ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς, ἐν ῥυπαρᾷ ἐσθῆτι,
  - `Nestle1904`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `RP2018 (Byz)`: Ἐὰν γὰρ εἰσέλθῃ εἰς τὴν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `TR (KJTR)`: Ἐὰν γὰρ εἰσέλθῃ εἰς τήν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος, ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι·
  - `B (03)`: εαν γαρ εισελθη εισ συναγωγην υμων ανηρ χρυσοδακτυλιοσ εν εσθητι λαμπρα εισελθη δε και πτωχοσ εν ρυπαρα εσθητι
  - `א (01)`: εαν γαρ εισελθη εισ συναγωγην υμων ανηρ χρυσοδακτυλιοσ εν αισθητι λαμπρα εισελθη δε και πτωχοσ εν ρυπαρα αισθητι
  - `NA28 (TAGNT)`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι
  - `THGNT`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι
  - `WH1881`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `Tisch8`: ἐὰν γὰρ εἰσέλθῃ εἰς συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `TCGNT (Byz)`: ἐὰν γὰρ εἰσέλθῃ εἰς τὴν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `PT1904 (Byz)`: ἐὰν γὰρ εἰσέλθῃ εἰς τὴν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `TR-Scrivener (1894)`: ἐὰν γὰρ εἰσέλθῃ εἰς τὴν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐὰν γὰρ εἰσέλθῃ εἰς τὴν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `TR-Stephanus (1550)`: ἐὰν γὰρ εἰσέλθῃ εἰς τὴν συναγωγὴν ὑμῶν ἀνὴρ χρυσοδακτύλιος ἐν ἐσθῆτι λαμπρᾷ, εἰσέλθῃ δὲ καὶ πτωχὸς ἐν ῥυπαρᾷ ἐσθῆτι,
  - `TR-Elzevir (1624)`: εαν γαρ εισελθη εις την συναγωγην υμων ανηρ χρυσοδακτυλιος εν εσθητι λαμπρα εισελθη δε και πτωχος εν ρυπαρα εσθητι
  - `A (02)`: εαν γαρ εισελθη εισ την συναγωγην υμων ανηρ χρυσοδακτυλιοσ εν αισθητι λαμπρα εισελθη δε και πτωχοσ εν ρυπαρα αισθητι
  - `C (04)`: εαν γαρ εισελθη εισ συναγωγην υμων ανηρ χρυσοδακτυλιοσ εν εσθητι λαμπρα εισελθη δε και πτωχοσ εν ρυπαρα εσθητι
  - `33`: εαν γαρ εισελθη εις την συναγωγην υμων ανηρ […] εν εσθητι λαμπρα εισελθη δε και πτωχος εν ρυπαρα εσθητι
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over τὴν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἐσθῆτι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αισθητι (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἐσθῆτι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αισθητι (א (01)). Reference apparatus (SBLGNT): εἰς WH Treg NA28 ] + τὴν RP Reference apparatus (SBLGNT): εἴπητε WH Treg NA28 ] + αὐτῷ RP Reference apparatus (SBLGNT): ἢ κάθου ἐκεῖ WH NA28 ] ἐκεῖ ἢ κάθου Treg NA27; ἐκεῖ ἢ κάθου ὧδε RP Reference apparatus (SBLGNT): φονεύσῃς WH Treg NA28 ] φονεύσεις RP Reference apparatus (SBLGNT): μοιχεύεις φονεύεις WH Treg NA28 ] μοιχεύσεις φονεύσεις RP Reference apparatus (SBLGNT): λειπόμενοι WH Treg NA27 ] + ὦσιν NA28 RP Reference apparatus (SBLGNT): ἔργων WH Treg NA28 ] + σου RP Reference apparatus (SBLGNT): σοι δείξω WH Treg NA28 ] δείξω σοι RP Reference apparatus (SBLGNT): πίστιν WH Treg NA28 ] + μου RP Reference apparatus (SBLGNT): χωρὶς WH NA28 ] + τῶν Treg RP Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 3 (Confidence: `57.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε· Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε· Σὺ στῆθι ἐκεῖ, ἢ κάθου ὑπὸ τὸ ὑποπόδιόν μου,
  - `SRGNT`: ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν, καὶ εἴπητε, “Σὺ κάθου ὧδε καλῶς”, καὶ τῷ πτωχῷ εἴπητε, “Σὺ στῆθι ἐκεῖ”, ἢ, “Κάθου ὑπὸ τὸ ὑποπόδιόν μου”,
  - `SBLGNT`: ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε· Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε· Σὺ στῆθι ἢ κάθου ἐκεῖ ὑπὸ τὸ ὑποπόδιόν μου,
  - `BHP`: ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν, καὶ εἴπητε, “σὺ κάθου ὧδε καλῶς”, καὶ τῷ πτωχῷ εἴπητε, “σὺ στῆθι ἐκεῖ”, ἢ, “κάθου ὑπὸ τὸ ὑποπόδιόν μου”,
  - `Nestle1904`: ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε Σὺ στῆθι ἐκεῖ ἢ κάθου ὑπὸ τὸ ὑποπόδιόν μου,
  - `RP2018 (Byz)`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπράν, καὶ εἴπητε αὐτῷ, Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε, Σὺ στῆθι ἐκεῖ, ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου·
  - `TR (KJTR)`: Καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν, καὶ εἴπητε αὐτῷ, Σὺ κάθου ὧδε καλῶς· καὶ τῷ πτωχῷ εἴπητε, Σὺ στῆθι ἐκεῖ, ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου:
  - `B (03)`: επιβλεψητε δε επι τον φορουντα την εσθητα την λαμπραν και ειπητε συ καθου ωδε καλωσ και τω πτωχω ειπητε συ στηθι η καθου εκει υπο το υποποδιον μου
  - `א (01)`: και επιβλεψηται επι τον φορουντα την εσθητα την λαμπραν και ειπητε συ καθου ωδε καλωσ και τω πτωχω ειπητε συ στηθι εκει η καθου ωδε υπο το ποποδιον μου
  - `NA28 (TAGNT)`: ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε· σὺ στῆθι ἢ κάθου ἐκεῖ ὑπὸ τὸ ὑποπόδιόν μου,
  - `THGNT`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε· σὺ στῆθι ἐκεῖ ἢ κάθου ὑπὸ τὸ ὑποπόδιόν μου,
  - `WH1881`: ἐπιβλέψητε δὲ ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε Σὺ στῆθι ἢ κάθου ἐκεῖ ὑπὸ τὸ ὑποπόδιόν μου,
  - `Tisch8`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε, σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε, σὺ στῆθι ἐκεῖ ἢ κάθου ὑπὸ τὸ ὑποπόδιόν μου,
  - `TCGNT (Byz)`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε αὐτῷ, Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε, Σὺ στῆθι ἐκεῖ ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου,
  - `PT1904 (Byz)`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν καὶ εἴπητε αὐτῷ, σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε, σὺ στῆθι ἐκεῖ ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου,
  - `TR-Scrivener (1894)`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπράν, καὶ εἴπητε αὐτῷ, Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε, Σὺ στῆθι ἐκεῖ, ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου·
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπράν, καὶ εἴπητε αὐτῷ, Σὺ κάθου ὧδε καλῶς, καὶ τῷ πτωχῷ εἴπητε, Σὺ στῆθι ἐκεῖ, ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου·
  - `TR-Stephanus (1550)`: καὶ ἐπιβλέψητε ἐπὶ τὸν φοροῦντα τὴν ἐσθῆτα τὴν λαμπρὰν, καὶ εἴπητε αὐτῷ, Σὺ κάθου ὧδε καλῶς· καὶ τῷ πτωχῷ εἴπητε, Σὺ στῆθι ἐκεῖ, ἢ κάθου ὧδε ὑπὸ τὸ ὑποπόδιόν μου·
  - `TR-Elzevir (1624)`: και επιβλεψητε επι τον φορουντα την εσθητα την λαμπραν και ειπητε αυτω συ καθου ωδε καλως και τω πτωχω ειπητε συ στηθι εκει η καθου ωδε υπο το υποποδιον μου
  - `A (02)`: και επιβλεψητε επι τον φορουντα την εσθητα την λαμπραν και ειπητε συ καθου ωδε καλωσ και τω πτωχω ειπητε συ στηθι εκει η καθου υπο το υποποδιον των ποδων σου
  - `C (04)`: επιβλεψητε δε επι τον φορουντα την εσθητα την λαμπραν και ειπητε συ καθου ωδε καλωσ και τω πτωχω ειπητε συ στηθι εκει και καθου υπο το υποποδιον μου
  - `33`: και επιβλεψειτε […] τον φορουντα την εσθητα την λαμπραν και ειπητε συ καθου ωδε καλως και τω […] ειπητε συ στηθι εκει η καθου επι το υποποδιον των ποδων μου
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over καὶ (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἐπιβλέψητε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over και (א (01)). [Omission in some witnesses] Adopted 'δὲ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)); επιβλεψηται (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over αὐτῷ (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'ἐκεῖ' [א (01), SRGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.01, confidence 96%) over om. (B (03), SBLGNT). [Omission in some witnesses] Adopted 'om.' [SRGNT, Nestle1904, BHP] (weight 2.73, confidence 62%) over ὧδε (א (01), RP2018 (Byz), TR (KJTR)); ἐκεῖ (B (03), SBLGNT). [Lexical, morphological, or word-order variant] Adopted 'ὑποπόδιόν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ποποδιον (א (01)). Also normalised 24 orthographic/surface variation(s).
- *confidence:* Verse confidence 57% = product of 7 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 4 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `SRGNT`: οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `SBLGNT`: οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `BHP`: οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `Nestle1904`: οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `RP2018 (Byz)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `TR (KJTR)`: Καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `B (03)`: διεκριθητε εν εαυτοισ και εγενεσθε κριται διαλογισμων πονηρων
  - `א (01)`: ου διεκριθηται εν εαυτοισ και εγενεσθαι κριται διαλογισμων πονηρων
  - `NA28 (TAGNT)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `THGNT`: οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `WH1881`: οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `Tisch8`: οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `TCGNT (Byz)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `PT1904 (Byz)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `TR-Scrivener (1894)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `TR-Stephanus (1550)`: καὶ οὐ διεκρίθητε ἐν ἑαυτοῖς, καὶ ἐγένεσθε κριταὶ διαλογισμῶν πονηρῶν;
  - `TR-Elzevir (1624)`: και ου διεκριθητε εν εαυτοις και εγενεσθε κριται διαλογισμων πονηρων
  - `A (02)`: ου διεκριθητε εν εαυτοισ και εγενεσθαι κριται διαλογισμων πονηρων
  - `C (04)`: ου διεκριθητε εν εαυτοισ και εγενεσθε κριται διαλογισμων πονηρων
  - `33`: ου […] εν εαυτοις και εγενεσθαι κριται διαλογισμων πονηρων
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over καὶ (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'οὐ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). [Lexical, morphological, or word-order variant] Adopted 'διεκρίθητε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over διεκριθηται (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἐγένεσθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εγενεσθαι (א (01)). Also normalised 6 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 5 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `SRGNT`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί: οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ, πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `SBLGNT`: ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `BHP`: ἀκούσατε, ἀδελφοί μου ἀγαπητοί: οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ, πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `Nestle1904`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `RP2018 (Byz)`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί. Οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `TR (KJTR)`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί, οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου τούτου πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `B (03)`: ακουσατε αδελφοι μου αγαπητοι ουχ ο θσ̅ εξελεξατο τουσ πτωχουσ τω κοσμω πλουσιουσ εν πιστει και κληρονομουσ τησ βασιλειασ ησ επηγγειλατο τοισ αγαπωσιν αυτον
  - `א (01)`: ακουσατε αδελφοι μου αγαπητοι ουκ ο θσ̅ εξελεξατο τουσ πτωχουσ τω κοσμω πλουσιουσ εν πιστι και κληρονομουσ τησ επαγγελιασ ησ επηγγειλατο τοισ αγαπωσιν αυτον
  - `NA28 (TAGNT)`: ἀκούσατε, ἀδελφοί μου ἀγαπητοί, οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `THGNT`: ἀκούσατε, ἀδελφοί μου ἀγαπητοί, οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `WH1881`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `Tisch8`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ θεὸς ἐξελέξατο τοὺς πτωχοὺς τῷ κόσμῳ πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `TCGNT (Byz)`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί· οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `PT1904 (Byz)`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου πλουσίους ἐν πίστει καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `TR-Scrivener (1894)`: ἀκούσατε, ἀδελφοί μου ἀγαπητοί. οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου τούτου, πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀκούσατε, ἀδελφοί μου ἀγαπητοί. Οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου τούτου πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν;
  - `TR-Stephanus (1550)`: Ἀκούσατε ἀδελφοί μου ἀγαπητοὶ, οὐχ ὁ Θεὸς ἐξελέξατο τοὺς πτωχοὺς τοῦ κόσμου τούτου πλουσίους ἐν πίστει, καὶ κληρονόμους τῆς βασιλείας ἧς ἐπηγγείλατο τοῖς ἀγαπῶσιν αὑτόν;
  - `TR-Elzevir (1624)`: ακουσατε αδελφοι μου αγαπητοι ουχ ο θεος εξελεξατο τους πτωχους του κοσμου τουτου πλουσιους εν πιστει και κληρονομους της βασιλειας ης επηγγειλατο τοις αγαπωσιν αυτον
  - `A (02)`: ακουσαται αδελφοι μου αγαπητοι ουχ ο θσ̅ εξελεξατο τουσ πτωχουσ τω κοσμω πλουσιουσ εν πιστει και κληρονομουσ τησ επαγγελειασ ησ επηγγειλατο τοισ αγαπωσιν αυτον
  - `C (04)`: ακουσατε αδελφοι μου αγαπητοι ουχ ο θσ̅ εξελεξατο τουσ πτωχουσ τω κοσμω πλουσιουσ εν πιστει και κληρονομουσ τησ βασιλειασ ησ επηγγειλατο τοισ αγαπωσιν αυτον
  - `33`: ακουσατε αγαπητοι μου αδελφοι ουχ ο θς̅ εξελεξατο τους πτωχους τω κοσμω πλουσιους εν πιστει και εν κληρονομια κληρονομους της βασιλειας οις επηγγειλατο τοις αγαπωσιν αυτον
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'οὐχ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR), RP2018 (Byz)] (weight 5.97, confidence 99%) over ουκ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'τῷ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over τοῦ (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'κόσμῳ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over κόσμου (RP2018 (Byz)); κόσμου τούτου (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'βασιλείας' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over επαγγελιασ (א (01)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `SRGNT`: Ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. Οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `SBLGNT`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `BHP`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `Nestle1904`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `RP2018 (Byz)`: Ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. Οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `TR (KJTR)`: Ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. Οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `B (03)`: υμεισ δε ητειμασατε τον πτωχον ουχ οι πλουσιοι καταδυναστευουσιν υμων και αυτοι ελκουσιν υμασ εισ κριτηρια
  - `א (01)`: υμεισ δε ητιμασατε τον πτωχον ουχ οι πλουσιοι καταδυναστευουσιν υμασ και αυτοι ελκουσιν υμασ εισ κριτηρια
  - `NA28 (TAGNT)`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `THGNT`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `WH1881`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `Tisch8`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμᾶς, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `TCGNT (Byz)`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `PT1904 (Byz)`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `TR-Scrivener (1894)`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `TR-Boyd (Elz/Scr/Steph)`: Ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. Οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `TR-Stephanus (1550)`: ὑμεῖς δὲ ἠτιμάσατε τὸν πτωχόν. οὐχ οἱ πλούσιοι καταδυναστεύουσιν ὑμῶν, καὶ αὐτοὶ ἕλκουσιν ὑμᾶς εἰς κριτήρια;
  - `TR-Elzevir (1624)`: υμεις δε ητιμασατε τον πτωχον ουχ οι πλουσιοι καταδυναστευουσιν υμων και αυτοι ελκουσιν υμας εις κριτηρια
  - `A (02)`: υμεισ δε ητιμασατε τον πτωχον ουχι οι πλουσιοι καταδυναστευουσιν υμασ και αυτοι ελκουσιν υμασ εισ κρητηρια
  - `C (04)`: υμεισ δε ητιμασατε τον πτωχον ουχι οι πλουσιοι καταδυστευουσιν υμων και αυτοι ελκουσιν υμασ εισ κρετηρια
  - `33`: υμεις δε ητημασατε τον πτωχον ουχ οι πλουσιοι καταδυναστευουσιν υμων και αυτοι ελκουσιν υμας εις κριτηρια
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ὑμῶν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over υμασ (א (01)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 7 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `SRGNT`: Οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `SBLGNT`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `BHP`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `Nestle1904`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ’ ὑμᾶς;
  - `RP2018 (Byz)`: Οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ’ ὑμᾶς;
  - `TR (KJTR)`: Οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `B (03)`: ουκ αυτοι βλασφημουσιν το καλον ονομα το επικληθεν εφ υμασ
  - `א (01)`: ουκ αυτοι βλασφημουσιν το καλον ονομα το επικληθεν εφ υμασ
  - `NA28 (TAGNT)`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ᾽ ὑμᾶς;
  - `THGNT`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ᾽ ὑμᾶς;
  - `WH1881`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `Tisch8`: οὐκ αὐτοὶ βλασφημοῦσιν τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ’ ὑμᾶς;
  - `TCGNT (Byz)`: οὐκ αὐτοὶ βλασφημοῦσι τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ᾽ ὑμᾶς;
  - `PT1904 (Byz)`: οὐκ αὐτοὶ βλασφημοῦσι τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ᾽ ὑμᾶς;
  - `TR-Scrivener (1894)`: οὐκ αὐτοὶ βλασφημοῦσι τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ᾽ ὑμᾶς;
  - `TR-Boyd (Elz/Scr/Steph)`: Οὐκ αὐτοὶ βλασφημοῦσι τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφ᾿ ὑμᾶς;
  - `TR-Stephanus (1550)`: οὐκ αὐτοὶ βλασφημοῦσι τὸ καλὸν ὄνομα τὸ ἐπικληθὲν ἐφʼ ὑμᾶς;
  - `TR-Elzevir (1624)`: ουκ αυτοι βλασφημουσιν το καλον ονομα το επικληθεν εφ υμας
  - `A (02)`: και αυτοι βλασφημουσιν το καλον ονομα το επικληθεν εφ υμασ
  - `C (04)`: ουκ αυτοι βλασφημουσιν το καλον ονομα το επικεκληθεν εφ υμασ
  - `33`: και αυτοι βλασφημουσι το καλον ονομα το επικληθεν εφ υμας
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 10 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 8 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `SRGNT`: Εἰ μέντοι νόμον τελεῖτε βασιλικὸν, κατὰ τὴν Γραφήν, “Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν”, καλῶς ποιεῖτε.
  - `SBLGNT`: Εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `BHP`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν, κατὰ τὴν Γραφήν, “ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν”, καλῶς ποιεῖτε.
  - `Nestle1904`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `RP2018 (Byz)`: Εἰ μέντοι νόμον τελεῖτε βασιλικόν, κατὰ τὴν γραφήν, Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `TR (KJTR)`: Εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν, Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε:
  - `B (03)`: ει μεντοι νομον τελειτε βασιλικον κατα την γραφην αγαπησεισ τον πλησιον σου ωσ σαυτον καλωσ ποιειτε
  - `א (01)`: ει μεντοι νομον τελιται βασιλικον κατα την γραφην αγαπησεισ τον πλησιον σου ωσ σεαυτον καλωσ ποιειται
  - `NA28 (TAGNT)`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν· ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `THGNT`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν· ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `WH1881`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `Tisch8`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν, ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `TCGNT (Byz)`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν, Ἀγαπήσεις τὸν πλησίον σου ὡς ἑαυτόν, καλῶς ποιεῖτε·
  - `PT1904 (Byz)`: εἰ μέντοι νόμον τελεῖτε βασιλικὸν κατὰ τὴν γραφήν, ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `TR-Scrivener (1894)`: εἰ μέντοι νόμον τελεῖτε βασιλικόν, κατὰ τὴν γραφήν, Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `TR-Boyd (Elz/Scr/Steph)`: Εἰ μέντοι νόμον τελεῖτε βασιλικόν, κατὰ τὴν γραφήν, Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν, καλῶς ποιεῖτε·
  - `TR-Stephanus (1550)`: Εἰ μέντοι νόμον τελεῖτε βασιλικὸν, κατὰ τὴν γραφὴν, Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτὸν, καλῶς ποιεῖτε·
  - `TR-Elzevir (1624)`: ει μεντοι νομον τελειτε βασιλικον κατα την γραφην αγαπησεις τον πλησιον σου ως σεαυτον καλως ποιειτε
  - `A (02)`: ει μεντοι νομον τελειτε βασιλεικον κατα την γραφην αγαπησεισ τον πλησιον σου ωσ σεαυτον αγαπησεισ τον πλησιον σου ωσ σεαυτον καλωσ ποιειτε
  - `C (04)`: ει μεντοι νομον βασιλικον τελειτε κατα την γραφην αγαπησεισ τον πλησιον σου ωσ σεαυτον καλωσ ποιειτε
  - `33`: […] […] νομον τελειτε βασιλικον κατα την γραφην αγαπησις τον πλησιον σου ως […] καλως ποιειτε
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'τελεῖτε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over τελιται (א (01)). [Lexical, morphological, or word-order variant] Adopted 'σεαυτόν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over σαυτον (B (03)). [Lexical, morphological, or word-order variant] Adopted 'ποιεῖτε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ποιειται (א (01)). Also normalised 12 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 9 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `SRGNT`: Εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `SBLGNT`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `BHP`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `Nestle1904`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `RP2018 (Byz)`: εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `TR (KJTR)`: Εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `B (03)`: ει δε προσωπολημπτειτε αμαρτιαν εργαζεσθε ελεγχομενοι υπο του νομου ωσ παραβαται
  - `א (01)`: ει δε προσωπολημπτιται αμαρτιαν εργαζεσθαι ελεγχομενοι υπο του νομου ωσ παραβαται
  - `NA28 (TAGNT)`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `THGNT`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `WH1881`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `Tisch8`: εἰ δὲ προσωπολημπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `TCGNT (Byz)`: εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `PT1904 (Byz)`: εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `TR-Scrivener (1894)`: εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `TR-Boyd (Elz/Scr/Steph)`: εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται.
  - `TR-Stephanus (1550)`: εἰ δὲ προσωποληπτεῖτε, ἁμαρτίαν ἐργάζεσθε, ἐλεγχόμενοι ὑπὸ τοῦ νόμου ὡς παραβάται·
  - `TR-Elzevir (1624)`: ει δε προσωποληπτειτε αμαρτιαν εργαζεσθε ελεγχομενοι υπο του νομου ως παραβαται
  - `A (02)`: ει δε προσωπολημπτειτε αμαρτιαν εργαζεσθε ελεγχομενοι υπο του νομου ωσ παραβαται
  - `C (04)`: ει δε προσωπολημπτειτε αμαρτιαν εργαζεσθε ελεγχομενοι υπο του νομου ωσ παραβαται
  - `33`: ει δε προσωπολειπτειτε αμαρτιαν εργαζεσθαι […] […] υπο του νομου ως παραβαται
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'προσωπολημπτεῖτε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over προσωποληπτεῖτε (RP2018 (Byz), TR (KJTR)); προσωπολημπτιται (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἐργάζεσθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εργαζεσθαι (א (01)). Also normalised 9 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `SRGNT`: Ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `SBLGNT`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `BHP`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `Nestle1904`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `RP2018 (Byz)`: Ὅστις γὰρ ὅλον τὸν νόμον τηρήσει, πταίσει δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `TR (KJTR)`: Ὅστις γὰρ ὅλον τὸν νόμον τηρήσει, πταίσει δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `B (03)`: οστισ γαρ ολον τον νομον τηρηση πταιση δε εν ενι γεγονεν παντων ενοχοσ
  - `א (01)`: οστισ γαρ ολον τον νομον τηρηση πταιση δε εν ενι γεγονεν παντων ενοχοσ
  - `NA28 (TAGNT)`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `THGNT`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `WH1881`: Ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `Tisch8`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονεν πάντων ἔνοχος.
  - `TCGNT (Byz)`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσει, πταίσει δὲ ἐν ἑνί, γέγονε πάντων ἔνοχος.
  - `PT1904 (Byz)`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσῃ, πταίσῃ δὲ ἐν ἑνί, γέγονε πάντων ἔνοχος.
  - `TR-Scrivener (1894)`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσει, πταίσει δὲ ἐν ἑνί, γέγονε πάντων ἔνοχος.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὅστις γὰρ ὅλον τὸν νόμον τηρήσει, πταίσει δὲ ἐν ἑνί, γέγονε πάντων ἔνοχος.
  - `TR-Stephanus (1550)`: ὅστις γὰρ ὅλον τὸν νόμον τηρήσει, πταίσει δὲ ἐν ἑνὶ, γέγονε πάντων ἔνοχος·
  - `TR-Elzevir (1624)`: οστις γαρ ολον τον νομον τηρησει πταισει δε εν ενι γεγονεν παντων ενοχος
  - `A (02)`: οστισ γαρ ολον τον νομον πληρωσει πταιση δε εν ενι γεγονεν παντων ενοχοσ
  - `C (04)`: οσ γαρ τον νομον ολον τηρηση πταιση δε εν ενι γεγονεν παντων ενοχοσ
  - `33`: ωστις γαρ ολον τον νομον πληρωσας τηρησει […] δε εν ενι γεγονεν παντων ενοχος
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'τηρήσῃ πταίσῃ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over τηρήσει πταίσει (RP2018 (Byz), TR (KJTR)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 11 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὁ γὰρ εἰπών· Μὴ μοιχεύσῃς εἶπεν καί· Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύεις φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `SRGNT`: Ὁ γὰρ εἰπών, “Μὴ μοιχεύσῃς”, εἶπεν καί, “Μὴ φονεύσῃς.” Εἰ δὲ οὐ μοιχεύεις, φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `SBLGNT`: ὁ γὰρ εἰπών· Μὴ μοιχεύσῃς εἶπεν καί· Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύεις φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `BHP`: ὁ γὰρ εἰπών, “μὴ μοιχεύσῃς”, εἶπεν καί, “μὴ φονεύσῃς.” εἰ δὲ οὐ μοιχεύεις, φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `Nestle1904`: ὁ γὰρ εἰπών Μὴ μοιχεύσῃς, εἶπεν καί Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύεις, φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `RP2018 (Byz)`: Ὁ γὰρ εἰπών, Μὴ μοιχεύσεις, εἶπεν καί, Μὴ φονεύσεις· εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας παραβάτης νόμου.
  - `TR (KJTR)`: Ὁ γὰρ εἰπών, Μὴ μοιχεύσῃς, εἶπεν καί, Μὴ φονεύσῃς. Εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας παραβάτης νόμου.
  - `B (03)`: ο γαρ ειπων μη μοιχευσησ ειπεν και μη φονευσησ ει δε ου μοιχευεισ φονευεισ δε γεγονασ παραβατησ νομου
  - `א (01)`: ο γαρ ειπων μη μοιχευσισ ειπεν και μη φονευσησ ει δε ου μοιχευεισ φονευεισ δε γεγονασ παραβατησ νομου
  - `NA28 (TAGNT)`: ὁ γὰρ εἰπών μὴ μοιχεύσῃς, εἶπεν καί μὴ φονεύσῃς. εἰ δὲ οὐ μοιχεύεις φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `THGNT`: ὁ γὰρ εἰπὼν μὴ μοιχεύσῃς, εἶπεν καὶ μὴ φονεύσῃς. εἰ δὲ οὐ μοιχεύεις φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `WH1881`: ὁ γὰρ εἰπών Μὴ μοιχεύσῃς εἶπεν καί Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύεις φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `Tisch8`: ὁ γὰρ εἰπών, μὴ μοιχεύσῃς, εἶπεν καί, μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύεις, φονεύεις δέ, γέγονας παραβάτης νόμου.
  - `TCGNT (Byz)`: ὁ γὰρ εἰπών, Μὴ μοιχεύσῃς, εἶπε καί, Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας παραβάτης νόμου.
  - `PT1904 (Byz)`: ὁ γὰρ εἰπὼν μὴ μοιχεύσῃς, εἶπε καὶ μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας παραβάτης νόμου.
  - `TR-Scrivener (1894)`: ὁ γὰρ εἰπών, Μὴ μοιχεύσῃς, εἶπε καί, Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας παραβάτης νόμου.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὁ γὰρ εἰπών, Μὴ μοιχεύσῃς, εἶπε καί, Μὴ φονεύσῃς· εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δέ, γέγονας παραβάτης νόμου.
  - `TR-Stephanus (1550)`: ὁ γὰρ εἰπὼν, Μὴ μοιχεύσῃς, εἶπε καὶ, Μὴ φονεύσῃς. εἰ δὲ οὐ μοιχεύσεις, φονεύσεις δὲ, γέγονας παραβάτης νόμου.
  - `TR-Elzevir (1624)`: ο γαρ ειπων μη μοιχευσης ειπεν και μη φονευσης ει δε ου μοιχευσεις φονευσεις δε γεγονας παραβατης νομου
  - `A (02)`: ο γαρ ειπασ μη μοιχευσησ ειπεν και μη φονευσησ ει δε ου μοιχευεισ φονευεισ δε εγενου αποστατησ νομου
  - `C (04)`: ο γαρ ειπων μη φονευσησ ειπεν και μη μοιχευσησ ει δε ου μοιχευεισ φονευεισ δε γεγονασ παραβατησ νομου
  - `33`: ο γαρ ειπων μη μοιχευσις ειπεν και μη […] […] […] […] μοιχευσεις μεν φονευσις δε εγενου παραβατης νομου
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'μοιχεύσῃς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 5.25, confidence 99%) over μοιχεύσεις (א (01), RP2018 (Byz)). [Lexical, morphological, or word-order variant] Adopted 'φονεύσῃς' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over φονεύσεις (RP2018 (Byz)). [Variation unit spanning several words] Adopted 'μοιχεύεις φονεύεις' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over μοιχεύσεις φονεύσεις (RP2018 (Byz), TR (KJTR)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 12 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `SRGNT`: Οὕτως λαλεῖτε, καὶ οὕτως ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `SBLGNT`: οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `BHP`: οὕτως λαλεῖτε, καὶ οὕτως ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `Nestle1904`: οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `RP2018 (Byz)`: Οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `TR (KJTR)`: Οὕτως λαλεῖτε, καὶ οὕτως ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `B (03)`: ουτωσ λαλειτε και ουτωσ ποιειτε ωσ δια νομου ελευθεριασ μελλοντεσ κρεινεσθαι
  - `א (01)`: ουτωσ λαλειτε και ουτω ποιειτε ωσ δια νομου ελευθεριασ μελλοντεσ κρινεσθαι
  - `NA28 (TAGNT)`: οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `THGNT`: οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `WH1881`: οὕτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `Tisch8`: οὗτως λαλεῖτε καὶ οὕτως ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `TCGNT (Byz)`: οὕτω λαλεῖτε καὶ οὕτω ποιεῖτε ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `PT1904 (Byz)`: οὕτω λαλεῖτε καὶ οὕτω ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι·
  - `TR-Scrivener (1894)`: οὕτω λαλεῖτε καὶ οὕτω ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὕτω λαλεῖτε καὶ οὕτω ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι.
  - `TR-Stephanus (1550)`: Οὕτω λαλεῖτε καὶ οὕτω ποιεῖτε, ὡς διὰ νόμου ἐλευθερίας μέλλοντες κρίνεσθαι·
  - `TR-Elzevir (1624)`: ουτως λαλειτε και ουτως ποιειτε ως δια νομου ελευθεριας μελλοντες κρινεσθαι
  - `A (02)`: ουτωσ λαλειτε και ουτωσ ποιειτε ωσ δια νομου ελευθεριασ μελλοντεσ κρινεσθαι
  - `C (04)`: ουτωσ λαλειτε και ουτωσ ποιειτε ωσ δια νομου ελευθεριασ μελλοντεσ κρινεσθαι
  - `33`: ουτως λαλειτε και […] ποιειτε ως δια νομου ελευθεριας μελλοντες κρινεσθαι
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 11 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence); Movable final sigma (οὕτω/οὕτως type)).

### Verse 13 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `SRGNT`: Ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος. Κατακαυχᾶται ἔλεος κρίσεως.
  - `SBLGNT`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `BHP`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος. κατακαυχᾶται ἔλεος κρίσεως.
  - `Nestle1904`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `RP2018 (Byz)`: Ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεον κρίσεως.
  - `TR (KJTR)`: Ἡ γὰρ κρίσις ἀνίλεως, τῷ μὴ ποιήσαντι ἔλεος· καὶ κατακαυχᾶται ἔλεος κρίσεως.
  - `B (03)`: η γαρ κρισισ ανελεοσ τω μη ποιησαντι ελεοσ κατακαυχατε ελεοσ κρισεωσ
  - `א (01)`: η γαρ κρισισ ανελεοσ τω μη ποιησαντι ελεοσ κατακαυχαται ελεοσ κρισεωσ
  - `NA28 (TAGNT)`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `THGNT`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `WH1881`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `Tisch8`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `TCGNT (Byz)`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεον κρίσεως.
  - `PT1904 (Byz)`: ἡ γὰρ κρίσις ἀνέλεος τῷ μὴ ποιήσαντι ἔλεος· κατακαυχᾶται ἔλεος κρίσεως.
  - `TR-Scrivener (1894)`: ἡ γὰρ κρίσις ἀνίλεως τῷ μὴ ποιήσαντι ἔλεος· καὶ κατακαυχᾶται ἔλεος κρίσεως.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἡ γὰρ κρίσις ἀνίλεως τῷ μὴ ποιήσαντι ἔλεος· καὶ κατακαυχᾶται ἔλεος κρίσεως.
  - `TR-Stephanus (1550)`: ἡ γὰρ κρίσις ἀνίλεως τῷ μὴ ποιήσαντι ἔλεος· καὶ κατακαυχᾶται ἔλεος κρίσεως.
  - `TR-Elzevir (1624)`: η γαρ κρισις ανιλεως τω μη ποιησαντι ελεος και κατακαυχαται ελεος κρισεως
  - `A (02)`: η γαρ κρισισ αναιλεοσ τω μη ποιησαντι ελεοσ κατακαυχασθω δε ελεοσ κρισεωσ
  - `C (04)`: η γαρ κρισισ ανελεοσ τω μη ποιησαντι ελεοσ κατακαυχαται ελεον κρισεωσ
  - `33`: η γαρ κρισις ανηλεος […] […] […] ελεος κατακαυχασθω δε ελεον κρισεως
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἀνέλεος' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over ἀνίλεως (TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over καὶ (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'κατακαυχᾶται' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over κατακαυχατε (B (03)). [Lexical, morphological, or word-order variant] Adopted 'ἔλεος' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over ἔλεον (RP2018 (Byz)). Also normalised 8 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 14 (Confidence: `68.2%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `SRGNT`: Τί ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις, ἔχειν ἔργα, δὲ μὴ ἔχῃ; Μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `SBLGNT`: Τί ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `BHP`: τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις, ἔχειν ἔργα, δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `Nestle1904`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `RP2018 (Byz)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; Μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `TR (KJTR)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `B (03)`: τι οφελοσ αδελφοι μου εαν πιστιν λεγη τισ εχειν εργα δε μη εχη μη δυναται η πιστισ σωσαι αυτον
  - `א (01)`: τι το οφελοσ αδελφοι μου εαν πιστιν λεγη τισ εχειν εργα δε μη εχη μη δυναται η πιστισ σωσαι αυτον
  - `NA28 (TAGNT)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `THGNT`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τίς ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `WH1881`: Τί ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `Tisch8`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `TCGNT (Byz)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `PT1904 (Byz)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `TR-Scrivener (1894)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `TR-Boyd (Elz/Scr/Steph)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τις ἔχειν, ἔργα δὲ μὴ ἔχῃ; Μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `TR-Stephanus (1550)`: Τί τὸ ὄφελος, ἀδελφοί μου, ἐὰν πίστιν λέγῃ τὶς ἔχειν, ἔργα δὲ μὴ ἔχῃ; μὴ δύναται ἡ πίστις σῶσαι αὐτόν;
  - `TR-Elzevir (1624)`: τι το οφελος αδελφοι μου εαν πιστιν λεγη τις εχειν εργα δε μη εχη μη δυναται η πιστις σωσαι αυτον
  - `A (02)`: τι το οφελοσ αδελφοι μου εαν πιστιν τισ λεγη εχειν εργα δε μη ερχη μη δυναται η πιστισ σωσαι αυτον
  - `C (04)`: τι οφελοσ αδελφοι μου εαν πιστιν τισ λεγη εχειν εργα δε μη εχη μη δυναται η πιστισ σωσαι αυτον
  - `33`: τι το οφελος αδελφοι μου εαν […] […] […] εχειν εργα δε μη εχει μη δυναται η πιστις σωσαι αυτον
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'τὸ' [א (01), Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.06, confidence 68%) over om. (B (03), SRGNT, SBLGNT). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 68% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 15 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `SRGNT`: Ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν, καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `SBLGNT`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `BHP`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν, καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `Nestle1904`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `RP2018 (Byz)`: Ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι ὦσιν τῆς ἐφημέρου τροφῆς,
  - `TR (KJTR)`: Ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν, καὶ λειπόμενοι ὦσιν τῆς ἐφημέρου τροφῆς,
  - `B (03)`: εαν αδελφοσ η αδελφη γυμνοι υπαρχωσιν και λειπομενοι τησ εφημερου τροφησ
  - `א (01)`: εαν αδελφοσ η αδελφη γυμνοι υπαρχωσιν και λειπομενοι τησ εφημερου τροφησ
  - `NA28 (TAGNT)`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι ὦσιν τῆς ἐφημέρου τροφῆς,
  - `THGNT`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `WH1881`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `Tisch8`: ἐὰν ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσιν καὶ λειπόμενοι τῆς ἐφημέρου τροφῆς,
  - `TCGNT (Byz)`: ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσι καὶ λειπόμενοι ὦσι τῆς ἐφημέρου τροφῆς,
  - `PT1904 (Byz)`: ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσι καὶ λειπόμενοι ὦσι τῆς ἐφημέρου τροφῆς,
  - `TR-Scrivener (1894)`: ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσι καὶ λειπόμενοι ὦσι τῆς ἐφημέρου τροφῆς,
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσι καὶ λειπόμενοι ὦσι τῆς ἐφημέρου τροφῆς,
  - `TR-Stephanus (1550)`: ἐὰν δὲ ἀδελφὸς ἢ ἀδελφὴ γυμνοὶ ὑπάρχωσι, καὶ λειπόμενοι ὦσι τῆς ἐφημέρου τροφῆς,
  - `TR-Elzevir (1624)`: εαν δε αδελφος η αδελφη γυμνοι υπαρχωσιν και λειπομενοι ωσιν της εφημερου τροφης
  - `A (02)`: εαν δε αδελφοσ η αδελφη γυμνοι υπαρχωσιν η λειπομενοι ωσιν τησ εφημερου τροφησ
  - `C (04)`: εαν δε αδελφοσ η αδελφη γυμνοι υπαρχωσιν και λειπομενοι τησ εφημερου τροφησ
  - `33`: εαν […] […] […] γυμνοι υπαρχουσιν ει λειπομενοι ωσιν της εφημερου τροφης
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over δὲ (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ὦσιν (RP2018 (Byz), TR (KJTR)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 16 (Confidence: `66.2%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν· Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `SRGNT`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, “Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε”, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί ὄφελος;
  - `SBLGNT`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν· Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί ὄφελος;
  - `BHP`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, “ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε”, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `Nestle1904`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `RP2018 (Byz)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `TR (KJTR)`: Εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε· μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος· τί τὸ ὄφελος;
  - `B (03)`: ειπη δε τισ αυτοισ εξ υμων υπαγετε εν ειρηνη θερμαινεσθε και χορταζεσθε μη δωτε δε αυτοισ τα επιτηδια του σωματοσ τι οφελοσ
  - `א (01)`: ειπε δε τι αυτοισ εξ υμων υπαγεται εν ιρηνη θερμαινεσθαι και χορταζεσθαι μη δωτε δε αυτοισ τα επιτηδια του σωματοσ τι το οφελοσ
  - `NA28 (TAGNT)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν· ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `THGNT`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν· ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `WH1881`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί ὄφελος;
  - `Tisch8`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `TCGNT (Byz)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `PT1904 (Byz)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `TR-Scrivener (1894)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `TR-Boyd (Elz/Scr/Steph)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε, μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `TR-Stephanus (1550)`: εἴπῃ δέ τις αὐτοῖς ἐξ ὑμῶν, Ὑπάγετε ἐν εἰρήνῃ, θερμαίνεσθε καὶ χορτάζεσθε· μὴ δῶτε δὲ αὐτοῖς τὰ ἐπιτήδεια τοῦ σώματος, τί τὸ ὄφελος;
  - `TR-Elzevir (1624)`: ειπη δε τις αυτοις εξ υμων υπαγετε εν ειρηνη θερμαινεσθε και χορταζεσθε μη δωτε δε αυτοις τα επιτηδεια του σωματος τι το οφελος
  - `A (02)`: και ειπη τισ αυτοισ εξ υμων υπαγετε εν ειρηνη θερμενεσθε και ορταζεσθε μη δωτε δε αυτοισ τα επιτηδια του σωματοσ τι το οφελοσ
  - `C (04)`: ειπη δε τισ αυτοισ εξ υμων υπαγε εν ειρηνη θερμαινεσθε και χορταζεσθε μη δωτε δε αυτοισ τα επιτηδεια του σωματοσ τι οφελοσ
  - `33`: και […] […] […] […] υμων υπαγετε εν ειρηνη θερμενεσθε και χορταζεσθε μη δοτε δε […] […] […] του σωματος τι το οφελος
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'εἴπῃ δέ τις' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ειπε δε τι (א (01)). [Lexical, morphological, or word-order variant] Adopted 'Ὑπάγετε' [B (03), SRGNT, SBLGNT, Nestle1904, RP2018 (Byz), TR (KJTR), BHP] (weight 5.97, confidence 99%) over υπαγεται (א (01)). [Variation unit spanning several words] Adopted 'θερμαίνεσθε καὶ χορτάζεσθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over θερμαινεσθαι και χορταζεσθαι (א (01)). [Addition / omission between witnesses] Adopted 'τὸ' [א (01), Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.06, confidence 68%) over om. (B (03), SRGNT, SBLGNT). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 66% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 17 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθʼ ἑαυτήν.
  - `SRGNT`: Οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθʼ ἑαυτήν.
  - `SBLGNT`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθʼ ἑαυτήν.
  - `BHP`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθʼ ἑαυτήν.
  - `Nestle1904`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθ’ ἑαυτήν.
  - `RP2018 (Byz)`: Οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστιν καθ’ ἑαυτήν.
  - `TR (KJTR)`: Οὕτως Καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστιν, καθʼ ἑαυτήν.
  - `B (03)`: ουτωσ και η πιστισ εαν μη εχη εργα νεκρα εστιν καθ εαυτην
  - `א (01)`: ουτωσ και η πιστισ εαν μη εχη εργα νεκρα εστιν καθ εαυτην
  - `NA28 (TAGNT)`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθ᾽ ἑαυτήν.
  - `THGNT`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθ᾽ ἑαυτήν.
  - `WH1881`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθʼ ἑαυτήν.
  - `Tisch8`: οὕτως καὶ ἡ πίστις, ἐὰν μὴ ἔχῃ ἔργα, νεκρά ἐστιν καθ’ ἑαυτήν.
  - `TCGNT (Byz)`: οὕτω καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστι καθ᾽ ἑαυτήν.
  - `PT1904 (Byz)`: οὕτω καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστι καθ᾽ ἑαυτήν.
  - `TR-Scrivener (1894)`: οὕτω καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστι καθ᾽ ἑαυτήν.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὕτω καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστι καθ᾿ ἑαυτήν.
  - `TR-Stephanus (1550)`: οὕτω καὶ ἡ πίστις, ἐὰν μὴ ἔργα ἔχῃ, νεκρά ἐστι καθʼ ἑαυτήν.
  - `TR-Elzevir (1624)`: ουτως και η πιστις εαν μη εργα εχη νεκρα εστιν καθ εαυτην
  - `A (02)`: ουτωσ και η πιστισ εαν μη εργα νεκρα εστιν καθ εαυτην
  - `C (04)`: ουτωσ και η πιστισ εαν μη εχη εργα νεκρα εστιν καθ εαυτην
  - `33`: ουτως και η πιστις εαν μη εχει […] […] […] καθ εαυτην
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ἔχῃ ἔργα' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἔργα ἔχῃ (RP2018 (Byz), TR (KJTR)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 18 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἀλλʼ ἐρεῖ τις· Σὺ πίστιν ἔχεις κἀγὼ ἔργα ἔχω. δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.
  - `SRGNT`: Ἀλλʼ ἐρεῖ τις, “Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω. Δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.”
  - `SBLGNT`: Ἀλλʼ ἐρεῖ τις· Σὺ πίστιν ἔχεις κἀγὼ ἔργα ἔχω. δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.
  - `BHP`: ἀλλʼ ἐρεῖ τις, “σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.”
  - `Nestle1904`: ἀλλ’ ἐρεῖ τις Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.
  - `RP2018 (Byz)`: Ἀλλ’ ἐρεῖ τις, Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου ἐκ τῶν ἔργων σου, κἀγὼ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `TR (KJTR)`: Ἀλλʼ, ἐρεῖ τις, Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω: δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων σου, κἀγώ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `B (03)`: αλλ ερει τισ συ πιστιν εχεισ καγω εργα εχω δειξον μοι την πιστιν σου χωρισ των εργων καγω σοι δειξω εκ των εργων μου την πιστιν
  - `א (01)`: αλλ ερι τισ συ πιστιν εχεισ καγω εργα εχω διξον μοι την πιστιν σου χωρισ των εργων καγω σοι δειξω εκ των εργων μου την πιστιν
  - `NA28 (TAGNT)`: Ἀλλ᾽ ἐρεῖ τις· σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν
  - `THGNT`: Ἀλλ᾽ ἐρεῖ τίς· σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν
  - `WH1881`: ἀλλʼ ἐρεῖ τις Σὺ πίστιν ἔχεις κἀγὼ ἔργα ἔχω. δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.
  - `Tisch8`: ἀλλ’ ἐρεῖ τις, σὺ πίστιν ἔχεις κἀγὼ ἔργα ἔχω. δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων, κἀγώ σοι δείξω ἐκ τῶν ἔργων μου τὴν πίστιν.
  - `TCGNT (Byz)`: Ἀλλ᾽ ἐρεῖ τις, Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω. δεῖξόν μοι τὴν πίστιν σου ἐκ τῶν ἔργων σου, κἀγὼ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `PT1904 (Byz)`: ἀλλ᾽ ἐρεῖ τις· σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου ἐκ τῶν ἔργων σου, κἀγὼ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `TR-Scrivener (1894)`: ἀλλ᾽ ἐρεῖ τις, Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου χωρὶς τῶν ἔργων σου, κἀγὼ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀλλ᾿ ἐρεῖ τις, Σὺ πίστιν ἔχεις, κἀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου ἐκ τῶν ἔργων σου, κἀγὼ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `TR-Stephanus (1550)`: Ἀλλʼ ἐρεῖ τις, Σὺ πίστιν ἔχεις, κᾀγὼ ἔργα ἔχω· δεῖξόν μοι τὴν πίστιν σου ἐκ τῶν ἔργων σου, κᾀγὼ δείξω σοι ἐκ τῶν ἔργων μου τὴν πίστιν μου.
  - `TR-Elzevir (1624)`: αλλ ερει τις συ πιστιν εχεις καγω εργα εχω δειξον μοι την πιστιν σου εκ των εργων σου καγω δειξω σοι εκ των εργων μου την πιστιν μου
  - `A (02)`: αλλα ερει τισ συ πιστισ εχεισ καγω εργα εχω ειξον μοι την πιστιν σου χωρεισ των εργων καγω δειξω σοι εκ των εργων μου την πιστιν μου
  - `C (04)`: αλλ ερει τισ συ πιστιν εχεισ καγω εργα εχω δειξον μοι την πιστιν σου χωρισ των εργων σου καγω δειξω σοι εκ των εργων μου την πιστιν
  - `33`: αλλ ερει τις συ πιστιν εχεις καγω εργα εχω δειξον […] […] […] […] χωρις των εργων καγω δειξω σοι εκ των εργων μου την πιστιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'χωρὶς' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over ἐκ (RP2018 (Byz)). [Variation unit spanning several words] Adopted 'κἀγώ σοι δείξω' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over σου κἀγὼ δείξω σοι (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over μου (RP2018 (Byz), TR (KJTR)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 19 (Confidence: `96.8%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ θεός; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `SRGNT`: Σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ Θεός. Καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `SBLGNT`: σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ θεός; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `BHP`: σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ Θεός. καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `Nestle1904`: σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ Θεός; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `RP2018 (Byz)`: Σὺ πιστεύεις ὅτι ὁ θεὸς εἷς ἐστίν· καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν, καὶ φρίσσουσιν.
  - `TR (KJTR)`: Σὺ πιστεύεις ὅτι ὁ Θεὸς εἷς ἐστιν· καλῶς ποιεῖς: καὶ τὰ δαιμόνια πιστεύουσιν, καὶ φρίσσουσιν.
  - `B (03)`: συ πιστευεισ οτι εισ θσ̅ εστιν καλωσ ποιεισ και τα δαιμονια πιστευουσιν και φρισσουσιν
  - `א (01)`: συ πιστευεισ οτι εισ εστιν ο θσ̅ καλωσ ποιεισ και τα δαιμονια πιστευουσιν και φρισσουσιν
  - `NA28 (TAGNT)`: σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ θεός· καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `THGNT`: σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ θεός· καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `WH1881`: σὺ πιστεύεις ὅτι εἷς θεὸς ἔστιν; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `Tisch8`: σὺ πιστεύεις ὅτι εἷς ἐστιν ὁ θεός; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσιν καὶ φρίσσουσιν.
  - `TCGNT (Byz)`: σὺ πιστεύεις ὅτι ὁ Θεὸς εἷς ἐστι; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσι—καὶ φρίσσουσι.
  - `PT1904 (Byz)`: σὺ πιστεύεις ὅτι ὁ Θεὸς εἷς ἐστι· καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσι καὶ φρίσσουσι.
  - `TR-Scrivener (1894)`: σὺ πιστεύεις ὅτι ὁ Θεὸς εἷς ἐστί· καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσι, καὶ φρίσσουσι.
  - `TR-Boyd (Elz/Scr/Steph)`: Σὺ πιστεύεις ὅτι ὁ Θεὸς εἷς ἐστί· καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσι, καὶ φρίσσουσι.
  - `TR-Stephanus (1550)`: Σὺ πιστεύεις ὅτι ὁ Θεὸς εἷς ἐστι; καλῶς ποιεῖς· καὶ τὰ δαιμόνια πιστεύουσι, καὶ φρίσσουσι.
  - `TR-Elzevir (1624)`: συ πιστευεις οτι ο θεος εις εστιν καλως ποιεις και τα δαιμονια πιστευουσιν και φρισσουσιν
  - `A (02)`: συ πιστευεισ οτι εισ εστιν ο θσ̅ καλωσ ποιεισ και τα δαιμονια πιστευουσιν και φρισσουσιν
  - `C (04)`: συ πιστευεισ οτι εισ ο θσ̅ εστιν καλωσ ποιεισ και τα δαιμονια πιστευουσιν και φρισσουσιν
  - `33`: συ […] […] […] ο θς̅ εστιν καλως ποιεις και τα δαιμονια πιστευουσιν και φρισσουσιν
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ὁ θεὸς (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.07, confidence 99%) over θσ̅ (= θεὸσ) (B (03)). [Variation unit spanning several words] Adopted 'ὁ θεός' [א (01), SRGNT, Nestle1904, BHP, SBLGNT] (weight 4.63, confidence 98%) over om. (B (03), RP2018 (Byz), TR (KJTR)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 20 (Confidence: `96.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `SRGNT`: Θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `SBLGNT`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `BHP`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `Nestle1904`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `RP2018 (Byz)`: Θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `TR (KJTR)`: Θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `B (03)`: θελεισ δε γνωναι ω ανθρωπε κενε οτι η πιστισ χωρισ των εργων αργη εστιν
  - `א (01)`: θελεισ δε γνωνε ω ανθρωπε καινε οτι η πιστισ χωρισ των εργων νεκρα εστιν
  - `NA28 (TAGNT)`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `THGNT`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `WH1881`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `Tisch8`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων ἀργή ἐστιν;
  - `TCGNT (Byz)`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `PT1904 (Byz)`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `TR-Scrivener (1894)`: θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `TR-Boyd (Elz/Scr/Steph)`: Θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενέ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `TR-Stephanus (1550)`: Θέλεις δὲ γνῶναι, ὦ ἄνθρωπε κενὲ, ὅτι ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν;
  - `TR-Elzevir (1624)`: θελεις δε γνωναι ω ανθρωπε κενε οτι η πιστις χωρις των εργων νεκρα εστιν
  - `A (02)`: θελεισ δε γνωναι ω ανε̅ καινε οτι η πιστισ χωρεισ των εργων νεκρα εστιν
  - `C (04)`: θελεισ δε γνωναι ω ανε̅ κενε οτι η πιστισ χωρισ των εργων αργη εστιν
  - `33`: […] […] […] ω ανε̅ κενε οτι η πιστις χωρις των εργων νεκρα εστιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'γνῶναι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over γνωνε (א (01)). [Lexical, morphological, or word-order variant] Adopted 'κενέ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over καινε (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἀργή' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over νεκρά (א (01), RP2018 (Byz), TR (KJTR)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 21 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `SRGNT`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `SBLGNT`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `BHP`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `Nestle1904`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `RP2018 (Byz)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `TR (KJTR)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `B (03)`: αβρααμ ο πατηρ ημων ουκ εξ εργων εδικαιωθη ανενεγκασ ισαακ τον υιον αυτου επι το θυσιαστηριον
  - `א (01)`: αβρααμ ο πατηρ ημων ουκ εξ εργων εδικαιωθη ανενεγκασ ισαακ τον υν̅ αυτου επι το θυσιαστηριον
  - `NA28 (TAGNT)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `THGNT`: ἁβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `WH1881`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `Tisch8`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `TCGNT (Byz)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `PT1904 (Byz)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `TR-Scrivener (1894)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὐτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `TR-Stephanus (1550)`: Ἁβραὰμ ὁ πατὴρ ἡμῶν οὐκ ἐξ ἔργων ἐδικαιώθη, ἀνενέγκας Ἰσαὰκ τὸν υἱὸν αὑτοῦ ἐπὶ τὸ θυσιαστήριον;
  - `TR-Elzevir (1624)`: αβρααμ ο πατηρ ημων ουκ εξ εργων εδικαιωθη ανενεγκας ισαακ τον υιον αυτου επι το θυσιαστηριον
  - `A (02)`: αβρααμ ο πηρ̅ ημων ουκ εξ εργων εδικαιωθη ανενεγκασ ισαακ τον υιον αυτου επι το θυσιαστηριον
  - `C (04)`: αβρααμ ο πηρ̅ ημων ουκ εξ εργων εδικαιωθη ανενεγκασ ισαακ τον υιον αυτου επι το θυσιαστηριον
  - `33`: αβρααμ ο πηρ̅ […] ουκ εξ […] εδικαιωθη ανενεγκας ισαακ τον υιον αυτου επι το θυσιαστηριον
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 16 surface variation(s) (Accentuation / capitalisation / breathing convention; Nomen sacrum (contracted sacred name) for the full word).

### Verse 22 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
  - `SRGNT`: Βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη.
  - `SBLGNT`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
  - `BHP`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη.
  - `Nestle1904`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
  - `RP2018 (Byz)`: Βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `TR (KJTR)`: Βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `B (03)`: βλεπεισ οτι η πιστισ συνηργει τοισ εργοισ αυτου και εκ των εργων η πιστισ ετελειωθη
  - `א (01)`: βλεπεισ οτι η πιστισ συνεργει τοισ εργοισ αυτου και εκ των εργων η πιστισ ετελειωθη
  - `NA28 (TAGNT)`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `THGNT`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `WH1881`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
  - `Tisch8`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
  - `TCGNT (Byz)`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `PT1904 (Byz)`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη,
  - `TR-Scrivener (1894)`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `TR-Boyd (Elz/Scr/Steph)`: Βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `TR-Stephanus (1550)`: βλέπεις ὅτι ἡ πίστις συνήργει τοῖς ἔργοις αὐτοῦ, καὶ ἐκ τῶν ἔργων ἡ πίστις ἐτελειώθη;
  - `TR-Elzevir (1624)`: βλεπεις οτι η πιστις συνηργει τοις εργοις αυτου και εκ των εργων η πιστις ετελειωθη
  - `A (02)`: βλεπεισ οτι η πιστισ συνεργει τοισ εργοισ αυτου και εκ των εργων η πιστισ ετελιωθη
  - `C (04)`: βλεπεισ οτι η πιστισ συνηργει τοισ εργοισ αυτου και εκ των εργων η πιστισ ετελειωθη
  - `33`: […] οτι […] […] συνεργει τοις εργοις αυτου και εκ των εργων η πιστις […]
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'συνήργει' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over συνεργει (א (01)). Also normalised 14 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 23 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· Ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος θεοῦ ἐκλήθη.
  - `SRGNT`: Καὶ ἐπληρώθη ἡ Γραφὴ ἡ λέγουσα, “Ἐπίστευσεν δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην”, καὶ φίλος Θεοῦ ἐκλήθη.
  - `SBLGNT`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· Ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος θεοῦ ἐκλήθη.
  - `BHP`: καὶ ἐπληρώθη ἡ Γραφὴ ἡ λέγουσα, “ἐπίστευσεν δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην”, καὶ φίλος Θεοῦ ἐκλήθη.
  - `Nestle1904`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα Ἐπίστευσεν δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος Θεοῦ ἐκλήθη.
  - `RP2018 (Byz)`: Καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος θεοῦ ἐκλήθη.
  - `TR (KJTR)`: Καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Ἐπίστευσεν δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην: καὶ Φίλος Θεοῦ ἐκλήθη.
  - `B (03)`: και επληρωθη η γραφη η λεγουσα επιστευσεν δε αβρααμ τω θω̅ και ελογισθη αυτω εισ δικαιοσυνην και φιλοσ θυ̅ εκληθη
  - `א (01)`: και επληρωθη η γραφη η λεγουσα επιστευσεν δε αβρααμ τω θω̅ και ελογισθη αυτω εισ δικαιοσυνην και φιλοσ θυ̅ εκληθη
  - `NA28 (TAGNT)`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην καὶ φίλος θεοῦ ἐκλήθη.
  - `THGNT`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· ἐπίστευσεν δὲ ἁβραὰμ τῷ θεῷ καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην καὶ φίλος θεοῦ ἐκλήθη.
  - `WH1881`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα Ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος θεοῦ ἐκλήθη.
  - `Tisch8`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· ἐπίστευσεν δὲ Ἀβραὰμ τῷ θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος θεοῦ ἐκλήθη.
  - `TCGNT (Byz)`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Ἐπίστευσε δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος Θεοῦ ἐκλήθη.
  - `PT1904 (Byz)`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα· ἐπίστευσε δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος Θεοῦ ἐκλήθη.
  - `TR-Scrivener (1894)`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Ἐπίστευσε δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος Θεοῦ ἐκλήθη.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Ἐπίστευσε δὲ Ἀβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος Θεοῦ ἐκλήθη.
  - `TR-Stephanus (1550)`: καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Ἐπίστευσε δὲ Ἁβραὰμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην, καὶ φίλος Θεοῦ ἐκλήθη.
  - `TR-Elzevir (1624)`: και επληρωθη η γραφη η λεγουσα επιστευσεν δε αβρααμ τω θεω και ελογισθη αυτω εις δικαιοσυνην και φιλος θεου εκληθη
  - `A (02)`: και επληρωθη η γραφη η λεγουσα επιστευσεν δε αβρααμ τω θω̅ και ελογισθη αυτω εισ δικαιοσυνην και φιλοσ θυ̅ εκληθη
  - `C (04)`: και επληρωθη η γραφη η λεγουσα επιστευσεν δε αβρααμ τω θω̅ και ελογισθη αυτω εισ δικαιοσυνην και φιλοσ θυ̅ εκληθη
  - `33`: και […] η γραφη η λεγουσα επιστευσεν δε αβρααμ τω θω̅ και ελογισθη αυτω […] δικαιωσυνην […] […] θυ̅ εκληθη
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 20 surface variation(s) (Accentuation / capitalisation / breathing convention; Nomen sacrum (contracted sacred name) for the full word).

### Verse 24 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `SRGNT`: Ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον.
  - `SBLGNT`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `BHP`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον.
  - `Nestle1904`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `RP2018 (Byz)`: Ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον.
  - `TR (KJTR)`: Ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον.
  - `B (03)`: οραται οτι εξ εργων δικαιουται ανθρωποσ και ουκ εκ πιστεωσ μονον
  - `א (01)`: ορατε οτι εξ εργων δικαιουται ανθρωποσ και ουκ εκ πιστεωσ μονον
  - `NA28 (TAGNT)`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `THGNT`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `WH1881`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `Tisch8`: ὁρᾶτε ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `TCGNT (Byz)`: ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `PT1904 (Byz)`: ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον.
  - `TR-Scrivener (1894)`: ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον;
  - `TR-Stephanus (1550)`: Ὁρᾶτε τοίνυν ὅτι ἐξ ἔργων δικαιοῦται ἄνθρωπος, καὶ οὐκ ἐκ πίστεως μόνον;
  - `TR-Elzevir (1624)`: ορατε τοινυν οτι εξ εργων δικαιουται ανθρωπος και ουκ εκ πιστεως μονον
  - `A (02)`: οραται οτι εξ εργων δικαιουται ανοσ̅ και ουκ εκ πιστεωσ μονον
  - `C (04)`: ορατε οτι εξ εργων δικαιουται ανοσ̅ και ουκ εκ πιστεωσ μονον
  - `33`: ορατε οτι εξ εργων δικαιουται ανος̅ και […] […] […] […]
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ὁρᾶτε' [א (01), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, Nestle1904, BHP] (weight 5.95, confidence 99%) over οραται (B (03)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over τοίνυν (RP2018 (Byz), TR (KJTR)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 25 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `SRGNT`: Ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `SBLGNT`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `BHP`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `Nestle1904`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `RP2018 (Byz)`: Ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους, καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `TR (KJTR)`: Ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους, καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `B (03)`: ομοιωσ δε και ρααβ η πορνη ουκ εξ εργων εδικαιωθη υποδεξαμενη τουσ αγγελουσ και ετερα οδω εκβαλουσα
  - `א (01)`: ομοιωσ δε και ρααβ η πορνη ουκ εξ εργων εδικαιωθη υποδεξαμενη τουσ αγγελουσ και ετερα οδω εκβαλουσα
  - `NA28 (TAGNT)`: Ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `THGNT`: Ὁμοίως δὲ καὶ ̔ραὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `WH1881`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `Tisch8`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `TCGNT (Byz)`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `PT1904 (Byz)`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `TR-Scrivener (1894)`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους, καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `TR-Boyd (Elz/Scr/Steph)`: Ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους, καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα;
  - `TR-Stephanus (1550)`: ὁμοίως δὲ καὶ Ῥαὰβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη, ὑποδεξαμένη τοὺς ἀγγέλους, καὶ ἑτέρᾳ ὁδῷ ἐκβαλοῦσα.
  - `TR-Elzevir (1624)`: ομοιως δε και ρααβ η πορνη ουκ εξ εργων εδικαιωθη υποδεξαμενη τους αγγελους και ετερα οδω εκβαλουσα
  - `A (02)`: ομοιωσ δε και ρααβ η πορνη ουκ εξ εργων εδικαιωθη υποδεξαμενη τουσ αγγελουσ και ετερα οδω εκβαλουσα
  - `C (04)`: ουτωσ και ρααβ η πορνη ουκ εξ εργων εδικαιωθη υποδεξαμενη τουσ κατασκοπουσ και ετερα οδω εκβαλουσα
  - `33`: […] […] και ρααβ η πορνη ουκ εξ εργων εδικαιωθη υποδεξαμενη τους […] και […] […] εκβαλουσα
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 17 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 26 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `SRGNT`: Ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `SBLGNT`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `BHP`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `Nestle1904`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `RP2018 (Byz)`: Ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν.
  - `TR (KJTR)`: Ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστιν.
  - `B (03)`: ωσπερ το σωμα χωρισ πνευματοσ νεκρον εστιν ουτωσ και η πιστισ χωρισ εργων νεκρα εστιν
  - `א (01)`: ωσπερ γαρ το σωμα χωρισ πνσ̅ νεκρον εστιν ουτωσ και η πιστισ χωρισ εργων νεκρα εστιν
  - `NA28 (TAGNT)`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `THGNT`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `WH1881`: ὥσπερ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `Tisch8`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτως καὶ ἡ πίστις χωρὶς ἔργων νεκρά ἐστιν.
  - `TCGNT (Byz)`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτω καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστι.
  - `PT1904 (Byz)`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτω καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστι.
  - `TR-Scrivener (1894)`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτω καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστι.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτω καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστι.
  - `TR-Stephanus (1550)`: ὥσπερ γὰρ τὸ σῶμα χωρὶς πνεύματος νεκρόν ἐστιν, οὕτω καὶ ἡ πίστις χωρὶς τῶν ἔργων νεκρά ἐστι.
  - `TR-Elzevir (1624)`: ωσπερ γαρ το σωμα χωρις πνευματος νεκρον εστιν ουτως και η πιστις χωρις των εργων νεκρα εστιν
  - `A (02)`: ωσπερ γαρ το σωμα χωρεισ πνσ̅ νεκρον εστιν ουτωσ και η πιστισ χωρεισ των εργων νεκρα εστιν
  - `C (04)`: ωσπερ γαρ το σωμα χωρισ πνσ̅ νεκρον εστιν ουτωσ και η πιστισ χωρισ των εργων νεκρα εστιν
  - `33`: ωσπερ γαρ το σωμα χωρις του πνς̅ νεκρον […] […] […] […] […] […] εργων νεκρα εστιν
- **Philological Rationale:** [Omission in some witnesses] Adopted 'γὰρ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over τῶν (RP2018 (Byz), TR (KJTR)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).
