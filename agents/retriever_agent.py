# agents/retriever_agent.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # 384 is embedding size for this model
        self.texts = []

    def add_documents(self, documents):
        """
        documents: List of strings (titles/summaries of earnings news)
        """
        self.texts.extend(documents)
        embeddings = self.model.encode(documents)
        self.index.add(np.array(embeddings))

    def retrieve(self, query, top_k=3):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), top_k)
        return [self.texts[i] for i in indices[0]]

# Test
if __name__ == "__main__":
    docs = [
        "TCS Q4 earnings beat expectations with 9% profit growth.",
        "Infosys misses revenue targets in Q1 due to global slowdown.",
        "Wipro posts strong Q3 results backed by cloud deals."
    ]
    agent = RetrieverAgent()
    agent.add_documents(docs)

    query = "What are the latest earnings results of Indian tech companies?"
    results = agent.retrieve(query)

    print("🔍 Retrieved Info:")
    for r in results:
        print(f"- {r}")
