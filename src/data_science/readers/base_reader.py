"""
==========================================================
TechMind
Componente Data Science

Módulo:
    base_reader.py

Descripción:
    Define la clase base para todos los lectores de
    archivos utilizados por los loaders.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


# ==========================================================
# Base Reader
# ==========================================================

class BaseReader(ABC):
    """
    Clase base para todos los lectores de archivos.

    Cada implementación es responsable de interpretar
    un formato específico (TXT, JSON, PDF, CSV, etc.).
    """

    @abstractmethod
    def read(
        self,
        file: Path,
    ) -> Any:
        """
        Lee un archivo y devuelve su contenido.

        Parameters
        ----------
        file : Path
            Ruta del archivo a leer.

        Returns
        -------
        Any
            Contenido interpretado según el tipo de archivo.
        """
        raise NotImplementedError
    
