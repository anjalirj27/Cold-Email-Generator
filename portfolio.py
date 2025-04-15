import pandas as pd
import chromadb
import uuid
import os

class Portfolio:
    def __init__(self, file_path=None):
        # Use a safe default file path with raw string to avoid escape issues
        if file_path is None:
            file_path = r"E:\Projects\app\resources\my_portfolio.csv"

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Portfolio file not found at: {file_path}")

        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient(path="vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
        self.loaded = False  # flag to prevent reloading

    def load_portfolio(self):
        # Prevent reloading if already loaded or collection is not empty
        if self.loaded or self.collection.count() > 0:
            return

        for _, row in self.data.iterrows():
            try:
                self.collection.add(
                    documents=[row["Techstack"]],  # Must be a list
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )
            except Exception as e:
                print(f"Error adding document: {e}")
        self.loaded = True  # Mark as loaded

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
