from rag.chroma_client import collection
from services.embedding_client import get_embedding

SEED_MARKER_ID = "__seed_completed__"
def seed_knowledge_if_needed():
    existing = collection.get(ids=[SEED_MARKER_ID])

    if existing and existing["ids"]:
        print("Knowledge already seeded. Skipping....")
        return
    print("Seeding knowledge base...")

    documents = [
        {
            "id": "rule_1",
            "text": "Transactions above 80,000 INR to crypto exchanges are high risk.",
            "metadata": {"type": "rule"}
        },
        {
            "id": "rule_2",
            "text": "Foreign country transactions without prior history are risky.",
            "metadata": {"type": "rule"}
        },
        {
            "id": "cust_99_1",
            "text": "Customer cust_99 was previously flagged for suspicious crypto activity.",
            "metadata": {"type": "customer", "customer_id": "cust_99"}
        }
    ]

    for doc in documents:
        embedding = get_embedding(doc["text"])
        collection.add(
            documents = doc["text"],
            embeddings= [embedding],
            metadatas=[doc["metadata"]],
            ids = [doc["id"]]
        )

    collection.add(
        documents=["Knowledge base seeded"],
        embeddings=[get_embedding("seed marker")],
        ids = [SEED_MARKER_ID]
    )

    print("Knowledge seeding completed")

