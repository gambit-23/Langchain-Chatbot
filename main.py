from src.loaders.pdf_loader import load_pdfs_from_directory
from src.processing.chunker import chunk_text
from src.embeddings.hf_embeddings import HuggingFaceEmbeddingModel
from src.vectorstore.pinecone_store import PineconeVectorStore

def main()->None:
    pdf_texts=load_pdfs_from_directory("data/pdfs")
    print(f"Loaded {len(pdf_texts)} PDFs")

    chunks=chunk_text(pdf_texts)
    print(f"Generated {len(chunks)} text chunks")

    embedder=HuggingFaceEmbeddingModel()
    embeddings=embedder.embed_texts(chunks)
    print(f"Generated {len(embeddings)} embeddings")
    print(f"Embedding vector length: {len(embeddings[0])}")
    # if pdf_texts:
    #     print(f"Sample extract")
    #     print(pdf_texts[0][:1000])

    # if chunks:
    #     print("Sample chunks")
    #     print(chunks[1])

    vector_store=PineconeVectorStore(dimension=len(embeddings[0]))
    vector_store.upsert_vectors(embeddings, chunks)

    query="What is attention mechanism?"
    query_embedding=embedder.embed_texts([query])[0]

    results=vector_store.query(query_embedding=query_embedding)
    print(results)

    for match in results["matches"]:
        print(match["metadata"]["text"][:300])
        print("-"*50)

if __name__ == "__main__":
    main()

#  the above if statement is used so that the main() function runs only when this file is executed directly and not when imported