from langchain.agents import create_agent
from langchain_aws import ChatBedrockConverse
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    model = ChatBedrockConverse(
        model="us.amazon.nova-lite-v1:0",
    )
    result = model.invoke("What is capital of France")
    result.pretty_print()


if __name__ == "__main__":
    main()