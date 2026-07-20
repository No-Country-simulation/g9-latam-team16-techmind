"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_technical_docs_loader.py

Descripción:
    Pruebas unitarias para TechnicalDocsLoader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pandas as pd
import pytest

from src.data_science.loaders.technical_docs_loader import (
    TechnicalDocsLoader,
)


# ==========================================================
# Tests
# ==========================================================

def test_load_returns_dataframe() -> None:
    """
    Verifica que TechnicalDocsLoader
    devuelva un DataFrame.
    """

    loader = TechnicalDocsLoader(
        "tests/data_science/fixtures"
    )

    result = loader.load()

    assert isinstance(result, pd.DataFrame)


def test_load_reads_pdf() -> None:
    """
    Verifica que el PDF sea leído.
    """

    loader = TechnicalDocsLoader(
        "tests/data_science/fixtures"
    )

    result = loader.load()

    assert len(result) == 1


def test_source_is_technical_docs() -> None:
    """
    Verifica el origen del documento.
    """

    loader = TechnicalDocsLoader(
        "tests/data_science/fixtures"
    )

    result = loader.load()

    assert (result["source"] == "technical_docs").all()


def test_document_id_matches_filename() -> None:
    """
    Verifica document_id.
    """

    loader = TechnicalDocsLoader(
        "tests/data_science/fixtures"
    )

    result = loader.load()

    assert result.iloc[0]["document_id"] == "sample.pdf"


def test_load_non_existing_directory() -> None:
    """
    Verifica que una ruta inexistente
    genere FileNotFoundError.
    """

    loader = TechnicalDocsLoader(
        "carpeta_inexistente"
    )

    with pytest.raises(FileNotFoundError):
        loader.load()