from rag.vector_store import VectorStore

vector_store = VectorStore()

def retrieve_context(transaction: dict) -> str:
    query_text = f"""
    Customer ID: {transaction['customer_id']}
    Amount: {transaction['amount']}
    Merchant: {transaction['merchant']}
    Country: {transaction['country']}
"""
    docs = vector_store.query(
        query_text = query_text,
        top_k=5
    )

    return "\n".join(docs)