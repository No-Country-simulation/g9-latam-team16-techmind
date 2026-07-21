"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_reader_factory.py

Descripción:
    Pruebas unitarias para ReaderFactory.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pytest

from data_science.readers.csv_reader import CsvReader
from data_science.readers.json_reader import JsonReader
from data_science.readers.pdf_reader import PdfReader
from data_science.readers.reader_factory import ReaderFactory
from data_science.readers.text_reader import TextReader


# ==========================================================
# Tests
# ==========================================================

def test_create_text_reader() -> None:
    """
    Verifica que se cree un TextReader
    para archivos TXT.
    """

    reader = ReaderFactory.create(Path("archivo.txt"))

    assert isinstance(reader, TextReader)


def test_create_markdown_reader() -> None:
    """
    Verifica que se cree un TextReader
    para archivos Markdown.
    """

    reader = ReaderFactory.create(Path("README.md"))

    assert isinstance(reader, TextReader)


def test_create_json_reader() -> None:
    """
    Verifica que se cree un JsonReader.
    """

    reader = ReaderFactory.create(Path("archivo.json"))

    assert isinstance(reader, JsonReader)


def test_create_csv_reader() -> None:
    """
    Verifica que se cree un CsvReader.
    """

    reader = ReaderFactory.create(Path("archivo.csv"))

    assert isinstance(reader, CsvReader)


def test_create_pdf_reader() -> None:
    """
    Verifica que se cree un PdfReader.
    """

    reader = ReaderFactory.create(Path("archivo.pdf"))

    assert isinstance(reader, PdfReader)


def test_create_reader_with_uppercase_extension() -> None:
    """
    Verifica que la extensión sea tratada
    sin distinguir mayúsculas y minúsculas.
    """

    reader = ReaderFactory.create(Path("README.MD"))

    assert isinstance(reader, TextReader)


def test_create_reader_with_unsupported_extension() -> None:
    """
    Verifica que una extensión no soportada
    genere ValueError.
    """

    with pytest.raises(ValueError):
        ReaderFactory.create(Path("archivo.xml"))