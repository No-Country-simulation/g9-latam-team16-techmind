"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : integrity_validator.py

Descripción:
Validador encargado de verificar la integridad de los artefactos
almacenados mediante hashes SHA-256.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

from pathlib import Path

from src.data_science.ml.persistence.exceptions.corrupted_artifact_exception import (
    CorruptedArtifactException,
)
from src.data_science.ml.persistence.utils.hash_utils import HashUtils


class IntegrityValidator:
    """
    Valida la integridad de artefactos persistidos.
    """

    @staticmethod
    def validate_checksum(
        checksum: str,
        expected_checksum: str,
    ) -> None:
        """
        Verifica que dos checksums sean iguales.

        Parameters
        ----------
        checksum:
            Checksum calculado.

        expected_checksum:
            Checksum esperado.

        Raises
        ------
        CorruptedArtifactException
            Cuando ambos checksums son diferentes.
        """

        if not HashUtils.verify_checksum(
            checksum,
            expected_checksum,
        ):
            raise CorruptedArtifactException(
                "Checksum inválido. "
                f"Esperado: {expected_checksum}. "
                f"Calculado: {checksum}."
            )

    @staticmethod
    def validate_file(
        file_path: Path,
        expected_checksum: str,
    ) -> None:
        """
        Verifica la integridad de un archivo.

        Parameters
        ----------
        file_path:
            Archivo a validar.

        expected_checksum:
            Checksum esperado.
        """

        checksum = HashUtils.calculate_file_hash(file_path)

        IntegrityValidator.validate_checksum(
            checksum,
            expected_checksum,
        )
