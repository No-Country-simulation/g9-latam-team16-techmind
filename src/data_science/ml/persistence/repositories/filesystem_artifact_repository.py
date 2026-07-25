"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : filesystem_artifact_repository.py

Descripción:
Implementación de ArtifactRepository utilizando el sistema de archivos
local como mecanismo de persistencia.

En esta primera etapa únicamente se implementa la inicialización del
repositorio y la preparación del directorio raíz de almacenamiento.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

from pathlib import Path

from src.data_science.ml.persistence.contracts.artifact_repository import (
    ArtifactRepository,
)
from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)
from src.data_science.ml.persistence.domain.model_metadata import (
    ModelMetadata,
)


class FilesystemArtifactRepository(ArtifactRepository):
    """
    Repositorio de persistencia basado en el sistema de archivos.
    """

    def __init__(
        self,
        root_directory: str | Path,
    ) -> None:
        """
        Inicializa el repositorio.

        Parameters
        ----------
        root_directory:
            Directorio raíz donde se almacenarán los modelos.
        """

        self._root_directory = Path(root_directory)
        self._root_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    @property
    def root_directory(self) -> Path:
        """
        Obtiene el directorio raíz del repositorio.
        """

        return self._root_directory

    def save(
        self,
        bundle: ArtifactBundle,
    ) -> str:
        """
        Almacena un conjunto de artefactos.
        """

        raise NotImplementedError

    def load(
        self,
        identifier: str,
    ) -> ArtifactBundle:
        """
        Recupera un conjunto de artefactos.
        """

        raise NotImplementedError

    def exists(
        self,
        identifier: str,
    ) -> bool:
        """
        Verifica si un modelo existe.
        """

        raise NotImplementedError

    def delete(
        self,
        identifier: str,
    ) -> None:
        """
        Elimina un modelo almacenado.
        """

        raise NotImplementedError

    def list_models(
        self,
    ) -> list[ModelMetadata]:
        """
        Lista los modelos disponibles.
        """

        raise NotImplementedError
