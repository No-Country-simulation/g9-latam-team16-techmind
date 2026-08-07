"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_artifact_constants.py

Descripción:
Pruebas unitarias para las constantes del módulo de persistencia.
-----------------------------------------------------------------------
"""

from src.data_science.ml.persistence.constants.artifact_constants import (
    LABEL_ENCODER_FILENAME,
    METADATA_FILENAME,
    MODEL_FILENAME,
    VECTORIZER_FILENAME,
)


def test_model_filename() -> None:
    assert MODEL_FILENAME == "model.joblib"


def test_vectorizer_filename() -> None:
    assert VECTORIZER_FILENAME == "vectorizer.joblib"


def test_label_encoder_filename() -> None:
    assert LABEL_ENCODER_FILENAME == "label_encoder.joblib"


def test_metadata_filename() -> None:
    assert METADATA_FILENAME == "metadata.json"
