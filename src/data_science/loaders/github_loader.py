"""
==========================================================
TechMind
Componente Data Science

Módulo:
    github_loader.py

Descripción:
    Implementa el cargador para documentación técnica
    proveniente de repositorios GitHub almacenados
    localmente.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
from typing import Any

import pandas as pd

from ..data.domain import DocumentRecord
from .base_loader import BaseLoader


# ==========================================================
# GitHub Loader
# ==========================================================

class GitHubLoader(BaseLoader):
    """
    Cargador para documentación proveniente de GitHub.
    """

    SOURCE = "github"

    DEFAULT_CATEGORY = "documentation"

    DEFAULT_LANGUAGE = "en"

    DEFAULT_AUTHOR = "unknown"

    SUPPORTED_EXTENSIONS = (
        ".md",
        ".txt",
    )

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(
        self,
        source_path: str = "knowledge_sources/github",
    ) -> None:

        super().__init__(source_path)

    # ======================================================
    # API pública
    # ======================================================

    def load(self) -> pd.DataFrame:

        self._validate_source_path()

        files = self._find_files()

        sources = []

        for file in files:

            sources.append(
                {
                    "file": file,
                    "content": self._read(file),
                }
            )

        records = self._build_records(sources)

        return self._build_dataframe(records)

    # ======================================================
    # Métodos protegidos
    # ======================================================

    def _build_record(
        self,
        source: Any,
    ) -> DocumentRecord:

        file: Path = source["file"]

        content: str = source["content"]

        return {
            "document_id": file.relative_to(
                self._source_path
            ).as_posix(),

            "title": file.stem,

            "text": content,

            "source": self.SOURCE,

            "category": self.DEFAULT_CATEGORY,

            "language": self.DEFAULT_LANGUAGE,

            "author": self.DEFAULT_AUTHOR,

            "tags": [],

            "url": file.as_posix(),

            "metadata": {
                "extension": file.suffix,
                "relative_path": file.relative_to(
                    self._source_path
                ).as_posix(),
                "loader": self.__class__.__name__,
            },
        }