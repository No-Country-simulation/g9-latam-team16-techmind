"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : version_manager.py

Descripción:
Gestiona la validación, comparación y ordenamiento de versiones de
modelos siguiendo el estándar PEP 440.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

from packaging.version import InvalidVersion, Version

from src.data_science.ml.persistence.exceptions.invalid_version_exception import (
    InvalidVersionException,
)


class VersionManager:
    """
    Gestiona versiones de modelos.
    """

    @staticmethod
    def validate(version: str) -> Version:
        """
        Valida una versión y devuelve un objeto Version.

        Parameters
        ----------
        version:
            Versión a validar.

        Returns
        -------
        Version
            Objeto Version válido.

        Raises
        ------
        InvalidVersionException
            Si la versión no cumple con PEP 440.
        """

        try:
            return Version(version)

        except InvalidVersion as error:
            raise InvalidVersionException(f"Versión inválida: {version}") from error

    @staticmethod
    def compare(
        version1: str,
        version2: str,
    ) -> int:
        """
        Compara dos versiones.

        Returns
        -------
        int
            -1 si version1 < version2
             0 si son iguales
             1 si version1 > version2
        """

        v1 = VersionManager.validate(version1)
        v2 = VersionManager.validate(version2)

        if v1 < v2:
            return -1

        if v1 > v2:
            return 1

        return 0

    @staticmethod
    def sort_versions(
        versions: list[str],
    ) -> list[str]:
        """
        Ordena una lista de versiones.

        Returns
        -------
        list[str]
            Versiones ordenadas.
        """

        return sorted(
            versions,
            key=Version,
        )

    @staticmethod
    def latest(
        versions: list[str],
    ) -> str:
        """
        Devuelve la versión más reciente.

        Raises
        ------
        ValueError
            Si la lista está vacía.
        """

        if not versions:
            raise ValueError("La lista de versiones está vacía.")

        return max(
            versions,
            key=Version,
        )
