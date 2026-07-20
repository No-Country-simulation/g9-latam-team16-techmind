"""
==========================================================
TechMind
Componente Data Science

Módulo:
    csv_reader.py

Descripción:
    Implementa el lector para archivos CSV.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pandas as pd

from .base_reader import BaseReader


# ==========================================================
# CSV Reader
# ==========================================================

class CsvReader(BaseReader):
    """
    Lector para archivos CSV.
    """

    DEFAULT_SEPARATOR = ","

    DEFAULT_ENCODING = "utf-8"

    # ======================================================
    # API pública
    # ======================================================

    def read(
        self,
        file: Path,
    ) -> pd.DataFrame:
        """
        Lee un archivo CSV y devuelve un DataFrame.

        Parameters
        ----------
        file : Path
            Ruta del archivo.

        Returns
        -------
        pd.DataFrame
            Contenido del archivo.
        """

        return pd.read_csv(
            file,
            sep=self.DEFAULT_SEPARATOR,
            encoding=self.DEFAULT_ENCODING,
        )
