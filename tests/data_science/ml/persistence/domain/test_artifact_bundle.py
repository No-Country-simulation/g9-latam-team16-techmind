"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_artifact_bundle.py

Descripción:
Pruebas unitarias para la entidad ArtifactBundle.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.domain.artifact_bundle import ArtifactBundle
from src.data_science.ml.persistence.domain.model_metadata import ModelMetadata


def create_metadata() -> ModelMetadata:
    """Crea una instancia válida de ModelMetadata para las pruebas."""

    return ModelMetadata(
        model_name="Clasificador",
        version="1.0.0",
        algorithm="LogisticRegression",
        created_at="2026-07-24T12:00:00",
        training_dataset="dataset.csv",
        feature_count=150,
        label_count=5,
        checksum="abc123",
    )


def test_create_bundle() -> None:
    """Debe crear correctamente un ArtifactBundle."""

    bundle = ArtifactBundle(
        model=object(),
        vectorizer=object(),
        metadata=create_metadata(),
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
        label_encoder=object(),
        label_encoder_filename="encoder.joblib",
    )

    assert bundle.model is not None
    assert bundle.vectorizer is not None
    assert bundle.metadata.model_name == "Clasificador"
    assert bundle.has_label_encoder is True


def test_create_bundle_without_label_encoder() -> None:
    """Debe permitir crear un bundle sin LabelEncoder."""

    bundle = ArtifactBundle(
        model=object(),
        vectorizer=object(),
        metadata=create_metadata(),
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
    )

    assert bundle.has_label_encoder is False


def test_artifact_count_with_encoder() -> None:
    """Debe contar cuatro artefactos cuando existe LabelEncoder."""

    bundle = ArtifactBundle(
        model=object(),
        vectorizer=object(),
        metadata=create_metadata(),
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
        label_encoder=object(),
        label_encoder_filename="encoder.joblib",
    )

    assert bundle.artifact_count == 4


def test_artifact_count_without_encoder() -> None:
    """Debe contar tres artefactos cuando no existe LabelEncoder."""

    bundle = ArtifactBundle(
        model=object(),
        vectorizer=object(),
        metadata=create_metadata(),
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
    )

    assert bundle.artifact_count == 3


def test_artifact_names() -> None:
    """Debe devolver los nombres de los artefactos."""

    bundle = ArtifactBundle(
        model=object(),
        vectorizer=object(),
        metadata=create_metadata(),
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
        label_encoder=object(),
        label_encoder_filename="encoder.joblib",
    )

    assert bundle.artifact_names == (
        "model.joblib",
        "vectorizer.joblib",
        "encoder.joblib",
    )


def test_model_required() -> None:
    """Debe lanzar excepción cuando el modelo es None."""

    try:
        ArtifactBundle(
            model=None,
            vectorizer=object(),
            metadata=create_metadata(),
            model_filename="model.joblib",
            vectorizer_filename="vectorizer.joblib",
        )
        assert False
    except ValueError:
        assert True


def test_vectorizer_required() -> None:
    """Debe lanzar excepción cuando el vectorizador es None."""

    try:
        ArtifactBundle(
            model=object(),
            vectorizer=None,
            metadata=create_metadata(),
            model_filename="model.joblib",
            vectorizer_filename="vectorizer.joblib",
        )
        assert False
    except ValueError:
        assert True


def test_metadata_required() -> None:
    """Debe lanzar excepción cuando metadata es None."""

    try:
        ArtifactBundle(
            model=object(),
            vectorizer=object(),
            metadata=None,
            model_filename="model.joblib",
            vectorizer_filename="vectorizer.joblib",
        )
        assert False
    except ValueError:
        assert True
