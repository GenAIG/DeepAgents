<<<<<<< HEAD
from langchain.agents import create_agent
#from langchain_aws import ChatBedrockConverse
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json
load_dotenv()

@tool()
def add(a: int|float, b: int|float) -> int|float:
    """Adds two numbers together.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Sum of two numbers

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b
@tool()
def subtract(a: int|float, b: int|float) -> int|float:
    """Subtracts two numbers.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Difference of two numbers

    Examples:
        >>> subtract(5, 2)
        3
    """
    return a - b
@tool()
def multiply(a: int|float, b: int|float) -> int|float:
    """Multiplies two numbers.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Product of two numbers

    Examples:
        >>> multiply(2, 3)
        6
    """
    return a * b

@tool()
def divide(a: int|float, b: int|float) -> int|float:
    """Divides two numbers.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Quotient of two numbers

    Examples:
        >>> divide(6, 2)
        3.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def model():
    ai = ChatGoogleGenerativeAI(model="gemini-3.5-flash",
                                project=os.getenv("GOOGLE_CLOUD_PROJECT"))
    agent = create_agent(
        model=ai, 
        tools=[add, subtract, multiply, divide])
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "What is 5 plus 3?"
            }
        ]
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    model()
=======
from langchain.agents import create_agent
#from langchain_aws import ChatBedrockConverse
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json
load_dotenv()

@tool()
def add(a: int|float, b: int|float) -> int|float:
    """Adds two numbers together.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Sum of two numbers

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b
@tool()
def subtract(a: int|float, b: int|float) -> int|float:
    """Subtracts two numbers.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Difference of two numbers

    Examples:
        >>> subtract(5, 2)
        3
    """
    return a - b
@tool()
def multiply(a: int|float, b: int|float) -> int|float:
    """Multiplies two numbers.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Product of two numbers

    Examples:
        >>> multiply(2, 3)
        6
    """
    return a * b

@tool()
def divide(a: int|float, b: int|float) -> int|float:
    """Divides two numbers.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Quotient of two numbers

    Examples:
        >>> divide(6, 2)
        3.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def model():
    ai = ChatGoogleGenerativeAI(model="gemini-3.5-flash",
                                project=os.getenv("GOOGLE_CLOUD_PROJECT"))
    agent = create_agent(
        model=ai, 
        tools=[add, subtract, multiply, divide])
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "What is 5 plus 3?"
            }
        ]
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    model()
>>>>>>> 31a4bb9f3242bee215c7793706c4f3462f262e3e
