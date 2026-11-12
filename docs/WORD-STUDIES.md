# Highlighted Word and Phrase Studies

**Version 1.0 · 12 November 2026 · Proposed expansion of existing popups**

Companion to the [translation roadmap](../ROADMAP.md) and [standard](../TRANSLATION-STANDARD.md). The owner requested this workstream specifically, using James 2:24 as the pilot. This document plans content and behaviour; it does not claim that new popups have been installed.

## 1. Reader outcome

When a reader opens a highlighted word or phrase, explain **what the Greek says here, why Saints renders it this way, what other renderings are defensible, and where theological interpretation begins**. Give a short answer first, with deeper evidence available on request.

Expand the existing highlighted-text studies and their records. Inventory the current storage, popup renderer, stable IDs and lexicon links before implementing an adapter. Reuse suitable records; preserve earlier notes with dates and review qualifications. Avoid creating a second competing dictionary or popup system.

## 2. A consistent study card

| Layer | What the reader sees | Editorial requirement |
| --- | --- | --- |
| **At a glance** | Highlighted Saints wording, verse and a concise contextual explanation. | An explanation of this occurrence, not a pasted list of every possible meaning. |
| **Greek word or phrase** | Actual inflected form, readable transliteration, lemma and a plain-language grammatical explanation. | Match the declared edition; distinguish the form in the verse from the dictionary headword. |
| **Why this wording** | Why the current English was chosen; a note when the wording remains provisional. | Traceable to the translation decision and exact edition snapshot. |
| **Other renderings** | A small table of genuinely relevant alternatives and the differences they introduce. | Label direct rendering, explanatory paraphrase and interpretive reading separately. Do not imply that every gloss is interchangeable. |
| **In this passage** | Clause relationships, speaker, audience and relevant surrounding verses. | Include meaningful qualifiers and phrase boundaries; avoid isolating one word from its argument. |
| **Elsewhere in Scripture** | Selected same-lemma occurrences and relevant passages, with their relation labelled. | Same lemma does not prove identical meaning. Distinguish a quotation, shared construction and thematic connection. |
| **Interpretation and reception** | Attributed interpretations where the issue warrants them. | Separate lexical observations from claims about salvation, sacraments, judgment or other theological questions. Cite the actual interpreter or document. |
| **Sources and review** | Edition, precise lexicon/grammar/source references, revision date and review state. | Name only resources actually consulted and the scope actually checked. |

Keep the initial summary compact; use expandable sections for technical material. Offer a stable link to the full study and a route back to the original verse. Reader-facing language should explain uncertainty plainly without exposing internal data fields.

## 3. James 2:24 pilot

### Evidence baseline

The archived [James reading edition](../james/James.html) reads “is justified” and already contains a historical note retaining the verb while leaving interpretation review outstanding. Its inheritance is evidence to assess, not a reason to discard it or claim a new independent review.

The publisher's [NA28 James 2](https://www.die-bibel.de/en/bible/NA28/JAS.2) displays **δικαιοῦται**, transliterated **dikaioutai**, from **δικαιόω** (*dikaioō*). Analyse it here as present passive indicative, third person singular: the subject is a person. A preliminary lexical reference is [Middle Liddell, δικαιόω, hosted by Perseus](https://atlas.perseus.tufts.edu/dictionaries/entry/urn:cite2:scaife-viewer:dictionary-entries.atlas_v1:middle-liddell.perseus-eng2-n8418/), which includes the NT senses of deeming righteous and justifying. This general historical lexicon is a starting reference; a completed NT study should also document consultation of a suitable specialist lexicon and the passage's syntax.

### Proposed concise card — editorial draft

> **Justified — δικαιοῦται (dikaioutai)**  
> “Is justified” can be explained as “is declared righteous.” Some interpreters understand the emphasis here as being shown or vindicated as righteous. That is a contextual interpretation to evaluate, not an automatic replacement gloss. James connects faith and works in this passage; the verb alone does not settle how that relationship fits a complete doctrine of salvation.

### Alternative-rendering table

| Wording | Role in this pilot | What needs explanation |
| --- | --- | --- |
| **Is justified** | Existing Saints wording; retained during planning. | Concise and traditional, but readers may bring differing technical definitions to it. |
| **Is declared righteous** | Explanatory rendering to assess against context and specialist lexical evidence. | Makes a declarative sense explicit; it does not by itself establish a particular theological system. |
| **Is shown to be righteous / is vindicated** | Interpretive alternative to examine, not an equally certain replacement asserted by this plan. | Explain the argument for this reading and its limitations rather than presenting it as the only literal meaning. |
| **Declared righteousness** | Correct the expression before publication. | “Righteous” describes the person; “righteousness” is a noun. It is not the appropriate substitute in this sentence. |

The phrase-level study must also address **ἐξ ἔργων** and **οὐκ ἐκ πίστεως μόνον**. The popup must preserve the force of works and the explicit qualification about faith alone. It should not silently add “before people,” change the verb to “saved,” or remove the difficult wording to reconcile James with another passage.

Link James 2:14–26 and relevant comparison passages, beginning with Romans 3:21–31; verify each relation and destination before publishing. A full theological comparison remains a separate, sourced task. The form's present tense alone does not prove a theory of continuing or repeated justification.

### Interpretation comparison policy

Explain disagreements fairly through named sources, not broad unsupported labels such as “all Protestants believe” or “the Orthodox meaning.” Where relevant, compare an identified Protestant confession/commentary, a Catholic source and an Orthodox source, together with relevant early Christian interpretation. Record differences within traditions when material.

Do not publish this comparison until the actual sources have been read and the summaries checked. Keep three questions visible:

1. What meanings and grammatical relationships does the Greek support?
2. What does this author appear to be arguing in this passage?
3. How does a named interpreter connect it with wider theology?

An English alternative does not automatically belong to one denomination. A dictionary entry alone does not decide all three questions.

## 4. Highlight colours and study availability

Preserve the established seven thematic categories and confirm their live labels during the inventory. The current planning baseline is Red (Father, identity, relationships, creation), Orange (revelation, communication, calling, action), Yellow (holiness, worship, honor), Green (Christ, life, growth, understanding), Blue (covenant, instruction, truth, order), Indigo (sin, judgment, opposition, separation), and Violet (Holy Spirit, grace, gifts, care).

A colour marks an editorial theme, not a fixed Greek sense or a doctrinal verdict. Record why the span has that theme and how overlaps were handled. The same lemma may receive different contextual themes or no colour. Never choose an English translation to make it fit a colour, and never force seven colours onto a chapter without textual support.

Keep word-study access available when thematic colours are turned off, through a clearly labelled study control or another accessible marker. A meaningful uncoloured word can still have a study. Distinguish editorial highlights from the user's personal highlighting.

## 5. Data and translation integration

Use two linked records:

- **Lemma entry:** general lexical range, spelling/transliteration, sources and links to occurrences.
- **Occurrence or phrase study:** exact passage, source edition, inflected forms, token/span alignment, chosen sense, current Saints text, alternatives, contextual argument and review status.

A phrase can involve several lemmas, and a Greek construction can map to non-contiguous English wording. Support overlapping phrase studies without nested interactive controls. Use a stable composite passage identity because verse anchors such as `v1-1` may repeat in separate reading sections.

The [word-study template](../templates/word-study.json) records publication state, source references, evidence, theological interpretations, thematic categories and the exact text revision. It does not prescribe a replacement database schema before the existing implementation is inspected.

When a verse changes:

1. Identify every attached popup, glossary citation and phrase span.
2. Compare the study's recorded English and source edition with the new snapshot.
3. Re-anchor and review affected studies; flag unresolved mismatches as stale.
4. Prevent stale text-specific claims from being presented as reviewed current notes.
5. Rebuild relevant search/offline outputs and verify the actual display.

Do not attach studies by global English string replacement. Identical English words may represent different Greek forms or senses.

## 6. Delivery sequence

| Batch | Deliverable | Acceptance |
| --- | --- | --- |
| **WS-001 — Inventory** | Map existing highlighted studies, storage, rendering, labels, source notices, IDs and export/offline behaviour. | Coverage denominator and owners are known; previous records preserved; missing evidence is labelled. |
| **WS-002 — James pilot** | Draft the word and phrase studies for James 2:24, with surrounding-context links and a separate interpretation layer. | Greek form and grammar checked; alternatives classified; factual/theological claims cited; no unsupported replacement of Scripture. |
| **WS-003 — Representative set** | Select 10–20 occurrences covering spirit/breath, faith/faithfulness, justify, righteousness, covenant, law, servant/slave and angel/messenger across OT and NT. | Evidence and usability checked for each selected occurrence; selection count is not a completed-work claim. |
| **WS-004 — Staging integration** | Adapt the existing popup system to the reviewed records and exact text revisions. | Keyboard, touch, screen reader, narrow-screen, both-theme, colours-off and offline tests pass for the pilot. |
| **WS-005 — Book-by-book expansion** | Add and review studies alongside each translation batch. Prioritize ambiguities, technical words, important phrases and misleading familiar glosses. | A chapter coverage report distinguishes existing, drafted, source checked, independently reviewed, stale and published studies. |

Coordinate WS-002 with GT-005, while allowing James to be the first popup pilot at the owner's request. Popup work does not imply that the whole James translation has completed its new review cycle.

## 7. Interaction and release checks

Use click/tap and keyboard activation; hover may preview but cannot be the only route. Choose a consistent accessible popover/dialog pattern, with clear title, close action, Escape behaviour, appropriate focus management and return to the invoking word. Keep text selectable and preserve normal reading/copying. On phones, use a panel that fits the viewport and does not cover the passage without a clear return.

A non-interactive or no-script fallback should still expose the study link. Label available offline study content and its revision; do not make a network-only source appear cached.

Before release, check:

- Correct verse, Greek form, edition and English span; no reference collisions.
- Exact source links and correctly mapped Saints passage destinations.
- Grammar explained without overstating what morphology proves.
- Contextual alternatives separated from theological conclusions.
- Named primary sources for attributed theological positions.
- Theme labels understandable without colour alone; accessible contrast and focus.
- Existing personal notes, highlights and stable URLs preserved.
- Popup text and Scripture remain separate in copying, search and exports.
- Coverage and review labels match evidence; unreviewed drafts remain unreviewed.

**Completion means:** a reader can understand the selected wording, inspect a reasonable alternative, identify the evidence and distinguish the translator's decision from theological interpretation.
