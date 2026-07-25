"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_filesystem_artifact_repository.py

Descripción:
Pruebas unitarias para FilesystemArtifactRepository.

En esta etapa únicamente se valida la inicialización del repositorio.
-----------------------------------------------------------------------
"""

from pathlib import Path

from src.data_science.ml.persistence.repositories.filesystem_artifact_repository import (
    FilesystemArtifactRepository,
)


from datetime import datetime

from sklearn.linear_model import LogisticRegression

from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)
from src.data_science.ml.persistence.domain.model_metadata import (
    ModelMetadata,
)


def test_constructor_creates_directory(
    tmp_path: Path,
) -> None:
    """
    Debe crear automáticamente el directorio raíz.
    """

    repository_path = tmp_path / "models"

    repository = FilesystemArtifactRepository(
        repository_path,
    )

    assert repository.root_directory.exists()
    assert repository.root_directory.is_dir()


def test_constructor_accepts_existing_directory(
    tmp_path: Path,
) -> None:
    """
    Debe aceptar un directorio existente.
    """

    repository_path = tmp_path / "models"
    repository_path.mkdir()

    repository = FilesystemArtifactRepository(
        repository_path,
    )

    assert repository.root_directory == repository_path


def test_root_directory_is_path(
    tmp_path: Path,
) -> None:
    """
    Debe exponer la ruta como objeto Path.
    """

    repository = FilesystemArtifactRepository(
        tmp_path,
    )

    assert isinstance(
        repository.root_directory,
        Path,
    )


def test_save_model(
    tmp_path: Path,
) -> None:
    """
    Debe guardar correctamente un modelo.
    """

    repository = FilesystemArtifactRepository(
        tmp_path,
    )

    metadata = ModelMetadata(
        model_name="classifier",
        version="1.0.0",
        algorithm="LogisticRegression",
        created_at=datetime.now(),
        training_dataset="dataset.csv",
        feature_count=100,
        label_count=2,
        checksum="abc",
    )

    bundle = ArtifactBundle(
        model=LogisticRegression(),
        vectorizer=object(),
        metadata=metadata,
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
    )

    identifier = repository.save(
        bundle,
    )

    assert identifier == metadata.identifier

    assert (tmp_path / identifier / "model.joblib").exists()
