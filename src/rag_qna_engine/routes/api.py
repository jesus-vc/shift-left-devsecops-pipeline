from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.chunking import chunk_text
from ..services.embeddings import get_embeddings
from ..services.storage import store_document_and_chunks, search_chunks
from ..services.llm import generate_questions, evaluate_answer
from ..models.pydantic_models import (
    ChunkResponse,
    QuestionRequest,
    AnswerEvaluationRequest,
    AnswerEvaluationResponse,
)
from ..services.ingestion_pipeline import IngestionPipeline
from typing import List

router = APIRouter()


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    pipeline = IngestionPipeline()  # Add adapters as needed
    try:
        content = pipeline.extract_text(file.filename, file.content_type, file_bytes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    chunks = chunk_text(content)
    embeddings = get_embeddings(chunks)
    store_document_and_chunks(file.filename, chunks, embeddings)
    return {"message": "Document uploaded and processed."}


@router.post("/search", response_model=List[ChunkResponse])
def search(query: str):
    query_embedding = get_embeddings([query])[0]
    chunks = search_chunks(query_embedding)
    return [ChunkResponse(id=c.id, content=c.content) for c in chunks]


@router.post("/generate-questions")
def generate_questions_route(req: QuestionRequest):
    # For demo, just concatenate chunk contents
    context = " ".join([c.content for c in search_chunks([req.chunk_ids])])
    questions = generate_questions(context)
    return {"questions": questions}


@router.post("/evaluate-answer", response_model=AnswerEvaluationResponse)
def evaluate_answer_route(req: AnswerEvaluationRequest):
    result = evaluate_answer(req.question, req.answer, req.context)
    return AnswerEvaluationResponse(**result)
