from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        project=os.getenv('GOOGLE_CLOUD_PROJECT')
    )
