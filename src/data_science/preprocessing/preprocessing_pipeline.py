"""
==========================================================
TechMind
Data Science Component

Module:
    preprocessing_pipeline.py

Description:
    Orchestrates the preprocessing components.

Sprint:
    DS-04 - Preprocesamiento del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from copy import deepcopy

from data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)

from data_science.preprocessing.text_cleaner import (
    TextCleaner,
)

from data_science.preprocessing.text_normalizer import (
    TextNormalizer,
)

from data_science.preprocessing.stopwords_remover import (
    StopWordsRemover,
)

from data_science.preprocessing.tokenizer import (
    Tokenizer,
)

from data_science.preprocessing.lemmatizer import (
    Lemmatizer,
)


# ==========================================================
# Preprocessing Pipeline
# ==========================================================

class PreprocessingPipeline:
    """
    Executes the complete preprocessing workflow.
    """

    def __init__(self):

        self._cleaner = TextCleaner()

        self._normalizer = TextNormalizer()

        self._stopwords = StopWordsRemover()

        self._tokenizer = Tokenizer()

        self._lemmatizer = Lemmatizer()

    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Executes the preprocessing pipeline.
        """

        working_document = deepcopy(document)

        processed = self._cleaner.process(
            working_document
        )

        working_document["text"] = processed.processed_text

        processed = self._normalizer.process(
            working_document
        )

        working_document["text"] = processed.processed_text

        processed = self._stopwords.process(
            working_document
        )

        working_document["text"] = processed.processed_text

        tokens = self._tokenizer.process(
            working_document
        )

        lemmas = self._lemmatizer.process(
            working_document
        )

        return ProcessedDocument(
            document=document,
            processed_text=processed.processed_text,
            tokens=tokens.tokens,
            lemmas=lemmas.lemmas,
        )