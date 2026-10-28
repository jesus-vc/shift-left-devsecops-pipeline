import pytest
from rag_qna_engine.services.ingestion_pipeline import IngestionPipeline


class DummyFile:
    def __init__(
        self,
        content: bytes,
        filename: str = "test.txt",
        content_type: str = "text/plain",
    ):
        self.content = content
        self.filename = filename
        self.content_type = content_type


def test_plain_text_adapter():
    pipeline = IngestionPipeline()
    dummy = DummyFile(b"Hello world!\nThis is a test.")
    text = pipeline.extract_text(dummy.filename, dummy.content_type, dummy.content)
    assert "Hello world!" in text
    assert "test" in text


if __name__ == "__main__":
    pytest.main()
