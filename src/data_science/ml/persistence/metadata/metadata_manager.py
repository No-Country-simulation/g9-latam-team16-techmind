"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : metadata_manager.py

Descripción:
Gestiona la serialización y deserialización de ModelMetadata.

Autor    : Equipo Data Science
-----------------------------------------------------------------------
"""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from typing import Any

from src.data_science.ml.persistence.domain.model_metadata import (
    ModelMetadata,
)


class MetadataManager:
    """
    Gestiona la serialización y deserialización de ModelMetadata.
    """

    @staticmethod
    def to_dict(
        metadata: ModelMetadata,
    ) -> dict[str, Any]:
        """
        Convierte ModelMetadata a un diccionario serializable.
        """

        data = asdict(metadata)

        data["created_at"] = metadata.created_at.isoformat()

        return data

    @staticmethod
    def from_dict(
        data: dict[str, Any],
    ) -> ModelMetadata:
        """
        Construye un ModelMetadata desde un diccionario.
        """

        return ModelMetadata(
            model_name=str(data["model_name"]),
            version=str(data["version"]),
            algorithm=str(data["algorithm"]),
            created_at=datetime.fromisoformat(str(data["created_at"])),
            training_dataset=str(data["training_dataset"]),
            feature_count=int(data["feature_count"]),
            label_count=int(data["label_count"]),
            checksum=str(data["checksum"]),
            framework=str(data["framework"]),
            serialization_format=str(data["serialization_format"]),
            description=str(data["description"]),
            author=str(data["author"]),
        )

    @staticmethod
    def to_json(
        metadata: ModelMetadata,
    ) -> str:
        """
        Convierte ModelMetadata a JSON.
        """

        return json.dumps(
            MetadataManager.to_dict(metadata),
            indent=4,
            ensure_ascii=False,
        )

    @staticmethod
    def from_json(
        json_text: str,
    ) -> ModelMetadata:
        """
        Reconstruye un ModelMetadata desde JSON.
        """

        data = json.loads(json_text)

        return MetadataManager.from_dict(data)
