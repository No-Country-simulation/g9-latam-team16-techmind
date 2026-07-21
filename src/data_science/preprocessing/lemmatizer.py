"""
==========================================================
TechMind
Data Science Component

Module:
    lemmatizer.py

Description:
    Implements the lemmatization component of the
    preprocessing pipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from nltk.stem import WordNetLemmatizer

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

class Lemmatizer(BasePreprocessor):
    """
    Converts words to their base form (lemma).
    """

    _LEMMATIZER = WordNetLemmatizer()

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Executes the lemmatization process.
        """

        original_text = document["text"]

        lemmas = self._lemmatize_text(
            original_text,
        )

        return ProcessedDocument(
            document=document,
            processed_text=original_text,
            lemmas=lemmas,
        )

    def _lemmatize_text(
        self,
        text: str,
    ) -> list[str]:
        """
        Converts the text into a list of lemmas.
        """

        if not text:
            return []

        words = text.split()

        return [
            self._LEMMATIZER.lemmatize(word)
            for word in words
        ]