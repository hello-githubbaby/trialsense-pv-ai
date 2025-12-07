"""
Simple FAISS + SentenceTransformers vector store.
Provides basic semantic search capabilities.
"""

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class SimpleVectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.texts = []
        self.embeddings = None

    def add_texts(self, texts: list):
        embs = self.model.encode(texts, convert_to_numpy=True)

        if self.index is None:
            dim = embs.shape[1]
            self.index = faiss.IndexFlatL2(dim)
            self.embeddings = embs
        else:
            self.embeddings = np.vstack([self.embeddings, embs])

        self.index.add(embs)
        self.texts.extend(texts)

    def search(self, query: str, k=4):
        q_emb = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(q_emb, k)

        return [self.texts[i] for i in indices[0]]
