"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_stackexchange_loader.py

Descripción:
    Pruebas unitarias para StackExchangeLoader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

from pathlib import Path

import pandas as pd
import pytest

from data_science.loaders.stackexchange_loader import (
    StackExchangeLoader,
)


def test_load_returns_dataframe(tmp_path: Path) -> None:
    data = [
        {
            "question_id": 1,
            "title": "Python",
            "body": "What is Python?",
        }
    ]

    json_file = tmp_path / "questions.json"
    json_file.write_text(__import__("json").dumps(data), encoding="utf-8")

    loader = StackExchangeLoader(str(tmp_path))

    result = loader.load()

    assert isinstance(result, pd.DataFrame)


def test_load_returns_one_record(tmp_path: Path) -> None:
    data = [
        {
            "question_id": 1,
            "title": "Python",
            "body": "What is Python?",
        }
    ]

    (tmp_path / "questions.json").write_text(
        __import__("json").dumps(data),
        encoding="utf-8",
    )

    loader = StackExchangeLoader(str(tmp_path))

    result = loader.load()

    assert len(result) == 1


def test_source_is_stack_exchange(tmp_path: Path) -> None:
    data = [
        {
            "question_id": 15,
            "title": "Title",
            "body": "Body",
        }
    ]

    (tmp_path / "questions.json").write_text(
        __import__("json").dumps(data),
        encoding="utf-8",
    )

    loader = StackExchangeLoader(str(tmp_path))

    result = loader.load()

    assert (result["source"] == "stack_exchange").all()


def test_document_id_matches_question_id(tmp_path: Path) -> None:
    data = [
        {
            "question_id": 99,
            "title": "Title",
            "body": "Body",
        }
    ]

    (tmp_path / "questions.json").write_text(
        __import__("json").dumps(data),
        encoding="utf-8",
    )

    loader = StackExchangeLoader(str(tmp_path))

    result = loader.load()

    assert result.iloc[0]["document_id"] == "99"


def test_default_author_is_used(tmp_path: Path) -> None:
    data = [
        {
            "question_id": 1,
            "title": "Python",
            "body": "Body",
        }
    ]

    (tmp_path / "questions.json").write_text(
        __import__("json").dumps(data),
        encoding="utf-8",
    )

    loader = StackExchangeLoader(str(tmp_path))

    result = loader.load()

    assert result.iloc[0]["author"] == "community"


def test_load_non_existing_directory() -> None:
    loader = StackExchangeLoader("carpeta_inexistente")

    with pytest.raises(FileNotFoundError):
        loader.load()