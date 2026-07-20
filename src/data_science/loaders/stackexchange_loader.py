"""
==========================================================
TechMind
Componente Data Science

Módulo:
    stackexchange_loader.py

Descripción:
    Implementa el cargador para preguntas y respuestas
    provenientes de Stack Exchange.

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
# Stack Exchange Loader
# ==========================================================

class StackExchangeLoader(BaseLoader):
    """
    Cargador de preguntas y respuestas de Stack Exchange.
    """

    SOURCE = "stack_exchange"

    DEFAULT_LANGUAGE = "en"

    DEFAULT_CATEGORY = "question_answer"

    DEFAULT_AUTHOR = "community"

    SUPPORTED_EXTENSIONS = (
        ".json",
    )

    def __init__(
        self,
        source_path: str = "knowledge_sources/stack_exchange",
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

            questions = self._read(file)

            records.extend(
                self._build_records(questions)
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
                source["question_id"]
            ),

            "title": source["title"],

            "text": source["body"],

            "source": self.SOURCE,

            "category": self.DEFAULT_CATEGORY,

            "language": self.DEFAULT_LANGUAGE,

            "author": source.get(
                "author",
                self.DEFAULT_AUTHOR,
            ),

            "tags": source.get(
                "tags",
                [],
            ),

            "url": source.get(
                "link",
                "",
            ),

            "metadata": {

                "score": source.get(
                    "score"
                ),

                "views": source.get(
                    "views"
                ),

                "answers": source.get(
                    "answers"
                ),

                "accepted": source.get(
                    "accepted"
                ),

                "loader": self.__class__.__name__,
            },
        }