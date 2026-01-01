import os
from groq import Groq

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

def call_groq(prompt: str) -> str :
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role":"system", "content": "You are a fraud detection system."},
            {"role":"system", "content": prompt}
        ]
    )
    return response.choices[0].message.content