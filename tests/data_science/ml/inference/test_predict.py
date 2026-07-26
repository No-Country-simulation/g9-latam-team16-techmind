"""
==========================================================
TechMind
Data Science Component

Module:
    test_predict.py

Description:
    Unit tests for the public predict() function.

Sprint:
    DS-08 - Inference Engine
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from unittest.mock import Mock
from unittest.mock import patch

from src.data_science.ml.inference.predict import predict

from src.data_science.ml.inference.prediction_result import (
    PredictionResult,
)

# ==========================================================
# Unit Tests
# ==========================================================


@patch("src.data_science.ml.inference.predict.InferenceEngine")
@patch("src.data_science.ml.inference.predict.ArtifactLoader")
def test_predict_delegates_to_inference_engine(
    mock_loader_class,
    mock_engine_class,
):
    """
    Verifies that the public predict() function creates
    the required services and delegates the prediction
    process to the InferenceEngine.
    """

    # ------------------------------------------------------
    # Arrange
    # ------------------------------------------------------

    repository = Mock()

    expected_result = PredictionResult(
        category="Backend",
        confidence=0.98,
    )

    loader_instance = Mock()

    engine_instance = Mock()

    mock_loader_class.return_value = loader_instance

    mock_engine_class.return_value = engine_instance

    engine_instance.predict.return_value = expected_result

    # ------------------------------------------------------
    # Act
    # ------------------------------------------------------

    result = predict(
        identifier="modelo_prueba",
        title="API REST",
        content="Spring Boot",
        repository=repository,
    )

    # ------------------------------------------------------
    # Assert
    # ------------------------------------------------------

    assert result == expected_result

    mock_loader_class.assert_called_once_with(
        repository=repository,
    )

    mock_engine_class.assert_called_once_with(
        loader=loader_instance,
    )

    engine_instance.predict.assert_called_once_with(
        identifier="modelo_prueba",
        title="API REST",
        content="Spring Boot",
    )