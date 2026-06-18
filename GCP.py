from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    ai = ChatGoogleGenerativeAI(model="gemini-3.5-flash",
                                project=os.getenv("GOOGLE_CLOUD_PROJECT"))

    result = ai.invoke("What is the capital of France?")
    try:
        # Prefer pretty_print if available
        result.pretty_print()
    except Exception:
        print(result)


if __name__ == "__main__":
    main()
