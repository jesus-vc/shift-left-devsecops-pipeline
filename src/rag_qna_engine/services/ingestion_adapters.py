from abc import ABC, abstractmethod


class IngestionAdapter(ABC):
    @abstractmethod
    def can_handle(self, filename: str, content_type: str) -> bool:
        pass

    @abstractmethod
    def extract_text(self, file_bytes: bytes) -> str:
        pass


class PlainTextAdapter(IngestionAdapter):
    def can_handle(self, filename: str, content_type: str) -> bool:
        return filename.endswith(".txt") or content_type == "text/plain"

    def extract_text(self, file_bytes: bytes) -> str:
        return file_bytes.decode(errors="ignore")


# Future: PDFAdapter, TranscriptAdapter, etc.
