import chromadb
from chromadb.config import Settings
import os
import json

class VectorDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="data/chroma")
        self.collection = self.client.get_or_create_collection(name="itmo_knowledge")
        self.load_data()

    def load_data(self):
        if os.path.exists('data/parsed_data.json'):
            with open('data/parsed_data.json', 'r') as f:
                data = json.load(f)
                self.collection.add(
                    documents=[item['text'] for item in data],
                    metadatas=[{"url": item['url']} for item in data],
                    ids=[str(i) for i in range(len(data))]
                )

    async def search(self, query: str, top_k=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        return [
            {"text": doc, "url": meta["url"]}
            for doc, meta in zip(results["documents"][0], results["metadatas"][0])
        ]