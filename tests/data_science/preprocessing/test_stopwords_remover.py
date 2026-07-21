"""
==========================================================
TechMind
Data Science Component

Module:
    test_stopwords_remover.py

Description:
    Unit tests for the StopWordsRemover component.

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

from data_science.preprocessing.stopwords_remover import (
    StopWordsRemover,
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
# Unit Tests
# ==========================================================

def test_process_returns_processed_document():
    """
    Should return a ProcessedDocument instance.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "this is a simple test"
    )

    result = remover.process(document)

    assert isinstance(result, ProcessedDocument)


def test_remove_english_stopwords():
    """
    Should remove English stop words.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "this is a simple test",
        "en",
    )

    result = remover.process(document)

    assert result.processed_text == "simple test"


def test_remove_spanish_stopwords():
    """
    Should remove Spanish stop words.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "este es un documento de prueba",
        "es",
    )

    result = remover.process(document)

    assert result.processed_text == "documento prueba"


def test_preserve_technical_words():
    """
    Should preserve technical vocabulary.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "FastAPI Docker JWT Python",
        "en",
    )

    result = remover.process(document)

    assert result.processed_text == "FastAPI Docker JWT Python"


def test_unsupported_language_returns_original_text():
    """
    Should return original text for unsupported languages.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "ceci est un document",
        "fr",
    )

    result = remover.process(document)

    assert result.processed_text == "ceci est un document"


def test_empty_text():
    """
    Should handle empty text.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "",
        "en",
    )

    result = remover.process(document)

    assert result.processed_text == ""


def test_only_stopwords():
    """
    Should remove all stop words.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "the is a an of",
        "en",
    )

    result = remover.process(document)

    assert result.processed_text == ""


def test_case_insensitive_stopwords():
    """
    Should remove stop words regardless of case.
    """

    remover = StopWordsRemover()

    document = _create_document(
        "The API Is Running",
        "en",
    )

    result = remover.process(document)

    assert result.processed_text == "API Running"