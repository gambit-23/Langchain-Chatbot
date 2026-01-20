import os
from typing import List
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()


class AnswerGenerator:
    def __init__(self, model_id: str = "mistralai/Mistral-7B-Instruct-v0.2"):
        self.client = InferenceClient(
            model=model_id, token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )

    def generate_answer(self, question: str, contexts: List[str]) -> str:

        context_text = "\n\n".join(contexts)
        # pinecone returned multiple chunks, therefore we push all the text that was found as similar text for the query to the LLM
        # \n\n converts a list of text chunks into one well-formatted context string for the LLM.

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Answer the question using ONLY the provided context. "
                    "If the answer is not in the context, say you don't know."
                ),
            },
            {
                "role": "user",
                "content": f""" 
Context:
{context_text}

Question:
{question}
""",
            },
        ]

        response = self.client.chat_completion(
            messages=messages, max_tokens=300, temperature=0.3
        )

        return response.choices[0].message.content.strip()
