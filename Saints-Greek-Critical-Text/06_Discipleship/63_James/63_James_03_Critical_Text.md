# James 03 — Saints Greek Critical Text

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

**1** Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα·
**2** πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
**3** εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
**4** ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται·
**5** οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. Ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
**6** καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
**7** πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
**8** τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
**9** ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθʼ ὁμοίωσιν θεοῦ γεγονότας·
**10** ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
**11** μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
**12** μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
**13** Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
**14** εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
**15** οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης·
**16** ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
**17** ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος·
**18** καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### James 3:1
- *Disregarded Surface Variant:* kept `Μὴ` over `μη`, `μὴ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πολλοὶ` over `πολλοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διδάσκαλοι` over `διδασκαλοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γίνεσθε,` over `γεινεσθε`, `γινεσθε` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου` (B (03), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `εἰδότες` over `ειδοτεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεῖζον` over `μειζον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίμα` over `κριμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λημψόμεθα·` over `λημψομεθα`, `ληψόμεθα.` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Nasal spelling (λημψ- / ληψ-)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `λημψόμεθα· / ληψόμεθα·`, `λημψόμεθα· / ληψόμεθα.`, `λημψόμεθα· / ληψόμεθα.`, `λημψόμεθα· / ληψόμεθα.`, `λημψόμεθα· / ληψομεθα`, `λημψόμεθα· / ληψόμεθα.`, `λημψόμεθα· / ληψόμεθα·` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Nasal spelling (λημψ- / ληψ-)*

### James 3:2
- **Apparatus:** `πταίομεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πταιωμεν** 33
- **Apparatus:** `εἴ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 WH1881 **]** **η** 33 ; **εἴτις** TR-Stephanus (1550)
- **Apparatus:** `δυνατὸς` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δυναμενοσ** א (01) C (04) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `πολλὰ` over `πολλα`, `Πολλὰ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πταίομεν` over `πταιομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἅπαντες.` over `απαντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴ` over `ει`, `Εἴ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τις` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγῳ` over `λογω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πταίει,` over `πταιει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὗτος` over `ουτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τέλειος` over `τελειοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνήρ,` over `ανηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαλιναγωγῆσαι` over `χαλιναγωγησαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅλον` over `ολον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶμα.` over `σωμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `εἴ τις / εἴτις` (TR-Stephanus (1550)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### James 3:3
- **Apparatus:** `εἰ δὲ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **Ἴδε** RP2018 (Byz) TR (KJTR) C (04) PT1904 (Byz) TCGNT (Byz) ; **Ἰδού,** TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **γαρ** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τὰ στόματα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **το στομα** A (02)
- **Apparatus:** `εἰς` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **πρὸς** RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ημιν** 33 A (02) C (04)
- **Apparatus:** `ἡμῖν,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 33 A (02) C (04)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **μεταγομεν** A (02)
- **Apparatus:** `μετάγομεν.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** A (02)
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἵππων` over `ιππων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαλινοὺς` over `χαλινουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στόματα` over `στοματα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βάλλομεν` over `βαλλομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πείθεσθαι` over `πειθεσθαι`, `πιθεσθαι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτοὺς` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν,` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅλον` over `ολον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶμα` over `σωμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῶν` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετάγομεν.` over `μεταγομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:4
- **Apparatus:** `om.` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **τα** B (03) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀνέμων σκληρῶν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **σκληρῶν ἀνέμων** RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ἂν** RP2018 (Byz) TR (KJTR) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `βούλεται` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **βούληται** RP2018 (Byz) TR (KJTR) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **βουληθη** 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἰδοὺ` over `ιδου`, `Ἰδοὺ,`, `Ἰδού,`, `Ἰδοὺ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλοῖα,` over `πλοια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τηλικαῦτα` over `τηλικαυτα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὄντα` over `οντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλαυνόμενα,` over `ελαυνομενα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετάγεται` over `μεταγεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλαχίστου` over `ελαχιστου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πηδαλίου` over `πηδαλιου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅπου` over `οπου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁρμὴ` over `ορμη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐθύνοντος` over `ευθυνοντοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:5
- **Apparatus:** `οὕτως` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ωσαυτωσ** A (02)
- **Apparatus:** `μεγάλα αὐχεῖ` B (03) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **μεγαλαυχεῖ** א (01) RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `ἡλίκον` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ὀλίγον** RP2018 (Byz) TR (KJTR) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ολυγον** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἡλίκην` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υλικην** 33
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ`, `Οὕτως` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλῶσσα` over `γλωσσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μικρὸν` over `μεικρον`, `μικρον` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `μέλος` over `μελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστὶν` over `εστιν`, `ἐστίν,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰδοὺ` over `ιδου`, `ἰδοὺ`, `ἰδοὺ,`, `Ἰδού,` (B (03), BHP, Nestle1904, RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πῦρ` over `πυρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡλίκην` over `ηλικην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὕλην` over `υλην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνάπτει·` over `αναπτει`, `αναπτι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / Οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Movable final sigma (οὕτω/οὕτως type)*

### James 3:6
- **Apparatus:** `καὶ` B (03) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **om.** א (01) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **οὕτως** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `καθίσταται` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καθισται** B (03) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἡ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **και** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ημων** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλῶσσα` over `γλωσσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πῦρ,` over `πυρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κόσμος` over `κοσμοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδικίας` over `αδικιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλῶσσα` over `γλωσσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μέλεσιν` over `μελεσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῶν,` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σπιλοῦσα` over `σπιλουσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅλον` over `ολον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶμα` over `σωμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φλογίζουσα` over `φλογιζουσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τροχὸν` over `τροχον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γενέσεως` over `γενεσεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φλογιζομένη` over `φλογιζομενη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γεέννης.` over `γεεννησ`, `Γεέννης.` (B (03), BHP, SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:7
- **Apparatus:** `τε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** A (02)
- **Apparatus:** `δαμάζεται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δαμαζετε** A (02)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δεδαμασται και** C (04)
- **Apparatus:** `καὶ δεδάμασται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** C (04)
- **Apparatus:** `ἀνθρωπίνῃ·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ανθρωπινων** A (02)
- *Disregarded Surface Variant:* kept `πᾶσα` over `πασα`, `Πᾶσα` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φύσις` over `φυσισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θηρίων` over `θηριων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πετεινῶν` over `πετεινων`, `πετινων` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἑρπετῶν` over `ερπετων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τε` over `τε,` (TR (KJTR)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐναλίων` over `εναλιων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δαμάζεται` over `δαμαζεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεδάμασται` over `δεδαμασται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φύσει` over `φυσει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνθρωπίνῃ·` over `ανθρωπεινη`, `ανθρωπινη` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### James 3:8
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δαμασαι** 33
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δυναται** א (01) A (02) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'δύναται' together form one word-order variant (א (01) transpose).
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δαμάσαι` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT WH1881 **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `δύναται` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** א (01) A (02) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'δύναται' together form one word-order variant (א (01) transpose).
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀκατάστατον` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **δαμάσαι ἀκατάσχετον** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ακατασχετον** C (04) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `τὴν` over `την`, `Τὴν` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλῶσσαν` over `γλωσσαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐδεὶς` over `ουδεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνθρώπων·` over `ανθρωπων`, `ανων̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `κακόν,` over `κακον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεστὴ` over `μεστη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἰοῦ` over `ιου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θανατηφόρου.` over `θανατηφορου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:9
- **Apparatus:** `κύριον` B (03) א (01) SRGNT Nestle1904 BHP SBLGNT 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **θεὸν** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `γεγονότας·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **γεγενημενους** 33 A (02)
- *Disregarded Surface Variant:* kept `ἐν` over `εν`, `Ἐν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῇ` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐλογοῦμεν` over `ευλογουμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατέρα,` over `πατερα`, `Πατέρα,`, `Πατέρα·` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῇ` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καταρώμεθα` over `καταρωμεθα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνθρώπους` over `ανθρωπουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καθʼ` over `καθ`, `καθ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ὁμοίωσιν` over `ομοιωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `γεγονότας·` over `γεγονοτασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:10
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ`, `Ἐκ` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στόματος` over `στοματοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξέρχεται` over `εξερχεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐλογία` over `ευλογια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατάρα.` over `καταρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου`, `Οὐ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χρή,` over `χρη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου` (B (03), BHP, SRGNT, א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ταῦτα` over `ταυτα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γίνεσθαι.` over `γεινεσθαι`, `γινεσθαι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Movable final sigma (οὕτω/οὕτως type)*

### James 3:11
- **Apparatus:** `πηγὴ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πη** A (02)
- *Disregarded Surface Variant:* kept `μήτι` over `μητι`, `Μήτι` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πηγὴ` over `πηγη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῆς` over `αυτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀπῆς` over `οπησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βρύει` over `βρυει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλυκὺ` over `γλυκυ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πικρόν;` over `πικρον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:12
- **Apparatus:** `ἐλαίας` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ελεασ** א (01) ; **om.** 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `οὔτε` B (03) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **Οὕτως οὐδεμία πηγὴ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ουτωσ ουδε** א (01) ; **om.** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **καὶ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `μὴ` over `μη`, `Μὴ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δύναται,` over `δυναται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου` (B (03), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `συκῆ` over `συκη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιῆσαι` over `ποιησαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἢ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄμπελος` over `αμπελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῦκα;` over `συκα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁλυκὸν` over `αλυκον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλυκὺ` over `γλυκυ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιῆσαι` over `ποιησαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὕδωρ.` over `υδωρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:13
- **Apparatus:** `ἐπιστήμων` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επιστιμων** 33
- **Apparatus:** `δειξάτω` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δειξατο** 33
- *Disregarded Surface Variant:* kept `Τίς` over `τισ`, `τίς` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σοφὸς` over `σοφοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιστήμων` over `επιστημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν;` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δειξάτω` over `δειξατω`, `Δειξάτω` (B (03), RP2018 (Byz), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καλῆς` over `καλησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀναστροφῆς` over `αναστροφησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργα` over `εργα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πραΰτητι` over `πραυτητι`, `πρᾳΰτητι` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Spelling variant pooled before the vote with the reading 'πραΰτητι' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `σοφίας.` over `σοφιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:14
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αρα** 33 A (02)
- **Apparatus:** `ἐριθείαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ερεθιαν** 33
- **Apparatus:** `τῇ καρδίᾳ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ταισ καρδιαισ** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **κατακαυχασθαι τησ αληθιασ και ψευδεσθαι** א (01) ; **καυχασθε και ψευδεσθε κατα τησ αληθειασ** A (02) ; **κατακαυχᾶσθε τῆς ἀληθείας καὶ ψεύδεσθε.** Tisch8 *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `εἰ` over `ει`, `Εἰ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζῆλον` over `ζηλον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πικρὸν` over `πικρον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχετε` over `εχετε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐριθείαν` over `ερειθιαν`, `εριθιαν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν,` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:15
- **Apparatus:** `αὕτη` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** C (04)
- **Apparatus:** `ἄνωθεν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ανοθεν** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ`, `Οὐκ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὕτη` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σοφία` over `σοφια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατερχομένη,` over `κατερχομενη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλὰ` over `αλλα`, `ἀλλ’`, `ἀλλʼ` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Elision (κατὰ / κατ’ type)*
- *Disregarded Surface Variant:* kept `ἐπίγειος,` over `επιγειοσ`, `επιγιοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ψυχική,` over `ψυχικη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δαιμονιώδης·` over `δαιμονιωδησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἀλλὰ / αλλ`, `ἀλλὰ / αλλ`, `ἀλλὰ / αλλ`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / αλλ`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλʼ` (33, A (02), C (04), NA28 (TAGNT), PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### James 3:16
- **Apparatus:** `ἐριθεία,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ερεισ** C (04)
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **και** א (01) 33 A (02) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὅπου` over `οπου`, `Ὅπου` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζῆλος` over `ζηλοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐριθεία,` over `ερειθεια`, `εριθια` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐκεῖ` over `εκει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκαταστασία` over `ακαταστασια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶν` over `παν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φαῦλον` over `φαυλον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρᾶγμα.` over `πραγμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:17
- **Apparatus:** `ἔπειτα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επητα** 33
- **Apparatus:** `εὐπειθής,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ευπηθεις** 33 ; **ευπηθησ** C (04)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εργων** C (04)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **καὶ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἡ` over `η`, `Ἡ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνωθεν` over `ανωθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σοφία` over `σοφια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρῶτον` over `πρωτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὲν` over `μεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁγνή` over `αγνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν,` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔπειτα` over `επειτα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρηνική,` over `ειρηνικη`, `ιρηνικη` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐπιεικής,` over `επιεικησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐπειθής,` over `ευπειθησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεστὴ` over `μεστη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλέους` over `ελεουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καρπῶν` over `καρπων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαθῶν,` over `αγαθων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδιάκριτος,` over `αδιακριτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνυπόκριτος·` over `ανυποκριτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 3:18
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **τῆς** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ο** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `σπείρεται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **σπειρετε** A (02) ; **σπειραιται** C (04)
- *Disregarded Surface Variant:* kept `καρπὸς` over `καρποσ`, `Καρπὸς` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δικαιοσύνης` over `δικαιοσυνησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρήνῃ` over `ειρηνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σπείρεται` over `σπειρεται`, `σπιρεται` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιοῦσιν` over `ποιουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρήνην.` over `ειρηνην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα·
  - `SRGNT`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα.
  - `SBLGNT`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα·
  - `BHP`: μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα.
  - `Nestle1904`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα.
  - `RP2018 (Byz)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα ληψόμεθα.
  - `TR (KJTR)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα ληψόμεθα.
  - `B (03)`: μη πολλοι διδασκαλοι γεινεσθε αδελφοι μου ειδοτεσ οτι μειζον κριμα λημψομεθα
  - `א (01)`: μη πολλοι διδασκαλοι γινεσθε αδελφοι μου ειδοτεσ οτι μειζον κριμα λημψομεθα
  - `NA28 (TAGNT)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα.
  - `THGNT`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα.
  - `WH1881`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα·
  - `Tisch8`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα λημψόμεθα.
  - `TCGNT (Byz)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα ληψόμεθα.
  - `PT1904 (Byz)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρῖμα ληψόμεθα·
  - `TR-Scrivener (1894)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα ληψόμεθα.
  - `TR-Boyd (Elz/Scr/Steph)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρίμα ληψόμεθα.
  - `TR-Stephanus (1550)`: Μὴ πολλοὶ διδάσκαλοι γίνεσθε, ἀδελφοί μου, εἰδότες ὅτι μεῖζον κρῖμα ληψόμεθα·
  - `TR-Elzevir (1624)`: μη πολλοι διδασκαλοι γινεσθε αδελφοι μου ειδοτες οτι μειζον κριμα ληψομεθα
  - `A (02)`: μη πολλοι διδασκαλοι γινεσθε αδελφοι μου ειδοτεσ οτι μειζον κριμα λημψομεθα
  - `C (04)`: μη πολλοι διδασκαλοι γινεσθε αδελφοι μου ειδοτεσ οτι μειζον κριμα λημψομεθα
  - `33`: μη πολλοι διδασκαλοι γινεσθαι […] […] […] οτι […] […] […]
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 11 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence); Nasal spelling (λημψ- / ληψ-); Punctuation / spacing difference only).

### Verse 2 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `SRGNT`: Πολλὰ γὰρ πταίομεν ἅπαντες. Εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `SBLGNT`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `BHP`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `Nestle1904`: πολλὰ γὰρ πταίομεν ἅπαντες· εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `RP2018 (Byz)`: Πολλὰ γὰρ πταίομεν ἅπαντες. Εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `TR (KJTR)`: Πολλὰ γὰρ πταίομεν ἅπαντες. Εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `B (03)`: πολλα γαρ πταιομεν απαντεσ ει τισ εν λογω ου πταιει ουτοσ τελειοσ ανηρ δυνατοσ χαλιναγωγησαι και ολον το σωμα
  - `א (01)`: πολλα γαρ πταιομεν απαντεσ ει τισ εν λογω ου πταιει ουτοσ τελειοσ ανηρ δυναμενοσ χαλιναγωγησαι και ολον το σωμα
  - `NA28 (TAGNT)`: πολλὰ γὰρ πταίομεν ἅπαντες· εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνὴρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `THGNT`: πολλὰ γὰρ πταίομεν ἅπαντες· εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `WH1881`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `Tisch8`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `TCGNT (Byz)`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `PT1904 (Byz)`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `TR-Scrivener (1894)`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `TR-Boyd (Elz/Scr/Steph)`: Πολλὰ γὰρ πταίομεν ἅπαντες. Εἴ τις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνήρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `TR-Stephanus (1550)`: πολλὰ γὰρ πταίομεν ἅπαντες. εἴτις ἐν λόγῳ οὐ πταίει, οὗτος τέλειος ἀνὴρ, δυνατὸς χαλιναγωγῆσαι καὶ ὅλον τὸ σῶμα.
  - `TR-Elzevir (1624)`: πολλα γαρ πταιομεν απαντες ει τις εν λογω ου πταιει ουτος τελειος ανηρ δυνατος χαλιναγωγησαι και ολον το σωμα
  - `A (02)`: πολλα γαρ πταιομεν απαντεσ ει τισ εν λογω ου πταιει ουτοσ τελειοσ ανηρ δυνατοσ χαλιναγωγησαι και ολον το σωμα
  - `C (04)`: πολλα γαρ πταιομεν απαντεσ ει τισ εν λογω ου πταιει ουτοσ τελειοσ ανηρ δυναμενοσ χαλιναγωγησαι και ολον το σωμα
  - `33`: πολλα γαρ πταιωμεν απαντες η τις εν λογω […] […] […] […] […] […] χαλιναγωγησαι και ολον το σωμα
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'δυνατὸς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over δυναμενοσ (א (01)). Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 3 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `SRGNT`: Εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν, εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `SBLGNT`: εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `BHP`: εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν, εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `Nestle1904`: εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `RP2018 (Byz)`: Ἴδε, τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `TR (KJTR)`: Ἰδε, τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν, πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν· καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `B (03)`: ει δε των ιππων τουσ χαλινουσ εισ τα στοματα βαλλομεν εισ το πειθεσθαι αυτουσ ημιν και ολον το σωμα αυτων μεταγομεν
  - `א (01)`: ει δε γαρ των ιππων τουσ χαλινουσ εισ τα στοματα βαλλομεν εισ το πιθεσθαι αυτουσ ημιν και ολον το σωμα αυτων μεταγομεν
  - `NA28 (TAGNT)`: Εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `THGNT`: Εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `WH1881`: εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `Tisch8`: εἰ δὲ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `TCGNT (Byz)`: ἴδε, τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `PT1904 (Byz)`: ἴδε τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `TR-Scrivener (1894)`: ἰδού, τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἰδού, τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν.
  - `TR-Stephanus (1550)`: Ἰδοὺ τῶν ἵππων τοὺς χαλινοὺς εἰς τὰ στόματα βάλλομεν πρὸς τὸ πείθεσθαι αὐτοὺς ἡμῖν, καὶ ὅλον τὸ σῶμα αὐτῶν μετάγομεν·
  - `TR-Elzevir (1624)`: ιδου των ιππων τους χαλινους εις τα στοματα βαλλομεν προς το πειθεσθαι αυτους ημιν και ολον το σωμα αυτων μεταγομεν
  - `A (02)`: ει δε των ιππων τουσ χαλινουσ εισ το στομα βαλλομεν προσ το πειθεσθαι ημιν αυτουσ και ολον το σωμα μεταγομεν αυτων
  - `C (04)`: ιδε των ιππων τουσ χαλινουσ εισ τα στοματα βαλλομεν εισ το πειθεσθαι ημιν αυτουσ και ολον το σωμα αυτων μεταγομεν
  - `33`: ει δε των […] […] […] […] […] […] […] […] […] πειθεσθαι ημιν αυτους και ολον το σωμα […] […]
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'εἰ δὲ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over Ἴδε (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over γαρ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'εἰς' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over πρὸς (RP2018 (Byz), TR (KJTR)). Reference apparatus (SBLGNT): εἰ δὲ WH Treg NA28 ] Ἴδε RP Reference apparatus (SBLGNT): εἰς WH Treg NA28 ] πρὸς RP Reference apparatus (SBLGNT): ἡ … βούλεται WH Treg NA28 ] ἂν ἡ … βούληται RP Reference apparatus (SBLGNT): ἡλίκον WH Treg NA28 ] ὀλίγον RP Reference apparatus (SBLGNT): ἀκατάστατον WH Treg NA28 ] ἀκατάσχετον RP Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 4 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται·
  - `SRGNT`: Ἰδοὺ, καὶ τὰ πλοῖα, τηλικαῦτα ὄντα, καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου, ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται.
  - `SBLGNT`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται·
  - `BHP`: ἰδοὺ, καὶ τὰ πλοῖα, τηλικαῦτα ὄντα, καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου, ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται.
  - `Nestle1904`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται·
  - `RP2018 (Byz)`: Ἰδού, καὶ τὰ πλοῖα, τηλικαῦτα ὄντα, καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου, ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται.
  - `TR (KJTR)`: Ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα, καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου, ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται.
  - `B (03)`: ιδου και τα πλοια τα τηλικαυτα οντα και υπο ανεμων σκληρων ελαυνομενα μεταγεται υπο ελαχιστου πηδαλιου οπου η ορμη του ευθυνοντοσ βουλεται
  - `א (01)`: ιδου και τα πλοια τηλικαυτα οντα και υπο ανεμων σκληρων ελαυνομενα μεταγεται υπο ελαχιστου πηδαλιου οπου η ορμη του ευθυνοντοσ βουλεται
  - `NA28 (TAGNT)`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται.
  - `THGNT`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται.
  - `WH1881`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται·
  - `Tisch8`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἡ ὁρμὴ τοῦ εὐθύνοντος βούλεται·
  - `TCGNT (Byz)`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται.
  - `PT1904 (Byz)`: ἰδοὺ καὶ τὰ πλοῖα, τηλικαῦτα ὄντα καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται.
  - `TR-Scrivener (1894)`: ἰδού, καὶ τὰ πλοῖα, τηλικαῦτα ὄντα, καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου, ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἰδού, καὶ τὰ πλοῖα, τηλικαῦτα ὄντα, καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου, ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται.
  - `TR-Stephanus (1550)`: ἰδοὺ καὶ τὰ πλοῖα τηλικαῦτα ὄντα, καὶ ὑπὸ σκληρῶν ἀνέμων ἐλαυνόμενα, μετάγεται ὑπὸ ἐλαχίστου πηδαλίου ὅπου ἂν ἡ ὁρμὴ τοῦ εὐθύνοντος βούληται·
  - `TR-Elzevir (1624)`: ιδου και τα πλοια τηλικαυτα οντα και υπο σκληρων ανεμων ελαυνομενα μεταγεται υπο ελαχιστου πηδαλιου οπου αν η ορμη του ευθυνοντος βουληται
  - `A (02)`: ιδου και τα πλοια τηλικαυτα οντα και υπο σκληρων ανεμων ελαυνομενα μεταγεται υπο ελαχιστου πηδαλιου οπου αν η ορμη του ευθυνοντοσ βουληται
  - `C (04)`: ιδου και τα πλοια τηλικαυτα οντα και υπο ανεμων σκληρων ελαυνομενα μεταγεται υπο ελαχιστου πηδαλιου οπου αν η ορμη του ευθυνοντοσ βουληται
  - `33`: […] […] […] […] […] οντα και υπο σκληρων ανεμων […] […] υπο […] […] […] αν η ορμη του ευθυνοντος βουληθη
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.07, confidence 99%) over τα (B (03)). [Variation unit spanning several words] Adopted 'ἀνέμων σκληρῶν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over σκληρῶν ἀνέμων (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἂν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'βούλεται' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over βούληται (RP2018 (Byz), TR (KJTR)). Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 5 (Confidence: `96.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. Ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `SRGNT`: Οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν, καὶ μεγάλα αὐχεῖ. Ἰδοὺ, ἡλίκον πῦρ, ἡλίκην ὕλην ἀνάπτει.
  - `SBLGNT`: οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. Ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `BHP`: οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν, καὶ μεγάλα αὐχεῖ. ἰδοὺ, ἡλίκον πῦρ, ἡλίκην ὕλην ἀνάπτει.
  - `Nestle1904`: οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `RP2018 (Byz)`: Οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστίν, καὶ μεγαλαυχεῖ. Ἰδού, ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει.
  - `TR (KJTR)`: Οὕτως Καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν, καὶ μεγάλαυχεῖ. Ἰδοὺ, ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει!
  - `B (03)`: ουτωσ και η γλωσσα μεικρον μελοσ εστιν και μεγαλα αυχει ιδου ηλικον πυρ ηλικην υλην αναπτει
  - `א (01)`: ουτωσ και η γλωσσα μικρον μελοσ εστιν και μεγαλαυχει ιδου ηλικον πυρ ηλικην υλην αναπτι
  - `NA28 (TAGNT)`: Οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `THGNT`: Οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `WH1881`: οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `Tisch8`: οὕτως καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶν καὶ μεγάλα αὐχεῖ. ἰδοὺ ἡλίκον πῦρ ἡλίκην ὕλην ἀνάπτει·
  - `TCGNT (Byz)`: οὕτω καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶ καὶ μεγαλαυχεῖ. Ἰδού, ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει.
  - `PT1904 (Byz)`: οὕτω καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶ καὶ μεγαλαυχεῖ. ἰδοὺ ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει!
  - `TR-Scrivener (1894)`: οὕτω καὶ ἡ γλῶσσα μικρὸν μέλος ἐστί, καὶ μεγαλαυχεῖ. ἰδού, ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὕτω καὶ ἡ γλῶσσα μικρὸν μέλος ἐστί, καὶ μεγαλαυχεῖ. Ἰδού, ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει.
  - `TR-Stephanus (1550)`: οὕτω καὶ ἡ γλῶσσα μικρὸν μέλος ἐστὶ, καὶ μεγαλαυχεῖ. ἰδοὺ ὀλίγον πῦρ ἡλίκην ὕλην ἀνάπτει.
  - `TR-Elzevir (1624)`: ουτως και η γλωσσα μικρον μελος εστιν και μεγαλαυχει ιδου ολιγον πυρ ηλικην υλην αναπτει
  - `A (02)`: ωσαυτωσ και η γλωσσα μικρον μελοσ εστιν και μεγαλα αυχει ιδου ολιγον πυρ ηλικην υλην αναπτει
  - `C (04)`: ουτωσ και η γλωσσα μικρον μελοσ εστιν και μεγαλα αυχει ιδου ολιγον πυρ ηλικην υλην αναπτει
  - `33`: […] […] […] […] […] […] […] […] […] αυχη ιδου ολυγον πυρ υλικην υλην […]
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'μεγάλα αὐχεῖ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over μεγαλαυχεῖ (א (01), RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἡλίκον' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ὀλίγον (RP2018 (Byz), TR (KJTR)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `95.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `SRGNT`: Καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως, καὶ φλογιζομένη ὑπὸ τῆς Γεέννης.
  - `SBLGNT`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `BHP`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως, καὶ φλογιζομένη ὑπὸ τῆς Γεέννης.
  - `Nestle1904`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας, ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `RP2018 (Byz)`: Καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως, καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `TR (KJTR)`: Καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας: οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως· καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `B (03)`: και η γλωσσα πυρ ο κοσμοσ τησ αδικιασ η γλωσσα καθισται εν τοισ μελεσιν ημων η σπιλουσα ολον το σωμα και φλογιζουσα τον τροχον τησ γενεσεωσ και φλογιζομενη υπο τησ γεεννησ
  - `א (01)`: η γλωσσα πυρ ο κοσμοσ τησ αδικιασ η γλωσσα καθισταται εν τοισ μελεσιν ημων και σπιλουσα ολον το σωμα και φλογιζουσα τον τροχον τησ γενεσεωσ ημων και φλογιζομενη υπο τησ γεεννησ
  - `NA28 (TAGNT)`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `THGNT`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `WH1881`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `Tisch8`: ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας, ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `TCGNT (Byz)`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `PT1904 (Byz)`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας. οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν ἡ σπιλοῦσα ὅλον τὸ σῶμα καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `TR-Scrivener (1894)`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως, καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως, καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `TR-Stephanus (1550)`: καὶ ἡ γλῶσσα πῦρ, ὁ κόσμος τῆς ἀδικίας· οὕτως ἡ γλῶσσα καθίσταται ἐν τοῖς μέλεσιν ἡμῶν, ἡ σπιλοῦσα ὅλον τὸ σῶμα, καὶ φλογίζουσα τὸν τροχὸν τῆς γενέσεως, καὶ φλογιζομένη ὑπὸ τῆς γεέννης.
  - `TR-Elzevir (1624)`: και η γλωσσα πυρ ο κοσμος της αδικιας ουτως η γλωσσα καθισταται εν τοις μελεσιν ημων η σπιλουσα ολον το σωμα και φλογιζουσα τον τροχον της γενεσεως και φλογιζομενη υπο της γεεννης
  - `A (02)`: και η γλωσσα πυρ ο κοσμοσ τησ αδικειασ η γλωσσα καθισταται εν τοισ μελεσιν ημων η σπιλουσα ολον το σωμα και φλογιζουσα τον τροχον τησ γενεσεωσ και φλογιζομενη υπο τησ γεεννησ
  - `C (04)`: και η γλωσσα πυρ ο κοσμοσ τησ αδικιασ η γλωσσα καθισταται εν τοισ μελεσιν ημων η σπιλουσα ολον το σωμα και φλογιζουσα τον τροχον τησ γενεσεωσ και φλογιζομενη υπο τησ γεεννησ
  - `33`: και η γλωσσα […] […] […] […] […] […] γλωσσα καθισταται εν τοις μελεσιν […] […] […] […] […] […] […] […] […] […] […] γενεσεως και […] […] […] […]
- **Philological Rationale:** [Omission in some witnesses] Adopted 'καὶ' [B (03), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, Nestle1904, BHP] (weight 5.97, confidence 99%) over om. (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over οὕτως (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'καθίσταται' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over καθισται (B (03)). [Lexical, morphological, or word-order variant] Adopted 'ἡ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over και (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over ημων (א (01)). Also normalised 28 orthographic/surface variation(s).
- *confidence:* Verse confidence 95% = product of 5 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 7 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `SRGNT`: Πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων, δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `SBLGNT`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `BHP`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων, δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `Nestle1904`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ,
  - `RP2018 (Byz)`: Πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων, δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `TR (KJTR)`: Πᾶσα γὰρ φύσις θηρίων, τε καὶ πετεινῶν, ἑρπετῶν τε, καὶ ἐναλίων, δαμάζεται, καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ:
  - `B (03)`: πασα γαρ φυσισ θηριων τε και πετεινων ερπετων τε και εναλιων δαμαζεται και δεδαμασται τη φυσει τη ανθρωπεινη
  - `א (01)`: πασα γαρ φυσισ θηριων τε και πετινων ερπετων τε και εναλιων δαμαζεται και δεδαμασται τη φυσει τη ανθρωπινη
  - `NA28 (TAGNT)`: Πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `THGNT`: Πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `WH1881`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `Tisch8`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `TCGNT (Byz)`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων, δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ,
  - `PT1904 (Byz)`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ,
  - `TR-Scrivener (1894)`: πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων, δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `TR-Boyd (Elz/Scr/Steph)`: Πᾶσα γὰρ φύσις θηρίων τε καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων, δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `TR-Stephanus (1550)`: Πᾶσα γὰρ φύσις θηρίων τὲ καὶ πετεινῶν, ἑρπετῶν τε καὶ ἐναλίων δαμάζεται καὶ δεδάμασται τῇ φύσει τῇ ἀνθρωπίνῃ·
  - `TR-Elzevir (1624)`: πασα γαρ φυσις θηριων τε και πετεινων ερπετων τε και εναλιων δαμαζεται και δεδαμασται τη φυσει τη ανθρωπινη
  - `A (02)`: πασα γαρ φυσισ θηριων τε και πετινων ερπετων και εναλιων δαμαζετε και δεδαμασται τη φυσι τη ανθρωπινων
  - `C (04)`: πασα γαρ φυσισ θηριων τε και πετεινων ερπετων τε και εναλιων δεδαμασται και δαμαζεται τη φυσει τη ανθρωπινη
  - `33`: […] […] […] […] […] […] […] ερπετων τε και […] […] […] […] […] […] […] […]
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 17 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence); Punctuation / spacing difference only).

### Verse 8 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `SRGNT`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων, ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `SBLGNT`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `BHP`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων, ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `Nestle1904`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `RP2018 (Byz)`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάσχετον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `TR (KJTR)`: Τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάσχετον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `B (03)`: την δε γλωσσαν ουδεισ δαμασαι δυναται ανθρωπων ακαταστατον κακον μεστη ιου θανατηφορου
  - `א (01)`: την δε γλωσσαν ουδεισ δυναται δαμασαι ανων̅ ακαταστατον κακον μεστη ιου θανατηφορου
  - `NA28 (TAGNT)`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `THGNT`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `WH1881`: τὴν δὲ γλῶσσαν οὐδεὶς δαμάσαι δύναται ἀνθρώπων· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `Tisch8`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάστατον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `TCGNT (Byz)`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάσχετον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `PT1904 (Byz)`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάσχετον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `TR-Scrivener (1894)`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάσχετον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `TR-Boyd (Elz/Scr/Steph)`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι· ἀκατάσχετον κακόν, μεστὴ ἰοῦ θανατηφόρου.
  - `TR-Stephanus (1550)`: τὴν δὲ γλῶσσαν οὐδεὶς δύναται ἀνθρώπων δαμάσαι, ἀκατάσχετον κακόν· μεστὴ ἰοῦ θανατηφόρου.
  - `TR-Elzevir (1624)`: την δε γλωσσαν ουδεις δυναται ανθρωπων δαμασαι ακατασχετον κακον μεστη ιου θανατηφορου
  - `A (02)`: την δε γλωσσαν ουδεισ δυναται δαμασαι ανων̅ ακαταστατον κακον μεστη ιου θανατηφορου
  - `C (04)`: την δε γλωσσαν ουδεισ δαμασαι δυναται ανθρωπων ακατασχετον κακον μεστη ιου θανατηφορου
  - `33`: την δε γλωσσαν δαμασαι ουδεις […] […] […] […] […] […] […]
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over δυναται (א (01)). [Omission in some witnesses] Adopted 'δαμάσαι' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'δύναται' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἀκατάστατον' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over δαμάσαι ἀκατάσχετον (RP2018 (Byz), TR (KJTR)). Also normalised 9 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 9 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθʼ ὁμοίωσιν θεοῦ γεγονότας·
  - `SRGNT`: Ἐν αὐτῇ εὐλογοῦμεν τὸν Κύριον καὶ Πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους, τοὺς καθʼ ὁμοίωσιν Θεοῦ γεγονότας.
  - `SBLGNT`: ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθʼ ὁμοίωσιν θεοῦ γεγονότας·
  - `BHP`: ἐν αὐτῇ εὐλογοῦμεν τὸν Κύριον καὶ Πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους, τοὺς καθʼ ὁμοίωσιν Θεοῦ γεγονότας.
  - `Nestle1904`: ἐν αὐτῇ εὐλογοῦμεν τὸν Κύριον καὶ Πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ’ ὁμοίωσιν Θεοῦ γεγονότας·
  - `RP2018 (Byz)`: Ἐν αὐτῇ εὐλογοῦμεν τὸν θεὸν καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ’ ὁμοίωσιν θεοῦ γεγονότας·
  - `TR (KJTR)`: Ἐν αὐτῇ εὐλογοῦμεν τὸν Θεὸν, καὶ Πατέρα· καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους, τοὺς καθʼ ὁμοίωσιν Θεοῦ γεγονότας.
  - `B (03)`: εν αυτη ευλογουμεν τον κν̅ και πατερα και εν αυτη καταρωμεθα τουσ ανθρωπουσ τουσ καθ ομοιωσιν θυ̅ γεγονοτασ
  - `א (01)`: εν αυτη ευλογουμεν τον κν̅ και πατερα και εν αυτη καταρωμεθα τουσ ανθρωπουσ τουσ καθ ομοιωσιν θυ̅ γεγονοτασ
  - `NA28 (TAGNT)`: ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ᾽ ὁμοίωσιν θεοῦ γεγονότας·
  - `THGNT`: ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ᾽ ὁμοίωσιν θεοῦ γεγονότας·
  - `WH1881`: ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθʼ ὁμοίωσιν θεοῦ γεγονότας·
  - `Tisch8`: ἐν αὐτῇ εὐλογοῦμεν τὸν κύριον καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ’ ὁμοίωσιν θεοῦ γεγονότας·
  - `TCGNT (Byz)`: ἐν αὐτῇ εὐλογοῦμεν τὸν Θεὸν καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ᾽ ὁμοίωσιν Θεοῦ γεγονότας·
  - `PT1904 (Byz)`: ἐν αὐτῇ εὐλογοῦμεν τὸν Θεὸν καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ᾽ ὁμοίωσιν Θεοῦ γεγονότας·
  - `TR-Scrivener (1894)`: ἐν αὐτῇ εὐλογοῦμεν τὸν Θεὸν καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ᾽ ὁμοίωσιν Θεοῦ γεγονότας·
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐν αὐτῇ εὐλογοῦμεν τὸν Θεὸν καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθ᾿ ὁμοίωσιν Θεοῦ γεγονότας·
  - `TR-Stephanus (1550)`: Ἐν αὐτῇ εὐλογοῦμεν τὸν Θεὸν καὶ πατέρα, καὶ ἐν αὐτῇ καταρώμεθα τοὺς ἀνθρώπους τοὺς καθʼ ὁμοίωσιν Θεοῦ γεγονότας·
  - `TR-Elzevir (1624)`: εν αυτη ευλογουμεν τον θεον και πατερα και εν αυτη καταρωμεθα τους ανθρωπους τους καθ ομοιωσιν θεου γεγονοτας
  - `A (02)`: εν αυτη ευλογουμεν τον κν̅ και πρα̅ και εν αυτη καταρωμεθα τουσ ανουσ̅ τουσ καθ ομοιωσιν θυ̅ γεγενημενουσ
  - `C (04)`: εν αυτη ευλογουμεν τον κν̅ και πρα̅ και εν αυτη καταρωμεθα τουσ ανουσ̅ τουσ καθ ομοιωσιν θυ̅ γεγονοτασ
  - `33`: […] […] ευλογουμεν τον κν̅ και […] […] […] […] […] […] […] […] […] ομοιωσιν θυ̅ γεγενημενους
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'κύριον' [B (03), א (01), SRGNT, Nestle1904, BHP, SBLGNT] (weight 5.61, confidence 99%) over θεὸν (RP2018 (Byz), TR (KJTR)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `SRGNT`: Ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. Οὐ χρή ἀδελφοί μου ταῦτα οὕτως γίνεσθαι.
  - `SBLGNT`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `BHP`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή ἀδελφοί μου ταῦτα οὕτως γίνεσθαι.
  - `Nestle1904`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `RP2018 (Byz)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. Οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `TR (KJTR)`: Ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. Οὐ χρή ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `B (03)`: εκ του αυτου στοματοσ εξερχεται ευλογια και καταρα ου χρη αδελφοι μου ταυτα ουτωσ γεινεσθαι
  - `א (01)`: εκ του αυτου στοματοσ εξερχεται ευλογια και καταρα ου χρη αδελφοι μου ταυτα ουτωσ γινεσθαι
  - `NA28 (TAGNT)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `THGNT`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `WH1881`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `Tisch8`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτως γίνεσθαι.
  - `TCGNT (Byz)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτω γίνεσθαι.
  - `PT1904 (Byz)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτω γίνεσθαι.
  - `TR-Scrivener (1894)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. οὐ χρή, ἀδελφοί μου, ταῦτα οὕτω γίνεσθαι.
  - `TR-Boyd (Elz/Scr/Steph)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. Οὐ χρή, ἀδελφοί μου, ταῦτα οὕτω γίνεσθαι.
  - `TR-Stephanus (1550)`: ἐκ τοῦ αὐτοῦ στόματος ἐξέρχεται εὐλογία καὶ κατάρα. Οὐ χρὴ, ἀδελφοί μου, ταῦτα οὕτω γίνεσθαι·
  - `TR-Elzevir (1624)`: εκ του αυτου στοματος εξερχεται ευλογια και καταρα ου χρη αδελφοι μου ταυτα ουτως γινεσθαι
  - `A (02)`: εκ του αυτου στοματοσ εξερχεται ευλογια και καταρα ου χρη αδελφοι μου ταυτα ουτωσ γινεσθαι
  - `C (04)`: εκ του αυτου στοματοσ εξερχεται ευλογια και καταρα ου χρη αδελφοι μου ταυτα ουτωσ γινεσθαι
  - `33`: […] […] […] […] […] […] […] […] […] […] […] μου ταυτα ουτως […]
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 15 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence); Punctuation / spacing difference only).

### Verse 11 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `SRGNT`: Μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `SBLGNT`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `BHP`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `Nestle1904`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `RP2018 (Byz)`: Μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `TR (KJTR)`: Μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `B (03)`: μητι η πηγη εκ τησ αυτησ οπησ βρυει το γλυκυ και το πικρον
  - `א (01)`: μητι η πηγη εκ τησ αυτησ οπησ βρυει το γλυκυ και το πικρον
  - `NA28 (TAGNT)`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `THGNT`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `WH1881`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `Tisch8`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `TCGNT (Byz)`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `PT1904 (Byz)`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `TR-Scrivener (1894)`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `TR-Boyd (Elz/Scr/Steph)`: Μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `TR-Stephanus (1550)`: μήτι ἡ πηγὴ ἐκ τῆς αὐτῆς ὀπῆς βρύει τὸ γλυκὺ καὶ τὸ πικρόν;
  - `TR-Elzevir (1624)`: μητι η πηγη εκ της αυτης οπης βρυει το γλυκυ και το πικρον
  - `A (02)`: μητι η πη εκ τησ αυτησ οπησ βρυει το γλυκυ και το πικρον
  - `C (04)`: μητι η πηγη εκ τησ αυτησ οπησ βρυει το γλυκυ και το πικρον
  - `33`: […] […] […] […] […] […] […] […] […] […] […] […] πικρον
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 13 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 12 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `SRGNT`: Μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; Οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `SBLGNT`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `BHP`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `Nestle1904`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `RP2018 (Byz)`: Μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι, ἢ ἄμπελος σῦκα; Οὕτως οὐδεμία πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `TR (KJTR)`: Μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι; ἢ ἄμπελος, σῦκα; οὕτως οὐδεμια πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `B (03)`: μη δυναται αδελφοι μου συκη ελαιασ ποιησαι η αμπελοσ συκα ουτε αλυκον γλυκυ ποιησαι υδωρ
  - `א (01)`: μη δυναται αδελφοι μου συκη ελεασ ποιησαι η αμπελοσ συκα ουτωσ ουδε αλυκον γλυκυ ποιησαι υδωρ
  - `NA28 (TAGNT)`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `THGNT`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `WH1881`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `Tisch8`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὔτε ἁλυκὸν γλυκὺ ποιῆσαι ὕδωρ.
  - `TCGNT (Byz)`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὕτως οὐδεμία πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `PT1904 (Byz)`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι ἢ ἄμπελος σῦκα; οὕτως οὐδεμία πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `TR-Scrivener (1894)`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι, ἢ ἄμπελος σῦκα; οὕτως οὐδεμία πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `TR-Boyd (Elz/Scr/Steph)`: Μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι, ἢ ἄμπελος σῦκα; Οὕτως οὐδεμία πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `TR-Stephanus (1550)`: μὴ δύναται, ἀδελφοί μου, συκῆ ἐλαίας ποιῆσαι, ἢ ἄμπελος σῦκα; οὕτως οὐδεμία πηγὴ ἁλυκὸν καὶ γλυκὺ ποιῆσαι ὕδωρ.
  - `TR-Elzevir (1624)`: μη δυναται αδελφοι μου συκη ελαιας ποιησαι η αμπελος συκα ουτως ουδεμια πηγη αλυκον και γλυκυ ποιησαι υδωρ
  - `A (02)`: μη δυναται αδελφοι μου συκη ελαιασ ποιησαι η αμπελοσ συκα ουτε αλυκον γλυκυ ποιησαι υδωρ
  - `C (04)`: μη δυναται αδελφοι μου συκη ελαιασ ποιησαι η αμπελοσ συκα ουτε αλυκον γλυκυ ποιησαι υδωρ
  - `33`: μη δυναται
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐλαίας' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ελεασ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'οὔτε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over Οὕτως οὐδεμία πηγὴ (RP2018 (Byz), TR (KJTR)); ουτωσ ουδε (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over καὶ (RP2018 (Byz), TR (KJTR)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 13 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `SRGNT`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; Δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `SBLGNT`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `BHP`: τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `Nestle1904`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `RP2018 (Byz)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; Δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πρᾳΰτητι σοφίας.
  - `TR (KJTR)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πρᾳΰτητι σοφίας.
  - `B (03)`: τισ σοφοσ και επιστημων εν υμιν δειξατω εκ τησ καλησ αναστροφησ τα εργα αυτου εν πραυτητι σοφιασ
  - `א (01)`: τισ σοφοσ και επιστημων εν υμιν δειξατω εκ τησ καλησ αναστροφησ τα εργα αυτου εν πραυτητι σοφιασ
  - `NA28 (TAGNT)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `THGNT`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `WH1881`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `Tisch8`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `TCGNT (Byz)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `PT1904 (Byz)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πραΰτητι σοφίας.
  - `TR-Scrivener (1894)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πρᾳΰτητι σοφίας.
  - `TR-Boyd (Elz/Scr/Steph)`: Τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; Δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὐτοῦ ἐν πρᾳΰτητι σοφίας.
  - `TR-Stephanus (1550)`: τίς σοφὸς καὶ ἐπιστήμων ἐν ὑμῖν; δειξάτω ἐκ τῆς καλῆς ἀναστροφῆς τὰ ἔργα αὑτοῦ ἐν πραΰτητι σοφίας.
  - `TR-Elzevir (1624)`: τις σοφος και επιστημων εν υμιν δειξατω εκ της καλης αναστροφης τα εργα αυτου εν πραυτητι σοφιας
  - `A (02)`: τισ σοφοσ και επιστημων εν υμιν διξατω εκ τησ καλησ αναστροφησ τα εργα αυτου εν πραυτητι σοφιασ
  - `C (04)`: τισ σοφοσ και επιστημων εν υμιν δειξατω εκ τησ καλησ αναστροφησ τα εργα αυτου εν πραυτητι σοφιασ
  - `33`: τις σοφος και επιστιμων εν υμιν δειξατο εκ της καλης αναστροφης τα εργα […] εν πραυτητι σοφιας
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 17 surface variation(s) (Accentuation / capitalisation / breathing convention; Spelling variant pooled before the vote with the reading 'πραΰτητι' (same word, different spelling); whether that reading was adopted is shown in the apparatus).

### Verse 14 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `SRGNT`: Εἰ δὲ ζῆλον πικρὸν ἔχετε, καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `SBLGNT`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `BHP`: εἰ δὲ ζῆλον πικρὸν ἔχετε, καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `Nestle1904`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `RP2018 (Byz)`: Εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `TR (KJTR)`: Εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε, καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `B (03)`: ει δε ζηλον πικρον εχετε και ερειθιαν εν τη καρδια υμων μη κατακαυχασθε και ψευδεσθε κατα τησ αληθειασ
  - `א (01)`: ει δε ζηλον πικρον εχετε και εριθιαν εν ταισ καρδιαισ υμων μη κατακαυχασθαι τησ αληθιασ και ψευδεσθαι
  - `NA28 (TAGNT)`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `THGNT`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `WH1881`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθίαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `Tisch8`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε τῆς ἀληθείας καὶ ψεύδεσθε.
  - `TCGNT (Byz)`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `PT1904 (Byz)`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `TR-Scrivener (1894)`: εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `TR-Boyd (Elz/Scr/Steph)`: Εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐριθείαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας.
  - `TR-Stephanus (1550)`: Εἰ δὲ ζῆλον πικρὸν ἔχετε καὶ ἐρίθειαν ἐν τῇ καρδίᾳ ὑμῶν, μὴ κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας·
  - `TR-Elzevir (1624)`: ει δε ζηλον πικρον εχετε και εριθειαν εν τη καρδια υμων μη κατακαυχασθε και ψευδεσθε κατα της αληθειας
  - `A (02)`: ει δε αρα ζηλον πικρον εχετε και ερειθειαν εν τη καρδια υμων μη καυχασθε και ψευδεσθε κατα τησ αληθειασ
  - `C (04)`: ει δε ζηλον πικρον εχετε και εριθειαν εν τη καρδια υμων μη κατακαυχασθε και ψευδεσθε κατα τησ αληθειασ
  - `33`: ει δε αρα ζηλον πικρον εχετε και ερεθιαν εν τη καρδια υμων […] […] και ψευδεσθαι κατα της αληθειας
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'τῇ καρδίᾳ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ταισ καρδιαισ (א (01)). [Variation unit spanning several words] Adopted 'κατακαυχᾶσθε καὶ ψεύδεσθε κατὰ τῆς ἀληθείας' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over κατακαυχασθαι τησ αληθιασ και ψευδεσθαι (א (01)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 15 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης·
  - `SRGNT`: Οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `SBLGNT`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης·
  - `BHP`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `Nestle1904`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης·
  - `RP2018 (Byz)`: Οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλ’ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `TR (KJTR)`: Οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλʼ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `B (03)`: ουκ εστιν αυτη η σοφια ανωθεν κατερχομενη αλλα επιγειοσ ψυχικη δαιμονιωδησ
  - `א (01)`: ουκ εστιν αυτη η σοφια ανοθεν κατερχομενη αλλα επιγιοσ ψυχικη δαιμονιωδησ
  - `NA28 (TAGNT)`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλ᾽ ἐπίγειος ψυχική δαιμονιώδης.
  - `THGNT`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος ψυχικὴ δαιμονιώδης.
  - `WH1881`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης·
  - `Tisch8`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλὰ ἐπίγειος, ψυχική, δαιμονιώδης·
  - `TCGNT (Byz)`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλ᾽ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `PT1904 (Byz)`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλ᾽ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `TR-Scrivener (1894)`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλ᾽ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλ᾿ ἐπίγειος, ψυχική, δαιμονιώδης.
  - `TR-Stephanus (1550)`: οὐκ ἔστιν αὕτη ἡ σοφία ἄνωθεν κατερχομένη, ἀλλʼ ἐπίγειος, ψυχικὴ, δαιμονιώδης·
  - `TR-Elzevir (1624)`: ουκ εστιν αυτη η σοφια ανωθεν κατερχομενη αλλ επιγειος ψυχικη δαιμονιωδης
  - `A (02)`: ουκ εστιν αυτη η σοφια ανωθεν κατερχομενη αλλ επιγιοσ ψυχικη δαιμονιωδησ
  - `C (04)`: ουκ εστιν η σοφια αυτη ανωθεν κατερχομενη αλλ επιγειοσ ψυχικη δαιμονιωδησ
  - `33`: ουκ εστιν αυτη η σοφια ανωθεν κατερχομενη αλλ επιγειος ψυχικη δαιμονιωδης
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἄνωθεν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ανοθεν (א (01)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 16 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `SRGNT`: Ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `SBLGNT`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `BHP`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `Nestle1904`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `RP2018 (Byz)`: Ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `TR (KJTR)`: Ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `B (03)`: οπου γαρ ζηλοσ και ερειθεια εκει ακαταστασια και παν φαυλον πραγμα
  - `א (01)`: οπου γαρ ζηλοσ και εριθια εκει και ακαταστασια και παν φαυλον πραγμα
  - `NA28 (TAGNT)`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `THGNT`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `WH1881`: ὅπου γὰρ ζῆλος καὶ ἐριθία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `Tisch8`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `TCGNT (Byz)`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `PT1904 (Byz)`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `TR-Scrivener (1894)`: ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὅπου γὰρ ζῆλος καὶ ἐριθεία, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `TR-Stephanus (1550)`: ὅπου γὰρ ζῆλος καὶ ἐρίθεια, ἐκεῖ ἀκαταστασία καὶ πᾶν φαῦλον πρᾶγμα.
  - `TR-Elzevir (1624)`: οπου γαρ ζηλος και εριθεια εκει ακαταστασια και παν φαυλον πραγμα
  - `A (02)`: οπου γαρ ζηλοσ και εριθεια εκει και ακαταστασια και παν φαυλον πραγμα
  - `C (04)`: οπου γαρ ζηλοσ και ερεισ εκει ακαταστασια και παν φαυλον πραγμα
  - `33`: οπου γαρ ζηλος και εριθια εκει και ακαταστασια […] παν φαυλον πραγμα
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over και (א (01)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 17 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος·
  - `SRGNT`: Ἡ δὲ ἄνωθεν σοφία, πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος.
  - `SBLGNT`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος·
  - `BHP`: ἡ δὲ ἄνωθεν σοφία, πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος.
  - `Nestle1904`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος.
  - `RP2018 (Byz)`: Ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος καὶ ἀνυπόκριτος.
  - `TR (KJTR)`: Ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, καὶ ἀνυπόκριτος.
  - `B (03)`: η δε ανωθεν σοφια πρωτον μεν αγνη εστιν επειτα ειρηνικη επιεικησ ευπειθησ μεστη ελεουσ και καρπων αγαθων αδιακριτοσ ανυποκριτοσ
  - `א (01)`: η δε ανωθεν σοφια πρωτον μεν αγνη εστιν επειτα ιρηνικη επιεικησ ευπειθησ μεστη ελεουσ και καρπων αγαθων αδιακριτοσ ανυποκριτοσ
  - `NA28 (TAGNT)`: Ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος.
  - `THGNT`: Ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος.
  - `WH1881`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος·
  - `Tisch8`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος·
  - `TCGNT (Byz)`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος καὶ ἀνυπόκριτος.
  - `PT1904 (Byz)`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος καὶ ἀνυπόκριτος.
  - `TR-Scrivener (1894)`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος καὶ ἀνυπόκριτος.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος καὶ ἀνυπόκριτος.
  - `TR-Stephanus (1550)`: ἡ δὲ ἄνωθεν σοφία πρῶτον μὲν ἁγνή ἐστιν, ἔπειτα εἰρηνικὴ, ἐπιεικὴς, εὐπειθὴς, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος καὶ ἀνυπόκριτος.
  - `TR-Elzevir (1624)`: η δε ανωθεν σοφια πρωτον μεν αγνη εστιν επειτα ειρηνικη επιεικης ευπειθης μεστη ελεους και καρπων αγαθων αδιακριτος και ανυποκριτος
  - `A (02)`: η δε ανωθεν σοφια πρωτον μεν αγνη εστιν επειτα ειρηνεικη επιεικησ ευπιθησ μεστη ελεουσ και καρπων αγαθων αδιακριτοσ ανυποκριτοσ
  - `C (04)`: η δε ανωθεν σοφια πρωτον μεν αγνη εστιν επειτα ειρηνικη επιεικησ ευπηθησ μεστη ελεουσ και καρπων εργων αγαθων αδιακριτοσ ανυποκριτοσ
  - `33`: η δε ανωθεν σοφια πρωτον μεν αγνη εστιν επητα ειρηνικη επιεικης ευπηθεις μεστη ελεους και καρπων αγαθων αδιακριτος ανυποκριτος
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over καὶ (RP2018 (Byz), TR (KJTR)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 18 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `SRGNT`: Καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται, τοῖς ποιοῦσιν εἰρήνην.
  - `SBLGNT`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `BHP`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται, τοῖς ποιοῦσιν εἰρήνην.
  - `Nestle1904`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `RP2018 (Byz)`: Καρπὸς δὲ τῆς δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `TR (KJTR)`: Καρπὸς δὲ τῆς δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `B (03)`: καρποσ δε δικαιοσυνησ εν ειρηνη σπειρεται τοισ ποιουσιν ειρηνην
  - `א (01)`: καρποσ δε ο δικαιοσυνησ εν ειρηνη σπιρεται τοισ ποιουσιν ειρηνην
  - `NA28 (TAGNT)`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `THGNT`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `WH1881`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `Tisch8`: καρπὸς δὲ δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `TCGNT (Byz)`: καρπὸς δὲ τῆς δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `PT1904 (Byz)`: καρπὸς δὲ τῆς δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `TR-Scrivener (1894)`: καρπὸς δὲ τῆς δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `TR-Boyd (Elz/Scr/Steph)`: Καρπὸς δὲ τῆς δικαιοσύνης ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `TR-Stephanus (1550)`: καρπὸς δὲ τῆς δικαιοσύνης, ἐν εἰρήνῃ σπείρεται τοῖς ποιοῦσιν εἰρήνην.
  - `TR-Elzevir (1624)`: καρπος δε της δικαιοσυνης εν ειρηνη σπειρεται τοις ποιουσιν ειρηνην
  - `A (02)`: καρποσ δε δικαιοσυνησ εν ειρηνη σπειρετε τοισ ποιουσιν ειρηνην
  - `C (04)`: καρποσ δε δικαιοσυνησ εν ειρηνη σπειραιται τοισ ποιουσιν ειρηνην
  - `33`: καρπος δε δικαιωσυνης εν ειρηνη σπειρεται τοις ποιουσιν ειρηνην
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.77, confidence 99%) over τῆς (RP2018 (Byz), TR (KJTR)); ο (א (01)). Also normalised 9 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).
