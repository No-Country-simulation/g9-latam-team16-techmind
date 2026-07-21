"""
==========================================================
TechMind
Data Science Component

Module:
    test_lemmatizer.py

Description:
    Unit tests for the Lemmatizer component.

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

from data_science.preprocessing.lemmatizer import (
    Lemmatizer,
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

    lemmatizer = Lemmatizer()

    document = _create_document(
        "running"
    )

    result = lemmatizer.process(document)

    assert isinstance(result, ProcessedDocument)


def test_lemmatize_single_word():

    lemmatizer = Lemmatizer()

    document = _create_document(
        "running"
    )

    result = lemmatizer.process(document)

    assert result.lemmas == [
        "running"
    ]


def test_lemmatize_plural_words():

    lemmatizer = Lemmatizer()

    document = _create_document(
        "cars containers"
    )

    result = lemmatizer.process(document)

    assert result.lemmas == [
        "car",
        "container",
    ]


def test_empty_text():

    lemmatizer = Lemmatizer()

    document = _create_document(
        ""
    )

    result = lemmatizer.process(document)

    assert result.lemmas == []


def test_single_token():

    lemmatizer = Lemmatizer()

    document = _create_document(
        "Docker"
    )

    result = lemmatizer.process(document)

    assert result.lemmas == [
        "Docker"
    ]


def test_numbers():

    lemmatizer = Lemmatizer()

    document = _create_document(
        "Version 2.0"
    )

    result = lemmatizer.process(document)

    assert result.lemmas == [
        "Version",
        "2.0",
    ]


def test_technical_vocabulary():

    lemmatizer = Lemmatizer()

    document = _create_document(
        "FastAPI Docker JWT PostgreSQL"
    )

    result = lemmatizer.process(document)

    assert result.lemmas == [
        "FastAPI",
        "Docker",
        "JWT",
        "PostgreSQL",
    ]


def test_mixed_sentence():

    lemmatizer = Lemmatizer()

    document = _create_document(
        "cars use Docker"
    )

    result = lemmatizer.process(document)

    assert result.lemmas == [
        "car",
        "use",
        "Docker",
    ]