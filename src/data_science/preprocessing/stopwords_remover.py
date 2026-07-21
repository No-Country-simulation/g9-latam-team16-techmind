"""
==========================================================
TechMind
Data Science Component

Module:
    stopwords_remover.py

Description:
    Implements the stop words removal component of the
    preprocessing pipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from nltk.corpus import stopwords

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

class StopWordsRemover(BasePreprocessor):
    """
    Removes stop words from the document text according
    to the document language.
    """

    _STOPWORDS = {
        "es": set(stopwords.words("spanish")),
        "en": set(stopwords.words("english")),
    }

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Executes the stop words removal process.
        """

        original_text = document["text"]
        language = document.get("language", "en")

        processed_text = self._remove_stopwords(
            original_text,
            language,
        )

        return ProcessedDocument(
            document=document,
            processed_text=processed_text,
        )

    def _remove_stopwords(
        self,
        text: str,
        language: str,
    ) -> str:
        """
        Removes stop words from the input text.
        """

        stop_words = self._STOPWORDS.get(language)

        if stop_words is None:
            return text

        words = text.split()

        filtered_words = [
            word
            for word in words
            if word.lower() not in stop_words
        ]

        return " ".join(filtered_words)