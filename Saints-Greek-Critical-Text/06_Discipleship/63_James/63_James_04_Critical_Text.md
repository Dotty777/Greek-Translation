# James 04 — Saints Greek Critical Text

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

**1** Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
**2** ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
**3** αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
**4** μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
**5** ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει· Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;
**6** μείζονα δὲ δίδωσιν χάριν· διὸ λέγει· Ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται ταπεινοῖς δὲ δίδωσιν χάριν.
**7** ὑποτάγητε οὖν τῷ θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν·
**8** ἐγγίσατε τῷ θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
**9** ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν·
**10** ταπεινώθητε ἐνώπιον κυρίου, καὶ ὑψώσει ὑμᾶς.
**11** Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
**12** εἷς ἐστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
**13** Ἄγε νῦν οἱ λέγοντες· Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
**14** οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον ποία ἡ ζωὴ ὑμῶν· ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη·
**15** ἀντὶ τοῦ λέγειν ὑμᾶς· Ἐὰν ὁ κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
**16** νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
**17** εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### James 4:1
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εν υμιν** A (02)
- **Apparatus:** `πόθεν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `μάχαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 33
- **Apparatus:** `ἐν ὑμῖν;` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** A (02)
- **Apparatus:** `ἡδονῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ειδωνων** 33
- *Disregarded Surface Variant:* kept `Πόθεν` over `ποθεν`, `πόθεν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλεμοι` over `πολεμοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μάχαι` over `μαχαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν;` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ`, `Οὐκ` (B (03), RP2018 (Byz), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐντεῦθεν,` over `εντευθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡδονῶν` over `ηδονων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στρατευομένων` over `στρατευομενων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μέλεσιν` over `μελεσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν;` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:2
- **Apparatus:** `οὐκ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ουχ** B (03) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἔχετε·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εχεται** A (02)
- **Apparatus:** `φονεύετε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **φονευεται** 33
- **Apparatus:** `ζηλοῦτε,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ζηλουται** 33
- **Apparatus:** `δύνασθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δυνασθαι** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `μάχεσθε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **μαχεσθαι** 33
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **και** א (01) PT1904 (Byz) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **δὲ** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `αἰτεῖσθαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αιτεισθε** A (02)
- *Disregarded Surface Variant:* kept `ἐπιθυμεῖτε,` over `επιθυμειτε`, `Ἐπιθυμεῖτε`, `Ἐπιθυμεῖτε,` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχετε·` over `εχετε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φονεύετε` over `φονευετε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζηλοῦτε,` over `ζηλουτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιτυχεῖν·` over `επιτυχειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μάχεσθε` over `μαχεσθε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πολεμεῖτε.` over `πολεμειτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ`, `Οὐκ` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχετε` over `εχετε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διὰ` over `δια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰτεῖσθαι` over `αιτεισθαι`, `αιτισθαι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ὑμᾶς·` over `υμασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:3
- **Apparatus:** `αἰτεῖσθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αιτισθαι** א (01) 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δαπανήσητε` SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δαπανησετε** B (03) ; **καταδαπανησητε** א (01) ; **δαπανησειται** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `αἰτεῖτε` over `αιτειτε`, `αιτιτε`, `Αἰτεῖτε,` (B (03), TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαμβάνετε,` over `λαμβανετε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διότι` over `διοτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κακῶς` over `κακωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἵνα` over `ινα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡδοναῖς` over `ηδοναισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:4
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **Μοιχοὶ καὶ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *transcriptional: homoeoarcton:* The omission in B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP is explicable by homoeoarcton (μοιχ… / μοιχ…); B and א both omit, so the shorter reading keeps its credit.
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἔχθρα τοῦ θεοῦ ἐστιν ὃς` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) RP2018 (Byz) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **τουτου εχθρα εστιν τω θω̅ (= τουτου εχθρα εστιν τω θῶ)** א (01) ; **ἔχθρα ἐστὶν τῷ θεῷ; ὃς** Tisch8 *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐὰν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ἂν** RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐχθρὸς` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εχθρα** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `καθίσταται.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καθιστατε** 33
- *Disregarded Surface Variant:* kept `μοιχαλίδες,` over `μοιχαλιδεσ`, `μοιχαλειδεσ`, `Μοιχαλίδες!` (B (03), SRGNT, א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ`, `Οὐκ` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἴδατε` over `οιδατε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φιλία` over `φιλια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κόσμου` over `κοσμου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὖν` over `ουν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βουληθῇ` over `βουληθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φίλος` over `φιλοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶναι` over `ειναι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κόσμου,` over `κοσμου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καθίσταται.` over `καθισταται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:5
- **Apparatus:** `δοκεῖτε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δοκειται** א (01) ; **δωκειται** 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `κενῶς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καινωσ** A (02)
- **Apparatus:** `κατῴκισεν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **κατῴκησεν** RP2018 (Byz) TR (KJTR) 33 PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἢ` over `η`, `Ἢ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κενῶς` over `κενωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γραφὴ` over `γραφη`, `Γραφὴ` (B (03), BHP, SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λέγει·` over `λεγει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Πρὸς` over `προσ`, `“πρὸς` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φθόνον` over `φθονον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιποθεῖ` over `επιποθει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεῦμα` over `πνευμα`, `πνα̅`, `Πνεῦμα` (B (03), BHP, SRGNT, א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ὃ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν;` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:6
- **Apparatus:** `μείζονα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **μειζωνα** 33
- **Apparatus:** `ὑπερηφάνοις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υπεριφανοις** 33
- **Apparatus:** `ἀντιτάσσεται` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αντιτασσετε** B (03) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `μείζονα` over `μειζονα`, `μιζονα`, `Μείζονα` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίδωσιν` over `διδωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χάριν·` over `χαριν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διὸ` over `διο`, `Διὸ` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λέγει·` over `λεγει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ὁ` over `ο`, `“ὁ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸς` over `θσ̅`, `Θεὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ὑπερηφάνοις` over `υπερηφανοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταπεινοῖς` over `ταπεινοισ`, `ταπινοισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίδωσιν` over `διδωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χάριν.` over `χαριν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:7
- **Apparatus:** `ὑποτάγητε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υποταγηται** 33
- **Apparatus:** `ἀντίστητε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αντιστηται** 33
- **Apparatus:** `δὲ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 33 A (02) NA28 (TAGNT) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **om.** TR (KJTR) PT1904 (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `φεύξεται` SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **φευξετε** B (03) א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὑποτάγητε` over `υποταγητε`, `Ὑποτάγητε` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὖν` over `ουν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ·` over `θω̅`, `Θεῷ.`, `Θεῷ·` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἀντίστητε` over `αντιστητε`, `Ἀντίστητε` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διαβόλῳ,` over `διαβολω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀφʼ` over `αφ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν·` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:8
- **Apparatus:** `ἐγγιεῖ` א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **ἐγγίσει** B (03) Nestle1904 WH1881 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε** Nestle1904 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): modern critical editions.
- *Disregarded Surface Variant:* kept `ἐγγίσατε` over `εγγισατε`, `Ἐγγίσατε` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ,` over `θω̅`, `Θεῷ,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν.` over `υμειν`, `υμιν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καθαρίσατε` over `καθαρισατε`, `Καθαρίσατε` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χεῖρας,` over `χειρασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτωλοί,` over `αμαρτωλοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁγνίσατε` over `αγνισατε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καρδίας,` over `καρδιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίψυχοι.` over `διψυχοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:9
- **Apparatus:** `ταλαιπωρήσατε καὶ πενθήσατε` B (03) א (01) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT BHP A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** Nestle1904 ; **ταλεπορισατε και πενθησατε** 33 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): modern critical editions.
- **Apparatus:** `καὶ` B (03) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **om.** א (01) Nestle1904 A (02) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `κλαύσατε` B (03) א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** Nestle1904 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): modern critical editions.
- **Apparatus:** `γέλως` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **γελος** 33
- **Apparatus:** `μετατραπήτω` B (03) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) Tisch8 WH1881 **]** **μεταστραφήτω** א (01) RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **μεταστραφειτο** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γέλως` over `γελωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πένθος` over `πενθοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαρὰ` over `χαρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατήφειαν·` over `κατηφειαν`, `κατηφιαν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### James 4:10
- **Apparatus:** `ταπεινώθητε` B (03) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ταπινωθητε ουν** א (01) ; **ταπεινωθησεται** 33 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) THGNT Tisch8 WH1881 **]** **τοῦ** RP2018 (Byz) TR (KJTR) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἐνώπιον` over `ενωπιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου,` over `κυ̅`, `Κυρίου,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑψώσει` over `υψωσει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμᾶς.` over `υμασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:11
- **Apparatus:** `καταλαλεῖτε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καταλαλειται** א (01) ; **καταλαληται αδελφοι μου** 33 ; **καταλαλειτε αδελφοι μου** A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀδελφοί·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** A (02)
- **Apparatus:** `ἢ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **καὶ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `εἰ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **η** A (02)
- *Disregarded Surface Variant:* kept `Μὴ` over `μη`, `μὴ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλήλων,` over `αλληλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί·` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καταλαλῶν` over `καταλαλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοῦ` over `αδελφου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίνων` over `κρεινων`, `κρινων` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφὸν` over `αδελφον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καταλαλεῖ` over `καταλαλει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμου` over `νομου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίνει` over `κρεινει`, `κρινι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `νόμον·` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰ` over `ει`, `Εἰ` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμον` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίνεις,` over `κρεινεισ`, `κρινισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶ` over `ει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιητὴς` over `ποιητησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμου` over `νομου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλὰ` over `αλλα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κριτής.` over `κριτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:12
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP WH1881 **]** **ὁ** א (01) RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `καὶ κριτής` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) NA28 (TAGNT) PT1904 (Byz) THGNT Tisch8 WH1881 **]** **om.** RP2018 (Byz) TR (KJTR) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *transcriptional: homoeoteleuton:* The omission in RP2018 (Byz), TR (KJTR) is explicable by homoeoteleuton (…τησ / …τησ) (a possibility only; the vote is unchanged).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `δὲ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **om.** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ὁ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ὃς** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `κρίνων` א (01) SRGNT SBLGNT Nestle1904 BHP B (03) 33 A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **κρίνεις** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `πλησίον` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ἕτερον** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `εἷς` over `εισ`, `Εἷς` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν`, `ἐστὶν` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `νομοθέτης` over `νομοθετησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δυνάμενος` over `δυναμενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶσαι` over `σωσαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπολέσαι·` over `απολεσαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σὺ` over `συ`, `Σὺ` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τίς` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶ,` over `ει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίνων` over `κρινων`, `κρεινων` (B (03), א (01)) — *Spelling variant pooled before the vote with the reading 'κρίνων' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:13
- **Apparatus:** `ἢ αὔριον πορευσόμεθα` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 WH1881 **]** **καὶ αὔριον πορευσώμεθα** RP2018 (Byz) A (02) TCGNT (Byz) TR-Stephanus (1550) ; **καὶ αὔριον πορευσόμεθα** PT1904 (Byz) *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ποιήσομεν` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) NA28 (TAGNT) PT1904 (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 WH1881 **]** **ποιήσωμεν** א (01) RP2018 (Byz) 33 A (02) TCGNT (Byz) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ἕνα** RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐμπορευσόμεθα καὶ κερδήσομεν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 WH1881 **]** **ἐμπορευσώμεθα καὶ κερδήσωμεν** RP2018 (Byz) TCGNT (Byz) TR-Stephanus (1550) *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Ἄγε` over `αγε`, `ἄγε` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νῦν` over `νυν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λέγοντες·` over `λεγοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Σήμερον` over `σημερον`, `“σήμερον` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τήνδε` over `τηνδε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την`, `τήν` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλιν` over `πολιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκεῖ` over `εκει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐνιαυτὸν` over `ενιαυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:14
- **Apparatus:** `τὸ` א (01) SBLGNT BHP RP2018 (Byz) TR (KJTR) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **om.** B (03) SRGNT Nestle1904 WH1881 ; **τα** 33 A (02) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) TCGNT (Byz) THGNT WH1881 **]** **γὰρ** RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἡ` א (01) SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** B (03) ; **γὰρ** SRGNT *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `ὑμῶν·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ἡμῶν;** 33
- **Apparatus:** `ἀτμὶς` SRGNT RP2018 (Byz) TR (KJTR) SBLGNT Nestle1904 BHP B (03) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** א (01) ; **ατμης** 33 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `γάρ` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) RP2018 (Byz) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** א (01) ; **εστιν** 33 ; **εσται** A (02) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐστε` B (03) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **om.** א (01) 33 A (02) ; **ἔσται** RP2018 (Byz) PT1904 (Byz) TCGNT (Byz) ; **ἐστιν** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `ἡ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **om.** B (03) WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δὲ** RP2018 (Byz) 33 PT1904 (Byz) TCGNT (Byz) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `καὶ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **δὲ** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `οἵτινες` over `οιτινεσ`, `Οἵτινες` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπίστασθε` over `επιστασθε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὔριον` over `αυριον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποία` over `ποια`, `Ποία` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζωὴ` over `ζωη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν·` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἀτμὶς` over `ἀτμὶς`, `ατμεισ` (B (03), BHP, Nestle1904, SBLGNT) — *Spelling variant pooled before the vote with the reading 'Ἀτμὶς' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀλίγον` over `ολιγον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φαινομένη,` over `φαινομενη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔπειτα` over `επειτα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀφανιζομένη·` over `αφανιζομενη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:15
- **Apparatus:** `θελήσῃ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **θελη** B (03) 33 WH1881 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ζήσομεν καὶ ποιήσομεν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) THGNT TR-Scrivener (1894) Tisch8 WH1881 **]** **ζήσωμεν καὶ ποιήσωμεν** RP2018 (Byz) 33 TCGNT (Byz) TR-Stephanus (1550) ; **ζήσωμεν, καὶ ποιήσομεν** TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐκεῖνο.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κεινο** A (02)
- *Disregarded Surface Variant:* kept `ἀντὶ` over `αντι`, `Ἀντὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λέγειν` over `λεγειν`, `λεγιν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ὑμᾶς·` over `υμασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἐὰν` over `εαν`, `“ἐὰν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κύριος` over `κσ̅`, `Κύριος` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦτο` over `τουτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἢ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκεῖνο.` over `εκεινο`, `εκινο` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### James 4:16
- **Apparatus:** `καυχᾶσθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κατακαυχασθε** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `πᾶσα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **απασα** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `καύχησις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καυχισις** 33
- *Disregarded Surface Variant:* kept `νῦν` over `νυν`, `Νῦν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλαζονείαις` over `αλαζονιαισ`, `ἀλαζονίαις` (B (03), BHP, Nestle1904, א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ὑμῶν·` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καύχησις` over `καυχησισ`, `καυχησεισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τοιαύτη` over `τοιαυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πονηρά` over `πονηρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν.` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 4:17
- **Apparatus:** `ποιεῖν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ποιησαι** A (02)
- *Disregarded Surface Variant:* kept `εἰδότι` over `ειδοτι`, `Εἰδότι` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὖν` over `ουν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καλὸν` over `καλον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιεῖν` over `ποιειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιοῦντι,` over `ποιουντι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτία` over `αμαρτια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῷ` over `αυτω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν.` over `εστιν`, `ἐστίν.` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `SRGNT`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; Οὐκ ἐντεῦθεν ἐκ τῶν ἡδονῶν ὑμῶν, τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `SBLGNT`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `BHP`: πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν ἐκ τῶν ἡδονῶν ὑμῶν, τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `Nestle1904`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `RP2018 (Byz)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; Οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `TR (KJTR)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `B (03)`: ποθεν πολεμοι και ποθεν μαχαι εν υμιν ουκ εντευθεν εκ των ηδονων υμων των στρατευομενων εν τοισ μελεσιν υμων
  - `א (01)`: ποθεν πολεμοι και ποθεν μαχαι εν υμιν ουκ εντευθεν εκ των ηδονων υμων των στρατευομενων εν τοισ μελεσιν υμων
  - `NA28 (TAGNT)`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `THGNT`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `WH1881`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `Tisch8`: Πόθεν πόλεμοι καὶ πόθεν μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `TCGNT (Byz)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `PT1904 (Byz)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `TR-Scrivener (1894)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `TR-Boyd (Elz/Scr/Steph)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; Οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `TR-Stephanus (1550)`: Πόθεν πόλεμοι καὶ μάχαι ἐν ὑμῖν; οὐκ ἐντεῦθεν, ἐκ τῶν ἡδονῶν ὑμῶν τῶν στρατευομένων ἐν τοῖς μέλεσιν ὑμῶν;
  - `TR-Elzevir (1624)`: ποθεν πολεμοι και μαχαι εν υμιν ουκ εντευθεν εκ των ηδονων υμων των στρατευομενων εν τοις μελεσιν υμων
  - `A (02)`: ποθεν πολεμοι εν υμιν και ποθεν μαχαι ουκ εντευθεν εκ των ηδονων υμων των στρατευομενων εν τοισ μελεσιν υμων
  - `C (04)`: ποθεν πολεμοι και ποθεν μαχαι εν υμιν ουκ εντευθεν εκ των ηδονων υμων των στρατευομενων εν τοισ μελεσιν υμων
  - `33`: ποθεν πολεμοι και ποθεν εν υμιν […] ουκ εντευθεν εκ των ειδωνων υμων των στρατευομενων εν τοις μελεσιν υμων
- **Philological Rationale:** [Omission in some witnesses] Adopted 'πόθεν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). Reference apparatus (SBLGNT): πόθεν WH Treg NA28 ] – RP Reference apparatus (SBLGNT): ἐὰν WH NA28 ] ἂν Treg RP Reference apparatus (SBLGNT): καὶ κριτής WH Treg NA28 ] – RP Reference apparatus (SBLGNT): ὁ κρίνων WH Treg NA28 ] ὃς κρίνεις RP Reference apparatus (SBLGNT): πλησίον WH Treg NA28 ] ἕτερον RP Reference apparatus (SBLGNT): πορευσόμεθα WH Treg NA28 ] πορευσώμεθα RP Reference apparatus (SBLGNT): ποιήσομεν WH NA28 ] ποιήσωμεν Treg RP Reference apparatus (SBLGNT): ἐνιαυτὸν WH Treg NA28 ] + ἕνα RP Reference apparatus (SBLGNT): ἐμπορευσόμεθα WH Treg NA28 ] ἐμπορευσώμεθα RP Reference apparatus (SBLGNT): κερδήσομεν WH Treg NA28 ] κερδήσωμεν RP Reference apparatus (SBLGNT): ποία WH NA28 ] + γὰρ Treg RP Reference apparatus (SBLGNT): ἐστε WH Treg NA28 ] ἔσται RP Reference apparatus (SBLGNT): ἡ Treg NA28 RP ] – WH Reference apparatus (SBLGNT): ἔπειτα WH Treg NA28 ] + δὲ RP Reference apparatus (SBLGNT): ζήσομεν WH Treg NA28 ] ζήσωμεν RP Reference apparatus (SBLGNT): ποιήσομεν WH Treg NA28 ] ποιήσωμεν RP Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 2 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `SRGNT`: Ἐπιθυμεῖτε καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. Οὐκ ἔχετε, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `SBLGNT`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `BHP`: ἐπιθυμεῖτε καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε· οὐκ ἔχετε, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `Nestle1904`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `RP2018 (Byz)`: Ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε, οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `TR (KJTR)`: Ἐπιθυμεῖτε, καὶ οὐκ ἔχετε: φονεύετε, καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν: μάχεσθε καὶ πολεμεῖτε, οὐκ ἔχετε δὲ, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς.
  - `B (03)`: επιθυμειτε και ουχ εχετε φονευετε και ζηλουτε και ου δυνασθε επιτυχειν μαχεσθε και πολεμειτε ουκ εχετε δια το μη αιτεισθαι υμασ
  - `א (01)`: επιθυμειτε και ουκ εχετε φονευετε και ζηλουτε και ου δυνασθαι επιτυχειν μαχεσθε και πολεμειτε και ουκ εχετε δια το μη αιτισθαι υμασ
  - `NA28 (TAGNT)`: ἐπιθυμεῖτε καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε· οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `THGNT`: ἐπιθυμεῖτε καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε· οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `WH1881`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `Tisch8`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. καὶ οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `TCGNT (Byz)`: ἐπιθυμεῖτε καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε. οὐκ ἔχετε διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `PT1904 (Byz)`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε, καὶ οὐκ ἔχετε, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `TR-Scrivener (1894)`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε, οὐκ ἔχετε δέ, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε, οὐκ ἔχετε δέ, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `TR-Stephanus (1550)`: ἐπιθυμεῖτε, καὶ οὐκ ἔχετε· φονεύετε καὶ ζηλοῦτε, καὶ οὐ δύνασθε ἐπιτυχεῖν· μάχεσθε καὶ πολεμεῖτε, οὐκ ἔχετε δὲ, διὰ τὸ μὴ αἰτεῖσθαι ὑμᾶς·
  - `TR-Elzevir (1624)`: επιθυμειτε και ουκ εχετε φονευετε και ζηλουτε και ου δυνασθε επιτυχειν μαχεσθε και πολεμειτε ουκ εχετε δε δια το μη αιτεισθαι υμας
  - `A (02)`: επιθυμειτε και ουκ εχεται φονευετε και ζηλουτε και ου δυνασθε επιτυχειν μαχεσθε και πολεμειτε ουχ εχετε δια το μη αιτεισθε υμασ
  - `C (04)`: επιθυμειτε και ουκ εχετε φονευετε και ζηλουτε και ου δυνασθε επιτυχειν μαχεσθε και πολεμειτε …
  - `33`: […] και ουκ εχετε φονευεται και ζηλουται και ου δυνασθε επιτυχειν μαχεσθαι και […] ουκ εχετε δια το μη αιτεισθαι υμας
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'οὐκ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over ουχ (B (03)). [Lexical, morphological, or word-order variant] Adopted 'δύνασθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over δυνασθαι (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over και (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over δὲ (TR (KJTR)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 3 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `SRGNT`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `SBLGNT`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `BHP`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `Nestle1904`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `RP2018 (Byz)`: αἰτεῖτε, καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `TR (KJTR)`: Αἰτεῖτε, καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `B (03)`: αιτειτε και ου λαμβανετε διοτι κακωσ αιτεισθε ινα εν ταισ ηδοναισ υμων δαπανησετε
  - `א (01)`: αιτιτε και ου λαμβανετε διοτι κακωσ αιτισθαι ινα εν ταισ ηδοναισ υμων καταδαπανησητε
  - `NA28 (TAGNT)`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `THGNT`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `WH1881`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `Tisch8`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `TCGNT (Byz)`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `PT1904 (Byz)`: αἰτεῖτε καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `TR-Scrivener (1894)`: αἰτεῖτε, καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `TR-Boyd (Elz/Scr/Steph)`: αἰτεῖτε, καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `TR-Stephanus (1550)`: αἰτεῖτε, καὶ οὐ λαμβάνετε, διότι κακῶς αἰτεῖσθε, ἵνα ἐν ταῖς ἡδοναῖς ὑμῶν δαπανήσητε.
  - `TR-Elzevir (1624)`: αιτειτε και ου λαμβανετε διοτι κακως αιτεισθε ινα εν ταις ηδοναις υμων δαπανησητε
  - `A (02)`: αιτειτε και ου λαμβανετε διοτι κακωσ αιτεισθε ινα εν ταισ ηδοναισ υμων δαπανησητε
  - `33`: αιτειτε και ου λαμβανετε διοτι κακως αιτεισθαι ινα εν […] ειδοναις υμων δαπανησειται
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'αἰτεῖσθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αιτισθαι (א (01)). [Lexical, morphological, or word-order variant] Adopted 'δαπανήσητε' [SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.99, confidence 99%) over δαπανησετε (B (03)); καταδαπανησητε (א (01)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 4 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `SRGNT`: Μοιχαλίδες! Οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου, ἔχθρα τοῦ Θεοῦ ἐστιν; Ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `SBLGNT`: μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `BHP`: μοιχαλίδες! οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου, ἔχθρα τοῦ Θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `Nestle1904`: μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ Θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `RP2018 (Byz)`: Μοιχοὶ καὶ μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστίν; Ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `TR (KJTR)`: Μοιχοὶ καὶ μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ Θεοῦ ἐστιν; ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `B (03)`: μοιχαλιδεσ ουκ οιδατε οτι η φιλια του κοσμου εχθρα του θυ̅ εστιν οσ εαν ουν βουληθη φιλοσ ειναι του κοσμου εχθροσ του θυ̅ καθισταται
  - `א (01)`: μοιχαλειδεσ ουκ οιδατε οτι η φιλια του κοσμου τουτου εχθρα εστιν τω θω̅ εαν ουν βουληθη φιλοσ ειναι του κοσμου εχθρα του θυ̅ καθισταται
  - `NA28 (TAGNT)`: μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `THGNT`: μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστιν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `WH1881`: μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστίν; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `Tisch8`: μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα ἐστὶν τῷ θεῷ; ὃς ἐὰν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ θεοῦ καθίσταται.
  - `TCGNT (Byz)`: μοιχοὶ καὶ μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ Θεοῦ ἐστιν; ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `PT1904 (Byz)`: μοιχοὶ καὶ μοιχαλίδες! οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ Θεοῦ ἐστιν; ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `TR-Scrivener (1894)`: μοιχοὶ καὶ μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ Θεοῦ ἐστίν; ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `TR-Boyd (Elz/Scr/Steph)`: Μοιχοὶ καὶ μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ Θεοῦ ἐστίν; Ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `TR-Stephanus (1550)`: μοιχοὶ καὶ μοιχαλίδες, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου, ἔχθρα τοῦ Θεοῦ ἐστιν; ὃς ἂν οὖν βουληθῇ φίλος εἶναι τοῦ κόσμου, ἐχθρὸς τοῦ Θεοῦ καθίσταται.
  - `TR-Elzevir (1624)`: μοιχοι και μοιχαλιδες ουκ οιδατε οτι η φιλια του κοσμου εχθρα του θεου εστιν ος αν ουν βουληθη φιλος ειναι του κοσμου εχθρος του θεου καθισταται
  - `A (02)`: μοιχαλιδεσ ουκ οιδατε οτι η φιλια του κοσμου εχθρα του θυ̅ εστιν οσ αν ουν βουληθη φιλοσ ειναι του κοσμου εχθροσ του θυ̅ καθισταται
  - `33`: μυχαλλιδες ουκ οιδατε οτι η φιλια του κοσμου εχθρα του […] […] ος αν βουληθη φιλος ειναι του κοσμου εχθρος του θυ̅ καθιστατε
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over Μοιχοὶ καὶ (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'ἔχθρα τοῦ θεοῦ ἐστιν ὃς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR), RP2018 (Byz)] (weight 5.97, confidence 99%) over τουτου εχθρα εστιν τω θω̅ (= τουτου εχθρα εστιν τω θῶ) (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἐὰν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἂν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἐχθρὸς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εχθρα (א (01)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 5 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει· Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;
  - `SRGNT`: Ἢ δοκεῖτε ὅτι κενῶς ἡ Γραφὴ λέγει, “Πρὸς φθόνον ἐπιποθεῖ τὸ Πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;”
  - `SBLGNT`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει· Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;
  - `BHP`: ἢ δοκεῖτε ὅτι κενῶς ἡ Γραφὴ λέγει, “πρὸς φθόνον ἐπιποθεῖ τὸ Πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;”
  - `Nestle1904`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;
  - `RP2018 (Byz)`: Ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει; Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν.
  - `TR (KJTR)`: Ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει, Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν;
  - `B (03)`: η δοκειτε οτι κενωσ η γραφη λεγει προσ φθονον επιποθει το πνευμα ο κατωκισεν εν ημιν
  - `א (01)`: η δοκειται οτι κενωσ η γραφη λεγει προσ φθονον επιποθει το πνα̅ ο κατωκισεν εν ημιν
  - `NA28 (TAGNT)`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει; πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν,
  - `THGNT`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει; πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν,
  - `WH1881`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;
  - `Tisch8`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει, πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;
  - `TCGNT (Byz)`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει; πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν,
  - `PT1904 (Byz)`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει, πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν ;
  - `TR-Scrivener (1894)`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει, Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν;
  - `TR-Boyd (Elz/Scr/Steph)`: Ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει, Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν;
  - `TR-Stephanus (1550)`: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει, Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκησεν ἐν ἡμῖν;
  - `TR-Elzevir (1624)`: η δοκειτε οτι κενως η γραφη λεγει προς φθονον επιποθει το πνευμα ο κατωκησεν εν ημιν
  - `A (02)`: η δοκειτε οτι καινωσ η γραφη λεγει προσ φθονον επιποθει το πνα̅ ο κατωκεισεν εν ημιν
  - `33`: ει δωκειται οτι […] […] γραφη λεγει προς φθονον επιποθει το πνα̅ ο κατωκησεν εν ημιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'δοκεῖτε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over δοκειται (א (01)). [Lexical, morphological, or word-order variant] Adopted 'κατῴκισεν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over κατῴκησεν (RP2018 (Byz), TR (KJTR)). Also normalised 14 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μείζονα δὲ δίδωσιν χάριν· διὸ λέγει· Ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται ταπεινοῖς δὲ δίδωσιν χάριν.
  - `SRGNT`: Μείζονα δὲ δίδωσιν χάριν. Διὸ λέγει, “Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.”
  - `SBLGNT`: μείζονα δὲ δίδωσιν χάριν· διὸ λέγει· Ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται ταπεινοῖς δὲ δίδωσιν χάριν.
  - `BHP`: μείζονα δὲ δίδωσιν χάριν. διὸ λέγει, “ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.”
  - `Nestle1904`: μείζονα δὲ δίδωσιν χάριν· διὸ λέγει Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.
  - `RP2018 (Byz)`: Μείζονα δὲ δίδωσιν χάριν· διὸ λέγει, Ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.
  - `TR (KJTR)`: Μείζονα δὲ δίδωσιν χάριν. Διὸ λέγει, Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.
  - `B (03)`: μειζονα δε διδωσιν χαριν διο λεγει ο θσ̅ υπερηφανοισ αντιτασσετε ταπεινοισ δε διδωσιν χαριν
  - `א (01)`: μιζονα δε διδωσιν χαριν διο λεγει ο θσ̅ υπερηφανοισ αντιτασσεται ταπινοισ δε διδωσιν χαριν
  - `NA28 (TAGNT)`: μείζονα δὲ δίδωσιν χάριν· διὸ λέγει· ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.
  - `THGNT`: μείζονα δὲ δίδωσιν χάριν· διὸ λέγει· ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.
  - `WH1881`: μείζονα δὲ δίδωσιν χάριν· διὸ λέγει Ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται ταπεινοῖς δὲ δίδωσιν χάριν.
  - `Tisch8`: μείζονα δὲ δίδωσιν χάριν· διὸ λέγει, ὁ θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν.
  - `TCGNT (Byz)`: μείζονα δὲ δίδωσι χάριν· διὸ λέγει, Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσι χάριν.
  - `PT1904 (Byz)`: μείζονα δὲ δίδωσι χάριν· διὸ λέγει· ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσι χάριν.
  - `TR-Scrivener (1894)`: μείζονα δὲ δίδωσι χάριν· διὸ λέγει, Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσι χάριν.
  - `TR-Boyd (Elz/Scr/Steph)`: Μείζονα δὲ δίδωσι χάριν· διὸ λέγει, Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσι χάριν.
  - `TR-Stephanus (1550)`: μείζονα δὲ δίδωσι χάριν· διὸ λέγει, Ὁ Θεὸς ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσι χάριν.
  - `TR-Elzevir (1624)`: μειζονα δε διδωσιν χαριν διο λεγει ο θεος υπερηφανοις αντιτασσεται ταπεινοις δε διδωσιν χαριν
  - `A (02)`: μειζονα δε διδωσιν χαριν διο λεγει ο θσ̅ υπερηφανοισ αντιτασσεται ταπεινοισ δε διδωσιν χαριν
  - `33`: μειζωνα δε […] […] διο λεγει ο θς̅ υπεριφανοις αντιτασσεται ταπεινοις δε διδωσιν χαριν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἀντιτάσσεται' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over αντιτασσετε (B (03)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 7 (Confidence: `95.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὑποτάγητε οὖν τῷ θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν·
  - `SRGNT`: Ὑποτάγητε οὖν τῷ Θεῷ. Ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν.
  - `SBLGNT`: ὑποτάγητε οὖν τῷ θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν·
  - `BHP`: ὑποτάγητε οὖν τῷ Θεῷ. ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν.
  - `Nestle1904`: ὑποτάγητε οὖν τῷ Θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφ’ ὑμῶν·
  - `RP2018 (Byz)`: Ὑποτάγητε οὖν τῷ θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφ’ ὑμῶν.
  - `TR (KJTR)`: Ὑποτάγητε οὖν τῷ Θεῷ. Ἀντίστητε τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν.
  - `B (03)`: υποταγητε ουν τω θω̅ αντιστητε δε τω διαβολω και φευξετε αφ υμων
  - `א (01)`: υποταγητε ουν τω θω̅ αντιστητε δε τω διαβολω και φευξετε αφ υμων
  - `NA28 (TAGNT)`: ὑποτάγητε οὖν τῷ θεῷ. ἀντίστητε δὲ τῷ διαβόλῳ καὶ φεύξεται ἀφ᾽ ὑμῶν,
  - `THGNT`: ὑποτάγητε οὖν τῷ θεῷ. ἀντίστητε δὲ τῷ διαβόλῳ καὶ φεύξεται ἀφ᾽ ὑμῶν,
  - `WH1881`: Ὑποτάγητε οὖν τῷ θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν·
  - `Tisch8`: ὑποτάγητε οὖν τῷ θεῷ· ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφ’ ὑμῶν·
  - `TCGNT (Byz)`: ὑποτάγητε οὖν τῷ Θεῷ, ἀντίστητε δὲ τῷ διαβόλῳ, καὶ φεύξεται ἀφ᾽ ὑμῶν.
  - `PT1904 (Byz)`: Ὑποτάγητε οὖν τῷ Θεῷ. ἀντίστητε τῷ διαβόλῳ, καὶ φεύξεται ἀφ᾽ ὑμῶν·
  - `TR-Scrivener (1894)`: ὑποτάγητε οὖν τῷ Θεῷ· ἀντίστητε τῷ διαβόλῳ, καὶ φεύξεται ἀφ᾽ ὑμῶν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὑποτάγητε οὖν τῷ Θεῷ· ἀντίστητε τῷ διαβόλῳ, καὶ φεύξεται ἀφ᾿ ὑμῶν.
  - `TR-Stephanus (1550)`: Ὑποτάγητε οὖν τῷ Θεῷ, ἀντίστητε τῷ διαβόλῳ, καὶ φεύξεται ἀφʼ ὑμῶν·
  - `TR-Elzevir (1624)`: υποταγητε ουν τω θεω αντιστητε τω διαβολω και φευξεται αφ υμων
  - `A (02)`: υποταγητε ουν τω θω̅ αντιστητε δε τω διαβολω και φευξεται αφ υμων
  - `33`: υποταγηται ουν τω θω̅ αντιστηται δε τω διαβολω και φευξεται αφ υμων
- **Philological Rationale:** [Omission in some witnesses] Adopted 'δὲ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over om. (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'φεύξεται' [SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.99, confidence 96%) over φευξετε (B (03), א (01)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 95% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 8 (Confidence: `95.6%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐγγίσατε τῷ θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `SRGNT`: Ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν. Καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `SBLGNT`: ἐγγίσατε τῷ θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `BHP`: ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `Nestle1904`: ἐγγίσατε τῷ Θεῷ, καὶ ἐγγίσει ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι. ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε·
  - `RP2018 (Byz)`: Ἐγγίσατε τῷ θεῷ, καὶ ἐγγιεῖ ὑμῖν· καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `TR (KJTR)`: Ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν. Καθαρίσατε χεῖρας, ἁμαρτωλοί· καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `B (03)`: εγγισατε τω θω̅ και εγγισει υμειν καθαρισατε χειρασ αμαρτωλοι και αγνισατε καρδιασ διψυχοι
  - `א (01)`: εγγισατε τω θω̅ και εγγιει υμιν καθαρισατε χειρασ αμαρτωλοι και αγνισατε καρδιασ διψυχοι
  - `NA28 (TAGNT)`: ἐγγίσατε τῷ θεῷ καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `THGNT`: ἐγγίσατε τῷ θεῷ καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `WH1881`: ἐγγίσατε τῷ θεῷ, καὶ ἐγγίσει ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `Tisch8`: ἐγγίσατε τῷ θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `TCGNT (Byz)`: ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `PT1904 (Byz)`: ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας ἁμαρτωλοὶ καὶ ἁγνίσατε καρδίας δίψυχοι.
  - `TR-Scrivener (1894)`: ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν· καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν· καθαρίσατε χεῖρας, ἁμαρτωλοί, καὶ ἁγνίσατε καρδίας, δίψυχοι.
  - `TR-Stephanus (1550)`: ἐγγίσατε τῷ Θεῷ, καὶ ἐγγιεῖ ὑμῖν. καθαρίσατε χεῖρας ἁμαρτωλοὶ, καὶ ἁγνίσατε καρδίας δίψυχοι.
  - `TR-Elzevir (1624)`: εγγισατε τω θεω και εγγιει υμιν καθαρισατε χειρας αμαρτωλοι και αγνισατε καρδιας διψυχοι
  - `A (02)`: εγγεισατε τω θω̅ και εγγιει υμιν καθαρισατε χειρασ αμαρτωλοι και αγνισατε καρδιασ διψυχοι
  - `33`: εγγισατε τω θω̅ και εγγιει υμιν καθαρισατε χειρας αμαρτωλοι και αγνισατε καρδιας διψυχοι
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐγγιεῖ' [א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.05, confidence 97%) over ἐγγίσει (B (03), Nestle1904). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.15, confidence 99%) over ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε (Nestle1904). Also normalised 12 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 9 (Confidence: `92.8%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν·
  - `SRGNT`: Ταλαιπωρήσατε, καὶ πενθήσατε, καὶ κλαύσατε. Ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `SBLGNT`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν·
  - `BHP`: ταλαιπωρήσατε, καὶ πενθήσατε, καὶ κλαύσατε. ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `Nestle1904`: ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `RP2018 (Byz)`: Ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `TR (KJTR)`: Ταλαιπωρήσατε, καὶ πενθήσατε, καὶ κλαύσατε: ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `B (03)`: ταλαιπωρησατε και πενθησατε και κλαυσατε ο γελωσ υμων εισ πενθοσ μετατραπητω και η χαρα εισ κατηφειαν
  - `א (01)`: ταλαιπωρησατε και πενθησατε κλαυσατε ο γελωσ υμων εισ πενθοσ μεταστραφητω και η χαρα εισ κατηφιαν
  - `NA28 (TAGNT)`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `THGNT`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `WH1881`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν·
  - `Tisch8`: ταλαιπωρήσατε καὶ πενθήσατε, κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μετατραπήτω καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `TCGNT (Byz)`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `PT1904 (Byz)`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `TR-Scrivener (1894)`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `TR-Stephanus (1550)`: ταλαιπωρήσατε καὶ πενθήσατε καὶ κλαύσατε· ὁ γέλως ὑμῶν εἰς πένθος μεταστραφήτω, καὶ ἡ χαρὰ εἰς κατήφειαν.
  - `TR-Elzevir (1624)`: ταλαιπωρησατε και πενθησατε και κλαυσατε ο γελως υμων εις πενθος μεταστραφητω και η χαρα εις κατηφειαν
  - `A (02)`: ταλαιπωρησατε και πενθησατε κλαυσατε ο γελωσ υμων εισ πενθοσ μεταστραφητω και η χαρα εισ κατηφειαν
  - `33`: ταλεπορισατε και πενθησατε και κλαυσατε ο γελος υμων εις πενθος μεταστραφειτο και η χαρα εις κατηφειαν
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ταλαιπωρήσατε καὶ πενθήσατε' [B (03), א (01), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, BHP] (weight 6.03, confidence 99%) over om. (Nestle1904). [Omission in some witnesses] Adopted 'καὶ' [B (03), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.07, confidence 97%) over om. (א (01), Nestle1904). [Omission in some witnesses] Adopted 'κλαύσατε' [B (03), א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.03, confidence 99%) over om. (Nestle1904). [Lexical, morphological, or word-order variant] Adopted 'μετατραπήτω' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over μεταστραφήτω (א (01), RP2018 (Byz), TR (KJTR)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 93% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ταπεινώθητε ἐνώπιον κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `SRGNT`: Ταπεινώθητε ἐνώπιον Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `SBLGNT`: ταπεινώθητε ἐνώπιον κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `BHP`: ταπεινώθητε ἐνώπιον Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `Nestle1904`: ταπεινώθητε ἐνώπιον Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `RP2018 (Byz)`: Ταπεινώθητε ἐνώπιον τοῦ κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `TR (KJTR)`: Ταπεινώθητε ἐνώπιον τοῦ Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `B (03)`: ταπεινωθητε ενωπιον κυ̅ και υψωσει υμασ
  - `א (01)`: ταπινωθητε ουν ενωπιον κυ̅ και υψωσει υμασ
  - `NA28 (TAGNT)`: ταπεινώθητε ἐνώπιον τοῦ κυρίου καὶ ὑψώσει ὑμᾶς.
  - `THGNT`: ταπεινώθητε ἐνώπιον κυρίου καὶ ὑψώσει ὑμᾶς.
  - `WH1881`: ταπεινώθητε ἐνώπιον Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `Tisch8`: ταπεινώθητε ἐνώπιον κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `TCGNT (Byz)`: ταπεινώθητε ἐνώπιον τοῦ Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `PT1904 (Byz)`: ταπεινώθητε ἐνώπιον τοῦ Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `TR-Scrivener (1894)`: ταπεινώθητε ἐνώπιον τοῦ Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `TR-Boyd (Elz/Scr/Steph)`: Ταπεινώθητε ἐνώπιον τοῦ Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `TR-Stephanus (1550)`: ταπεινώθητε ἐνώπιον τοῦ Κυρίου, καὶ ὑψώσει ὑμᾶς.
  - `TR-Elzevir (1624)`: ταπεινωθητε ενωπιον του κυριου και υψωσει υμας
  - `A (02)`: ταπινωθητε ενωπιον κυ̅ και υψωσει υμασ
  - `33`: ταπεινωθησεται ενωπιον κυ̅ και υψωσει υμας
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ταπεινώθητε' [B (03), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, Nestle1904, BHP] (weight 5.97, confidence 99%) over ταπινωθητε ουν (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over τοῦ (RP2018 (Byz), TR (KJTR)). Also normalised 5 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 11 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `SRGNT`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. Ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ, καταλαλεῖ νόμου καὶ κρίνει νόμον. Εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `SBLGNT`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `BHP`: μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ, καταλαλεῖ νόμου καὶ κρίνει νόμον. εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `Nestle1904`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `RP2018 (Byz)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. Ὁ καταλαλῶν ἀδελφοῦ, καὶ κρίνων τὸν ἀδελφὸν αὐτοῦ, καταλαλεῖ νόμου, καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `TR (KJTR)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. Ὁ καταλαλῶν ἀδελφοῦ, καὶ κρίνων τὸν ἀδελφὸν αὐτοῦ, καταλαλεῖ νόμου, καὶ κρίνει νόμον: εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `B (03)`: μη καταλαλειτε αλληλων αδελφοι ο καταλαλων αδελφου η κρεινων τον αδελφον αυτου καταλαλει νομου και κρεινει νομον ει δε νομον κρεινεισ ουκ ει ποιητησ νομου αλλα κριτησ
  - `א (01)`: μη καταλαλειται αλληλων αδελφοι ο καταλαλων αδελφου η κρινων τον αδελφον αυτου καταλαλει νομου και κρινι νομον ει δε νομον κρινισ ουκ ει ποιητησ νομου αλλα κριτησ
  - `NA28 (TAGNT)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `THGNT`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `WH1881`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `Tisch8`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ ἢ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `TCGNT (Byz)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. ὁ καταλαλῶν ἀδελφοῦ καὶ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου ἀλλὰ κριτής.
  - `PT1904 (Byz)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. ὁ καταλαλῶν ἀδελφοῦ καὶ κρίνων τὸν ἀδελφὸν αὐτοῦ καταλαλεῖ νόμου καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `TR-Scrivener (1894)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. ὁ καταλαλῶν ἀδελφοῦ, καὶ κρίνων τὸν ἀδελφὸν αὐτοῦ, καταλαλεῖ νόμου, καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `TR-Boyd (Elz/Scr/Steph)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί. Ὁ καταλαλῶν ἀδελφοῦ, καὶ κρίνων τὸν ἀδελφὸν αὐτοῦ, καταλαλεῖ νόμου, καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `TR-Stephanus (1550)`: Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί· ὁ καταλαλῶν ἀδελφοῦ, καὶ κρίνων τὸν ἀδελφὸν αὑτοῦ, καταλαλεῖ νόμου, καὶ κρίνει νόμον· εἰ δὲ νόμον κρίνεις, οὐκ εἶ ποιητὴς νόμου, ἀλλὰ κριτής.
  - `TR-Elzevir (1624)`: μη καταλαλειτε αλληλων αδελφοι ο καταλαλων αδελφου και κρινων τον αδελφον αυτου καταλαλει νομου και κρινει νομον ει δε νομον κρινεις ουκ ει ποιητης νομου αλλα κριτης
  - `A (02)`: μη καταλαλειτε αδελφοι μου αλληλων ο καταλαλων αδελφου η κρινων τον αδελφον αυτου καταλαλει νομου και κρινει νομον η δε νομον κρινεισ ουκ ει ποιητησ νομου αλλα κριτησ
  - `33`: μη καταλαληται αδελφοι μου αλληλων […] καταλαλων αδελφου η κρινων τον αδελφον αυτου καταλαλει νομου και κρινει νομον ει δε […] κρινεις ουκ ει ποιητης νομου αλλα κριτης
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'καταλαλεῖτε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over καταλαλειται (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἢ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over καὶ (RP2018 (Byz), TR (KJTR)). Also normalised 25 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 12 (Confidence: `93.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἷς ἐστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `SRGNT`: Εἷς ἐστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι. Σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `SBLGNT`: εἷς ἐστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `BHP`: εἷς ἐστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι. σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `Nestle1904`: εἷς ἐστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `RP2018 (Byz)`: Εἷς ἐστὶν ὁ νομοθέτης, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `TR (KJTR)`: Εἷς ἐστιν ὁ νομοθέτης, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι: σὺ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `B (03)`: εισ εστιν νομοθετησ και κριτησ ο δυναμενοσ σωσαι και απολεσαι συ δε τισ ει ο κρεινων τον πλησιον
  - `א (01)`: εισ εστιν ο νομοθετησ και κριτησ ο δυναμενοσ σωσαι και απολεσαι συ δε τισ ει ο κρινων τον πλησιον
  - `NA28 (TAGNT)`: εἷς ἐστιν ὁ νομοθέτης καὶ κριτὴς ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ ὁ κρίνων τὸν πλησίον;
  - `THGNT`: εἷς ἐστιν ὁ νομοθέτης καὶ κριτὴς ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ ὁ κρίνων τὸν πλησίον;
  - `WH1881`: εἷς ἔστιν νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `Tisch8`: εἷς ἐστιν ὁ νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ, ὁ κρίνων τὸν πλησίον;
  - `TCGNT (Byz)`: εἷς ἐστιν ὁ νομοθέτης, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `PT1904 (Byz)`: εἷς ἐστιν ὁ νομοθέτης καὶ κριτής, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ δὲ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `TR-Scrivener (1894)`: εἷς ἐστιν ὁ νομοθέτης, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `TR-Boyd (Elz/Scr/Steph)`: Εἷς ἐστὶν ὁ νομοθέτης, ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι· σὺ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `TR-Stephanus (1550)`: εἷς ἐστιν ὁ νομοθέτης ὁ δυνάμενος σῶσαι καὶ ἀπολέσαι. σὺ τίς εἶ ὃς κρίνεις τὸν ἕτερον;
  - `TR-Elzevir (1624)`: εις εστιν ο νομοθετης ο δυναμενος σωσαι και απολεσαι συ τις ει ος κρινεις τον ετερον
  - `A (02)`: εισ εστιν ο νομοθετησ και κριτησ δυναμενοσ σωσαι και απολεσαι συ δε τισ … ο κρινων τον πλησιον
  - `33`: εις εστιν ο νομοθετης και κριτης ο δυναμενος σωσαι και απολεσαι συ δε τις ει ο κρινων τον πλησιον
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.77, confidence 98%) over ὁ (א (01), RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'καὶ κριτής' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'δὲ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over om. (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ὁ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ὃς (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'κρίνων' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, B (03)] (weight 5.61, confidence 99%) over κρίνεις (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'πλησίον' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἕτερον (RP2018 (Byz), TR (KJTR)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 93% = product of 6 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 13 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἄγε νῦν οἱ λέγοντες· Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `SRGNT`: Ἄγε νῦν, οἱ λέγοντες, “Σήμερον ἢ αὔριον, πορευσόμεθα εἰς τήνδε τὴν πόλιν, καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν, καὶ ἐμπορευσόμεθα, καὶ κερδήσομεν.”
  - `SBLGNT`: Ἄγε νῦν οἱ λέγοντες· Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `BHP`: ἄγε νῦν, οἱ λέγοντες, “σήμερον ἢ αὔριον, πορευσόμεθα εἰς τήνδε τὴν πόλιν, καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν, καὶ ἐμπορευσόμεθα, καὶ κερδήσομεν.”
  - `Nestle1904`: Ἄγε νῦν οἱ λέγοντες Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `RP2018 (Byz)`: Ἄγε νῦν οἱ λέγοντες, Σήμερον καὶ αὔριον πορευσώμεθα εἰς τήνδε τὴν πόλιν, καὶ ποιήσωμεν ἐκεῖ ἐνιαυτὸν ἕνα, καὶ ἐμπορευσώμεθα, καὶ κερδήσωμεν·
  - `TR (KJTR)`: Ἄγε νῦν, οἱ λέγοντες, Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τήν πόλιν, καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν ἕνα, καὶ ἐμπορευσόμεθα καὶ κερδήσομεν:
  - `B (03)`: αγε νυν οι λεγοντεσ σημερον η αυριον πορευσομεθα εισ τηνδε την πολιν και ποιησομεν εκει ενιαυτον και εμπορευσομεθα και κερδησομεν
  - `א (01)`: αγε νυν οι λεγοντεσ σημερον η αυριον πορευσομεθα εισ τηνδε την πολιν και ποιησωμεν εκει ενιαυτον και εμπορευσομεθα και κερδησομεν
  - `NA28 (TAGNT)`: Ἄγε νῦν οἱ λέγοντες· σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `THGNT`: Ἄγε νῦν οἱ λέγοντες· σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `WH1881`: Ἄγε νῦν οἱ λέγοντες Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `Tisch8`: Ἄγε νῦν οἱ λέγοντες, σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `TCGNT (Byz)`: Ἄγε νῦν οἱ λέγοντες, Σήμερον καὶ αὔριον πορευσώμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσωμεν ἐκεῖ ἐνιαυτὸν ἕνα καὶ ἐμπορευσώμεθα καὶ κερδήσωμεν,
  - `PT1904 (Byz)`: Ἄγε νῦν οἱ λέγοντες· σήμερον καὶ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν ἕνα καὶ ἐμπορευσόμεθα καὶ κερδήσομεν·
  - `TR-Scrivener (1894)`: Ἄγε νῦν οἱ λέγοντες, Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν, καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν ἕνα, καὶ ἐμπορευσόμεθα, καὶ κερδήσομεν·
  - `TR-Boyd (Elz/Scr/Steph)`: Ἄγε νῦν οἱ λέγοντες, Σήμερον ἢ αὔριον πορευσόμεθα εἰς τήνδε τὴν πόλιν, καὶ ποιήσομεν ἐκεῖ ἐνιαυτὸν ἕνα, καὶ ἐμπορευσόμεθα, καὶ κερδήσομεν·
  - `TR-Stephanus (1550)`: Ἄγε νῦν οἱ λέγοντες, Σήμερον καὶ αὔριον πορευσώμεθα εἰς τήνδε τὴν πόλιν, καὶ ποιήσωμεν ἐκεῖ ἐνιαυτὸν ἕνα, καὶ ἐμπορευσώμεθα, καὶ κερδήσωμεν·
  - `TR-Elzevir (1624)`: αγε νυν οι λεγοντες σημερον η αυριον πορευσομεθα εις τηνδε την πολιν και ποιησομεν εκει ενιαυτον ενα και εμπορευσομεθα και κερδησομεν
  - `A (02)`: αγε νυν οι λεγοντεσ σημερον και αυριον πορευσωμεθα εισ τηνδε την πολιν και ποιησωμεν ενιαυτον ενα και εμπορευσομεθα και κερδησομεν
  - `33`: αγε νυν οι λεγοντες σημερον η […] πορευσωμεθα εις τηνδε την πολιν και ποιησωμεν ενιαυτον ενα και […] […] […]
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ἢ αὔριον πορευσόμεθα' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over καὶ αὔριον πορευσώμεθα (RP2018 (Byz)). [Lexical, morphological, or word-order variant] Adopted 'ποιήσομεν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 5.25, confidence 99%) over ποιήσωμεν (א (01), RP2018 (Byz)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἕνα (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'ἐμπορευσόμεθα καὶ κερδήσομεν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over ἐμπορευσώμεθα καὶ κερδήσωμεν (RP2018 (Byz)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 14 (Confidence: `64.5%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον ποία ἡ ζωὴ ὑμῶν· ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη·
  - `SRGNT`: Οἵτινες οὐκ ἐπίστασθε τῆς αὔριον, ποία γὰρ ζωὴ ὑμῶν; Ἀτμὶς γάρ ἐστε, ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη.
  - `SBLGNT`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον ποία ἡ ζωὴ ὑμῶν· ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη·
  - `BHP`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον, ποία ἡ ζωὴ ὑμῶν; ἀτμὶς γάρ ἐστε, ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη.
  - `Nestle1904`: οἵτινες οὐκ ἐπίστασθε τῆς αὔριον ποία ἡ ζωὴ ὑμῶν· ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη·
  - `RP2018 (Byz)`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον. Ποία γὰρ ἡ ζωὴ ὑμῶν; Ἀτμὶς γὰρ ἔσται ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ καὶ ἀφανιζομένη.
  - `TR (KJTR)`: Οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον. Ποία γὰρ ἡ ζωὴ ὑμῶν; Ἀτμὶς γάρ ἐστιν, ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ ἀφανιζομένη.
  - `B (03)`: οιτινεσ ουκ επιστασθε τησ αυριον ποια ζωη υμων ατμεισ γαρ εστε προσ ολιγον φαινομενη επειτα και αφανιζομενη
  - `א (01)`: οιτινεσ ουκ επιστασθε το τησ αυριον ποια η ζωη υμων η προσ ολιγον φαινομενη επειτα και αφανιζομενη
  - `NA28 (TAGNT)`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον ποία ἡ ζωὴ ὑμῶν. ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη ἔπειτα καὶ ἀφανιζομένη·
  - `THGNT`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον ποία ἡ ζωὴ ὑμῶν. ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη ἔπειτα καὶ ἀφανιζομένη·
  - `WH1881`: οἵτινες οὐκ ἐπίστασθε τῆς αὔριον ποία ἡ ζωὴ ὑμῶν· ἀτμὶς γάρ ἐστε πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη·
  - `Tisch8`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον ποία γὰρ ἡ ζωὴ ὑμῶν. ἀτμὶς γάρ ἐστε ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα καὶ ἀφανιζομένη·
  - `TCGNT (Byz)`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον—ποία γὰρ ἡ ζωὴ ὑμῶν; ἀτμὶς γὰρ ἔσται ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ καὶ ἀφανιζομένη—
  - `PT1904 (Byz)`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον· ποία γὰρ ἡ ζωὴ ὑμῶν; ἀτμὶς γάρ ἔσται ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ καὶ ἀφανιζομένη·
  - `TR-Scrivener (1894)`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον. ποία γὰρ ἡ ζωὴ ὑμῶν; ἀτμὶς γάρ ἐστιν ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ ἀφανιζομένη.
  - `TR-Boyd (Elz/Scr/Steph)`: οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον. Ποία γὰρ ἡ ζωὴ ὑμῶν; Ἀτμὶς γάρ ἐστιν ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ ἀφανιζομένη.
  - `TR-Stephanus (1550)`: (οἵτινες οὐκ ἐπίστασθε τὸ τῆς αὔριον· ποία γὰρ ἡ ζωὴ ὑμῶν; ἀτμὶς γάρ ἐστιν ἡ πρὸς ὀλίγον φαινομένη, ἔπειτα δὲ ἀφανιζομένη·)
  - `TR-Elzevir (1624)`: οιτινες ουκ επιστασθε το της αυριον ποια γαρ η ζωη υμων ατμις γαρ εστιν η προς ολιγον φαινομενη επειτα δε αφανιζομενη
  - `A (02)`: οιτεινεσ ουκ επιστασθε τα τησ αυριον ποια γαρ η ζωη υμων ατμισ εσται η προσ ολιγον φαινομενη επειτα και αφανιζομενη
  - `33`: […] ουκ επιστασθε τα της αυριον ποια γαρ η ζωη ημων ατμης εστιν η προς ολιγον φαινομενη επιτα δε και αφανιζομενη
- **Philological Rationale:** [Omission in some witnesses] Adopted 'τὸ' [א (01), SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.10, confidence 70%) over om. (B (03), SRGNT, Nestle1904). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over γὰρ (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'ἡ' [א (01), SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.00, confidence 98%) over om. (B (03)); γὰρ (SRGNT). [Omission in some witnesses] Adopted 'ἀτμὶς' [SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, Nestle1904, BHP, B (03)] (weight 5.97, confidence 99%) over om. (א (01)). [Omission in some witnesses] Adopted 'γάρ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR), RP2018 (Byz)] (weight 5.97, confidence 99%) over om. (א (01)). [Omission in some witnesses] Adopted 'ἐστε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over om. (א (01)); ἔσται (RP2018 (Byz)); ἐστιν (TR (KJTR)). [Omission in some witnesses] Adopted 'ἡ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.33, confidence 99%) over δὲ (RP2018 (Byz)). [Lexical, morphological, or word-order variant] Adopted 'καὶ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over δὲ (TR (KJTR)). Also normalised 14 orthographic/surface variation(s).
- *confidence:* Verse confidence 64% = product of 9 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 15 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἀντὶ τοῦ λέγειν ὑμᾶς· Ἐὰν ὁ κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `SRGNT`: Ἀντὶ τοῦ λέγειν ὑμᾶς, “Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν, τοῦτο ἢ ἐκεῖνο.”
  - `SBLGNT`: ἀντὶ τοῦ λέγειν ὑμᾶς· Ἐὰν ὁ κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `BHP`: ἀντὶ τοῦ λέγειν ὑμᾶς, “ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν, τοῦτο ἢ ἐκεῖνο.”
  - `Nestle1904`: ἀντὶ τοῦ λέγειν ὑμᾶς Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `RP2018 (Byz)`: Ἀντὶ τοῦ λέγειν ὑμᾶς, Ἐὰν ὁ κύριος θελήσῃ, καὶ ζήσωμεν, καὶ ποιήσωμεν τοῦτο ἢ ἐκεῖνο.
  - `TR (KJTR)`: Ἀντὶ τοῦ λέγειν ὑμᾶς, Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσομεν, καὶ ποιήσομεν τοῦτο, ἢ ἐκεῖνο.
  - `B (03)`: αντι του λεγειν υμασ εαν ο κσ̅ θελη και ζησομεν και ποιησομεν τουτο η εκεινο
  - `א (01)`: αντι του λεγιν υμασ εαν ο κσ̅ θεληση και ζησομεν και ποιησομεν τουτο η εκινο
  - `NA28 (TAGNT)`: ἀντὶ τοῦ λέγειν ὑμᾶς· ἐὰν ὁ κύριος θελήσῃ καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `THGNT`: ἀντὶ τοῦ λέγειν ὑμᾶς· ἐὰν ὁ κύριος θελήσῃ καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `WH1881`: ἀντὶ τοῦ λέγειν ὑμᾶς Ἐὰν ὁ κύριος θέλῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `Tisch8`: ἀντὶ τοῦ λέγειν ὑμᾶς· ἐὰν ὁ κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `TCGNT (Byz)`: ἀντὶ τοῦ λέγειν ὑμᾶς, Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσωμεν καὶ ποιήσωμεν τοῦτο ἢ ἐκεῖνο.
  - `PT1904 (Byz)`: ἀντὶ τοῦ λέγειν ὑμᾶς, ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσομεν καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `TR-Scrivener (1894)`: ἀντὶ τοῦ λέγειν ὑμᾶς, Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσομεν, καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀντὶ τοῦ λέγειν ὑμᾶς, Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσωμεν, καὶ ποιήσομεν τοῦτο ἢ ἐκεῖνο.
  - `TR-Stephanus (1550)`: ἀντὶ τοῦ λέγειν ὑμᾶς, Ἐὰν ὁ Κύριος θελήσῃ, καὶ ζήσωμεν, καὶ ποιήσωμεν τοῦτο ἢ ἐκεῖνο.
  - `TR-Elzevir (1624)`: αντι του λεγειν υμας εαν ο κυριος θεληση και ζησωμεν και ποιησομεν τουτο η εκεινο
  - `A (02)`: αντι του λεγειν υμασ εαν ο κσ̅ θεληση και ζησομεν και ποιησομεν τουτο η κεινο
  - `33`: αντι του λεγειν υμας εαν ο κς̅ θελη και ζησωμεν και ποιησωμεν τουτο η εκεινο
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'θελήσῃ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over θελη (B (03)). [Variation unit spanning several words] Adopted 'ζήσομεν καὶ ποιήσομεν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over ζήσωμεν καὶ ποιήσωμεν (RP2018 (Byz)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 16 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `SRGNT`: Νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν. Πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `SBLGNT`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `BHP`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονίαις ὑμῶν. πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `Nestle1904`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονίαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `RP2018 (Byz)`: Νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `TR (KJTR)`: Νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν: πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `B (03)`: νυν δε καυχασθε εν ταισ αλαζονιαισ υμων πασα καυχησισ τοιαυτη πονηρα εστιν
  - `א (01)`: νυν δε κατακαυχασθε εν ταισ αλαζονιαισ υμων απασα καυχησεισ τοιαυτη πονηρα εστιν
  - `NA28 (TAGNT)`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `THGNT`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονίαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `WH1881`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονίαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `Tisch8`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονίαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `TCGNT (Byz)`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `PT1904 (Byz)`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `TR-Scrivener (1894)`: νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `TR-Boyd (Elz/Scr/Steph)`: Νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν· πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `TR-Stephanus (1550)`: Νῦν δὲ καυχᾶσθε ἐν ταῖς ἀλαζονείαις ὑμῶν. πᾶσα καύχησις τοιαύτη πονηρά ἐστιν.
  - `TR-Elzevir (1624)`: νυν δε καυχασθε εν ταις αλαζονειαις υμων πασα καυχησις τοιαυτη πονηρα εστιν
  - `A (02)`: νυν δε καυχασθε εν ταισ αλαζονιαισ υμων πασα καυχησεισ τοιαυτη πονηρα εστιν
  - `33`: νυν δε καυχασθε εν ταις […] […] πασα καυχισις τοιαυτη πονηρα εστιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'καυχᾶσθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over κατακαυχασθε (א (01)). [Lexical, morphological, or word-order variant] Adopted 'πᾶσα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απασα (א (01)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 17 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `SRGNT`: Εἰδότι οὖν καλὸν ποιεῖν, καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `SBLGNT`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `BHP`: εἰδότι οὖν καλὸν ποιεῖν, καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `Nestle1904`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `RP2018 (Byz)`: Εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστίν.
  - `TR (KJTR)`: Εἰδότι οὖν καλὸν ποιεῖν, καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `B (03)`: ειδοτι ουν καλον ποιειν και μη ποιουντι αμαρτια αυτω εστιν
  - `א (01)`: ειδοτι ουν καλον ποιειν και μη ποιουντι αμαρτια αυτω εστιν
  - `NA28 (TAGNT)`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `THGNT`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `WH1881`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστίν.
  - `Tisch8`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `TCGNT (Byz)`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `PT1904 (Byz)`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `TR-Scrivener (1894)`: εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστίν.
  - `TR-Boyd (Elz/Scr/Steph)`: Εἰδότι οὖν καλὸν ποιεῖν καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστίν.
  - `TR-Stephanus (1550)`: εἰδότι οὖν καλὸν ποιεῖν, καὶ μὴ ποιοῦντι, ἁμαρτία αὐτῷ ἐστιν.
  - `TR-Elzevir (1624)`: ειδοτι ουν καλον ποιειν και μη ποιουντι αμαρτια αυτω εστιν
  - `A (02)`: ειδοτι ουν καλον ποιησαι και μη ποιουντι αμαρτια αυτω εστιν
  - `33`: ειδοτι ουν καλον ποιειν και μη ποιουντη […] […] εστιν
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 10 surface variation(s) (Accent or breathing differs between accented editions (editorial interpretation); Accentuation / capitalisation / breathing convention).
