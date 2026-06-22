**LinkedIn Article Writer Skill**

Purpose:
- Craft LinkedIn-optimized long-form posts and articles derived from a topic or source content. Focus on professional tone, strong headline, engaging opening, practical takeaways, and a clear call-to-action.

Inputs (JSON):
- `topic` (string) — main subject or idea (required).
- `source` (string) — optional longer source text to summarize or repurpose (article, notes).
- `audience` (string) — target readers (e.g., "product managers", "founders"). Default: "professionals".
- `tone` (string) — e.g., "thought-leadership", "helpful", "casual-professional". Default: "thought-leadership".
- `length` (string) — "short" (200-400 words), "medium" (500-900 words), "long" (900-1600 words). Default: "medium".
- `hashtags` (array of strings) — optional list of hashtags to include (max 6).
- `cta` (string) — optional call-to-action (comment, follow, visit link).

Output (JSON):
- `headline` (string) — 6–12 words, LinkedIn-friendly
- `lead_paragraph` (string) — the hook/opening paragraph
- `body` (string) — full article with subheadings and short paragraphs optimized for readability
- `closing` (string) — final paragraph + CTA
- `hashtags` (array of strings)
- `suggested_post_text` (string) — a concise post version (1–3 short paragraphs) ready to paste to LinkedIn

Behavior and constraints:
- Begin with a compelling hook in the lead paragraph to increase engagement.
- Convert long `source` text into a concise LinkedIn narrative while preserving key facts.
- Use short paragraphs and bold/italic markers sparingly (if producing markdown/HTML format).
- Keep professional tone and avoid controversial or policy-violating content.
- Do not expose PII from `source`; redact or mask if present and annotate the redaction.

Example Input:
{
  "topic": "Lessons from shipping a B2B MVP",
  "audience": "founders",
  "tone": "thought-leadership",
  "length": "short",
  "hashtags": ["MVP", "startups", "product"],
  "cta": "Share your MVP lesson below"
}

Example Output (excerpt):
{
  "headline": "5 MVP Lessons We Learned Building for B2B",
  "lead_paragraph": "Shipping an MVP changed how we prioritized product-market fit...",
  "body": "...",
  "closing": "If you built an MVP, what surprised you the most?",
  "hashtags": ["#MVP", "#startups", "#product"],
  "suggested_post_text": "Headline\n\nTL;DR: ...\n\nWhat surprised you?"
}

Notes for integrators:
- Provide a `format` parameter if HTML/Markdown output is required; default is plain text.
- Consider adding a `language` input for localization.
- Validate hashtags: return up to 6 and ensure they are plain tokens (no punctuation).
