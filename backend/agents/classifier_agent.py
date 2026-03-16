#  Classification Agent

import json
from langchain_openai import ChatOpenAI
from backend.config import OPENAI_API_KEY, OPENAI_BASE_URL
from backend.utils.prompts import CLASSIFICATION_PROMPT


def classify_message(message: str):
    """
    Takes cleaned message and returns:
    {
        "urgency": "...",
        "intent": "..."
    }
    """

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",
        temperature=0,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL
    )

    prompt = CLASSIFICATION_PROMPT.format(message=message)

    response = llm.invoke(prompt)

    raw_output = response.content.strip()

    print("RAW LLM OUTPUT:")
    print(raw_output)
    print("----")

    # Remove markdown code fences if present
    if raw_output.startswith("```"):
        raw_output = raw_output.replace("```json", "")
        raw_output = raw_output.replace("```", "")
        raw_output = raw_output.strip()

    try:
        result = json.loads(raw_output)
        return result
    except json.JSONDecodeError:
        return {
            "urgency": "Unknown",
            "intent": "Unknown"
        }
