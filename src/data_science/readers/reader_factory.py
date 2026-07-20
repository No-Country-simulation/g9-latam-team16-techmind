"""
==========================================================
TechMind
Componente Data Science

Módulo:
    reader_factory.py

Descripción:
    Implementa la fábrica de lectores de archivos.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

from .base_reader import BaseReader
from .csv_reader import CsvReader
from .json_reader import JsonReader
from .pdf_reader import PdfReader
from .text_reader import TextReader


# ==========================================================
# Reader Factory
# ==========================================================

class ReaderFactory:
    """
    Fábrica para crear lectores según la extensión del
    archivo.
    """

    _READERS = {
        ".txt": TextReader,
        ".md": TextReader,
        ".json": JsonReader,
        ".csv": CsvReader,
        ".pdf": PdfReader,
    }

    @classmethod
    def create(
        cls,
        file: Path,
    ) -> BaseReader:
        """
        Devuelve el lector correspondiente a un archivo.

        Parameters
        ----------
        file : Path
            Archivo cuyo formato se desea leer.

        Returns
        -------
        BaseReader
            Instancia del lector correspondiente.

        Raises
        ------
        ValueError
            Si la extensión no está soportada.
        """

        extension = file.suffix.lower()

        reader_class = cls._READERS.get(extension)

        if reader_class is None:
            raise ValueError(
                f"No existe un reader para '{extension}'."
            )

        return reader_class()