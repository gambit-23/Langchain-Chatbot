from typing import List
from sentence_transformers import SentenceTransformer

class HuggingFaceEmbeddingModel:
    def __init__(self, model_name: str="sentence-transformers/all-MiniLM-L6-v2"):
        self.model=SentenceTransformer(model_name_or_path=model_name)
        # when a new object is created, embedder=model(), init runs once per object creation, now calling the methods inside this class, it resues the same model that the object carries using self.

    def embed_texts(self, texts: List[str])->List[List[float]]:
        embeddings=self.model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()
    # embeddings return a numpy array, so to convert it into a python list we do .tolist()
    
