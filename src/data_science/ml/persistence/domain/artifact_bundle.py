"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : artifact_bundle.py

Descripción:
Define la entidad de dominio que agrupa todos los artefactos generados
durante el entrenamiento de un modelo de Machine Learning. Esta entidad
es utilizada por los servicios de persistencia para almacenar y recuperar
un modelo completo junto con sus componentes asociados.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.data_science.ml.persistence.domain.model_metadata import ModelMetadata

ModelArtifact = Any
VectorizerArtifact = Any
LabelEncoderArtifact = Any


@dataclass(frozen=True, slots=True)
class ArtifactBundle:
    """
    Agrupa todos los artefactos necesarios para reconstruir un modelo
    entrenado.
    """

    model: ModelArtifact
    vectorizer: VectorizerArtifact
    metadata: ModelMetadata

    model_filename: str
    vectorizer_filename: str

    label_encoder: LabelEncoderArtifact | None = None
    label_encoder_filename: str | None = None

    def __post_init__(self) -> None:
        """Valida la consistencia mínima del bundle."""

        if self.model is None:
            raise ValueError("El modelo no puede ser None.")

        if self.vectorizer is None:
            raise ValueError("El vectorizador no puede ser None.")

        if self.metadata is None:
            raise ValueError("Los metadatos no pueden ser None.")

    @property
    def has_label_encoder(self) -> bool:
        """Indica si el bundle contiene un Label Encoder."""
        return self.label_encoder is not None

    @property
    def artifact_count(self) -> int:
        """Devuelve la cantidad de artefactos incluidos."""
        return 4 if self.has_label_encoder else 3

    @property
    def artifact_names(self) -> tuple[str, ...]:
        """Devuelve los nombres de los archivos de los artefactos."""

        names = [
            self.model_filename,
            self.vectorizer_filename,
        ]

        if self.label_encoder_filename is not None:
            names.append(self.label_encoder_filename)

        return tuple(names)
