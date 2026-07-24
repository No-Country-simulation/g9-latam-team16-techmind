"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    test_training_result.py

Descripción:
    Pruebas unitarias para la clase TrainingResult.
==========================================================
"""

from dataclasses import FrozenInstanceError

import pytest

from data_science.ml.training.training_result import TrainingResult


def test_should_create_training_result():
    """
    Verifica que un objeto TrainingResult se cree correctamente.
    """
    result = TrainingResult(
        model="dummy-model",
        accuracy=0.95,
        precision=0.94,
        recall=0.93,
        f1_score=0.92,
        training_time=1.25,
    )

    assert result.model == "dummy-model"
    assert result.accuracy == 0.95
    assert result.precision == 0.94
    assert result.recall == 0.93
    assert result.f1_score == 0.92
    assert result.training_time == 1.25


def test_should_be_immutable():
    """
    Verifica que el objeto sea inmutable.
    """
    result = TrainingResult(
        model="dummy-model",
        accuracy=0.95,
        precision=0.94,
        recall=0.93,
        f1_score=0.92,
        training_time=1.25,
    )

    with pytest.raises(FrozenInstanceError):
        result.accuracy = 1.0


def test_should_keep_model_reference():
    """
    Verifica que conserve la referencia al modelo.
    """
    model = object()

    result = TrainingResult(
        model=model,
        accuracy=0.90,
        precision=0.89,
        recall=0.88,
        f1_score=0.87,
        training_time=2.50,
    )

    assert result.model is model