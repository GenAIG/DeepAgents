from deepagents import create_deep_agent
from utils import get_model
from todotools import (
    time_tool,
    news_tool,
    location_info_tool,
    food_recommendation_tool,
    weather_tool,
)


llm = get_model()


agent = create_deep_agent(
    model=llm,
    tools=[weather_tool, time_tool, location_info_tool, food_recommendation_tool],
    system_prompt=(
        "You are a helpful agent that can assist with location info, weather,"
        " food recommendations, news and time queries."
    ),
)


if __name__ == "__main__":
    TASK = "Can you provide the weather report in Hyderabad? Also, what are some good food places there? And what's the current time? Also, can you tell me a bit about the city? And finally, what's the latest news there?"
    # Invoke the agent with a user message
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": TASK}
        ]
    })

    # Print returned messages (use pretty_print when available)
    messages = result.get("messages") if isinstance(result, dict) else getattr(result, "messages", None)
    if not messages:
        print("No messages returned:", result)
    else:
        for msg in messages:
            try:
                if hasattr(msg, "pretty_print"):
                    msg.pretty_print()
                else:
                    print(msg)
            except Exception:
                print(msg)
