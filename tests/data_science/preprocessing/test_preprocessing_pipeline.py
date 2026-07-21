"""
==========================================================
TechMind
Data Science Component

Module:
    test_preprocessing_pipeline.py

Description:
    Integration tests for the PreprocessingPipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)

from data_science.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)


# ==========================================================
# Test Helpers
# ==========================================================

def _create_document(
    text: str,
    language: str = "en",
) -> DocumentRecord:
    """
    Creates a sample DocumentRecord for testing.
    """

    return DocumentRecord(
        document_id="DOC-001",
        source="unit-test",
        title="Sample Document",
        text=text,
        category="Backend",
        language=language,
    )


# ==========================================================
# Integration Tests
# ==========================================================

def test_pipeline_returns_processed_document():
    """
    Should return a ProcessedDocument instance.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "FastAPI is AWESOME."
    )

    result = pipeline.process(document)

    assert isinstance(result, ProcessedDocument)


def test_pipeline_generates_processed_text():
    """
    Should generate processed text.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "FastAPI is AWESOME."
    )

    result = pipeline.process(document)

    assert isinstance(result.processed_text, str)


def test_pipeline_generates_tokens():
    """
    Should generate tokens.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "FastAPI uses JWT."
    )

    result = pipeline.process(document)

    assert len(result.tokens) > 0


def test_pipeline_generates_lemmas():
    """
    Should generate lemmas.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "cars use Docker"
    )

    result = pipeline.process(document)

    assert len(result.lemmas) > 0


def test_pipeline_handles_empty_text():
    """
    Should process empty text without errors.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        ""
    )

    result = pipeline.process(document)

    assert result.processed_text == ""
    assert result.tokens == []
    assert result.lemmas == []


def test_pipeline_preserves_document():
    """
    Should preserve the original document.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "FastAPI Docker"
    )

    result = pipeline.process(document)

    assert result.document["document_id"] == "DOC-001"


def test_pipeline_handles_spanish():
    """
    Should process Spanish documents.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "Este es un documento de prueba",
        "es",
    )

    result = pipeline.process(document)

    assert isinstance(result.processed_text, str)


def test_pipeline_complete_execution():
    """
    Should execute the complete preprocessing pipeline.
    """

    pipeline = PreprocessingPipeline()

    document = _create_document(
        "FastAPI uses JWT with Docker containers."
    )

    result = pipeline.process(document)

    assert isinstance(result, ProcessedDocument)
    assert isinstance(result.processed_text, str)
    assert isinstance(result.tokens, list)
    assert isinstance(result.lemmas, list)