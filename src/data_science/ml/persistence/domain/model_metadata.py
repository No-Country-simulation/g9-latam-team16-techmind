"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : model_metadata.py
Autor    : Equipo Data Science
Fecha    : 2026-07-24

Descripción:
Define la entidad de dominio ModelMetadata, encargada de representar
los metadatos asociados a un modelo entrenado.

Esta entidad almacena la información descriptiva del artefacto
persistido, incluyendo nombre, versión, algoritmo, framework,
dataset de entrenamiento, checksum de integridad y demás atributos
necesarios para identificar y validar un modelo.

Al pertenecer a la capa de Dominio, esta clase no contiene lógica
de persistencia, acceso al sistema de archivos ni dependencias con
la infraestructura del proyecto.
-----------------------------------------------------------------------
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

DEFAULT_FRAMEWORK = "scikit-learn"
DEFAULT_SERIALIZATION_FORMAT = "joblib"


@dataclass(frozen=True, slots=True)
class ModelMetadata:
    """
    Representa los metadatos de un modelo entrenado.

    Esta entidad contiene la información necesaria para identificar,
    validar y administrar un modelo persistido durante su ciclo de vida.

    Al ser una entidad de dominio es inmutable y no posee lógica de
    persistencia ni acceso a recursos externos.
    """

    model_name: str
    version: str
    algorithm: str
    created_at: datetime
    training_dataset: str
    feature_count: int
    label_count: int
    checksum: str

    framework: str = DEFAULT_FRAMEWORK
    serialization_format: str = DEFAULT_SERIALIZATION_FORMAT
    description: str = ""
    author: str = ""

    @property
    def identifier(self) -> str:
        """
        Obtiene un identificador único compuesto por el nombre y
        la versión del modelo.

        Returns
        -------
        str
            Identificador del modelo.
        """
        return f"{self.model_name}:{self.version}"

    @property
    def is_serialized_with_joblib(self) -> bool:
        """
        Indica si el modelo fue serializado utilizando Joblib.

        Returns
        -------
        bool
            True si el formato corresponde a Joblib.
        """
        return self.serialization_format.lower() == "joblib"
