"""
==========================================================
TechMind
Componente Data Science

Módulo:
    base_loader.py

Descripción:
    Define la clase base para todos los cargadores de
    datos del proyecto.

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

import pandas as pd

from ..data.domain import DocumentRecord
from ..readers import ReaderFactory


# ==========================================================
# Base Loader
# ==========================================================

class BaseLoader(ABC):
    """
    Clase base para todos los cargadores de datos.
    """

    # ======================================================
    # Configuración
    # ======================================================

    SUPPORTED_EXTENSIONS: tuple[str, ...] = ()

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(
        self,
        source_path: str,
    ) -> None:

        self._source_path = Path(source_path)

    # ======================================================
    # API pública
    # ======================================================

    @abstractmethod
    def load(self) -> pd.DataFrame:
        """
        Carga la información desde una fuente específica.
        """
        raise NotImplementedError

    # ======================================================
    # Métodos protegidos
    # ======================================================

    def _validate_source_path(self) -> None:
        """
        Verifica que exista la carpeta de origen.
        """

        if not self._source_path.exists():

            raise FileNotFoundError(
                f"No existe la ruta: {self._source_path}"
            )

    def _find_files(self) -> list[Path]:
        """
        Busca todos los archivos compatibles.
        """

        files: list[Path] = []

        for file in self._source_path.rglob("*"):

            if self._is_supported_file(file):

                files.append(file)

        return files

    def _is_supported_file(
        self,
        file: Path,
    ) -> bool:
        """
        Verifica si un archivo posee una extensión soportada.
        """

        return (
            file.is_file()
            and file.suffix.lower()
            in self.SUPPORTED_EXTENSIONS
        )

    def _read(
        self,
        file: Path,
    ) -> Any:
        """
        Lee un archivo utilizando el reader adecuado.
        """

        reader = ReaderFactory.create(file)

        return reader.read(file)

    def _build_records(
        self,
        sources: list[Any],
    ) -> list[DocumentRecord]:
        """
        Convierte una colección de elementos en registros
        del dominio.
        """

        return [
            self._build_record(source)
            for source in sources
        ]

    def _build_dataframe(
        self,
        records: list[DocumentRecord],
    ) -> pd.DataFrame:
        """
        Construye un DataFrame a partir de registros.
        """

        return pd.DataFrame(records)

    # ======================================================
    # Métodos abstractos
    # ======================================================

    @abstractmethod
    def _build_record(
        self,
        source: Any,
    ) -> DocumentRecord:
        """
        Convierte una fuente de datos en un registro del
        dominio.
        """
        raise NotImplementedError