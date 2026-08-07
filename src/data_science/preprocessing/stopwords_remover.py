"""
==========================================================
TechMind
Data Science Component

Module:
    stopwords_remover.py

Description:
    Implements the stop words removal component.

Sprint:
    DS-04
==========================================================
"""

from nltk.corpus import stopwords

from data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)

from data_science.preprocessing.base_preprocessor import (
    BasePreprocessor,
)


class StopWordsRemover(BasePreprocessor):
    """
    Removes stop words according to the document language.
    """

    _LANGUAGE_MAPPING = {
        "english": "english",
        "en": "english",
        "spanish": "spanish",
        "es": "spanish",
        "portuguese": "portuguese",
        "pt": "portuguese",
    }

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:

        # original_text = document["text"]

        # language = (
        #    document.get("language", "english")
        #    .lower()
        #    .strip()
        # )

        original_text = document.text

        language = document.language.lower().strip()

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

        nltk_language = self._LANGUAGE_MAPPING.get(
            language,
            "english",
        )

        stop_words = set(stopwords.words(nltk_language))

        words = text.split()

        filtered_words = [word for word in words if word.lower() not in stop_words]

        return " ".join(filtered_words)
