"""
==========================================================
TechMind
Data Science Component

Module:
    test_tokenizer.py

Description:
    Unit tests for the Tokenizer component.

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

from data_science.preprocessing.tokenizer import (
    Tokenizer,
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

    tokenizer = Tokenizer()

    document = _create_document(
        "FastAPI is awesome."
    )

    result = tokenizer.process(document)

    assert isinstance(result, ProcessedDocument)


def test_tokenize_simple_text():
    """
    Should tokenize a simple sentence.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        "FastAPI is awesome."
    )

    result = tokenizer.process(document)

    assert result.tokens == [
        "FastAPI",
        "is",
        "awesome",
        ".",
    ]


def test_empty_text():
    """
    Should return an empty token list.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        ""
    )

    result = tokenizer.process(document)

    assert result.tokens == []


def test_single_word():
    """
    Should tokenize a single word.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        "Docker"
    )

    result = tokenizer.process(document)

    assert result.tokens == [
        "Docker"
    ]


def test_numbers():
    """
    Should tokenize numbers.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        "Version 2.0"
    )

    result = tokenizer.process(document)

    assert result.tokens == [
        "Version",
        "2.0",
    ]


def test_preserve_punctuation():
    """
    Should preserve punctuation as tokens.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        "Hello, world!"
    )

    result = tokenizer.process(document)

    assert result.tokens == [
        "Hello",
        ",",
        "world",
        "!",
    ]


def test_technical_vocabulary():
    """
    Should tokenize technical vocabulary.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        "FastAPI JWT Docker PostgreSQL"
    )

    result = tokenizer.process(document)

    assert result.tokens == [
        "FastAPI",
        "JWT",
        "Docker",
        "PostgreSQL",
    ]


def test_mixed_sentence():
    """
    Should tokenize a mixed technical sentence.
    """

    tokenizer = Tokenizer()

    document = _create_document(
        "FastAPI uses JWT with Docker."
    )

    result = tokenizer.process(document)

    assert result.tokens == [
        "FastAPI",
        "uses",
        "JWT",
        "with",
        "Docker",
        ".",
    ]