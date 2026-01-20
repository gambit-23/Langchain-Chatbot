import os
from typing import List
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()


class PineconeVectorStore:
    def __init__(self, dimension: int):
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        # creates pinecone client object

        self.index_name = os.getenv("PINECONE_INDEX_NAME")

        if (
            self.index_name not in self.pc.list_indexes().names()
        ):  # -> creates index only if it doesn't exist
            self.pc.create_index(
                name=self.index_name,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws", region=os.getenv("PINECONE_ENVIRONMENT_REGION")
                ),
            )

        self.index = self.pc.Index(self.index_name)
        # this returns a reference to the pinecone index, and is then stored in self.index

    def upsert_vectors(
        self, embeddings: List[List[float]], texts: List[str], batch_size: int = 100
    ) -> None:
        total = len(embeddings)
        # batch_size-> max vectors per request
        # total tells how many vectors need to be uploaded

        for start in range(0, total, batch_size):
            # starts with 0, moves till the total with a gap/jump of the batch_size
            end = start + batch_size

            batch_vectors = []

            for i in range(start, min(end, total)):
                clean_vector = [float(x) for x in embeddings[i]]
                # explicitly casted each value to float before upserting since Pinecone requires Python floats, and the model returned NumPy scalar types
                batch_vectors.append(
                    {
                        "id": f"chunk-{i}",
                        "values": clean_vector,
                        "metadata": {"text": texts[i]},
                    }
                )

        # print(type(embeddings))
        # print(type(embeddings[0]))
        # print(type(embeddings[0][0]))

        self.index.upsert(vectors=batch_vectors)

    def query(self, query_embedding: List[float], top_k: int = 3):
        return self.index.query(
            vector=query_embedding, top_k=top_k, include_metadata=True
        )
