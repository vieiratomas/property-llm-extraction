from langchain_openai import ChatOpenAI
from config import API_KEY

def create_llm_client():
    return ChatOpenAI(
        model_name="gpt-4",
        temperature=0.0,
        openai_api_key=API_KEY
    )
