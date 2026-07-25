"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_integrity_validator.py

Descripción:
Pruebas unitarias para IntegrityValidator.
-----------------------------------------------------------------------
"""

from pathlib import Path

import pytest

from src.data_science.ml.persistence.exceptions.corrupted_artifact_exception import (
    CorruptedArtifactException,
)
from src.data_science.ml.persistence.utils.hash_utils import HashUtils
from src.data_science.ml.persistence.validators.integrity_validator import (
    IntegrityValidator,
)


def test_validate_checksum_ok() -> None:
    """
    No debe lanzar excepción cuando los checksums coinciden.
    """

    checksum = HashUtils.calculate_bytes_hash(b"AyniKortex")

    IntegrityValidator.validate_checksum(
        checksum,
        checksum,
    )


def test_validate_checksum_fail() -> None:
    """
    Debe lanzar CorruptedArtifactException cuando los
    checksums son diferentes.
    """

    checksum = HashUtils.calculate_bytes_hash(b"Ayni")
    expected = HashUtils.calculate_bytes_hash(b"Kortex")

    with pytest.raises(CorruptedArtifactException):
        IntegrityValidator.validate_checksum(
            checksum,
            expected,
        )


def test_validate_file_ok(tmp_path: Path) -> None:
    """
    Debe validar correctamente un archivo íntegro.
    """

    file_path = tmp_path / "modelo.joblib"

    file_path.write_text(
        "Modelo de prueba",
        encoding="utf-8",
    )

    checksum = HashUtils.calculate_file_hash(file_path)

    IntegrityValidator.validate_file(
        file_path,
        checksum,
    )


def test_validate_file_fail(tmp_path: Path) -> None:
    """
    Debe detectar cuando un archivo fue modificado.
    """

    file_path = tmp_path / "modelo.joblib"

    file_path.write_text(
        "Contenido original",
        encoding="utf-8",
    )

    checksum = HashUtils.calculate_file_hash(file_path)

    file_path.write_text(
        "Contenido modificado",
        encoding="utf-8",
    )

    with pytest.raises(CorruptedArtifactException):
        IntegrityValidator.validate_file(
            file_path,
            checksum,
        )
