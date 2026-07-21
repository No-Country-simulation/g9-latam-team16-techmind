"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_pdf_reader.py

Descripción:
    Pruebas unitarias para PdfReader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pytest

from data_science.readers.pdf_reader import PdfReader


# ==========================================================
# Tests
# ==========================================================

def test_read_valid_pdf() -> None:
    """
    Verifica que un PDF válido
    sea leído correctamente.
    """

    file = Path("tests/data_science/fixtures/sample.pdf")
 

    reader = PdfReader()

    result = reader.read(file)

    assert isinstance(result, str)

    assert "TechMind" in result


def test_read_non_existing_pdf() -> None:
    """
    Verifica que un archivo inexistente
    genere FileNotFoundError.
    """

    reader = PdfReader()

    with pytest.raises(FileNotFoundError):
        reader.read(Path("archivo_inexistente.pdf"))