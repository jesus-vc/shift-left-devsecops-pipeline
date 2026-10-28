from sqlalchemy.orm import Session
from ..models.db_models import Document, Chunk
from ..database.db import SessionLocal
from typing import List
from sqlalchemy import text


def store_document_and_chunks(filename: str, chunks: List[str], embeddings: List[list]):
    db: Session = SessionLocal()
    doc = Document(filename=filename)
    db.add(doc)
    db.flush()  # get doc.id
    for chunk, emb in zip(chunks, embeddings):
        db.add(Chunk(document_id=doc.id, content=chunk, embedding=emb))
    db.commit()
    db.close()


def search_chunks(query_embedding: list, top_k: int = 5) -> List[Chunk]:
    db: Session = SessionLocal()
    sql = text(
        """
        SELECT *, (embedding <#> :query_embedding) AS distance
        FROM chunks
        ORDER BY distance ASC
        LIMIT :top_k
    """
    )
    result = db.execute(sql, {"query_embedding": query_embedding, "top_k": top_k})
    chunks = [Chunk(**row._mapping) for row in result]
    db.close()
    return chunks
