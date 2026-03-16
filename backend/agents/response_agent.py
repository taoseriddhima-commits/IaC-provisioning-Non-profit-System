#  Response Generator Agent

from langchain_openai import ChatOpenAI
from backend.config import OPENAI_API_KEY, OPENAI_BASE_URL
from backend.utils.prompts import RESPONSE_PROMPT


def generate_response(message: str, classification: dict, entities: dict):
    """
    Generates a draft response for the user based on message, classification, and extracted entities.
    """

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",
        temperature=0.3,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL
    )

    prompt = RESPONSE_PROMPT.format(
        message=message,
        classification=classification,
        entities=entities
    )

    response = llm.invoke(prompt)
    return response.content.strip()
