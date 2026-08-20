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

from src.data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)

from src.data_science.preprocessing.base_preprocessor import (
    BasePreprocessor,
)

# ==========================================================
# Preprocessing Components
# ==========================================================


class TextNormalizer(BasePreprocessor):
    """
    Normaliza el texto para obtener una representaciÃ³n
    consistente antes del procesamiento lingÃ¼Ã­stico.
    """

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Ejecuta la normalizaciÃ³n bÃ¡sica del texto.

        Parameters
        ----------
        document : DocumentRecord
            Documento de entrada.

        Returns
        -------
        ProcessedDocument
            Documento con el texto normalizado.
        """

        # original_text = document["text"]
        original_text = document.text

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
        convirtiÃ©ndolo a minÃºsculas.

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


