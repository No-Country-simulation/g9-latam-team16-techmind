"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : storage_exception.py

Descripción:
Excepción relacionada con errores de almacenamiento.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.exceptions.persistence_exception import (
    PersistenceException,
)


class StorageException(PersistenceException):
    """
    Error relacionado con el almacenamiento físico de artefactos.
    """

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            error_code="STORAGE_ERROR",
        )
