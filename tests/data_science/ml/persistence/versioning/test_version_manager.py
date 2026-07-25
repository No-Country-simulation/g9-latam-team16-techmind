"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_version_manager.py

Descripción:
Pruebas unitarias para VersionManager.
-----------------------------------------------------------------------
"""

import pytest
from packaging.version import Version

from src.data_science.ml.persistence.exceptions.invalid_version_exception import (
    InvalidVersionException,
)
from src.data_science.ml.persistence.versioning.version_manager import (
    VersionManager,
)


def test_validate_valid_version() -> None:
    """Debe aceptar una versión válida."""

    version = VersionManager.validate("1.0.0")

    assert isinstance(version, Version)


def test_validate_invalid_version() -> None:
    """Debe lanzar InvalidVersionException."""

    with pytest.raises(InvalidVersionException):
        VersionManager.validate("abc")


def test_compare_versions() -> None:
    """Debe comparar correctamente dos versiones."""

    assert VersionManager.compare("1.0.0", "2.0.0") == -1
    assert VersionManager.compare("2.0.0", "1.0.0") == 1
    assert VersionManager.compare("1.0.0", "1.0.0") == 0


def test_sort_versions() -> None:
    """Debe ordenar correctamente las versiones."""

    versions = [
        "2.0.0",
        "1.5.0",
        "1.0.0",
    ]

    assert VersionManager.sort_versions(versions) == [
        "1.0.0",
        "1.5.0",
        "2.0.0",
    ]


def test_latest_version() -> None:
    """Debe devolver la versión más reciente."""

    versions = [
        "1.0.0",
        "2.1.0",
        "1.8.0",
    ]

    assert VersionManager.latest(versions) == "2.1.0"


def test_latest_empty_list() -> None:
    """Debe lanzar ValueError si la lista está vacía."""

    with pytest.raises(ValueError):
        VersionManager.latest([])
