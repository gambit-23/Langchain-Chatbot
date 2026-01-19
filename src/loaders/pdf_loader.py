from pathlib import Path
# path helps work with file paths cleanly

import fitz
# fitz-> import PyMuPDF functionality

from typing import List

def load_pdfs_from_directory(directory_path: str)->List[str]:
    # input -> path to a folder, i.e., string
    # output -> list of extracted text, i.e., list of strings

    texts: List[str] =[]
    # empty list to store extracted text

    pdf_dir=Path(directory_path)
    # to represent the folder that is given as the input

    for pdf_file in pdf_dir.glob("*.pdf"):
        # this above line gives all files ending with .pdf, glob is regex for filenames -> file matching
        with fitz.open(pdf_file) as doc:
            full_text="" #-> to store all the pages text combined
            for page in doc:
                full_text+=page.get_text() # -> extract text from that page, and appends to the empty list
            texts.append(full_text)
    return texts



