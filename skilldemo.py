from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from utils import get_model
import os
import shutil

llm = get_model()
backend = FilesystemBackend(
    root_dir="./agent_workspace",
    virtual_mode=True
)

prompt = """
You are a technical article writing agent with skills.
Pick a right skill for acheiving the goal

Workflow:
1. create a short plan with todos and write all the todos to /todos.md
2. Use the tool to get article points
3. write rough notes /notes.md
4. Write the final article to /article.md
5. Return a short summary and mention the files created.

"""

# Ensure skills are available inside the backend root so SkillsMiddleware accepts them
#skills_src = os.path.abspath("./skills")
#skills_dest = os.path.abspath(os.path.join("./agent_workspace", "skills"))
#if os.path.isdir(skills_src) and not os.path.isdir(skills_dest):
 #   shutil.copytree(skills_src, skills_dest)

agent = create_deep_agent(
    model=llm,
    backend=backend,
    skills=["./skills/"],
    system_prompt=prompt,
)

if __name__ == "__main__":
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Write an python program to merge two sorted lists."
                }
            ]
        }
    )
    result["messages"][-1].pretty_print()