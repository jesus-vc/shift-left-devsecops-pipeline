import tiktoken
from typing import List


def chunk_text(text: str, max_tokens: int = 300) -> List[str]:
    # Use tiktoken to count tokens (OpenAI tokenizer)
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = enc.decode(tokens[i : i + max_tokens])
        chunks.append(chunk)
    return chunks
