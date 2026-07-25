"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : persistence_exception.py

Descripción:
Excepción base para todos los errores del módulo de persistencia.
-----------------------------------------------------------------------
"""


class PersistenceException(Exception):
    """
    Excepción base para el módulo de persistencia.
    """

    def __init__(
        self,
        message: str,
        error_code: str = "PERSISTENCE_ERROR",
    ) -> None:
        self.error_code = error_code
        super().__init__(message)
