"""
==========================================================
TechMind
Componente Data Science

Módulo:
    huggingface_loader.py

Descripción:
    Implementa el cargador para datasets tabulares
    provenientes de Hugging Face almacenados localmente.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from typing import Any

import pandas as pd

from ..data.domain import DocumentRecord
from .base_loader import BaseLoader


# ==========================================================
# Hugging Face Loader
# ==========================================================

class HuggingFaceLoader(BaseLoader):
    """
    Cargador para datasets tabulares.
    """

    SOURCE = "huggingface"

    DEFAULT_LANGUAGE = "en"

    DEFAULT_CATEGORY = "dataset"

    DEFAULT_AUTHOR = "unknown"

    SUPPORTED_EXTENSIONS = (
        ".csv",
    )

    def __init__(
        self,
        source_path: str = "knowledge_sources/huggingface",
    ) -> None:

        super().__init__(source_path)

    # ======================================================
    # API pública
    # ======================================================

    def load(self) -> pd.DataFrame:

        self._validate_source_path()

        files = self._find_files()

        records: list[DocumentRecord] = []

        for file in files:

            dataset = self._read(file)

            rows = dataset.to_dict(
                orient="records"
            )

            records.extend(
                self._build_records(rows)
            )

        return self._build_dataframe(records)

    # ======================================================
    # Métodos protegidos
    # ======================================================

    def _build_record(
        self,
        source: Any,
    ) -> DocumentRecord:

        return {

            "document_id": str(
                source.get(
                    "document_id",
                    ""
                )
            ),

            "title": source.get(
                "title",
                ""
            ),

            "text": source.get(
                "text",
                ""
            ),

            "source": self.SOURCE,

            "category": source.get(
                "category",
                self.DEFAULT_CATEGORY,
            ),

            "language": source.get(
                "language",
                self.DEFAULT_LANGUAGE,
            ),

            "author": source.get(
                "author",
                self.DEFAULT_AUTHOR,
            ),

            "tags": source.get(
                "tags",
                [],
            ),

            "url": source.get(
                "url",
                "",
            ),

            "metadata": source.get(
                "metadata",
                {},
            ),
        }