"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : artifact_not_found_exception.py

Descripción:
Excepción lanzada cuando un artefacto solicitado no existe.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.exceptions.persistence_exception import (
    PersistenceException,
)


class ArtifactNotFoundException(PersistenceException):
    """
    El artefacto solicitado no existe.
    """

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            error_code="ARTIFACT_NOT_FOUND",
        )
