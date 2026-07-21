"""
==========================================================
TechMind
Data Science Component

Module:
    tokenizer.py

Description:
    Implements the tokenization component of the
    preprocessing pipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from nltk.tokenize import word_tokenize

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

class Tokenizer(BasePreprocessor):
    """
    Tokenizes the document text into a sequence of words.
    """

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Executes the tokenization process.
        """

        original_text = document["text"]

        tokens = self._tokenize_text(
            original_text,
        )

        return ProcessedDocument(
            document=document,
            processed_text=original_text,
            tokens=tokens,
        )

    def _tokenize_text(
        self,
        text: str,
    ) -> list[str]:
        """
        Tokenizes the input text.
        """

        if not text:
            return []

        return word_tokenize(text)