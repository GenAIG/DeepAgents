# Deep Agents - Complete Notes

## References

- Bedrock: https://docs.langchain.com/oss/python/integrations/chat/bedrock#installation
- Create Agent: https://reference.langchain.com/python/langchain/agents/factory/create_agent
- Deep Agent: https://docs.langchain.com/oss/python/deepagents/customization

---

## Table of Contents

1. What is Deep Agents?
2. Core Components
3. Memory
4. Planning
5. TODO Management
6. Skills
7. Subagents
8. File System Access
9. Real-World Example
10. Deep Agent vs Simple Agent
11. Deep Agent Architecture
12. Skill Files
13. Storage Backends
14. Middleware
15. Travel Planning Example
16. Interview Definition
17. Deep Agents vs AWS AgentCore
18. Quick Revision

---

# What is Deep Agents?

Deep Agents is a framework from LangChain for building AI agents that can work on complex tasks over a long period of time, similar to coding assistants like Claude Code or Manus.

Think of a Deep Agent as an AI employee that can:

- Plan work
- Break tasks into steps
- Use tools
- Remember information
- Create and edit files
- Delegate work to sub-agents
- Continuously improve its plan

---

# Core Components

## Models

The brain of the agent.

### Example Models

#### Google Gemini

```python
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
```

#### Other Models

- OpenAI
- Anthropic Claude

---

## Memory

Allows the agent to remember previous conversations or task progress.

### Without Memory

Agent forgets after every request.

### With Memory

Agent remembers context and past decisions.

---

## Planning

Before acting, the agent creates a plan.

### Example Plan

```text
1. Create project structure
2. Create Flask app
3. Create routes
4. Add templates
5. Test application
```

---

## TODO Management

Task management for the agent.

```text
☐ Create API
☐ Write tests
☐ Deploy application
☑ Setup project
```

---

## Skills

Examples:

```text
Skill: Python Coding
Skill: AWS Deployment
Skill: Kubernetes Troubleshooting
```

---

## Subagents

```text
Main Agent
│
├── Research Agent
├── Coding Agent
└── Testing Agent
```

---

## File System Access

The agent can read and write files.

```text
project/
├── app.py
├── requirements.txt
└── README.md
```

The agent can:

- Create files
- Modify files
- Read files
- Organize projects

---

# Real-World Example

## User Request

```text
Create a Python application that reads AWS CloudWatch logs and stores them in Elasticsearch.
```

## Deep Agent Workflow

1. Create a plan
2. Create todo list
3. Research AWS APIs
4. Write Python code
5. Create requirements.txt
6. Generate README
7. Run tests
8. Fix errors
9. Save files
10. Return completed project

---

# Deep Agent vs Simple Agent

| Simple Agent | Deep Agent |
|--------------|------------|
| One response | Multi-step workflow |
| Minimal memory | Long-term memory |
| Few tools | Many tools |
| No planning | Built-in planning |
| No task tracking | Todos |
| Single worker | Subagents |
| Limited file handling | Full project workspace |
| Short tasks | Long-running tasks |

---

# Summary

```text
Chatbot = Answers questions
Agent = Can use tools
Deep Agent = Acts like a project engineer that plans, tracks tasks,
uses tools, creates files, delegates work, and completes complex
projects end-to-end.
```

### DevOps Use Cases

Deep Agents are especially useful for:

- CI/CD pipeline creation
- Terraform generation
- Kubernetes troubleshooting
- AWS infrastructure setup
- Log analysis using Datadog or Splunk
- End-to-end project scaffolding and code generation

---

# Deep Agents - Simplified Notes

## What is a Deep Agent?

A Deep Agent is an AI system that can:

1. Break a complex task into smaller tasks.
2. Assign tasks to specialized agents.
3. Execute tasks independently or in parallel.
4. Combine results into a final response.

Think of it as a **Manager + Team of Specialists**.

- Orchestrator Agent = Manager
- Sub Agents = Specialists

---

# High-Level Architecture

```text
User Request
      │
      ▼
 Orchestrator Agent
      │
 ┌────┼────┐
 ▼    ▼    ▼
Hotel Flight Itinerary
Agent Agent Agent
 │      │      │
 └──────┼──────┘
        ▼
  Final Response
```

The Orchestrator:

- Creates a plan
- Breaks tasks into smaller tasks
- Delegates work to sub-agents
- Collects outputs
- Generates the final response

---

# Sub Agents

Each sub-agent is designed for a specific purpose.

## Components of a Sub-Agent

### Instructions

```text
Hotel Agent:
Find hotels within budget.

Flight Agent:
Find the cheapest available flights.
```

### Tools

```text
Hotel Agent → Hotel Search API
Flight Agent → Flight Search API
```

### Context

Each agent only receives information relevant to its task.

Benefits:

- Better accuracy
- Reduced confusion
- Faster execution

---

# Skill Files

A Skill File acts like a job description for an agent.

```yaml
name: Hotel Finder

goal: Find top-rated hotels

tools:
  - Hotel Search API

output:
  - Hotel recommendations
```

The Orchestrator loads the required skill and executes the corresponding agent.

---

# Agent Storage Backends

## 1. State (Temporary Memory)

```python
trip_budget = 50000
```

Characteristics:

- Fast access
- Stored in memory
- Removed after execution

---

## 2. File System

Examples:

```text
itinerary.pdf
notes.txt
report.csv
```

---

## 3. Store (Persistent Memory)

Examples:

```text
User preferences
Past conversations
Saved settings
```

---

## 4. Composite Backend

```text
State + File System + Database
```

Provides flexibility and persistence.

---

# Middleware

```text
Orchestrator
     │
 Middleware
     │
 Sub-Agent
```

Responsibilities:

- Authentication
- Authorization
- Logging
- Monitoring
- Error handling
- Request validation

Think of Middleware as a **Security Guard + Auditor**.

---

# Example: Travel Planning Agent

## User Request

```text
Plan a 3-day trip to Northeast India
```

### Step 1: Planning

```text
- Hotel Search
- Flight Search
- Itinerary Creation
```

### Step 2: Agent Creation

```text
Hotel Finder Agent
Flight Search Agent
Itinerary Builder Agent
```

### Step 3: Parallel Execution

All agents execute simultaneously.

### Step 4: Collect Results

```text
Hotels
Flights
Places to Visit
```

### Step 5: Final Response

The Orchestrator combines outputs and generates the final travel plan.

---

# Interview Definition

> A Deep Agent is a multi-agent architecture where an orchestrator agent decomposes a complex task into smaller tasks, delegates them to specialized sub-agents with their own instructions, tools, and context, and combines their outputs to produce the final response.

---

# Deep Agents vs AWS AgentCore

| Deep Agent Concept | AWS AgentCore Equivalent |
|-------------------|--------------------------|
| Orchestrator | Agent Runtime |
| Sub Agents | Specialized Agents |
| State | Agent Memory |
| Persistent Store | Long-Term Memory |
| Middleware | Identity + Observability |
| Tools | AgentCore Gateway |

## Relationship

```text
Deep Agent = Architecture / Design Pattern

AWS AgentCore = Managed Platform to Build and Run Agents
```

### Example

```text
LangGraph / CrewAI
        │
        ▼
AWS AgentCore Runtime
        │
        ▼
Claude / Nova / GPT Models
```

---

# Quick Revision

## Deep Agent = Manager + Team

- Orchestrator → Manager
- Sub Agents → Specialists
- Skill File → Job Description
- State → Temporary Memory
- Store → Persistent Memory
- Middleware → Security & Monitoring
- Final Output → Combined Results

---

## Key Takeaway

If you understand the Travel Planner example, you understand the core Deep Agent architecture.

# 🚀 DeepAgents + LangGraph Studio Setup

A step-by-step guide for building AI agents using **DeepAgents**, **LangGraph Studio**, **LangSmith**, **Google Gemini**, and **LangChain Middleware**.

---

## 📋 Table of Contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Useful Resources](#useful-resources)
* [Project Setup](#project-setup)
* [Environment Configuration](#environment-configuration)
* [Create Your First Agent](#create-your-first-agent)
* [Project Structure](#project-structure)
* [LangGraph Configuration](#langgraph-configuration)
* [Run LangGraph Studio](#run-langgraph-studio)
* [Middleware](#middleware)
* [Common Commands](#common-commands)
* [Troubleshooting](#troubleshooting)
* [Learning References](#learning-references)

---

# Overview

This project demonstrates how to:

* Build AI agents using DeepAgents
* Configure LangSmith tracing
* Use Google Gemini models
* Run agents in LangGraph Studio
* Add Middleware for observability and guardrails
* Debug workflows visually

---

# Prerequisites

Before starting, ensure you have:

| Requirement          | Version  |
| -------------------- | -------- |
| Python               | 3.11+    |
| UV Package Manager   | Latest   |
| LangSmith Account    | Required |
| Google Cloud Project | Required |
| Gemini API Access    | Required |

---

# Useful Resources

## Core Frameworks

| Resource      | Link                                                       |
| ------------- | ---------------------------------------------------------- |
| LangSmith     | https://smith.langchain.com                                |
| DeepAgents    | https://docs.langchain.com/oss/python/deepagents           |
| LangGraph     | https://docs.langchain.com/oss/python/langgraph            |
| LangGraph CLI | https://docs.langchain.com/langgraph-platform/local-server |

## Middleware

| Resource            | Link                                                                |
| ------------------- | ------------------------------------------------------------------- |
| Middleware Overview | https://docs.langchain.com/oss/python/langchain/middleware/overview |
| Built-in Middleware | https://docs.langchain.com/oss/python/langchain/middleware/built-in |

## Google Gemini

| Resource                 | Link                                                                         |
| ------------------------ | ---------------------------------------------------------------------------- |
| Google GenAI Integration | https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai |
| Gemini Documentation     | https://ai.google.dev                                                        |

---

# Project Setup

## 1. Create Project Directory

```bash
mkdir deepagents
cd deepagents
```

## 2. Initialize UV Project

```bash
uv init .
```

## 3. Install Dependencies

```bash
uv add deepagents \
       langchain[google-genai] \
       python-dotenv \
       langgraph-cli[inmem]
```

---

# Environment Configuration

Create a `.env` file.

```env
PROJECT_ID=<your-google-cloud-project-id>

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your-api-key>
LANGSMITH_PROJECT=deepagents
```

---

# LangSmith Setup

1. Create a LangSmith account.
2. Generate an API key.
3. Configure the following environment variables:

```bash
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your-api-key>
LANGSMITH_PROJECT=deepagents
```

---

# Create Your First Agent

Create a file named `main.py`.

```python
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    project=os.getenv("PROJECT_ID")
)

agent = create_deep_agent(
    model=model,
    system_prompt="You are a research assistant."
)
```

---

# Project Structure

```text
deepagents/
│
├── .env
├── main.py
├── langgraph.json
├── pyproject.toml
└── .venv/
```

---

# LangGraph Configuration

Create a file named `langgraph.json`.

```json
{
  "dependencies": ".",
  "graphs": {
    "deepagent-default": "main:agent"
  }
}
```

---

# Run LangGraph Studio

Start the development server:

```bash
uv run langgraph dev
```

Once started, LangGraph Studio will be available locally.

---

# Middleware

DeepAgents supports LangChain Middleware for adding runtime controls and observability.

## Common Middleware Use Cases

* Logging
* Human Approval
* PII Detection
* Summarization
* Request Validation
* Auditing
* Security Controls
* Tool Call Monitoring

---

## Example: Summarization Middleware

```python
from langchain.middleware import SummarizationMiddleware

middleware = SummarizationMiddleware()
```

---

## Built-In Middleware

LangChain provides several prebuilt middleware components:

* SummarizationMiddleware
* HumanInTheLoopMiddleware
* PiiMiddleware
* ToolCallLimitMiddleware
* Logging Middleware
* Custom Middleware Support

Reference:

https://docs.langchain.com/oss/python/langchain/middleware/built-in

---

## Middleware Architecture

```text
User Request
      │
      ▼
 Middleware Layer
      │
 ┌────┼────┐
 ▼    ▼    ▼
PII Logging HITL
      │
      ▼
 Deep Agent
      │
      ▼
 LLM / Tools
      │
      ▼
 Response
```

---

# Common Commands

## Install Dependencies

```bash
uv sync
```

## Run Agent

```bash
uv run python main.py
```

## Run LangGraph Studio

```bash
uv run langgraph dev
```

## Upgrade Dependencies

```bash
uv lock --upgrade
uv sync
```

## View Installed Packages

```bash
uv pip list
```

---

# Troubleshooting

## Missing LangSmith API Key

Error:

```text
LANGSMITH_API_KEY not found
```

Solution:

```bash
export LANGSMITH_API_KEY=<your-key>
```

Windows:

```powershell
$env:LANGSMITH_API_KEY="<your-key>"
```

---

## Missing Google Cloud Project ID

Error:

```text
PROJECT_ID not found
```

Solution:

```env
PROJECT_ID=my-gcp-project
```

---

# Learning References

## DeepAgents

https://docs.langchain.com/oss/python/deepagents

## LangGraph

https://docs.langchain.com/oss/python/langgraph

## LangSmith

https://smith.langchain.com

## Middleware Overview

https://docs.langchain.com/oss/python/langchain/middleware/overview

## Built-In Middleware

https://docs.langchain.com/oss/python/langchain/middleware/built-in

## Google Gemini

https://ai.google.dev

---



## Backends

In Deep Agents, agents get file-like tools such as:

- ls
- read_file
- write_file
- glob
- grep

These tools do not directly decide where files are stored. The backend decides.

## References

### Official Documentation
- https://docs.langchain.com/oss/python/deepagents

### Backend Concepts

#### StateBackend
Used for:
- Temporary notes
- Current thread storage
- Session-level persistence

#### FileSystemBackend
Used for:
- Reading files from local system
- Working with project repositories
- Persistent file storage

#### Custom Backends
Examples:
- Amazon S3
- Google Cloud Storage (GCS)
- Azure Blob Storage
- Database-backed storage

Example:

```python
class S3Storage:
    ...
