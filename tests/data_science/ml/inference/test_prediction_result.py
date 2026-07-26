"""
==========================================================
TechMind
Data Science Component

Module:
    test_prediction_result.py

Description:
    Unit tests for the PredictionResult model.

Sprint:
    DS-08 - Inference Engine
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from data_science.ml.inference.prediction_result import (
    PredictionResult,
)

# ==========================================================
# Unit Tests
# ==========================================================


def test_prediction_result_stores_prediction_values():
    """
    Verifies that PredictionResult correctly stores
    the predicted category and confidence score.
    """

    result = PredictionResult(
        category="Backend",
        confidence=0.98,
    )

    assert result.category == "Backend"

    assert result.confidence == 0.98