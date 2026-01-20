# 📄 Document Search Assistant (RAG-based)

A **Retrieval-Augmented Generation (RAG)** system built from scratch using **HuggingFace models** and **Pinecone** to answer questions grounded in real documents (Google & Microsoft 10-K 2024 reports).

This project was intentionally built **without LangChain abstractions** at first, to deeply understand how each component works internally.

---

## 🚀 Features (Up to Phase 5)

* 📂 PDF ingestion (static PDFs)
* ✂️ Intelligent text chunking
* 🔢 HuggingFace embeddings (Sentence Transformers)
* ☁️ Cloud vector storage using Pinecone
* 🔍 Semantic search (vector similarity)
* 🤖 Answer generation using Mistral (HuggingFace)
* 🧠 Fully grounded answers (no hallucination)
* 🧱 Modular, OOP-based architecture

---

## 🧠 Architecture Overview

```
PDFs
 → Loader
 → Chunker
 → Embeddings
 → Pinecone Vector Store
 → Retriever
 → LLM (Mistral)
 → Answer
```

Each responsibility is isolated into its own module for clarity and scalability.

---

## 📁 Project Structure

```
document-search-assistant/
│
├── data/
│   └── pdfs/                  # Google & Microsoft 10-K PDFs (not committed)
│
├── src/
│   ├── loaders/
│   │   └── pdf_loader.py      # PDF text extraction (PyMuPDF)
│   │
│   ├── processing/
│   │   └── chunker.py         # Text chunking logic
│   │
│   ├── embeddings/
│   │   └── hf_embeddings.py   # HuggingFace embedding model
│   │
│   ├── vectorstore/
│   │   └── pinecone_store.py  # Pinecone index, upsert & query
│   │
│   ├── llm/
│   │   └── answer_generator.py # Mistral-based answer generation
│
├── main.py                    # Orchestrates the full RAG pipeline
├── requirements.txt
├── .env                       # API keys (not committed)
└── README.md
```

---

## ⚙️ Tech Stack

* **Language**: Python 3.10+
* **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
* **LLM**: `mistralai/Mistral-7B-Instruct-v0.2`
* **Vector DB**: Pinecone (Serverless)
* **PDF Parsing**: PyMuPDF (`fitz`)
* **Inference**: HuggingFace Inference API

---

## 🔑 Environment Variables

Create a `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxx
PINECONE_API_KEY=pcsk_xxxxxxxxxxxxx
PINECONE_ENV=us-east-1
PINECONE_INDEX_NAME=document-search-poc
```

---

## ▶️ How to Run (Phase 5)

```bash
# create & activate venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run the pipeline
python main.py
```

---

## 🧪 What Happens When You Run It

1. PDFs are loaded from `data/pdfs`
2. Text is chunked into ~500-800 character segments
3. Each chunk is converted into a 384-dim vector
4. Vectors are stored in Pinecone (batched upserts)
5. User query is embedded
6. Pinecone retrieves top-K relevant chunks
7. Retrieved chunks are passed as **context**
8. Mistral generates a grounded answer

---

## 🧠 Key Concepts Learned (So Far)

* How RAG works internally (no black boxes)
* Why batching is required for vector DBs
* Difference between embeddings and vectors
* How `__init__` and object state matter in ML systems
* Why context formatting (`"\n\n".join(contexts)`) matters
* How to debug real Pinecone & HuggingFace API errors
* Difference between `text_generation` vs `chat_completion`

---

## 🧾 Example Query

```text
What is the policy regarding incentive compensation recovery?
```

The answer is generated **only** from Google & Microsoft 10-K filings, not from the model’s training data.

---

## 🔮 Future Improvements

### 🚧 Phase 6 - API & UI Layer

* Convert pipeline into **FastAPI backend**
* Add `/query` endpoint
* Add request/response schemas
* Build **Streamlit UI** for interaction
* Support live user queries
* Improve error handling & logging

---

### 🚧 Phase 7 - Production Readiness

* Upload PDFs dynamically (user uploads)
* Add document metadata:

  * company name
  * year
  * source
* Add **citations per answer**
* Introduce `src/qa/` RAG orchestration layer
* Dockerize the application
* CI/CD with GitHub Actions
* Optional: migrate to LangChain or LlamaIndex (with understanding)

---

## 🎤 Interview-Ready Summary

> “I built a full RAG system using HuggingFace embeddings, Pinecone for semantic retrieval, and a Mistral-based LLM for grounded answer generation. I implemented the pipeline manually to deeply understand each component before adding abstractions.”

---

## ✅ Status

* ✔ Phase 1-5: **Completed**
* 🔜 Phase 6-7: **Planned**