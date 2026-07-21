"""
==========================================================
TechMind
Data Science Component

Module:
    text_normalizer.py

Description:
    Implements the text normalization component of the
    preprocessing pipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import unicodedata

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

class TextNormalizer(BasePreprocessor):
    """
    Normaliza el texto para obtener una representación
    consistente antes del procesamiento lingüístico.
    """

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Ejecuta la normalización básica del texto.

        Parameters
        ----------
        document : DocumentRecord
            Documento de entrada.

        Returns
        -------
        ProcessedDocument
            Documento con el texto normalizado.
        """

        original_text = document["text"]

        normalized_text = self._normalize_text(original_text)

        return ProcessedDocument(
            document=document,
            processed_text=normalized_text,
        )

    def _normalize_text(
        self,
        text: str,
    ) -> str:
        """
        Normaliza el texto utilizando Unicode y
        convirtiéndolo a minúsculas.

        Parameters
        ----------
        text : str
            Texto original.

        Returns
        -------
        str
            Texto normalizado.
        """

        text = unicodedata.normalize(
            "NFKC",
            text,
        )

        return text.lower()