"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_huggingface_loader.py

Descripción:
    Pruebas unitarias para HuggingFaceLoader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

from pathlib import Path

import pandas as pd
import pytest

from src.data_science.loaders.huggingface_loader import (
    HuggingFaceLoader,
)


def test_load_returns_dataframe(tmp_path: Path) -> None:
    csv_file = tmp_path / "dataset.csv"

    csv_file.write_text(
        "document_id,title,text\n"
        "1,Python,Programming language\n",
        encoding="utf-8",
    )

    loader = HuggingFaceLoader(str(tmp_path))

    result = loader.load()

    assert isinstance(result, pd.DataFrame)


def test_load_returns_one_record(tmp_path: Path) -> None:
    csv_file = tmp_path / "dataset.csv"

    csv_file.write_text(
        "document_id,title,text\n"
        "1,Python,Programming language\n",
        encoding="utf-8",
    )

    loader = HuggingFaceLoader(str(tmp_path))

    result = loader.load()

    assert len(result) == 1


def test_source_is_huggingface(tmp_path: Path) -> None:
    csv_file = tmp_path / "dataset.csv"

    csv_file.write_text(
        "document_id,title,text\n"
        "1,Python,Programming language\n",
        encoding="utf-8",
    )

    loader = HuggingFaceLoader(str(tmp_path))

    result = loader.load()

    assert (result["source"] == "huggingface").all()


def test_document_id_matches_csv(tmp_path: Path) -> None:
    csv_file = tmp_path / "dataset.csv"

    csv_file.write_text(
        "document_id,title,text\n"
        "25,Python,Programming language\n",
        encoding="utf-8",
    )

    loader = HuggingFaceLoader(str(tmp_path))

    result = loader.load()

    assert result.iloc[0]["document_id"] == "25"


def test_default_author_is_unknown(tmp_path: Path) -> None:
    csv_file = tmp_path / "dataset.csv"

    csv_file.write_text(
        "document_id,title,text\n"
        "1,Python,Programming language\n",
        encoding="utf-8",
    )

    loader = HuggingFaceLoader(str(tmp_path))

    result = loader.load()

    assert result.iloc[0]["author"] == "unknown"


def test_default_category_is_dataset(tmp_path: Path) -> None:
    csv_file = tmp_path / "dataset.csv"

    csv_file.write_text(
        "document_id,title,text\n"
        "1,Python,Programming language\n",
        encoding="utf-8",
    )

    loader = HuggingFaceLoader(str(tmp_path))

    result = loader.load()

    assert result.iloc[0]["category"] == "dataset"


def test_load_non_existing_directory() -> None:
    loader = HuggingFaceLoader("carpeta_inexistente")

    with pytest.raises(FileNotFoundError):
        loader.load()