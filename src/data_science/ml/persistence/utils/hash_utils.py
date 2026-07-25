"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : hash_utils.py

Descripción:
Utilidades para calcular y verificar hashes SHA-256 de archivos y
datos en memoria.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

import hashlib
from pathlib import Path


class HashUtils:
    """
    Utilidades para el cálculo y verificación de hashes SHA-256.
    """

    CHUNK_SIZE = 8192

    @staticmethod
    def calculate_file_hash(file_path: Path) -> str:
        """
        Calcula el hash SHA-256 de un archivo.

        Parameters
        ----------
        file_path:
            Ruta del archivo.

        Returns
        -------
        str
            Hash SHA-256 en formato hexadecimal.
        """

        sha256 = hashlib.sha256()

        with file_path.open("rb") as file:

            while chunk := file.read(HashUtils.CHUNK_SIZE):
                sha256.update(chunk)

        return sha256.hexdigest()

    @staticmethod
    def calculate_bytes_hash(data: bytes) -> str:
        """
        Calcula el hash SHA-256 de un bloque de bytes.

        Parameters
        ----------
        data:
            Datos en memoria.

        Returns
        -------
        str
            Hash SHA-256 en formato hexadecimal.
        """

        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def verify_checksum(
        checksum: str,
        expected_checksum: str,
    ) -> bool:
        """
        Verifica si dos hashes son iguales.

        Parameters
        ----------
        checksum:
            Hash calculado.

        expected_checksum:
            Hash esperado.

        Returns
        -------
        bool
            True si ambos hashes coinciden.
        """

        return checksum == expected_checksum
