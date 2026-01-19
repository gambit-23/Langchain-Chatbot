from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(texts: List[str], chunk_size: int=500, chunk_overlap: int=100) -> List[str]:
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks:List[str]=[]

    for text in texts:
        # texts -> list of full PDF texts, text -> one complete PDF
        split_chunks=splitter.split_text(text=text)
        # split chunks takes a huge string, breaks into small chunks and returns a list
        chunks.extend(split_chunks)
        # extend flattens all chunks into one list
    return chunks