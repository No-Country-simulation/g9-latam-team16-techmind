"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_mock_loader.py

Descripción:
    Pruebas unitarias para MockLoader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import pandas as pd

from data_science.loaders.mock_loader import MockLoader


# ==========================================================
# Tests
# ==========================================================

def test_load_returns_dataframe() -> None:
    """
    Verifica que MockLoader devuelva
    un DataFrame.
    """

    loader = MockLoader()

    result = loader.load()

    assert isinstance(result, pd.DataFrame)


def test_load_returns_two_records() -> None:
    """
    Verifica que el DataFrame contenga
    dos registros.
    """

    loader = MockLoader()

    result = loader.load()

    assert len(result) == 2


def test_dataframe_contains_expected_columns() -> None:
    """
    Verifica que el DataFrame contenga
    las columnas esperadas.
    """

    loader = MockLoader()

    result = loader.load()

    expected_columns = [
        "document_id",
        "title",
        "text",
        "source",
        "category",
        "language",
        "author",
        "tags",
        "url",
        "metadata",
    ]

    assert list(result.columns) == expected_columns


def test_all_records_have_mock_source() -> None:
    """
    Verifica que todos los registros
    pertenezcan al origen mock.
    """

    loader = MockLoader()

    result = loader.load()

    assert (result["source"] == "mock").all()


def test_document_id_is_not_empty() -> None:
    """
    Verifica que todos los registros
    tengan document_id.
    """

    loader = MockLoader()

    result = loader.load()

    assert result["document_id"].notna().all()

    assert (result["document_id"] != "").all()