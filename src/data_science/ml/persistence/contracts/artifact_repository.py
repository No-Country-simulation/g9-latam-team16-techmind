"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : artifact_repository.py

Descripción:
Define el contrato que deberán implementar los repositorios
encargados de almacenar y recuperar los artefactos de modelos
entrenados.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)
from src.data_science.ml.persistence.domain.model_metadata import (
    ModelMetadata,
)


class ArtifactRepository(ABC):
    """
    Contrato para el almacenamiento y recuperación de artefactos
    de modelos de Machine Learning.
    """

    @abstractmethod
    def save(self, bundle: ArtifactBundle) -> str:
        """
        Almacena un conjunto de artefactos.

        Parameters
        ----------
        bundle:
            Conjunto de artefactos del modelo.

        Returns
        -------
        str
            Identificador único del modelo almacenado.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, identifier: str) -> ArtifactBundle:
        """
        Recupera un conjunto de artefactos.

        Parameters
        ----------
        identifier:
            Identificador del modelo.

        Returns
        -------
        ArtifactBundle
            Artefactos recuperados.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(self, identifier: str) -> bool:
        """
        Verifica si un modelo existe.

        Parameters
        ----------
        identifier:
            Identificador del modelo.

        Returns
        -------
        bool
            True si existe.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, identifier: str) -> None:
        """
        Elimina un modelo almacenado.

        Parameters
        ----------
        identifier:
            Identificador del modelo.
        """
        raise NotImplementedError

    @abstractmethod
    def list_models(self) -> list[ModelMetadata]:
        """
        Lista los modelos disponibles.

        Returns
        -------
        list[ModelMetadata]
            Metadatos de los modelos disponibles.
        """
        raise NotImplementedError
