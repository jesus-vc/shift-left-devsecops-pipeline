from typing import List, Optional
from .ingestion_adapters import IngestionAdapter, PlainTextAdapter


class IngestionPipeline:
    def __init__(self, adapters: Optional[List[IngestionAdapter]] = None):
        self.adapters = adapters or [PlainTextAdapter()]

    def extract_text(self, filename: str, content_type: str, file_bytes: bytes) -> str:
        for adapter in self.adapters:
            if adapter.can_handle(filename, content_type):
                return adapter.extract_text(file_bytes)
        raise ValueError(f"No adapter found for {filename} ({content_type})")


# Usage: pipeline = IngestionPipeline([PlainTextAdapter(), PDFAdapter(), ...])
