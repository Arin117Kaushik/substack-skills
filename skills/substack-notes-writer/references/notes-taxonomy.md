# Substack Note Types

> Adapted from [Solo-AI-Lab/substack-notes-skills](https://github.com/Solo-AI-Lab/substack-notes-skills), MIT License, Copyright (c) 2026 Luan Doan. Changes: dashes replaced, minor wording. See LICENSE.

Taxonomy of 8 Substack Note formats for skill-driven generation. Each type has distinct template, hook pattern, and primary goal. Templates use `{placeholder}` notation, replace with concrete content.

## Core Principle

A Note is **one core idea**, told in **50-120 words**, opened by a **scroll-stopping hook**, closed by a **conversation invitation**. Type is determined by structural shape (story / list / question / etc.) and source (original / repurposed / restacked).

## Universal Anatomy

| Element | Constraint |
|---|---|
| Hook (line 1) | ≤10 words, standalone, specific |
| Body | 3-5 paragraphs, ≤3 lines each, line break every 1-3 lines |
| Length | 50-120w sweet spot · 250w hard ceiling |
| CTA | Conversation-driven · DO NOT use "subscribe" |
| Voice | First-person, conversational, read-aloud-friendly |

## Type Index

| # | ID | Goal | Length | Default Hook |
|---|---|---|---|---|
| 1 | `micro-story` | Subscriber conversion | 80-150w | In-medias-res |
| 2 | `one-liner` | Shareability / restacks | 10-40w | Self-quote |
| 3 | `contrarian-take` | Reach / visibility | 50-100w | Contrarian statement |
| 4 | `question-prompt` | Engagement / audience research | 30-80w | Direct question |
| 5 | `list-format` | Authority / saves | 60-150w | Numbered promise |
| 6 | `build-update` | Long-term retention | 70-140w | Specific number / colon setup |
| 7 | `repurpose-teaser` | Funnel to long-form | 40-100w | Pulled quote |
| 8 | `restack-commentary` | Cross-audience reach | 20-80w | Agree/disagree opener |

## 1. `micro-story`

**Goal:** Convert reader → subscriber via shared experience.
**Use when:** Recent personal experience yielded a transferable lesson.
**Avoid when:** No clear lesson; lesson is generic ("hard work pays off").

**Template:**
```
{in_medias_res_opening}.

{escalation_or_conflict_detail}.

{turning_point}.

{one_line_revelation}.
```

**Engagement profile:** High comments · High subs · Med restacks.

## 2. `one-liner`

**Goal:** Shareability, restacks, screenshots, pins.
**Use when:** Insight distills to ≤10 words and stands alone.
**Avoid when:** Idea needs setup; recycled platitude.

**Template:**
```
{punchy_wisdom_line}.

,  {optional_context_line}.
```

**Engagement profile:** High likes · **Highest restacks** · Low comments.

## 3. `contrarian-take`

**Goal:** Reach, algorithm rewards debate.
**Use when:** Direct experience contradicts popular belief.
**Avoid when:** >1 per 7 Notes; cannot defend in comments; contrarian for its own sake.

**Template:**
```
{popular_belief} is wrong.

{evidence_from_creator_experience}.

{contrarian_belief}.

{invitation_for_pushback}.
```

**Engagement profile:** **Highest likes** · **Highest comments** · Low subs.

## 4. `question-prompt`

**Goal:** Engagement + audience research (Feedback Note pattern).
**Use when:** Genuinely uncertain; question yields divergent answers.
**Avoid when:** Answer obvious to creator ("fake humility"); question too broad.

**Template:**
```
{specific_question}?

{brief_context_for_why_asking}.

{optional_creator_current_thinking}.
```

**Engagement profile:** Med likes · **Highest comments** · High trust.

## 5. `list-format`

**Goal:** Authority via scannable structure; save-worthy.
**Use when:** Content is genuinely list-shaped; 3-5 items achievable.
**Avoid when:** Filler items to reach round number; items overlap.

**Subformats:**
- **Step Stack**, numbered actions toward outcome
- **Prompt Library**, N reusable prompts/templates verbatim
- **Bullet Showcase**, ✦ feature bullets

**Template:**
```
{list_framing_line}:

• {item_1}
• {item_2}
• {item_3}

{optional_closing_invitation}.
```

**Engagement profile:** High likes · Med comments · High restacks (saveable).

## 6. `build-update`

**Goal:** Long-term retention via in-progress arc.
**Use when:** Actively building something visible; real friction or progress; audience benefits from the arc.
**Avoid when:** Progress fabricated; confidentiality blocks honest disclosure; post-hoc framing.

**Template:**
```
{specific_action} on {object} {recent_timeframe}.

{what_went_wrong_or_surprised}.

{what_is_working_now}.

Next: {next_step}.
```

**Engagement profile:** Med-high likes · High comments · **Very high subs (retention)**.

**Optional visual:** screenshot, photo, workflow diagram of real artifact.

## 7. `repurpose-teaser`

**Goal:** Drive traffic from Note feed → own long-form post.
**Use when:** Snippet from recent post stands alone AND benefits from full read.
**Avoid when:** Snippet meaningless without article context; post is paywalled with no preview value.

**Template:**
```
{pulled_quote_or_insight_from_post}.

{one_line_elaboration_or_question}.

{link_to_full_post}
```

**Engagement profile:** Med likes · Med comments · Med-high post clicks.

## 8. `restack-commentary`

**Goal:** Cross-pollinate audiences via algorithmic overlap signal.
**Use when:** Restacking another creator with adjacent audience; have substantive add.
**Avoid when:** Bare restack ("this!"); restacking without reading; restacking only own work.

**Template:**
```
{reaction_or_pivot_line}.

{what_the_original_misses_OR_what_it_nailed}.

{invitation_for_response}.

[restacked Note attached]
```

**Engagement profile:** Med likes · Med comments · **Cross-audience reach (algorithm)**.

## Hook Library

| Pattern | Form | Best paired with |
|---|---|---|
| In-medias-res | Mid-action open, no setup | micro-story |
| Stop/Start pivot | "I stopped {old}. I started {new}." | micro-story, build-update |
| Self-quote | Standalone wisdom line | one-liner |
| Contrarian statement | "{popular_belief} is {reversal}." | contrarian-take |
| Direct question | "{question}?" | question-prompt |
| Numbered promise | "{N} {things} that {outcome}:" | list-format |
| Colon setup | "{bold_statement}: {detail}" | build-update, list-format |
| Specific number | "{N} {unit}. {result}." | build-update, micro-story |
| Pulled quote | Single line lifted from long-form | repurpose-teaser |
| Agree/disagree opener | "I {agree/disagree}, here's why:" | restack-commentary |

## CTA Patterns

**Use (conversation-driven):**

| Pattern | Template |
|---|---|
| Direct experience ask | `What's your experience with {topic}?` |
| Counter-example invite | `Anyone else hit this?` |
| Quick poll | `{option_a} or {option_b}?` |
| Differentiation | `What would you do differently?` |
| Open close | (No explicit CTA, implicit invitation) |

**DO NOT use (suppress reach):** `Subscribe for more` · `Click link in bio` · `DM me` · `Like if you agree` · `Tag someone who needs this`.

## Goal → Type Selection

| Outcome | Primary | Secondary |
|---|---|---|
| Convert subscribers | micro-story | build-update |
| Maximize reach | contrarian-take | one-liner |
| Spark comments | question-prompt | contrarian-take |
| Get restacked / screenshotted | one-liner | list-format |
| Drive long-form clicks | repurpose-teaser | micro-story |
| Long-term subscriber retention | build-update | micro-story |
| Cross-audience growth | restack-commentary | contrarian-take |
| Establish authority | list-format | build-update |
| Audience research / feedback | question-prompt | none |

## Quality Heuristics

**Stronger when it:**
- Opens with specific concrete sentence (not abstract)
- Contains exactly **one** core idea
- Reads aloud naturally (sounds like speech)
- Could not be generated without creator's specific experience
- Uses first-person consistently

**Weaker when it:**
- Opens with generality, platitude, or jargon
- Mixes 2+ core ideas
- Could come from any account
- Contains direct subscribe CTA
- Reuses structure of previous 3 Notes

## Type Boundaries

| Overlap | Choose |
|---|---|
| Story with embedded list | `micro-story` (story dominates) |
| Question framed as contrarian | `contrarian-take` (claim dominates) |
| Quote from own past article | `repurpose-teaser` if linked, else `one-liner` |
| Build update with list of changes | `build-update` (arc dominates) |
| Restack of own Note | NOT `restack-commentary`, pick original type |
