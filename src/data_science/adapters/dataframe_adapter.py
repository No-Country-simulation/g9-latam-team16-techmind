"""
==========================================================
TechMind
Data Science Component

Module:
    dataframe_adapter.py
==========================================================
"""

from pandas import Series

from data_science.data.domain import DocumentRecord


class DataFrameAdapter:

    _LANGUAGE_MAPPING = {
        "English": "english",
        "Spanish": "spanish",
        "Portuguese": "portuguese",
    }

    def to_document(
        self,
        row: Series,
        source: str,
    ) -> DocumentRecord:

        language = self._LANGUAGE_MAPPING.get(
            str(row["language"]),
            "english",
        )

        return DocumentRecord(
            document_id=str(row["document_id"]),
            source=source,
            title=str(row["title"]),
            text=str(row["content"]),
            category=str(row["category"]),
            language=language,
        )
