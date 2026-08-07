"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_exceptions.py

Descripción:
Pruebas unitarias para la jerarquía de excepciones del módulo de
persistencia.
-----------------------------------------------------------------------
"""

import pytest

from src.data_science.ml.persistence.exceptions.artifact_not_found_exception import (
    ArtifactNotFoundException,
)
from src.data_science.ml.persistence.exceptions.corrupted_artifact_exception import (
    CorruptedArtifactException,
)
from src.data_science.ml.persistence.exceptions.invalid_version_exception import (
    InvalidVersionException,
)
from src.data_science.ml.persistence.exceptions.metadata_exception import (
    MetadataException,
)
from src.data_science.ml.persistence.exceptions.persistence_exception import (
    PersistenceException,
)
from src.data_science.ml.persistence.exceptions.storage_exception import (
    StorageException,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        StorageException,
        MetadataException,
        ArtifactNotFoundException,
        InvalidVersionException,
        CorruptedArtifactException,
    ],
)
def test_exceptions_inherit_from_persistence(
    exception_class: type[PersistenceException],
) -> None:
    """Todas las excepciones deben heredar de PersistenceException."""

    assert issubclass(exception_class, PersistenceException)


@pytest.mark.parametrize(
    "exception_class",
    [
        PersistenceException,
        StorageException,
        MetadataException,
        ArtifactNotFoundException,
        InvalidVersionException,
        CorruptedArtifactException,
    ],
)
def test_exceptions_inherit_from_exception(
    exception_class: type[Exception],
) -> None:
    """Todas las excepciones deben heredar de Exception."""

    assert issubclass(exception_class, Exception)


@pytest.mark.parametrize(
    "exception_class",
    [
        PersistenceException,
        StorageException,
        MetadataException,
        ArtifactNotFoundException,
        InvalidVersionException,
        CorruptedArtifactException,
    ],
)
def test_exception_message(
    exception_class: type[Exception],
) -> None:
    """Debe conservar el mensaje recibido."""

    message = "Error de prueba"

    exception = exception_class(message)

    assert str(exception) == message


@pytest.mark.parametrize(
    "exception_class",
    [
        PersistenceException,
        StorageException,
        MetadataException,
        ArtifactNotFoundException,
        InvalidVersionException,
        CorruptedArtifactException,
    ],
)
def test_raise_exception(
    exception_class: type[Exception],
) -> None:
    """Debe poder lanzarse mediante raise."""

    with pytest.raises(exception_class):
        raise exception_class("Error")
