from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()


google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment!")

# ------LLM INITIALIZATION ---
# Initialize ChatGoogleGenerativeAI with  API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    google_api_key=google_api_key
    
)

# Agent function 
def agent_2(user_query, location=None):
    prompt = f"The user asked: '{user_query}'. The user's location is: '{location or 'Unknown'}'. Give tenancy advice accordingly."
    response = llm.invoke(prompt)
    # Extract content from the response object
    return response.content 
