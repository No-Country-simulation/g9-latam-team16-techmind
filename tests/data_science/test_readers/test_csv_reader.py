"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_csv_reader.py

Descripción:
    Pruebas unitarias para CsvReader.

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

from src.data_science.readers.csv_reader import CsvReader


# ==========================================================
# Tests
# ==========================================================

def test_read_valid_csv(tmp_path: Path) -> None:
    """
    Verifica que un archivo CSV válido
    sea leído correctamente.
    """

    file = tmp_path / "sample.csv"

    file.write_text(
        "nombre,edad\nAna,30\nLuis,25",
        encoding="utf-8",
    )

    reader = CsvReader()

    result = reader.read(file)

    assert isinstance(result, pd.DataFrame)


def test_csv_columns(tmp_path: Path) -> None:
    """
    Verifica que las columnas del DataFrame
    sean las esperadas.
    """

    file = tmp_path / "sample.csv"

    file.write_text(
        "nombre,edad\nAna,30\nLuis,25",
        encoding="utf-8",
    )

    reader = CsvReader()

    result = reader.read(file)

    assert list(result.columns) == ["nombre", "edad"]


def test_csv_row_count(tmp_path: Path) -> None:
    """
    Verifica la cantidad de filas leídas.
    """

    file = tmp_path / "sample.csv"

    file.write_text(
        "nombre,edad\nAna,30\nLuis,25",
        encoding="utf-8",
    )

    reader = CsvReader()

    result = reader.read(file)

    assert len(result) == 2


def test_empty_csv(tmp_path: Path) -> None:
    """
    Verifica que un CSV vacío genere
    EmptyDataError.
    """

    file = tmp_path / "empty.csv"

    file.write_text(
        "",
        encoding="utf-8",
    )

    reader = CsvReader()

    with pytest.raises(pd.errors.EmptyDataError):
        reader.read(file)


def test_non_existing_csv() -> None:
    """
    Verifica que un archivo inexistente
    genere FileNotFoundError.
    """

    reader = CsvReader()

    with pytest.raises(FileNotFoundError):
        reader.read(Path("archivo_inexistente.csv"))