"""
==========================================================
AyniKortex
Data Science Component

Pruebas unitarias para TrainingPipeline.
==========================================================
"""

from __future__ import annotations

from unittest.mock import Mock

import pandas as pd

from data_science.ml.training.training_pipeline import (
    TrainingPipeline,
)
from data_science.ml.training.training_result import (
    TrainingResult,
)


class DummyFeaturePipeline:
    """
    Simula el FeaturePipeline.
    """

    def build(self, dataset):
        return (
            "x_train",
            "x_test",
            "y_train",
            "y_test",
        )


class DummyTrainer:
    """
    Simula un entrenador.
    """

    def __init__(self):
        self.train_called = False

    def train(
        self,
        features,
        target,
    ):
        self.train_called = True

    def get_model(self):
        return "dummy_model"


class DummyEvaluator:
    """
    Simula un evaluador.
    """

    def evaluate(
        self,
        model,
        features,
        target,
    ):
        return {
            "accuracy": 0.95,
            "precision": 0.94,
            "recall": 0.93,
            "f1_score": 0.92,
        }


def test_train_returns_training_result():
    """
    Debe devolver un TrainingResult.
    """

    pipeline = TrainingPipeline(
        feature_pipeline=DummyFeaturePipeline(),
        trainer=DummyTrainer(),
        evaluator=DummyEvaluator(),
    )

    dataset = Mock(spec=pd.DataFrame)

    result = pipeline.train(dataset)

    assert isinstance(result, TrainingResult)


def test_train_calls_trainer():
    """
    Debe ejecutar el entrenamiento.
    """

    trainer = DummyTrainer()

    pipeline = TrainingPipeline(
        feature_pipeline=DummyFeaturePipeline(),
        trainer=trainer,
        evaluator=DummyEvaluator(),
    )

    dataset = Mock(spec=pd.DataFrame)

    pipeline.train(dataset)

    assert trainer.train_called is True


def test_train_returns_expected_metrics():
    """
    Debe propagar correctamente las métricas.
    """

    pipeline = TrainingPipeline(
        feature_pipeline=DummyFeaturePipeline(),
        trainer=DummyTrainer(),
        evaluator=DummyEvaluator(),
    )

    dataset = Mock(spec=pd.DataFrame)

    result = pipeline.train(dataset)

    assert result.accuracy == 0.95
    assert result.precision == 0.94
    assert result.recall == 0.93
    assert result.f1_score == 0.92


def test_train_returns_model():
    """
    Debe devolver el modelo entrenado.
    """

    pipeline = TrainingPipeline(
        feature_pipeline=DummyFeaturePipeline(),
        trainer=DummyTrainer(),
        evaluator=DummyEvaluator(),
    )

    dataset = Mock(spec=pd.DataFrame)

    result = pipeline.train(dataset)

    assert result.model == "dummy_model"


def test_training_time_is_non_negative():
    """
    El tiempo de entrenamiento debe ser mayor o igual a cero.
    """

    pipeline = TrainingPipeline(
        feature_pipeline=DummyFeaturePipeline(),
        trainer=DummyTrainer(),
        evaluator=DummyEvaluator(),
    )

    dataset = Mock(spec=pd.DataFrame)

    result = pipeline.train(dataset)

    assert result.training_time >= 0