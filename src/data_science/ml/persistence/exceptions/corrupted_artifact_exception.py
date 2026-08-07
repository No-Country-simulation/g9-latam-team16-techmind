"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : corrupted_artifact_exception.py

Descripción:
Excepción lanzada cuando un artefacto almacenado está corrupto.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.exceptions.persistence_exception import (
    PersistenceException,
)


class CorruptedArtifactException(PersistenceException):
    """
    El artefacto almacenado está corrupto.
    """

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            error_code="CORRUPTED_ARTIFACT",
        )
