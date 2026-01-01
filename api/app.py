from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import process_transaction

app = FastAPI(
    title = "Autonomous Financial Risk Agent",
    description = "Real-time AI-powered transaction risk analysis",
    version = "1.0.0"

)

#Request Schema
class Transaction(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    currency: str
    merchant: str
    country: str

@app.post("/analyze")
def analyze_transaction(txn: Transaction):
    try:
        result = process_transaction(txn.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



