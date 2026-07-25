"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_artifact_repository.py

Descripción:
Pruebas unitarias para el contrato ArtifactRepository.
-----------------------------------------------------------------------
"""

from abc import ABC,abstractmethod

import pytest

from src.data_science.ml.persistence.contracts.artifact_repository import (
    ArtifactRepository,
)


def test_repository_is_abstract() -> None:
    """Debe heredar de ABC."""

    assert issubclass(ArtifactRepository, ABC)


def test_repository_cannot_be_instantiated() -> None:
    """No debe poder instanciarse directamente."""

    with pytest.raises(TypeError):
        ArtifactRepository()


def test_save_is_abstract() -> None:
    """El método save debe ser abstracto."""

    assert ArtifactRepository.save.__isabstractmethod__ is True


def test_load_is_abstract() -> None:
    """El método load debe ser abstracto."""

    assert ArtifactRepository.load.__isabstractmethod__ is True


def test_exists_is_abstract() -> None:
    """El método exists debe ser abstracto."""

    assert ArtifactRepository.exists.__isabstractmethod__ is True


def test_delete_is_abstract() -> None:
    """El método delete debe ser abstracto."""

    assert ArtifactRepository.delete.__isabstractmethod__ is True


def test_list_models_is_abstract() -> None:
    """El método list_models debe ser abstracto."""

    assert ArtifactRepository.list_models.__isabstractmethod__ is True
