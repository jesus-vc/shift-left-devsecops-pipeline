from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import VECTOR
from sqlalchemy.orm import relationship
from ..database.db import Base


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    chunks = relationship("Chunk", back_populates="document")


class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    content = Column(String, nullable=False)
    embedding = Column(VECTOR(1536))  # OpenAI embedding size
    document = relationship("Document", back_populates="chunks")
