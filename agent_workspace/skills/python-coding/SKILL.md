
---
name: python-coding
display_name: Python Coding
version: 0.1.0
description: Provide a safe, structured interface for generating, explaining, and refactoring Python code snippets and small scripts.
inputs:
  task:
    type: string
    required: true
  code:
    type: string
outputs:
  files: object
  code: string
  explanation: string
---

**Python Coding Skill**

Purpose:
- Provide a safe, structured interface for generating, explaining, and refactoring Python code snippets and small scripts.

Inputs (JSON):
- `task` (string) — concise description of what to implement (required).
- `code` (string) — optional existing code to modify or refactor.
- `constraints` (string) — runtime or style constraints (e.g., "no external network calls", "type hints", "compatible with Python 3.11").
- `examples` (array of strings) — optional example inputs/outputs to clarify expected behavior.
- `format` (string) — output format: `plain`, `file`, or `pytest` (default `plain`).

Output (JSON or files):
- `files` (object) — mapping of filename -> content when `format` is `file`.
- `code` (string) — primary code snippet or function implementation.
- `explanation` (string) — brief explanation of the approach and complexity.
- `tests` (string, optional) — suggested unit tests (when `format` is `pytest`).

Behavior and constraints:
- Prefer small, well-tested functions over monolithic scripts.
- Do not include secrets, API keys, or raw PII in outputs.
- If `code` input is provided, clearly indicate which lines were changed and why.
- When requested, produce unit tests using `pytest` that validate core behavior.
- Avoid executing code — the skill returns code to be run by the integrator.

Example Input:
{
  "task": "Implement a function to merge two sorted lists",
  "constraints": "O(n) time, Python 3.11",
  "format": "plain"
}

Example Output (excerpt):
{
  "code": "def merge(a, b):\n    ...",
  "explanation": "Linear merge using two pointers. O(n) time, O(1) extra space.",
  "tests": "def test_merge(): assert merge([1],[2]) == [1,2]"
}

Notes for integrators:
- When `format` is `file`, return a `files` object with one or more files (e.g., `module.py`, `tests/test_module.py`).
- Consider running linting and tests in CI before deploying generated code.
