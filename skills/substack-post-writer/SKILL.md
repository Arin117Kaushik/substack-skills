---
name: substack-post-writer
description: Use when the user wants a Substack newsletter post or long-form issue drafted from an idea or outline, or an existing draft packaged for publishing with title, subtitle, SEO title and description, slug, tags, section, and paywall placement. Not for short Notes (use substack-notes-writer) or reviewing tone (use substack-humanizer).
---

# Substack Post Writer

Draft a post from what the user actually has, then package every field Substack needs.

## Before drafting

1. Read `references/voice-rules.md`, `references/anti-fabrication.md`, `references/platform-limits.md`.
2. Read `~/.substack-skills/voice-profile.md` and `~/.substack-skills/story-bank.md` if they exist.

## Draft

- Build each section from the user's outline, message, Story Bank, or files. Where a section needs a fact you don't have, write around it with a slot: `[what the tool stack cost last month]`.
- When the input is thin (an outline of labels), the draft is a skeleton: a heading and 2 to 4 lines per section, made of the user's words plus slots. Still a draft, never a refusal.
- Working length 1,000 to 2,500 words unless the user sets one.
- **Clipping check:** Gmail clips emails over 102KB. If the user's target or past style is over about 6,000 words, or image-heavy, say so before drafting and offer: split into a series, cut, or accept that email readers see "View entire message".

`--mode package` skips drafting and packages an existing draft.

## Reply shape (always, in this order)

1. Clipping warning, if it applies.
2. The draft or skeleton.
3. The package block below, every field filled. Fields that depend on missing content get a best guess marked `(provisional)`.
4. Up to 3 questions whose answers fill the most slots, or suggest `substack-interviewer --mode post`.

## Package

```
Title: <60 characters or fewer, says what the reader gets>
Subtitle: <one sentence, adds what the title doesn't>
SEO title: <keyword-first version of the title, 60 characters or fewer>
SEO description: <150 to 160 characters, plain language, includes the main keyword>
Slug: <3 to 6 lowercase words joined by hyphens>
Tags: <2 to 4 existing or new topic tags>
Section: <section name from the voice profile, or "main">
Audience: <everyone | only_paid | founding | only_free>
Paywall: <none | after the paragraph starting "...", with one line on why>
Email subscribers: <yes | no | ask the user>
Words: <count> · Clipping risk: <yes | no>
Slots to fill: <list or "none">
```

Mark the paywall in the draft with `<!-- paywall -->` on its own line if there is one.

## Publishing

Hand the draft and package to `substack-publisher` when the user wants it live. This skill doesn't publish.

## Common mistakes

| Mistake | Fix |
|---|---|
| Replying with only questions | Skeleton, package, then questions |
| Leaving out SEO, slug or tags because the user didn't ask | The package is always complete |
| Ignoring a 9,000 word target | Warn about clipping first |
| Inventing the cost, date or result in a section | Slot it |
