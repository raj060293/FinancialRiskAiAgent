import config.env
from rag.seed_data import seed_knowledge_if_needed

if __name__ == "__main__":
    print("▶ Calling seed_knowledge_if_needed()")
    seed_knowledge_if_needed()
