"""
==========================================================
TechMind
Data Science Component

Module:
    text_cleaner.py

Description:
    Implements the text cleaning component of the
    preprocessing pipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import re

from data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)

from data_science.preprocessing.base_preprocessor import (
    BasePreprocessor,
)


# ==========================================================
# Preprocessing Components
# ==========================================================

class TextCleaner(BasePreprocessor):
    """
    Limpia el texto eliminando espacios innecesarios y
    normalizando caracteres de separación.
    """

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Ejecuta la limpieza básica del texto.

        Parameters
        ----------
        document : DocumentRecord
            Documento de entrada.

        Returns
        -------
        ProcessedDocument
            Documento con el texto limpio.
        """

        original_text = document["text"]

        cleaned_text = self._clean_text(original_text)

        return ProcessedDocument(
            document=document,
            processed_text=cleaned_text,
        )

    def _clean_text(
        self,
        text: str,
    ) -> str:
        """
        Elimina espacios innecesarios del texto.
        """

        text = re.sub(r"\s+", " ", text)

        return text.strip()