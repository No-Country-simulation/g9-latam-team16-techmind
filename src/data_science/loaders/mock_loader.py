"""
==========================================================
TechMind
Componente Data Science

Módulo:
    mock_loader.py

Descripción:
    Implementa un cargador de datos ficticios para pruebas.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

from typing import Any

import pandas as pd

from ..data.domain import DocumentRecord
from .base_loader import BaseLoader


class MockLoader(BaseLoader):
    """
    Loader utilizado para pruebas.
    """

    SOURCE = "mock"

    def __init__(self) -> None:

        super().__init__(source_path=".")

    def load(self) -> pd.DataFrame:

        sources = [

            {
                "title": "Python Lists",
                "text": "Lists are mutable sequences.",
                "category": "python",
            },

            {
                "title": "Vector Store",
                "text": "Vector databases store embeddings.",
                "category": "rag",
            },

        ]

        records = self._build_records(sources)

        return self._build_dataframe(records)

    def _build_record(
        self,
        source: Any,
    ) -> DocumentRecord:

        return {

            "document_id": source["title"],

            "title": source["title"],

            "text": source["text"],

            "source": self.SOURCE,

            "category": source["category"],

            "language": "en",

            "author": "TechMind",

            "tags": [],

            "url": "",

            "metadata": {},
        }