"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    BaseVectorizer

Descripción:
    Define el contrato que deben implementar todas las
    las estrategias de representación vectorial del texto.

Autor:
    Equipo Data Science

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Sequence


class BaseVectorizer(ABC):
    """
    Contrato para todas las estrategias de vectorización.

    Cualquier implementación (TF-IDF, Embeddings,
    Transformers, etc.) deberá implementar esta interfaz.

    Esto permite intercambiar la estrategia de representación
    sin afectar el resto del pipeline.
    """

    @abstractmethod
    def fit(self, documents: Sequence[str]) -> "BaseVectorizer":
        """
        Aprende la representación a partir de un conjunto
        de documentos.

        Parameters
        ----------
        documents : Sequence[str]
            Colección de documentos de entrenamiento.

        Returns
        -------
        BaseVectorizer
            Instancia entrenada.
        """
        raise NotImplementedError

    @abstractmethod
    def transform(self, documents: Sequence[str]) -> Any:
        """
        Convierte una colección de documentos en una
        representación numérica.

        Parameters
        ----------
        documents : Sequence[str]
            Documentos a transformar.

        Returns
        -------
        Any
            Representación vectorial.
        """
        raise NotImplementedError

    @abstractmethod
    def fit_transform(self, documents: Sequence[str]) -> Any:
        """
        Aprende la representación y transforma los documentos.

        Parameters
        ----------
        documents : Sequence[str]
            Documentos de entrenamiento.

        Returns
        -------
        Any
            Representación vectorial.
        """
        raise NotImplementedError