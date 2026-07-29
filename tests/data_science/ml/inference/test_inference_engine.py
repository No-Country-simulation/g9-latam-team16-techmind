"""
==========================================================
TechMind
Data Science Component

Module:
    test_inference_engine.py

Description:
    Unit tests for the InferenceEngine component.

Sprint:
    DS-08 - Inference Engine
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from unittest.mock import Mock

from src.data_science.ml.inference.inference_engine import (
    InferenceEngine,
)

from src.data_science.ml.inference.prediction_result import (
    PredictionResult,
)

from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)

# ==========================================================
# Unit Tests
# ==========================================================


def test_inference_engine_executes_prediction():
    """
    Verifies that the inference engine coordinates the
    artifact loading process and delegates the prediction
    to the PredictPipeline.
    """

    # ------------------------------------------------------
    # Arrange
    # ------------------------------------------------------

    loader = Mock()

    bundle = Mock(spec=ArtifactBundle)

    loader.load.return_value = bundle

    engine = InferenceEngine(
        loader=loader,
    )

    pipeline = Mock()

    expected_result = PredictionResult(
        category="Backend",
        confidence=0.98,
    )

    pipeline.predict.return_value = expected_result

    # Reemplazamos el pipeline real por uno simulado
    engine._pipeline = pipeline

    # ------------------------------------------------------
    # Act
    # ------------------------------------------------------

    result = engine.predict(
        identifier="modelo_prueba",
        title="API REST",
        content="Spring Boot",
    )

    # ------------------------------------------------------
    # Assert
    # ------------------------------------------------------

    assert result == expected_result

    loader.load.assert_called_once_with(
        "modelo_prueba",
    )

    pipeline.predict.assert_called_once_with(
        title="API REST",
        content="Spring Boot",
        artifacts=bundle,
    )