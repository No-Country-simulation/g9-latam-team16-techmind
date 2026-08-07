"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : filesystem_artifact_repository.py

Descripción:
Implementación de ArtifactRepository utilizando el sistema de archivos
local como mecanismo de persistencia.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

import shutil
from pathlib import Path

import joblib

from src.data_science.ml.persistence.constants.artifact_constants import (
    LABEL_ENCODER_FILENAME,
    METADATA_FILENAME,
    MODEL_FILENAME,
    VECTORIZER_FILENAME,
)
from src.data_science.ml.persistence.contracts.artifact_repository import (
    ArtifactRepository,
)
from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)
from src.data_science.ml.persistence.domain.model_metadata import (
    ModelMetadata,
)
from src.data_science.ml.persistence.metadata.metadata_manager import (
    MetadataManager,
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
        """

        self._root_directory = Path(root_directory)

        self._root_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    @property
    def root_directory(
        self,
    ) -> Path:
        """
        Devuelve el directorio raíz.
        """

        return self._root_directory

    def _model_directory(
        self,
        identifier: str,
    ) -> Path:
        """
        Obtiene (o crea) el directorio asociado a un modelo.
        """

        directory = self.root_directory / identifier

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return directory

    @staticmethod
    def _save_artifact(
        artifact: object,
        destination: Path,
    ) -> None:
        """
        Guarda un artefacto utilizando Joblib.
        """

        joblib.dump(
            artifact,
            destination,
        )

    @staticmethod
    def _save_metadata(
        metadata: ModelMetadata,
        destination: Path,
    ) -> None:
        """
        Guarda los metadatos del modelo.
        """

        destination.write_text(
            MetadataManager.to_json(metadata),
            encoding="utf-8",
        )

    def save(
        self,
        bundle: ArtifactBundle,
    ) -> str:
        """
        Guarda un conjunto de artefactos del modelo.

        Returns
        -------
        str
            Identificador del modelo almacenado.
        """

        identifier = bundle.metadata.identifier

        model_directory = self._model_directory(
            identifier,
        )

        self._save_artifact(
            bundle.model,
            model_directory / bundle.model_filename,
        )

        self._save_artifact(
            bundle.vectorizer,
            model_directory / bundle.vectorizer_filename,
        )

        if (
            bundle.has_label_encoder
            and bundle.label_encoder is not None
            and bundle.label_encoder_filename is not None
        ):
            self._save_artifact(
                bundle.label_encoder,
                model_directory / bundle.label_encoder_filename,
            )

        metadata_path = model_directory / METADATA_FILENAME

        self._save_metadata(
            bundle.metadata,
            metadata_path,
        )
        return identifier

    def load(
        self,
        identifier: str,
    ) -> ArtifactBundle:
        """
        Recupera un conjunto de artefactos previamente almacenados.
        """

        model_directory = self.root_directory / identifier

        metadata_path = model_directory / METADATA_FILENAME

        metadata = MetadataManager.from_json(
            metadata_path.read_text(
                encoding="utf-8",
            ),
        )

        model = joblib.load(
            model_directory / MODEL_FILENAME,
        )

        vectorizer = joblib.load(
            model_directory / VECTORIZER_FILENAME,
        )

        label_encoder_path = model_directory / LABEL_ENCODER_FILENAME

        label_encoder = None

        label_encoder_filename = None

        if label_encoder_path.exists():
            label_encoder = joblib.load(
                label_encoder_path,
            )

            label_encoder_filename = LABEL_ENCODER_FILENAME

        return ArtifactBundle(
            model=model,
            vectorizer=vectorizer,
            metadata=metadata,
            model_filename=MODEL_FILENAME,
            vectorizer_filename=VECTORIZER_FILENAME,
            label_encoder=label_encoder,
            label_encoder_filename=label_encoder_filename,
        )

    def exists(
        self,
        identifier: str,
    ) -> bool:
        """
        Verifica si existe un modelo almacenado.
        """

        return (self.root_directory / identifier).exists()

    def delete(
        self,
        identifier: str,
    ) -> None:
        """
        Elimina un modelo almacenado.
        """

        model_directory = self.root_directory / identifier

        if model_directory.exists():
            shutil.rmtree(
                model_directory,
            )

    def list_models(
        self,
    ) -> list[ModelMetadata]:
        """
        Lista los modelos disponibles.
        """

        models: list[ModelMetadata] = []

        for directory in self.root_directory.iterdir():

            if not directory.is_dir():
                continue

            metadata_path = directory / METADATA_FILENAME

            if not metadata_path.exists():
                continue

            metadata = MetadataManager.from_json(
                metadata_path.read_text(
                    encoding="utf-8",
                ),
            )

            models.append(
                metadata,
            )

        return models
