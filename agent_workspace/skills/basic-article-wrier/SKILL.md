(**Basic Article Writer Skill**)

Purpose:
- Produce a clear, well-structured article on a given topic suitable for blogs, internal docs, or general publishing.

Inputs (JSON):
- `topic` (string) — the subject the article should cover (required).
- `audience` (string) — who the article is for (e.g., "developers", "small business owners"). Default: "general audience".
- `tone` (string) — tone of voice (e.g., "informative", "conversational", "formal"). Default: "informative".
- `length` (string) — desired length ("short" 300-500 words, "medium" 600-900 words, "long" 1000+ words). Default: "medium".
- `key_points` (array of strings) — optional bullets or facts to include in the article.
- `call_to_action` (string) — optional CTA to include at the end.

Output (JSON):
- `title` (string)
- `subtitle` (string) — one-line summary
- `body` (string) — the full article text with paragraphs and subheadings
- `bullets` (array of strings) — 3–6 quick takeaways
- `estimated_word_count` (integer)

Behavior and constraints:
- Provide a descriptive, SEO-friendly title and a concise subtitle.
- Use the `key_points` when present; include them as subheadings or paragraphs.
- Maintain the requested `tone` and `length` guidelines.
- Avoid hallucinated citations — do not invent facts you are not confident about.
- Do not output any raw PII (emails, credit card numbers). If PII appears in inputs, redact or mask it and note the redaction.

Example Input:
{
	"topic": "Getting started with vector search",
	"audience": "software developers",
	"tone": "conversational",
	"length": "short",
	"key_points": ["what is vector search", "use-cases", "quick tutorial steps"],
	"call_to_action": "Try a small prototype with your dataset"
}

Example Output (excerpt):
{
	"title": "A Practical Intro to Vector Search",
	"subtitle": "What it is, when to use it, and a quick starter",
	"body": "...",
	"bullets": ["Definition of vector search", "Popular use-cases", "3-step prototype"],
	"estimated_word_count": 420
}

Notes for integrators:
- Prefer returning JSON to make downstream processing reliable.
- If generating HTML is needed, add a `format` input parameter with values `plain` or `html`.
- Keep outputs deterministic for the same inputs when used in tests.
