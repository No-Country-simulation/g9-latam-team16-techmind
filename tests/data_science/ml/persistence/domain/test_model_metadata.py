"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_model_metadata.py
Autor    : Equipo Data Science
Fecha    : 2026-07-24

Descripción:
Pruebas unitarias para la entidad de dominio ModelMetadata.

Estas pruebas verifican que la entidad cumpla con los principios
definidos para la capa de dominio:

- Creación correcta de la entidad.
- Inicialización de atributos.
- Valores por defecto.
- Inmutabilidad.
- Igualdad entre instancias.
- Generación del identificador.
- Validación del formato de serialización.

Las pruebas no realizan acceso a archivos ni dependen de otros
componentes del sistema.
-----------------------------------------------------------------------
"""

from datetime import datetime

import pytest

from src.data_science.ml.persistence.domain.model_metadata import (
    DEFAULT_FRAMEWORK,
    DEFAULT_SERIALIZATION_FORMAT,
    ModelMetadata,
)


def create_metadata() -> ModelMetadata:
    """
    Crea una instancia de ModelMetadata para reutilizar
    durante las pruebas unitarias.
    """
    return ModelMetadata(
        model_name="techmind_classifier",
        version="1.0.0",
        algorithm="LogisticRegression",
        created_at=datetime(2026, 7, 24, 10, 30),
        training_dataset="dataset_v1.csv",
        feature_count=250,
        label_count=8,
        checksum="abc123xyz456",
    )


def test_should_create_model_metadata_successfully() -> None:
    """Verifica la creación correcta de la entidad."""

    metadata = create_metadata()

    assert metadata.model_name == "techmind_classifier"
    assert metadata.version == "1.0.0"
    assert metadata.algorithm == "LogisticRegression"
    assert metadata.training_dataset == "dataset_v1.csv"
    assert metadata.feature_count == 250
    assert metadata.label_count == 8
    assert metadata.checksum == "abc123xyz456"


def test_should_use_default_values() -> None:
    """Verifica la inicialización de los valores por defecto."""

    metadata = create_metadata()

    assert metadata.framework == DEFAULT_FRAMEWORK
    assert metadata.serialization_format == DEFAULT_SERIALIZATION_FORMAT
    assert metadata.description == ""
    assert metadata.author == ""


def test_should_generate_identifier() -> None:
    """Verifica la generación del identificador único."""

    metadata = create_metadata()

    assert metadata.identifier == "techmind_classifier:1.0.0"


def test_should_identify_joblib_serialization() -> None:
    """Verifica el formato de serialización."""

    metadata = create_metadata()

    assert metadata.is_serialized_with_joblib is True


def test_should_compare_equal_instances() -> None:
    """Dos objetos con la misma información deben ser iguales."""

    metadata_1 = create_metadata()
    metadata_2 = create_metadata()

    assert metadata_1 == metadata_2


def test_should_be_immutable() -> None:
    """Verifica que la entidad sea inmutable."""

    metadata = create_metadata()

    with pytest.raises(AttributeError):
        metadata.model_name = "nuevo_modelo"
