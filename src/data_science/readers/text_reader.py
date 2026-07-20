"""
==========================================================
TechMind
Componente Data Science

Módulo:
    text_reader.py

Descripción:
    Implementa el lector para archivos de texto plano
    y Markdown.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

from .base_reader import BaseReader


# ==========================================================
# Text Reader
# ==========================================================

class TextReader(BaseReader):
    """
    Lector para archivos de texto plano y Markdown.
    """

    DEFAULT_ENCODING = "utf-8"

    DEFAULT_ERRORS = "ignore"

    # ======================================================
    # API pública
    # ======================================================

    def read(
        self,
        file: Path,
    ) -> str:
        """
        Lee un archivo de texto y devuelve su contenido.

        Parameters
        ----------
        file : Path
            Ruta del archivo.

        Returns
        -------
        str
            Contenido del archivo.
        """

        return file.read_text(
            encoding=self.DEFAULT_ENCODING,
            errors=self.DEFAULT_ERRORS,
        )