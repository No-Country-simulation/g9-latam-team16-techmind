"""
==========================================================
TechMind
Data Science Component

Module:
    test_text_cleaner.py

Description:
    Unit tests for the TextCleaner component.

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

from data_science.preprocessing.text_cleaner import (
    TextCleaner,
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
    document = _create_document("Hola mundo")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert isinstance(result, ProcessedDocument)
    assert result.document == document
    assert result.processed_text == "Hola mundo"
    assert result.tokens == []
    assert result.lemmas == []


def test_process_removes_multiple_spaces() -> None:
    """
    Verifica que elimina espacios múltiples.
    """

    # Arrange
    document = _create_document("Hola     mundo")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == "Hola mundo"


def test_process_replaces_tabs() -> None:
    """
    Verifica que reemplaza tabulaciones.
    """

    # Arrange
    document = _create_document("Hola\tmundo")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == "Hola mundo"


def test_process_replaces_new_lines() -> None:
    """
    Verifica que reemplaza saltos de línea.
    """

    # Arrange
    document = _create_document("Hola\nmundo")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == "Hola mundo"


def test_process_strips_text() -> None:
    """
    Verifica que elimina espacios al inicio y al final.
    """

    # Arrange
    document = _create_document("   Hola mundo   ")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == "Hola mundo"


def test_process_handles_empty_text() -> None:
    """
    Verifica que procesa correctamente un texto vacío.
    """

    # Arrange
    document = _create_document("")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == ""


def test_process_handles_only_spaces() -> None:
    """
    Verifica que un texto compuesto únicamente por espacios
    produce una cadena vacía.
    """

    # Arrange
    document = _create_document("       ")
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == ""


def test_process_handles_combined_whitespace() -> None:
    """
    Verifica la limpieza cuando existen espacios,
    tabulaciones y saltos de línea combinados.
    """

    # Arrange
    document = _create_document(
        " Hola\t\n mundo     de\t\tTechMind "
    )
    cleaner = TextCleaner()

    # Act
    result = cleaner.process(document)

    # Assert
    assert result.processed_text == "Hola mundo de TechMind"
