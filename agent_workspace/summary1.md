# Deepagent Lesson Summary

## TL;DR
Deepagents are autonomous AI systems that wrap Large Language Models in active execution loops. By coordinating planning, tool execution, and self-reflection, they dynamically solve open-ended tasks and resolve errors. This stateful design marks a major transition from static, passive prompt engineering to resilient agentic engineering.

## Key Takeaways
*   **Active Iteration:** Wraps the LLM in a planning-acting-reflecting loop to enable dynamic self-correction and multi-step task resolution.
*   **External Tool Use:** Integrates specialized external tools (like search engines or database connectors) to extend the agent's capabilities.
*   **Failure Resilience:** Implements loop boundaries and error feedback structures to prevent runaway executions and handle runtime failures gracefully.