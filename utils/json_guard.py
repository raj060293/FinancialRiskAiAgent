import json
import re

def extract_json(text: str) -> dict:
    """
    Extracts the first JSON object found in text.
    """

    match = re.search(r"\{.*}", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON object found in response:\n{text}")

    return json.loads(match.group())


def safe_json_parse(text: str) -> dict:
    try:
        return extract_json(text)
    except Exception as e:
        raise ValueError(f"Invalid JSON from LLM:\n{text}") from e