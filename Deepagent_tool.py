from deepagents import create_deep_agent
from langchain.tools import tool
from langchain.agents.middleware import PIIMiddleware

from utils import get_model

llm = get_model()

@tool
def weather_tool(location: str) -> str:
    """
    A tool that provides weather information for a given location.
    """
    # Here you would implement the logic to fetch weather data for the given location.
    # For demonstration purposes, we'll return a placeholder response.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


@tool
def complex_tool(payload: str) -> str:
    """
    A more complex tool for advanced processing.

    Accepts a JSON-like string describing a task, and returns a summary of the
    requested processing. Replace the placeholder logic with real integrations
    (databases, external APIs, heavy computation) as needed.
    """
    # Placeholder: echo back a transformed summary
    # Example payload could be: "analyze: sentiment of 'I love coding'"
    summary = f"Processed complex request: {payload}"
    return summary

agent = create_deep_agent(
    model=llm,
    tools=[weather_tool, complex_tool],
    system_prompt=(
        "You are a helpful assistant that can answer questions about the weather "
        "and perform complex processing tasks via the complex tool."
    ),
    middleware=[
        PIIMiddleware(
            "email",
            strategy="mask",
            apply_to_input=True,
            apply_to_output=True,
            apply_to_tool_results=True,
        ),
        PIIMiddleware(
            "credit_card",
            strategy="mask",
            apply_to_input=True,
            apply_to_output=True,
            apply_to_tool_results=True,
        ),
    ]
)

