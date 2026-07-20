"""
==========================================================
TechMind
Componente Data Science

Módulo:
    pdf_reader.py

Descripción:
    Implementa el lector para archivos PDF utilizando
    la biblioteca pypdf.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

# from pypdf import PdfReader
from pypdf import PdfReader as PyPdfReader

from .base_reader import BaseReader


# ==========================================================
# PDF Reader
# ==========================================================

class PdfReader(BaseReader):
    """
    Lector para archivos PDF.
    """

    # ======================================================
    # API pública
    # ======================================================

    def read(
        self,
        file: Path,
    ) -> str:
        """
        Lee un archivo PDF y devuelve todo su contenido
        textual.

        Parameters
        ----------
        file : Path
            Ruta del archivo PDF.

        Returns
        -------
        str
            Texto extraído del documento.
        """

        pdf = PyPdfReader(file)

        pages: list[str] = []

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                pages.append(text)

        return "\n".join(pages)