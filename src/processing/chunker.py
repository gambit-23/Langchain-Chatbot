from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(texts: List[str], chunk_size: int=500, chunk_overlap: int=100) -> List[str]:
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks:List[str]=[]

    for text in texts:
        split_chunks=splitter.split_text(text=text)
        chunks.extend(split_chunks)
    return chunks