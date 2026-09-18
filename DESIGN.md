# Eric Presentation Design System v1.2

Status: Canonical  
Language: zh-Hant first, bilingual editorial support  
Reference implementation: `AI_Playbook_DesignSystem_v1.1.html`

---

# 0. Rule Priority

When rules conflict, use this priority order:

1. **Contract**
2. **Canon**
3. **Pattern-specific rules**
4. **Language defaults**
5. **Critique suggestions**

Higher layers override lower layers.

A model or generator MUST NOT proceed to composition until the Contract is complete.

---

# 1. CONTRACT

The Contract defines what the deck is for before any visual decision is made.

## 1.1 Required Deck Contract

```yaml
deck_id:
language: zh-Hant
audience:
  type:
  description:

goal:
  type: understand | decide | adopt | align | teach
  outcome:

core_message:

constraints:
  time_min:
  slide_count_max:
  technical_depth: low | mid | high

must_include: []
must_avoid: []

reference_deck:
  - AI_Playbook_DesignSystem_v1.1.html

energy_plan: []
forbidden_patterns: []
```

## 1.2 Contract Gate

**RULE**  
A complete Contract is required before composition.

**WHEN**  
All generated presentation decks.

**CHECK**  
If any of the following are missing, STOP before layout generation:

- audience
- goal.type
- goal.outcome
- core_message
- slide_count_max
- technical_depth

**SEVERITY**  
ERROR

---

## 1.3 Narrative Contract

Before slide generation, define:

- Context
- Tension
- Insight
- Solution
- Action

The deck may adapt this structure, but it must still have a clear narrative spine.

Every slide must have:

```yaml
slide:
  intent:
  takeaway:
  pattern:
  density: LOW | MEDIUM | HIGH
  energy: CALM | FOCUSED | BOLD
  visual_anchor:
  transition:
```

If `intent` or `takeaway` cannot be written clearly, the slide should be removed or redesigned.

---

# 2. CANON

Canon rules are non-negotiable unless explicitly overridden by the Contract.

## C01 — One Slide, One Idea

**RULE**  
Each slide communicates one primary idea.

**WHEN**  
All non-appendix slides.

**CHECK**  
If the slide requires two independent takeaway sentences joined by "and", "also", or separate conclusions, split it.

**SEVERITY**  
ERROR

---

## C02 — One Primary Visual Anchor

**RULE**  
Each slide has exactly one primary visual anchor.

**WHEN**  
All non-appendix slides.

**CHECK**  
Visual QA must identify what the eye sees first.  
If two or more elements have approximately equal visual weight, flag:

`S15_MULTIPLE_ANCHOR`

**SEVERITY**  
WARNING

---

## C03 — BODY Minimum Size

**RULE**  
BODY text must not be smaller than 15 pt equivalent.

**WHEN**  
Presentation-mode slides.

**CHECK**  
- PPTX: BODY < 15 pt → fail
- HTML: BODY below mapped equivalent → fail

Exceptions:
- source
- footnote
- caption
- code

**SEVERITY**  
ERROR

---

## C04 — Never Shrink to Solve Complexity

**RULE**  
Do not reduce type size or visual scale merely to make content fit.

**ACTION ORDER**

1. Simplify
2. Visualize
3. Split

**SEVERITY**  
ERROR if text is reduced below minimums.

---

## C05 — Titles Communicate Meaning

**RULE**  
Titles should communicate the slide's takeaway, not merely the topic.

Bad:
- 系統架構
- 現況分析
- 未來規劃

Preferred:
- Playbook 將一次性的探索轉換成可重複利用的組織經驗。

**CHECK**  
Semantic lint asks:

> If the audience reads only the title, do they understand what this slide wants them to believe or remember?

**SEVERITY**  
WARNING

---

## C06 — Relationship Before Container

**RULE**  
Before using boxes/cards, determine the information relationship.

Possible relationships:
- sequence
- cause/effect
- hierarchy
- contrast
- dependency
- loop
- input/output

Containers are not the default.

**SEVERITY**  
WARNING

---

## C07 — Decoration Requires Justification

**RULE**  
Every visual element must serve communication.

**CHECK**  
Ask:

> If this element is removed, does communication become weaker?

If no, it is decoration.

**SEVERITY**  
WARNING

---

## C08 — One Structural Accent

**RULE**  
Each slide may use at most one structural accent color.

Structural accent examples:
- key path
- key step
- accent rule
- key number
- highlighted statement

Semantic colors do NOT count as a second structural accent if their meaning is explicit.

Examples:
- red/coral = danger / failure / rejected path
- green = success / verified
- amber = warning
- blue = primary structural accent

**SEVERITY**  
WARNING

---

## C09 — No Repeated Composition > 2

**RULE**  
The same visual silhouette must not appear more than twice consecutively.

**CHECK**  
Pattern ID alone is insufficient.  
Compare composition silhouette:
- title position
- major visual block placement
- dominant axis
- number of major regions

**SEVERITY**  
ERROR

---

## C10 — Content Maximum

**RULE**  
Presentation slide content must not exceed 120 words.

Recommended:
- LOW: 20–40
- MEDIUM: 40–80
- HIGH: 80–120

**SEVERITY**  
ERROR

---

## C11 — Narrative Purpose

**RULE**  
Every slide must have an explicit narrative purpose.

**CHECK**  
Must complete:

> This slide exists to...

**SEVERITY**  
ERROR

---

## C12 — Evidence Must Have Context

**RULE**  
An isolated number is not evidence.

A number should answer at least one:

- Compared with what?
- Before vs after?
- Expected vs actual?
- Part vs whole?
- Rate vs baseline?
- Why does it matter?

**SEVERITY**  
WARNING

---

## C13 — Honesty Over Completeness

**RULE**  
Unverified information must not be visually presented with the same certainty as verified information.

Confidence states:

- ✅ 已驗證
- ⚠️ 推測
- ❓ 未知
- ⏳ 暫緩

**SEVERITY**  
ERROR if uncertainty is hidden.

---

## C14 — Visual Boldness Is Rhythmic, Not Constant

**RULE**  
Use bold composition selectively.

**TARGET**  
At least one BOLD slide every 3–5 slides.

**CHECK**  
If 5 consecutive slides contain no BOLD slide, raise warning.

**SEVERITY**  
WARNING

---

## C15 — BOLD Slides Must Be Earned

**RULE**  
A BOLD slide must use at least one defined Signature Motif and reinforce the takeaway.

**CHECK**  
If removing the bold gesture does not weaken communication, it is decoration.

**SEVERITY**  
WARNING

---

# 3. LANGUAGE

Language defines typography, color, composition, motifs, patterns, and editorial behavior.

# 3.1 Art Direction

Target:

- 70% Editorial Tech
- 30% Strategy Deck

The deck should feel:

- clear
- restrained
- narrative-driven
- technical when needed
- visually intentional
- editorially bold
- memorable without being decorative

Avoid:

- generic SaaS deck look
- excessive cards
- decorative gradients
- glassmorphism
- neon glow
- random blobs
- icon-heavy layouts
- corporate-template repetition

Core rule:

> Be bold in scale and composition, not in decoration.

---

# 3.2 Typography

## Font Families

Chinese:
- Noto Sans TC
- Source Han Sans TC

English:
- Inter

Code:
- JetBrains Mono (optional; CODE pattern only)

## Type Scale

PPTX canonical:

- DISPLAY: 40–48 pt
- H1: 30–34 pt
- H2: 20–24 pt
- BODY: 15–17 pt
- SMALL: 11–12 pt
- CODE: 12–14 pt

Big numbers are governed primarily by visual area, not a strict point-size ceiling.

---

# 3.3 Chinese Editorial Typesetting

## CT01 — Avoid Orphan Characters

Do not leave 1–2 Chinese characters alone on the final title line when avoidable.

Bad:

```text
下一個人，不必重走我走過的
彎路。
```

Preferred:

```text
下一個人，
不必重走我走過的彎路。
```

---

## CT02 — Keep Number + Unit Together

Avoid line breaks between:

- 300 / 月
- 2.9 秒
- 5.3 倍
- 15 pt

---

## CT03 — Avoid Punctuation at Line Start

Do not allow:

- ，
- 。
- ：
- ；
- ）
- 】

to begin a line where controllable.

---

## CT04 — Mixed Chinese / English Hierarchy

Default bilingual hierarchy:

- eyebrow: English / uppercase
- primary title: Traditional Chinese
- technical identifiers: original English
- micro labels: English allowed
- explanations: Traditional Chinese

Do not apply English letter-spacing rules to Chinese text.

---

## CT05 — Conclusion Titles Use Sentence Logic

Titles are written as conclusions, not directory labels.

Use punctuation only when it improves reading rhythm.

---

# 3.4 Color

## Core Tokens

```text
CANVAS       #F7F7F5
SURFACE      #FFFFFF
INK          #18181B
MUTED        #71717A
LINE         #E4E4E7
LINE_STRONG  #A1A1AA
ACCENT       #2563EB
ACCENT_LIGHT #60A5FA
```

## Semantic Tokens

```text
SUCCESS      #16A34A
WARNING      #D97706
DANGER       #D85B42
INFO         #2563EB
```

Note:
`DANGER` is aligned to the reference deck coral.

## Color Rules

- Neutral palette dominates.
- One structural accent per slide.
- Semantic colors require explicit meaning.
- Different item ≠ different color.
- Avoid rainbow diagrams.
- Avoid decorative gradients by default.

---

# 3.5 Implementation Mapping

The system supports both PPTX and Offline HTML.

## Canonical Slide Coordinate System

16:9  
13.333 × 7.5 in

## Safe Area

- Left: 0.65"
- Right: 0.65"
- Top: 0.55"
- Bottom: 0.50"

## HTML Mapping

For a normalized 7.5in-high reference canvas:

```text
1vh ≈ 0.075in ≈ 5.4pt
```

This is a design-equivalent mapping, not a browser physical-inch guarantee.

Use:
- PPTX → pt / in
- HTML → vh / vw

Both implementations must preserve relative scale and hierarchy.

---

# 3.6 Grid and Spacing

12-column grid.

Common splits:

- 6 + 6
- 8 + 4
- 5 + 7
- 4 + 4 + 4
- 3 + 6 + 3
- 2 + 8 + 2

Spacing scale:

- 0.10"
- 0.20"
- 0.30"
- 0.40"
- 0.60"
- 0.80"
- 1.20"

Grid is for alignment, not automatic boxes.

---

# 3.7 Chrome

Chrome means recurring presentation furniture.

## Eyebrow

Default format:

```text
NN · LABEL
```

Examples:

- 01 · POSITIONING
- 05 · EVIDENCE
- 10 · ADOPTION

Style:
- English
- uppercase
- muted
- semibold
- letter spacing allowed

Dark slide:
- use light muted token

## Footer

Optional.

Use for:
- deck identity
- source note
- small contextual label

Do not repeat redundant information.

## Progress / Nav

Allowed for Offline HTML.

Do not count browser controls as slide content.

---

# 3.8 Signature Motifs

Use at most one dominant motif per slide.

## M-A — Editorial Scale

Use one oversized statement or number.

Target visual area:
- 30–65%

Use when:
- statement
- key evidence
- decision
- hero

---

## M-B — Directional Rule

One strong line / arrow acts as structural spine.

Use for:
- before → after
- experience → playbook → next person
- process
- transformation
- data flow

---

## M-C — Cropped Geometry

Use 1–2 large flat geometric forms entering from the canvas edge.

Use for:
- hero
- section transition
- conceptual framing

Do not use decorative blobs.

---

## M-D — Evidence Split

Default:
- 65% evidence
- 35% interpretation

Avoid automatic 50/50.

---

## M-E — Full Visual

One visual dominates nearly the entire slide.

Use:
- screenshot
- diagram
- photo
- code excerpt

Text becomes annotation.

---

## M-F — Dark Narrative Break

Use for:
- insight
- contradiction
- decision
- closing

Target:
- 1–3 slides per deck

Warning:
- dark slides > 25% of deck

---

## M-G — Broken Symmetry

Use asymmetry to reflect unequal information hierarchy.

---

## M-H — Editorial Framing

Use:
- labels
- rules
- margins
- negative space

Prefer spacing over containers.

---

# 3.9 Visual Energy

Each slide has one energy level.

## CALM

Use:
- technical detail
- tables
- architecture detail
- supporting explanation

## FOCUSED

Default.

Use:
- process
- evidence
- contrast
- relationship

## BOLD

Use:
- hero
- key statement
- key evidence
- decision
- narrative break
- closing

Preferred deck rhythm:

```text
BOLD → FOCUSED → FOCUSED → CALM → BOLD
```

Not a hard sequence.

---

# 3.10 Number Rhetoric

Numbers are first-class visual elements.

## NR01 — Mega Number

Use when:
- one number is the main evidence
- the number changes the interpretation
- there is a meaningful baseline

Example:
- 5,523 vs 1,038
- 9,702 created, then removed

## NR02 — Metric Band

Use when:
- 3–5 metrics together describe system state

Example:
- 12,895 nodes
- 18,618 edges
- 10,756 links
- 300/month

## NR03 — Before / After

Use:
- 860 → 11,038
- 2.9 → 11.7 sec

Prefer directional notation when change matters.

## NR04 — No Orphan KPI

A big number with no comparison, interpretation, or consequence is not EVIDENCE.

---

# 3.11 Confidence Legend

Confidence states:

| State | Meaning | Visual treatment |
|---|---|---|
| ✅ 已驗證 | direct evidence | normal/high confidence |
| ⚠️ 推測 | inferred | warning semantic color |
| ❓ 未知 | cannot determine | muted / explicit unknown |
| ⏳ 暫緩 | not reviewed yet | muted / pending |

Unverified content must not visually dominate verified content unless the point of the slide is uncertainty itself.

---

# 3.12 Optional Components

## Icons

Lucide only.

Use only when:
- architecture
- code
- technical labels
- meaning is improved

Do not add icons merely to decorate cards.

## Code

JetBrains Mono.

Prefer:
- 5–15 relevant lines
- no full IDE screenshot unless the IDE context matters

## Cards

Default: avoid.

Use only when:
- semantic grouping is necessary
- boundary matters
- spacing alone cannot explain grouping

If required:

- Background: #FFFFFF
- Border: #E4E4E7
- Radius: 6–8 px
- Shadow: none

---

# 4. PATTERN LIBRARY

Patterns are communication functions, not fixed templates.

Each pattern includes:

- Use when
- Do not use when
- Default motif
- Density
- Reference

---

## P01 HERO

Use when:
- introducing core idea
- opening a deck

Do not use when:
- slide is merely a section header
- no meaningful thesis exists

Default motif:
- M-A Editorial Scale
- M-C Cropped Geometry

Density:
- LOW

Reference:
- Reference Deck Slide 01

---

## P02 STATEMENT

Use when:
- one insight must be remembered
- narrative reset is needed

Do not use when:
- multiple supporting arguments are needed

Default motif:
- M-A
- M-F

Density:
- LOW

Reference:
- Slide 05

---

## P03 PROBLEM

Use when:
- friction, contradiction, or hidden cost must be visible

Do not use when:
- content is only a list of issues without structure

Default motif:
- M-A
- M-G

Density:
- MEDIUM

Reference:
- Slide 03

---

## P04 CONTRAST

Use when:
- before/after
- old/new
- A/B
- wrong/right

Do not use when:
- sides are not meaningfully comparable
- 50/50 would imply false equality

Default motif:
- M-D
- M-G

Density:
- MEDIUM

Reference:
- Slide 02

---

## P05 PROCESS

Use when:
- sequence matters
- transformation matters

Do not use when:
- items are merely related but unordered

Default motif:
- M-B

Density:
- MEDIUM

Reference:
- Slide 04

---

## P06 RELATIONSHIP

Use when:
- explaining conceptual relationships
- cause/effect
- dependency
- hierarchy

Do not use when:
- a process would be clearer

Density:
- MEDIUM

Reference:
- not primary in reference deck; use Architecture rules

---

## P07 ARCHITECTURE

Use when:
- system structure and flow matter

Do not use when:
- the audience only needs one conceptual relationship

Rules:
- one dominant flow direction
- boundaries visible
- progressive disclosure
- 7 ± 2 primary nodes recommended

Density:
- HIGH

---

## P08 EVIDENCE

Use when:
- data supports or overturns a claim

Do not use when:
- only an isolated KPI exists with no "so what"

Default motif:
- M-A
- M-D

Density:
- MEDIUM

Reference:
- Slide 06
- Slide 12

---

## P09 SCREENSHOT

Use when:
- real UI/result is evidence

Do not use when:
- screenshot is decorative
- content becomes unreadable

Default motif:
- M-E

Density:
- MEDIUM

Rules:
- crop
- zoom
- annotate
- 3–8 word annotations preferred

---

## P10 CODE

Use when:
- implementation detail proves a point

Do not use when:
- code is merely decorative

Density:
- HIGH

---

## P11 DECISION

Use when:
- a decision or next action is required

Do not use when:
- the deck only informs

Default motif:
- M-A
- M-F

Density:
- LOW/MEDIUM

Reference:
- Slide 13

---

## P12 SUMMARY

Use when:
- closing a narrative

Do not use when:
- it would become a bullet recap

Density:
- LOW

Reference:
- Slide 13

---

## P13 QUALITY GATE

Use when:
- distinguishing blockers vs monitored conditions
- deciding what must be zero now

Do not use when:
- categories are not operationally different

Default motif:
- asymmetric two-zone contrast

Density:
- MEDIUM

Reference:
- Slide 09

---

## P14 COST SPLIT

Use when:
- separating reusable vs recalibrated work
- explaining where cost actually occurs

Do not use when:
- cost is a single scalar number

Default motif:
- process + split interpretation

Density:
- MEDIUM

Reference:
- Slide 10

---

## P15 ADOPTION STEPS

Use when:
- onboarding stages exist
- one stage is especially critical

Do not use when:
- all stages are equal and no narrative focus exists

Default motif:
- M-B
- keyed middle step

Density:
- MEDIUM

Reference:
- Slide 11

---

# 5. REFERENCE DECK

Canonical reference:

`AI_Playbook_DesignSystem_v1.1.html`

When an abstract rule has multiple valid visual interpretations, prefer the visual language demonstrated by the reference deck.

## 5.1 Pattern Map

| Slide | Pattern | Energy | Motif |
|---|---|---|---|
| 01 | HERO | BOLD | M-A + M-C |
| 02 | CONTRAST | FOCUSED | M-G |
| 03 | PROBLEM | FOCUSED | M-A |
| 04 | PROCESS / REFRAME | FOCUSED | M-B |
| 05 | STATEMENT | BOLD | M-F |
| 06 | EVIDENCE | FOCUSED | M-A + M-D |
| 07 | EVIDENCE / PITFALL | BOLD | M-A |
| 08 | EVIDENCE | FOCUSED | text-led |
| 09 | QUALITY GATE | FOCUSED | asymmetric zone |
| 10 | COST SPLIT | FOCUSED | M-B |
| 11 | ADOPTION STEPS | BOLD | keyed step |
| 12 | EVIDENCE | FOCUSED | metric band |
| 13 | DECISION / SUMMARY | BOLD | M-F |

## 5.2 Reference Principle

The reference deck is not a template to copy literally.

Use it to calibrate:
- scale
- asymmetry
- whitespace
- headline behavior
- rhythm
- use of bold moments

---

# 6. CRITIQUE

Critique checks whether output follows the Contract, Canon, and Language.

# 6.1 Presentation Smells

Smells are warnings unless stated otherwise.

## S01 Card Grid Smell

Trigger:
- 3+ visually identical cards
- card use has no semantic grouping reason

---

## S02 Topic Title Smell

Trigger:
- title names subject but does not communicate takeaway

---

## S03 Wall of Text Smell

Trigger:
- LOW > 40 words
- MEDIUM > 80 words
- HIGH > 120 words
- 4+ long bullets

---

## S04 Tiny Text Smell

Trigger:
- BODY < 15 pt equivalent

Severity:
- ERROR

---

## S05 Decoration Smell

Trigger:
- element can be removed without information loss

---

## S06 Generic AI Imagery Smell

Trigger:
- generic AI / robot / glowing brain / handshake / rocket imagery
- no content-specific reason

---

## S07 Rainbow Smell

Trigger:
- multiple saturated colors with no semantic role

---

## S08 Everything-in-a-Box Smell

Trigger:
- text and concepts unnecessarily wrapped in containers

---

## S09 Perfect Symmetry Smell

Trigger:
- unequal information is given equal visual weight

---

## S10 Repeated Layout Smell

Trigger:
- same silhouette > 2 consecutive slides

Severity:
- ERROR

---

## S11 Diagram Spaghetti Smell

Trigger:
- too many nodes
- crossing connectors
- mixed flow directions
- unclear boundaries

---

## S12 Document-on-a-Slide Smell

Trigger:
- source document structure is copied directly
- slide behaves like a page of a report

---

## S13 Flat Design Smell

Trigger:
- every slide is safe but forgettable
- no visual reset across 5 consecutive slides

---

## S14 Template Rhythm Smell

Trigger:
- content differs but title/content skeleton is repeatedly identical

---

## S15 Multiple Anchor Smell

Trigger:
- two or more elements compete as primary anchor

---

# 6.2 Negative Composition Examples

Do not generate:

1. Three equal rounded cards, each with one icon + title + paragraph.
2. Three consecutive slides with the same title-top / content-bottom silhouette.
3. 50/50 comparison when information importance is not equal.
4. Source document section titles used directly as slide titles.
5. Dark background with dense bullet lists.
6. Large number followed by another equally dominant long paragraph block.
7. Multiple accent colors used only to make items look different.
8. Screenshot reduced until text is unreadable.

---

# 6.3 Structural Lint

Machine-checkable where possible.

Check:

- BODY minimum size
- total words
- overflow
- safe margins
- repeated composition
- slide count
- dark slide ratio
- structural accent count
- missing intent
- missing takeaway
- declared pattern
- declared density
- declared energy

---

# 6.4 Semantic Lint

Check:

- title is takeaway
- slide has one idea
- visual matches information relationship
- evidence has interpretation
- container is justified
- uncertainty is explicit
- slide contributes to narrative
- transition makes sense

---

# 6.5 Visual Lint

Render to image and inspect:

- visual hierarchy
- first-attention element
- whitespace
- balance
- line breaks
- screenshot readability
- diagram readability
- asymmetry quality
- deck rhythm
- visual repetition

---

# 6.6 QA Output Schema

Each issue MUST use:

```yaml
slide:
layer: structural | semantic | visual | deck
severity: P0 | P1 | P2 | P3
smell:
where:
what:
why:
action:
```

Example:

```yaml
slide: 7
layer: semantic
severity: P1
smell: S02_TOPIC_TITLE
where: title
what: 標題只描述主題
why: 聽眾不知道這頁要相信什麼
action: 改成「三個合理推論都被實測推翻」
```

No vague critique such as:
- make it more professional
- add visual interest
- improve consistency

---

# 6.7 Severity

## P0 — Broken

- overflow
- clipping
- unreadable text
- broken connectors

## P1 — Communication

- no takeaway
- confusing hierarchy
- misleading evidence
- hidden uncertainty
- confusing diagram

## P2 — Composition

- density
- spacing
- repetition
- weak balance

## P3 — Polish

- minor refinement

---

# 6.8 Deck-Level Rhythm Strip

Every deck should generate a rhythm strip:

```text
01 HERO       LOW    BOLD     M-A/M-C
02 CONTRAST   MED    FOCUSED  M-G
03 PROBLEM    MED    FOCUSED  M-A
04 PROCESS    MED    FOCUSED  M-B
05 STATEMENT  LOW    BOLD     M-F
...
```

Check:

- no same pattern > 2 consecutive
- no same silhouette > 2 consecutive
- no 5 consecutive slides without BOLD
- dark slides warning if > 25%
- density alternates enough to create breathing space

---

# 6.9 Acceptance Criteria

Final deck must satisfy:

- no P0
- no unresolved ERROR
- BODY >= 15 pt equivalent
- no overflow
- one idea per slide
- one explicit intent per slide
- one takeaway per slide
- one primary visual anchor per slide
- no repeated silhouette > 2 consecutive
- no hidden uncertainty
- evidence includes context
- opening and closing connect
- screenshots are readable
- diagrams are quickly understandable
- deck rhythm contains variation
- boldness comes from scale/composition, not decoration

Final status:

- PASS
- REVISE

Do not use numeric quality scores.

---

# 7. GENERATION WORKFLOW

Required order:

```text
Source Material
↓
Contract
↓
Narrative Spine
↓
Slide Intents
↓
Takeaways
↓
Pattern Selection
↓
Density
↓
Energy
↓
Visual Anchor
↓
Composition
↓
Generate
↓
Render
↓
Structural Lint
↓
Semantic Lint
↓
Visual Lint
↓
Rhythm Strip
↓
Revise
↓
Final Pass
```

Generation deliberately occurs late.

---

# 8. REVISION LOOP

Maximum recommended loop:

## Round 1
Structure + P0/P1

## Round 2
Narrative + composition

## Round 3
Polish

Do not endlessly revise after errors are resolved.

---

# 9. SOURCE MATERIAL TRANSFORMATION RULE

A presentation is not a document split across pages.

Never convert source headings directly into slides.

Transform source material through:

```text
Source Fact
↓
Communication Intent
↓
Takeaway
↓
Relationship
↓
Pattern
↓
Visual Form
```

This rule overrides convenience.

---

# 10. CHANGELOG

## v1.2

- Rebuilt structure into Contract / Canon / Language / Critique.
- Added rule priority.
- Added machine-fillable Contract YAML.
- Added explicit RULE / WHEN / CHECK logic for Canon.
- Added Implementation Mapping for PPTX vs HTML.
- Aligned color tokens with Reference Deck.
- Added Chrome rules.
- Added Chinese editorial typesetting.
- Added Number Rhetoric.
- Added Confidence Legend.
- Added Reference Deck as canonical implementation.
- Added Use / Do Not Use / Motif / Density / Reference to patterns.
- Added QUALITY GATE, COST SPLIT, ADOPTION STEPS patterns.
- Reordered smells to S01–S15.
- Added fixed QA schema.
- Added rhythm strip.
- Reduced duplicated philosophy.
- Converted boldness from vague guidance to deck-level measurable warning.

---

# 11. FINAL DESIGN INTENT

Eric Presentation should feel:

- structured but not rigid
- restrained but not flat
- technical but not dry
- bold but not decorative
- editorial but not artistic for its own sake
- consistent but not templated
- AI-assisted but clearly human-directed

The system is successful when the audience remembers the idea, not the template.
