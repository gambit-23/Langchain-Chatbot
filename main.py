from src.loaders.pdf_loader import load_pdfs_from_directory

def main()->None:
    pdf_texts=load_pdfs_from_directory("data/pdfs")

    print(f"Loaded {len(pdf_texts)} PDFs")

    if pdf_texts:
        print(f"Sample extract")
        print(pdf_texts[0][:1000])


if __name__ == "__main__":
    main()

#  the above if statement is used so that the main() function runs only when this file is executed directly and not when imported