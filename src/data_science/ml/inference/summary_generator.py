"""
----------------------------------------------------------
Proyecto : TechMind
Sprint   : Genera un resumen extractivo a partir del contenido de un documento.
Módulo   : Data Science
Archivo  : summary_generator.py
----------------------------------------------------------
"""

import re

import numpy as np


class SummaryGenerator:
    """
    Genera un resumen extractivo utilizando características TF-IDF.
    """

    def __init__(
        self,
        max_sentences: int = 3,
        max_characters: int = 500,
    ) -> None:
        self._max_sentences = max_sentences
        self._max_characters = max_characters

    def generate(self, text: str, vectorizer) -> str:
        """
        Genera un resumen de hasta `max_sentences` oraciones
        y `max_characters` caracteres.
        """

        if not text or not text.strip():
            return ""

        normalized_text = self._normalize_text(text)

        sentences = self._split_sentences(normalized_text)

        if not sentences:
            return ""

        if len(sentences) <= self._max_sentences:
            selected_sentences = sentences
        else:
            matrix = vectorizer.transform(sentences)

            scores = np.asarray(matrix.sum(axis=1)).ravel()

            ranked_indices = np.argsort(scores)[::-1][
                : self._max_sentences
            ]

            selected_indices = sorted(ranked_indices)

            selected_sentences = [
                sentences[index]
                for index in selected_indices
            ]

        summary = " ".join(selected_sentences)

        return self._limit_characters(summary)

    @staticmethod
    def _normalize_text(text: str) -> str:
        """
        Normaliza el contenido antes de generar el resumen.

        Elimina elementos básicos de formato Markdown y normaliza
        espacios y saltos de línea.
        """

        normalized = text.replace("\\r\\n", " ")
        normalized = normalized.replace("\\n", " ")
        normalized = normalized.replace("\r\n", " ")
        normalized = normalized.replace("\n", " ")
        normalized = normalized.replace("\r", " ")

        # Elimina formato Markdown básico.
        normalized = re.sub(r"\*\*(.*?)\*\*", r"\1", normalized)
        normalized = re.sub(r"__(.*?)__", r"\1", normalized)
        normalized = re.sub(r"`([^`]*)`", r"\1", normalized)

        # Elimina encabezados Markdown.
        normalized = re.sub(r"#{1,6}\s*", "", normalized)

        # Normaliza espacios.
        normalized = re.sub(r"\s+", " ", normalized)

        return normalized.strip()

    @staticmethod
    def _split_sentences(text: str) -> list[str]:
        """
        Divide el texto en oraciones.
        """

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text.strip(),
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

    def _limit_characters(self, text: str) -> str:
        """
        Limita el resumen al máximo de caracteres configurado.

        Procura terminar en una oración completa.
        """

        if len(text) <= self._max_characters:
            return text

        truncated = text[: self._max_characters]

        last_sentence_end = max(
            truncated.rfind("."),
            truncated.rfind("!"),
            truncated.rfind("?"),
        )

        if last_sentence_end > 0:
            return truncated[: last_sentence_end + 1].strip()

        last_space = truncated.rfind(" ")

        if last_space > 0:
            return truncated[:last_space].strip() + "..."

        return truncated.strip() + "..."