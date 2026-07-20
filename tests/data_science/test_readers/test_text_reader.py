"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_text_reader.py

Descripción:
    Pruebas unitarias para TextReader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pytest

from src.data_science.readers.text_reader import TextReader


# ==========================================================
# Tests
# ==========================================================

def test_read_valid_text_file(tmp_path: Path) -> None:
    """
    Verifica que un archivo de texto válido
    sea leído correctamente.
    """

    file = tmp_path / "sample.txt"
    file.write_text("Hola TechMind", encoding="utf-8")

    reader = TextReader()

    result = reader.read(file)

    assert result == "Hola TechMind"


def test_read_empty_text_file(tmp_path: Path) -> None:
    """
    Verifica que un archivo vacío devuelva
    una cadena vacía.
    """

    file = tmp_path / "empty.txt"
    file.write_text("", encoding="utf-8")

    reader = TextReader()

    result = reader.read(file)

    assert result == ""


def test_read_returns_string(tmp_path: Path) -> None:
    """
    Verifica que el tipo de retorno sea str.
    """

    file = tmp_path / "sample.txt"
    file.write_text("Contenido", encoding="utf-8")

    reader = TextReader()

    result = reader.read(file)

    assert isinstance(result, str)


def test_read_non_existing_file() -> None:
    """
    Verifica que intentar leer un archivo
    inexistente genere FileNotFoundError.
    """

    reader = TextReader()

    with pytest.raises(FileNotFoundError):
        reader.read(Path("archivo_inexistente.txt"))