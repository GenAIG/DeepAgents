from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    project=os.getenv('GOOGLE_CLOUD_PROJECT')
)

agent = create_deep_agent(
    model=llm,
    system_prompt="You are a helpful assistant that can answer questions about the weather.",
)
