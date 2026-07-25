"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : invalid_version_exception.py

Descripción:
Excepción lanzada cuando una versión solicitada es inválida.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.exceptions.persistence_exception import (
    PersistenceException,
)


class InvalidVersionException(PersistenceException):
    """
    La versión solicitada no es válida.
    """

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            error_code="INVALID_VERSION",
        )
