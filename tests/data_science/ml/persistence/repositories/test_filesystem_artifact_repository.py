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
