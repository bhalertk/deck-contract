# deck-contract

**Eric Presentation Design System v1.2** — a canonical, machine-checkable specification for generating presentation decks (PPTX or offline HTML), designed to be followed by both humans and AI generators.

Full specification: [DESIGN.md](DESIGN.md)

## What this is

A rule system that governs *what* a deck must define before any visual design happens, and *how* that design is judged afterward. It targets a **70% Editorial Tech / 30% Strategy Deck** feel — clear, restrained, narrative-driven — while explicitly avoiding generic SaaS-deck patterns (icon grids, gradients, glassmorphism, decorative cards).

Language: Traditional Chinese (zh-Hant) first, with bilingual editorial support.

## Structure

Rules are organized into layers with a strict priority order (higher overrides lower):

1. **Contract** — required metadata (audience, goal, core message, constraints) that must be complete before composition starts.
2. **Canon** (C01–C15) — non-negotiable rules: one idea per slide, one visual anchor, minimum body text size, no shrinking to fit, titles as takeaways, etc.
3. **Language** — typography, color tokens, grid/spacing, Chinese editorial typesetting, signature motifs (M-A–M-H), visual energy levels, and number rhetoric.
4. **Pattern Library** (P01–P15) — reusable communication patterns (HERO, CONTRAST, PROCESS, EVIDENCE, ARCHITECTURE, DECISION, etc.), each with usage conditions, default motif, and density.
5. **Critique** — presentation "smells" (S01–S15), structural/semantic/visual lint checks, severity levels (P0–P3), and acceptance criteria for a final PASS/REVISE verdict.

## Generation workflow

```
Source Material → Contract → Narrative Spine → Slide Intents → Takeaways
→ Pattern Selection → Density → Energy → Visual Anchor → Composition
→ Generate → Render → Structural Lint → Semantic Lint → Visual Lint
→ Rhythm Strip → Revise → Final Pass
```

Generation deliberately happens late — structure and intent are locked in before any visual work begins.

## Reference implementation

`AI_Playbook_DesignSystem_v1.1.html` is the canonical reference deck used to calibrate scale, asymmetry, whitespace, and rhythm when a rule has multiple valid visual interpretations.
