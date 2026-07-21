"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_json_reader.py

Descripción:
    Pruebas unitarias para JsonReader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import json

from pathlib import Path

import pytest

from data_science.readers.json_reader import JsonReader


# ==========================================================
# Tests
# ==========================================================

def test_read_valid_json_object(tmp_path: Path) -> None:
    """
    Verifica que un objeto JSON válido
    sea leído correctamente.
    """

    file = tmp_path / "sample.json"

    data = {
        "project": "TechMind",
        "version": 1,
    }

    file.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    reader = JsonReader()

    result = reader.read(file)

    assert result == data


def test_read_valid_json_list(tmp_path: Path) -> None:
    """
    Verifica que una lista JSON válida
    sea leída correctamente.
    """

    file = tmp_path / "sample.json"

    data = [
        "python",
        "pandas",
        "pytest",
    ]

    file.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    reader = JsonReader()

    result = reader.read(file)

    assert result == data


def test_read_returns_python_object(tmp_path: Path) -> None:
    """
    Verifica que JsonReader devuelva
    un objeto Python.
    """

    file = tmp_path / "sample.json"

    data = {
        "status": "ok",
    }

    file.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    reader = JsonReader()

    result = reader.read(file)

    assert isinstance(result, dict)


def test_read_invalid_json(tmp_path: Path) -> None:
    """
    Verifica que un JSON inválido
    genere JSONDecodeError.
    """

    file = tmp_path / "invalid.json"

    file.write_text(
        '{"name": "TechMind"',
        encoding="utf-8",
    )

    reader = JsonReader()

    with pytest.raises(json.JSONDecodeError):
        reader.read(file)


def test_read_empty_json_file(tmp_path: Path) -> None:
    """
    Verifica que un archivo JSON vacío
    genere JSONDecodeError.
    """

    file = tmp_path / "empty.json"

    file.write_text(
        "",
        encoding="utf-8",
    )

    reader = JsonReader()

    with pytest.raises(json.JSONDecodeError):
        reader.read(file)


def test_read_non_existing_json_file() -> None:
    """
    Verifica que intentar leer un archivo
    inexistente genere FileNotFoundError.
    """

    reader = JsonReader()

    with pytest.raises(FileNotFoundError):
        reader.read(Path("archivo_inexistente.json"))