"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    test_model_evaluator.py

Descripción:
    Pruebas unitarias para ModelEvaluator.
==========================================================
"""

import numpy as np
import pytest
from sklearn.linear_model import LogisticRegression

from data_science.ml.evaluation.evaluators.model_evaluator import (
    ModelEvaluator,
)
from data_science.ml.exceptions.training_exception import (
    TrainingException,
)


@pytest.fixture
def sample_training_data():
    """
    Proporciona un pequeño conjunto de datos para
    entrenamiento y evaluación.
    """
    return {
        "features": np.array(
            [
                [0, 0],
                [0, 1],
                [1, 0],
                [1, 1],
            ]
        ),
        "target": np.array(
            [
                0,
                0,
                1,
                1,
            ]
        ),
    }


def test_should_return_all_metrics(
    sample_training_data,
):
    """
    Verifica que el evaluador devuelva todas las métricas.
    """
    model = LogisticRegression(random_state=42)

    model.fit(
        sample_training_data["features"],
        sample_training_data["target"],
    )

    evaluator = ModelEvaluator()

    metrics = evaluator.evaluate(
        model,
        sample_training_data["features"],
        sample_training_data["target"],
    )

    expected_metrics = {
        "accuracy",
        "precision",
        "recall",
        "f1_score",
    }

    assert isinstance(metrics, dict)
    assert set(metrics.keys()) == expected_metrics


def test_should_return_metrics_between_zero_and_one(
    sample_training_data,
):
    """
    Verifica que todas las métricas estén entre 0 y 1.
    """
    model = LogisticRegression(random_state=42)

    model.fit(
        sample_training_data["features"],
        sample_training_data["target"],
    )

    evaluator = ModelEvaluator()

    metrics = evaluator.evaluate(
        model,
        sample_training_data["features"],
        sample_training_data["target"],
    )

    for value in metrics.values():
        assert 0.0 <= value <= 1.0


def test_should_evaluate_trained_model(
    sample_training_data,
):
    """
    Verifica que un modelo entrenado pueda evaluarse.
    """
    model = LogisticRegression(random_state=42)

    model.fit(
        sample_training_data["features"],
        sample_training_data["target"],
    )

    evaluator = ModelEvaluator()

    metrics = evaluator.evaluate(
        model,
        sample_training_data["features"],
        sample_training_data["target"],
    )

    assert metrics["accuracy"] > 0.0


def test_should_raise_training_exception_when_model_is_invalid(
    sample_training_data,
):
    """
    Verifica que los errores sean encapsulados
    en TrainingException.
    """
    evaluator = ModelEvaluator()

    with pytest.raises(TrainingException):
        evaluator.evaluate(
            None,
            sample_training_data["features"],
            sample_training_data["target"],
        )