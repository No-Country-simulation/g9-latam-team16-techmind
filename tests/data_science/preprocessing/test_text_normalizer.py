"""
==========================================================
TechMind
Data Science Component

Module:
    test_text_normalizer.py

Description:
    Unit tests for the TextNormalizer component.

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

from data_science.preprocessing.text_normalizer import (
    TextNormalizer,
)


# ==========================================================
# Helper Functions
# ==========================================================

def _create_document(
    text: str,
) -> DocumentRecord:
    """
    Crea un documento de prueba.
    """

    return {
        "document_id": "doc-001",
        "source": "unit-test",
        "title": "Documento de prueba",
        "text": text,
        "category": "test",
        "language": "es",
    }


# ==========================================================
# Test Cases
# ==========================================================

def test_process_returns_processed_document() -> None:
    """
    Verifica que process() devuelve un ProcessedDocument.
    """

    # Arrange
    document = _create_document("Hola Mundo")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert isinstance(result, ProcessedDocument)
    assert result.document == document
    assert result.processed_text == "hola mundo"
    assert result.tokens == []
    assert result.lemmas == []


def test_process_converts_to_lowercase() -> None:
    """
    Verifica que convierte el texto a minúsculas.
    """

    # Arrange
    document = _create_document("HOLA MUNDO")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == "hola mundo"


def test_process_normalizes_mixed_case() -> None:
    """
    Verifica la normalización de texto con mayúsculas y minúsculas.
    """

    # Arrange
    document = _create_document("FastAPI con PYTHON")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == "fastapi con python"


def test_process_normalizes_unicode() -> None:
    """
    Verifica la normalización Unicode utilizando NFKC.
    """

    # Arrange
    document = _create_document("ＡＰＩ")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == "api"


def test_process_keeps_normalized_text() -> None:
    """
    Verifica que un texto ya normalizado permanece igual.
    """

    # Arrange
    document = _create_document("python")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == "python"


def test_process_handles_empty_text() -> None:
    """
    Verifica que procesa correctamente un texto vacío.
    """

    # Arrange
    document = _create_document("")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == ""


def test_process_preserves_numbers() -> None:
    """
    Verifica que conserva los números del texto.
    """

    # Arrange
    document = _create_document("Python 3.14")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == "python 3.14"


def test_process_preserves_punctuation() -> None:
    """
    Verifica que conserva la puntuación.
    """

    # Arrange
    document = _create_document("Hola, Mundo!")
    normalizer = TextNormalizer()

    # Act
    result = normalizer.process(document)

    # Assert
    assert result.processed_text == "hola, mundo!"