"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    TfidfVectorizerAdapter

Descripción:
    Implementación concreta del contrato BaseVectorizer
    utilizando la técnica TF-IDF de Scikit-Learn.

Autor:
    Equipo Data Science

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

from __future__ import annotations

from typing import Sequence

from scipy.sparse import csr_matrix

from sklearn.feature_extraction.text import TfidfVectorizer

from data_science.ml.features.base_vectorizer import BaseVectorizer



class TfidfVectorizerAdapter(BaseVectorizer):
    """
    Adaptador de Scikit-Learn para la representación
    vectorial mediante TF-IDF.
    """

    def __init__(
        self,
        max_features: int | None = None,
        ngram_range: tuple[int, int] = (1, 1),
        lowercase: bool = True,
    ) -> None:
        """
        Inicializa el vectorizador TF-IDF.

        Parameters
        ----------
        max_features : int | None
            Número máximo de características.

        ngram_range : tuple[int, int]
            Rango de n-gramas.

        lowercase : bool
            Convierte el texto a minúsculas antes de
            construir el vocabulario.
        """

        self._vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            lowercase=lowercase,
        )

    def fit(self, documents: Sequence[str]) -> "TfidfVectorizerAdapter":
        """
        Aprende el vocabulario del conjunto de entrenamiento.
        """

        self._vectorizer.fit(documents)
        return self

    def transform(self, documents: Sequence[str]) -> csr_matrix:
        """
        Transforma documentos utilizando el vocabulario aprendido.

        Parameters
        ----------
        documents : Sequence[str]
            Documentos a transformar.

        Returns
        -------
        csr_matrix
            Matriz TF-IDF de los documentos.
        """

        return self._vectorizer.transform(documents)

    def fit_transform(self, documents: Sequence[str]) -> csr_matrix:
        """
        Aprende el vocabulario y transforma los documentos.

        Parameters
        ----------
        documents : Sequence[str]
            Documentos de entrenamiento.

        Returns
        -------
        csr_matrix
            Matriz TF-IDF de los documentos.
        """

        return self._vectorizer.fit_transform(documents)