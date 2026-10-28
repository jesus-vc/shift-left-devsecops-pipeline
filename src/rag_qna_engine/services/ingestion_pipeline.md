"""
Ingestion Pipeline Documentation
===============================

Overview:
---------
The IngestionPipeline provides a flexible, pluggable way to extract text from various file types (plain text, PDF, transcripts, etc.) for downstream processing.

Key Components:
---------------
- IngestionAdapter (abstract): Interface for file-type-specific adapters.
- PlainTextAdapter: Handles .txt and text/plain files.
- IngestionPipeline: Orchestrates adapters and selects the right one for each file.

Usage:
------
1. Instantiate the pipeline (optionally with custom adapters):

    pipeline = IngestionPipeline([PlainTextAdapter()])

2. Extract text from a file:

    text = pipeline.extract_text(filename, content_type, file_bytes)

3. Add new adapters (e.g., PDFAdapter) by implementing IngestionAdapter.

Testing:
--------
- See test_ingestion_pipeline.py for a simple test of plain text extraction.

Extensibility:
--------------
- Add new adapters for more file types without changing pipeline logic.
"""
