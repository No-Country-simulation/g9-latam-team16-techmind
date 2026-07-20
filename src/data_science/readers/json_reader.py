"""
==========================================================
TechMind
Componente Data Science

Módulo:
    json_reader.py

Descripción:
    Implementa el lector para archivos JSON.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import json

from pathlib import Path
from typing import Any

from .base_reader import BaseReader


# ==========================================================
# JSON Reader
# ==========================================================

class JsonReader(BaseReader):
    """
    Lector para archivos JSON.
    """

    DEFAULT_ENCODING = "utf-8"

    # ======================================================
    # API pública
    # ======================================================

    def read(
        self,
        file: Path,
    ) -> Any:
        
        """
        Lee un archivo JSON y devuelve su contenido.

        Parameters
        ----------
        file : Path
            Ruta del archivo.

        Returns
        -------
        Any
            Contenido del archivo convertido a objetos Python.
        """

        with file.open(
            mode="r",
            encoding=self.DEFAULT_ENCODING,
        ) as fp:

            return json.load(fp)