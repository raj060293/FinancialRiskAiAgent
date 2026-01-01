import json
from services.groq_client import call_groq
from services.openai_client import call_gpt
from utils.json_guard import safe_json_parse
from utils.retry import retry_call


def detect_risk(transaction: dict) -> dict:
    prompt = f"""
YOU MUST RESPOND WITH VALID JSON ONLY.
DO NOT ASK QUESTIONS.
DO NOT ADD ANY TEXT.    
Analyze the transaction below.

Transaction:
{json.dumps(transaction, indent=2)}

RETURN JSON:
{{
  "risk_level": "LOW | MEDIUM | HIGH",
  "signals": ["string"]
}}
"""
    try:
        raw = retry_call(lambda : call_groq(prompt))
        #print(f"Groq response is {raw}", raw)
        return safe_json_parse(raw)

    except Exception as e:
        print("Fallback Groq failed, switching to GPT:", e)


    raw = retry_call(lambda : call_gpt(prompt))
    return safe_json_parse(raw)
