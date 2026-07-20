"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_github_loader.py

Descripción:
    Pruebas unitarias para GitHubLoader.

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

from src.data_science.loaders.github_loader import GitHubLoader


# ==========================================================
# Tests
# ==========================================================

def test_load_returns_dataframe(tmp_path: Path) -> None:
    """
    Verifica que GitHubLoader devuelva un DataFrame.
    """

    file = tmp_path / "README.md"

    file.write_text(
        "# TechMind\nProyecto de prueba",
        encoding="utf-8",
    )

    loader = GitHubLoader(str(tmp_path))

    result = loader.load()

    assert isinstance(result, pd.DataFrame)


def test_load_reads_markdown_file(tmp_path: Path) -> None:
    """
    Verifica que se lea correctamente un archivo Markdown.
    """

    file = tmp_path / "README.md"

    file.write_text(
        "# TechMind",
        encoding="utf-8",
    )

    loader = GitHubLoader(str(tmp_path))

    result = loader.load()

    assert len(result) == 1


def test_load_reads_text_file(tmp_path: Path) -> None:
    """
    Verifica que se lea correctamente un archivo TXT.
    """

    file = tmp_path / "notes.txt"

    file.write_text(
        "Documentación",
        encoding="utf-8",
    )

    loader = GitHubLoader(str(tmp_path))

    result = loader.load()

    assert len(result) == 1


def test_ignores_unsupported_files(tmp_path: Path) -> None:
    """
    Verifica que los archivos con extensiones no soportadas
    sean ignorados.
    """

    (tmp_path / "README.md").write_text(
        "# TechMind",
        encoding="utf-8",
    )

    (tmp_path / "image.png").write_text(
        "fake",
        encoding="utf-8",
    )

    loader = GitHubLoader(str(tmp_path))

    result = loader.load()

    assert len(result) == 1


def test_source_is_github(tmp_path: Path) -> None:
    """
    Verifica que el origen del documento sea github.
    """

    file = tmp_path / "README.md"

    file.write_text(
        "# TechMind",
        encoding="utf-8",
    )

    loader = GitHubLoader(str(tmp_path))

    result = loader.load()

    assert (result["source"] == "github").all()


def test_document_id_matches_relative_path(tmp_path: Path) -> None:
    """
    Verifica que document_id corresponda
    a la ruta relativa del archivo.
    """

    file = tmp_path / "README.md"

    file.write_text(
        "# TechMind",
        encoding="utf-8",
    )

    loader = GitHubLoader(str(tmp_path))

    result = loader.load()

    assert result.iloc[0]["document_id"] == "README.md"


def test_load_non_existing_directory() -> None:
    """
    Verifica que una ruta inexistente
    genere FileNotFoundError.
    """

    loader = GitHubLoader("carpeta_inexistente")

    with pytest.raises(FileNotFoundError):
        loader.load()