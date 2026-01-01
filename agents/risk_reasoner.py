import json

from rag.context_retriever import retrieve_context
from services.openai_client import call_gpt
from utils.json_guard import safe_json_parse
from utils.retry import retry_call


def reason_risk(transaction: dict, detection: dict) -> dict:
    """
    Uses GPT to deeply analyze a risky transaction
    and provide explanation + risk score.
    """

    context = retrieve_context(transaction)
    prompt = f"""
    You are a senior financial risk officer
    Transaction:
    
    Relevant Context(rules + history)
    {context}
    {json.dumps(transaction, indent=2)}
    
    Initial Risk Detection:
    {json.dumps(detection, indent=2)}
    
    Your task:
    1. Explain why this transaction is risky
    2. Assign a risk score(0-100)
    3. Recommend an action
    
    Respond ONLY with valid JSON
    
    Format:
    {{
        "risk_score":0,
        "explanation": "string",
        "recommended_action": "ALLOW | ESCALATE | BLOCK"
    }}
"""
    raw = retry_call(lambda : call_gpt(prompt))
    return safe_json_parse(raw)
