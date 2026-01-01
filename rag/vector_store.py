from rag.chroma_client import collection
from services.embedding_client import get_embedding


class VectorStore:
    """
    Chroma-backed vector store abstraction
    """

    # --------ADD-------
    def add_document(self, *, doc_id: str, text: str, metadata: dict | None = None,):
        embedding = get_embedding(text)
        collection.add(
            ids = [doc_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}]
        )

    # --------QUERY-------
    def query(self, *, query_text: str, top_k: int=5, where: dict | None=None) -> list[str]:
        query_embedding = get_embedding(query_text)
        results = collection.query(
            query_embeddings = [query_embedding],
            n_results=top_k,
            where=where
        )
        return results.get("documents", [[]])[0]

    # --------DELETE BY ID-------
    def delete_by_id(self, doc_id: str):
        """
        Delete a single document by id
        """

        collection.delete(ids = [doc_id])

    # --------DELETE BY METADATA-------
    def delete_by_metadata(self, where: dict):
        """
        Delete documents matching metadata filter.
        Example:
            {"customer_id": "cust_99"}
        """
        collection.delete(where=where)

    # --------FULL RESET-------
    def clear_all(self):
        """
        Completely wipes the collection
        """
        collection.delete(where={})
