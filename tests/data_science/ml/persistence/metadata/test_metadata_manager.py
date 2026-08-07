"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_metadata_manager.py

Descripción:
Pruebas unitarias para MetadataManager.
-----------------------------------------------------------------------
"""

from datetime import datetime

from src.data_science.ml.persistence.domain.model_metadata import (
    ModelMetadata,
)
from src.data_science.ml.persistence.metadata.metadata_manager import (
    MetadataManager,
)


def create_metadata() -> ModelMetadata:
    """
    Construye un ModelMetadata válido para pruebas.
    """

    return ModelMetadata(
        model_name="Clasificador",
        version="1.0.0",
        algorithm="LogisticRegression",
        created_at=datetime(
            2026,
            7,
            24,
            12,
            0,
            0,
        ),
        training_dataset="dataset.csv",
        feature_count=150,
        label_count=5,
        checksum="abc123",
    )


def test_to_dict() -> None:
    """
    Debe convertir correctamente un ModelMetadata a diccionario.
    """

    metadata = create_metadata()

    data = MetadataManager.to_dict(metadata)

    assert data["model_name"] == "Clasificador"
    assert data["version"] == "1.0.0"
    assert data["created_at"] == "2026-07-24T12:00:00"


def test_from_dict() -> None:
    """
    Debe reconstruir correctamente un ModelMetadata.
    """

    metadata = create_metadata()

    data = MetadataManager.to_dict(metadata)

    restored = MetadataManager.from_dict(data)

    assert restored == metadata


def test_to_json() -> None:
    """
    Debe serializar correctamente a JSON.
    """

    metadata = create_metadata()

    json_text = MetadataManager.to_json(metadata)

    assert '"model_name"' in json_text
    assert '"version"' in json_text
    assert '"created_at"' in json_text


def test_from_json() -> None:
    """
    Debe reconstruir un ModelMetadata desde JSON.
    """

    metadata = create_metadata()

    json_text = MetadataManager.to_json(metadata)

    restored = MetadataManager.from_json(json_text)

    assert restored == metadata


def test_round_trip() -> None:
    """
    Debe conservar toda la información después de serializar y deserializar.
    """

    metadata = create_metadata()

    restored = MetadataManager.from_json(MetadataManager.to_json(metadata))

    assert restored == metadata
