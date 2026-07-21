"""
TechMind
Data Science Component

Module:
    base_preprocessor.py

Description:
    Define el contrato base para todos los componentes de
    preprocesamiento del pipeline.

Sprint:
    DS-04 - Preprocesamiento del Dataset
"""

from abc import ABC, abstractmethod

from data_science.data.domain import (
    DocumentRecord,
    ProcessedDocument,
)


class BasePreprocessor(ABC):
    """
    Clase base para todos los componentes de preprocesamiento.

    Cada implementación recibe un documento y devuelve un
    ProcessedDocument con las transformaciones realizadas.
    """

    @abstractmethod
    def process(
        self,
        document: DocumentRecord,
    ) -> ProcessedDocument:
        """
        Ejecuta el proceso de preprocesamiento sobre un documento.

        Parameters
        ----------
        document : DocumentRecord
            Documento de entrada.

        Returns
        -------
        ProcessedDocument
            Documento resultante del preprocesamiento.
        """
        raise NotImplementedError