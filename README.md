Bedrock: https://docs.langchain.com/oss/python/integrations/chat/bedrock#installation
Create Agent: https://reference.langchain.com/python/langchain/agents/factory/create_agent
Deep Agent: https://docs.langchain.com/oss/python/deepagents/customization

Deep Agents (Simple Explanation)

Deep Agents is a framework from LangChain for building AI agents that can work on complex tasks over a long period of time, similar to coding assistants like Claude Code or Manus.

Think of a Deep Agent as an AI employee that can:

    Plan work
    Break tasks into steps
    Use tools
    Remember information
    Create and edit files
    Delegate work to sub-agents
    Continuously improve its plan

Core Components
1. Models

The brain of the agent.

Examples:

    Google Gemini:
         model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
    OpenAI
    Anthropic Claude

Memory

Allows the agent to remember previous conversations or task progress.

Without memory:

Agent forgets after every request.

With memory:

Agent remembers context and past decisions.

Planning

Before acting, the agent creates a plan.

Agent plan:

1. Create project structure
2. Create Flask app
3. Create routes
4. Add templates
5. Test application

TODOS:
Task management for the agent.

☐ Create API
☐ Write tests
☐ Deploy application
☑ Setup project

Skills:

Skill: Python Coding
Skill: AWS Deployment
Skill: Kubernetes Troubleshooting

Subagents:

Main Agent
│
├── Research Agent
├── Coding Agent
└── Testing Agent

File System Access:
The agent can read and write files

project/
├── app.py
├── requirements.txt
└── README.md

The agent can:

Create files
Modify files
Read files
Organize projects

Real-World Example

Suppose you ask:

Create a Python application that reads AWS CloudWatch logs and stores them in Elasticsearch.

A Deep Agent may:

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


| Simple Agent          | Deep Agent             |
| --------------------- | ---------------------- |
| One response          | Multi-step workflow    |
| Minimal memory        | Long-term memory       |
| Few tools             | Many tools             |
| No planning           | Built-in planning      |
| No task tracking      | Todos                  |
| Single worker         | Subagents              |
| Limited file handling | Full project workspace |
| Short tasks           | Long-running tasks     |


Summary:

Chatbot = Answers questions.
Agent = Can use tools.
Deep Agent = Acts like a project engineer that plans, tracks tasks, uses tools, creates files, delegates work, and completes complex projects end-to-end.

Since you're learning DevOps, AWS, Jenkins, EKS, and Python, Deep Agents are especially useful for automating workflows such as:

CI/CD pipeline creation
Terraform generation
Kubernetes troubleshooting
AWS infrastructure setup
Log analysis using Datadog or Splunk
End-to-end project scaffolding and code generation.