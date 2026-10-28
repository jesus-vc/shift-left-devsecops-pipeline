from pydantic import BaseModel
from typing import List, Optional


class DocumentUpload(BaseModel):
    filename: str
    content: str


class ChunkResponse(BaseModel):
    id: int
    content: str
    similarity: Optional[float] = None


class QuestionRequest(BaseModel):
    chunk_ids: List[int]
    question: str


class AnswerEvaluationRequest(BaseModel):
    question: str
    answer: str
    context: str


class AnswerEvaluationResponse(BaseModel):
    is_correct: bool
    feedback: str
