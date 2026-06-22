# Demystifying Deepagents: Building Next-Generation AI Systems with Tool-Use and Reasoning

Welcome to this intermediate-level lesson on Deepagents. In this guide, you will learn how to transition from static, linear prompting to building dynamic, self-correcting AI agentic workflows that can plan, execute, and iterate.

---

## Learning Objectives
By the end of this lesson, you will be able to:
1. **Explain** the difference between standard passive LLMs and autonomous Deepagents.
2. **Implement** an agentic execution loop featuring planning, tool execution, and reflection in Python.
3. **Analyze** and mitigate common agent pitfalls such as infinite execution loops and unhandled tool failures.

---

## Background / Explanation

Many learners get confused when first trying to build agentic AI systems. If a standard Large Language Model (LLM) is so powerful, why can't we just ask it to solve a complex task in a single prompt? The answer lies in the limitations of "one-shot" reasoning. Standard LLMs generate responses sequentially, word by word. If they make a logical error early in their response or run into an unexpected barrier, they cannot "erase" their progress, step back, and try a different approach. They lack active working memory and a mechanism to self-correct.

A Deepagent solves this problem by wrapping the LLM in an active execution loop. Instead of generating a final response immediately, the agent acts like a human solver: it creates a plan, executes a step using external tools (like databases, web search, or file writers), inspects the results, and reflects on whether it is closer to the goal. In simple language, a Deepagent is a stateful system where the LLM is the "brain," tools are the "hands," and an orchestrator manages the control loop to ensure the agent can correct its mistakes and iterate dynamically.

---

## Step-by-Step Example

Below is a complete, lightweight Python implementation of a simple Deepagent. This example showcases a planning-execution-reflection loop where an agent must search for information and refine its answer before completing the task.

```python
import time
from typing import Dict, Any, List

# 1. Simulate External Tools available to the Deepagent
def mock_search_tool(query: str) -> str:
    """A simulated search tool to retrieve knowledge."""
    if "temperature" in query.lower():
        return "Current temperature in Seattle is 45°F and rainy."
    return "No results found."

# 2. Define the Deepagent Orchestrator
class SimpleDeepagent:
    def __init__(self, max_iterations: int = 5):
        self.max_iterations = max_iterations
        self.tools = {"search": mock_search_tool}

    def run(self, user_goal: str) -> str:
        # Initialize internal state
        state: Dict[str, Any] = {
            "goal": user_goal,
            "plan": [],
            "scratchpad": "",
            "iteration": 0,
            "status": "planning"
        }
        
        print(f"Goal received: {state['goal']}\n")

        while state["iteration"] < self.max_iterations:
            state["iteration"] += 1
            print(f"=== Iteration {state['iteration']} ===")

            if state["status"] == "planning":
                # Step 1: Planning phase
                print("[Brain] Formulating plan...")
                state["plan"] = ["Call search tool for weather in Seattle", "Analyze results and respond"]
                state["status"] = "executing"
                print(f"Plan created: {state['plan']}")

            elif state["status"] == "executing":
                # Step 2: Tool execution phase
                next_step = state["plan"].pop(0)
                print(f"[Hands] Executing step: {next_step}")
                
                # Simulate agent extracting keyword "temperature"
                tool_output = self.tools["search"]("temperature in Seattle")
                state["scratchpad"] += f"\nTool Output: {tool_output}"
                print(f"Tool output recorded: {tool_output}")
                
                state["status"] = "reflecting"

            elif state["status"] == "reflecting":
                # Step 3: Reflection / self-correction phase
                print("[Brain] Reflecting on tool output and scratchpad...")
                if "45°F" in state["scratchpad"]:
                    print("[Brain] We have sufficient information. Formulating final answer.")
                    state["status"] = "completed"
                    break
                else:
                    print("[Brain] Information insufficient. Re-planning...")
                    state["status"] = "planning"
            
            time.sleep(0.5)

        if state["status"] == "completed":
            final_answer = f"According to Seattle weather tools, it is currently 45°F and rainy."
            return f"Success! Final Answer: {final_answer}"
        else:
            return "Failed to complete the task within iteration limits."

# 3. Instantiate and run the Deepagent
agent = SimpleDeepagent()
result = agent.run("What is the current weather in Seattle?")
print(f"\n{result}")
```

---

## Common Mistakes

1. **Unbounded Loops (Infinite Execution):** Without a strict limit on the number of tool iterations (`max_iterations` or a timeout), an agent can get caught in a recursive loop when a tool returns unexpected or faulty data.
2. **Poor Tool Error Propagation:** If a tool call fails (e.g., API returns a 500 error), sending a blank string to the LLM will cause it to repeat the exact same call. You must feed the raw error message back into the agent's scratchpad so it can self-correct or try an alternative tool.
3. **State Bloat and Context Window Exceeded:** Over long execution loops, accumulating massive scratchpads or full tool logs can quickly consume the LLM's context window. Implement summary-reduction strategies to compress historical steps.

---

## Short Exercise

### Task 1: Add a Depth-Limit Safety Check
Modify the example agent loop to raise a ValueError immediately if the `iteration` count exceeds `3`, preventing unnecessary token usage when an agent fails to make progress.

### Task 2: Implement Tool Error Recovery
Update the mock search tool to throw an exception if the query is empty. Modify the execution block in the agent loop using a `try-except` block to capture the error, write "Error: Empty query entered" to the scratchpad, and let the agent plan a corrected query.

---

## Further Reading and Links
* [The ReAct Framework Paper](https://arxiv.org/abs/2210.03629) - Synergizing reasoning and acting in language models.
* [LLM Compiler Architectures](https://arxiv.org/abs/2312.04511) - Parallel function calling and execution structures.
* [Introduction to Agentic Workflows](https://deeplearning.ai) - Courses on multi-agent collaboration and design patterns.

---

## Next Steps Todo

| Owner Role | Task Description | Estimated Hours |
| :--- | :--- | :--- |
| **System Architect** | Define standard JSON schema for agent-to-tool communications and tool registry | 2.5 Hours |
| **Backend Engineer** | Integrate live search API client with robust retry-logic and error-reporting wrapper | 3.0 Hours |
| **QA Engineer** | Develop regression test suites checking agent reliability under simulated tool failures | 4.0 Hours |