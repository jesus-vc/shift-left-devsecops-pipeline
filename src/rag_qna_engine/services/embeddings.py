import openai
import os
from typing import List


def get_embeddings(texts: List[str]) -> List[list]:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Embedding.create(input=texts, model="text-embedding-ada-002")
    return [d["embedding"] for d in response["data"]]
