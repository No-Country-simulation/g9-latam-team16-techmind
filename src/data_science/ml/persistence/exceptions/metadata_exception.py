"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : metadata_exception.py

Descripción:
Excepción relacionada con errores en los metadatos.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.exceptions.persistence_exception import (
    PersistenceException,
)


class MetadataException(PersistenceException):
    """
    Error relacionado con los metadatos.
    """

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            error_code="METADATA_ERROR",
        )
