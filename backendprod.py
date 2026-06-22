from Deepagent import create_deep_agent
from utils import get_model
from deepagents.backends import CompositeBackend, FilesystemBackend, StateBackend

model = get_model()
backend = CompositeBackend(
    default=StateBackend(),
    routes={
        "/workspace/": FilesystemBackend(
            root_dir="./agent_workspace",
            virtual_mode=True
        ),
    },
)

def get_article_point(topic: str) -> str:
    """Return talking points for the given topic.

    This function is used by the agent as a tool to retrieve raw article
    talking points which are then formatted into lesson notes and a summary.
    """
    # Placeholder for a function that would fetch or generate an article point based on the topic
    return f"""Article Topic: {topic}

Talking Points:
1. Start with the learner's confusion
2. Explain the problem in simple language
3. Give a practical example
4. Explain common mistakes
5. End with a short summary
"""

system_prompt = """You are a helpful instructional writer and lesson designer. Use the `get_article_point(topic)` tool to fetch raw talking points, then produce three output files in this workspace:

1) roughnotes.md — raw, unordered bullet points and scratch notes derived directly from get_article_point(topic).
2) clearnotes.md — a clean, student-facing lesson in Markdown with these sections: Title, Learning Objectives (3), Background / Explanation (concise paragraphs), Step-by-step Example, Common Mistakes, Short Exercise (1-2 tasks), Further Reading / Links.
3) summary.md — a short summary (3–5 bullets) and a 2–3 sentence TL;DR.

Rules:
- ALWAYS call get_article_point(topic) once at start to obtain canonical points. Example call: get_article_point("<topic>")
- Do not invent additional tooling — derive content from the tool output and your knowledge.
- Preserve factual accuracy; if you lack information, state assumptions clearly in roughnotes.md.
- Keep workspace/clearnotes1.md readable: use headings, 2–4 sentence paragraphs, and 1–3 bullet lists where helpful.
- Length limits: workspace/clearnotes1.md ~400–800 words; summary.md max 120 words.
- Produce a short TODO list at the end of workspace/clearnotes1.md with 3 actionable next steps (owner role, estimate hours).
- Format files using valid Markdown (use fenced code blocks only for examples).
- Use a helpful, encouraging tone suitable for learners.

Acceptance criteria:
- workspace/roughnotes1.md contains the raw points returned by the tool (verbatim bullets).
- workspace/clearnotes1.md reorganizes those points into the specified sections and includes a practical example and exercise.
- workspace/summary1.md contains a concise TL;DR plus 3 bullets.

If the user supplies additional constraints (audience level, word-count, format), respect them; otherwise default to intermediate learner level.

WAIT for the topic input from the user and then call get_article_point(topic) to begin."""

agent = create_deep_agent(
    model=model,
    backend=backend,
    tools=[get_article_point],
    system_prompt=system_prompt,
)

if __name__ == "__main__":
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Write an article on algebra."
                }
            ]
        }
    )
    result["messages"][-1].pretty_print()