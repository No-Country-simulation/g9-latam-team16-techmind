"""
==========================================================
TechMind
Data Science Component

Module:
    test_predict_pipeline.py

Description:
    Unit tests for the PredictPipeline component.

Sprint:
    DS-08 - Inference Engine
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from unittest.mock import Mock

from src.data_science.data.domain import ProcessedDocument

from src.data_science.ml.inference.predict_pipeline import (
    PredictPipeline,
)

from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)

# ==========================================================
# Unit Tests
# ==========================================================


def test_predict_pipeline_returns_prediction():
    """
    Verifies that PredictPipeline executes the complete
    inference workflow and returns a PredictionResult.
    """

    # ------------------------------------------------------
    # Arrange
    # ------------------------------------------------------

    pipeline = PredictPipeline()

    preprocessing = Mock()

    processed_document = Mock(spec=ProcessedDocument)

    processed_document.processed_text = "texto procesado"

    preprocessing.process.return_value = processed_document

    pipeline._preprocessing = preprocessing

    vectorizer = Mock()

    vectorizer.transform.return_value = [[1, 2, 3]]

    model = Mock()

    model.predict.return_value = ["Backend"]

    model.predict_proba.return_value = [[0.02, 0.98]]

    metadata = Mock()

    artifacts = ArtifactBundle(
        model=model,
        vectorizer=vectorizer,
        metadata=metadata,
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
    )

    # ------------------------------------------------------
    # Act
    # ------------------------------------------------------

    result = pipeline.predict(
        title="API REST",
        content="Spring Boot integration",
        artifacts=artifacts,
    )

    # ------------------------------------------------------
    # Assert
    # ------------------------------------------------------

    assert result.category == "Backend"

    assert result.confidence == 0.98

    preprocessing.process.assert_called_once()

    vectorizer.transform.assert_called_once()

    model.predict.assert_called_once()

    model.predict_proba.assert_called_once()