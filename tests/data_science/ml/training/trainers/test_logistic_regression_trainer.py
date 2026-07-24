"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    test_logistic_regression_trainer.py

Descripción:
    Pruebas unitarias para LogisticRegressionTrainer.
==========================================================
"""

import pytest
from sklearn.linear_model import LogisticRegression

from data_science.ml.exceptions.training_exception import (
    TrainingException,
)
from data_science.ml.training.trainers.logistic_regression_trainer import (
    LogisticRegressionTrainer,
)

def test_should_initialize_trainer():
    """
    Verifica que el entrenador se inicialice correctamente.
    """
    trainer = LogisticRegressionTrainer()

    assert trainer.is_trained() is False


def test_should_train_model_successfully(
    sample_training_data,
):
    """
    Verifica que el entrenamiento se complete
    correctamente.
    """
    trainer = LogisticRegressionTrainer()

    trainer.train(
        sample_training_data["features"],
        sample_training_data["target"],
    )

    assert trainer.is_trained() is True


def test_should_return_trained_model(
    sample_training_data,
):
    """
    Verifica que se devuelva un modelo entrenado.
    """
    trainer = LogisticRegressionTrainer()

    trainer.train(
        sample_training_data["features"],
        sample_training_data["target"],
    )

    model = trainer.get_model()

    assert isinstance(
        model,
        LogisticRegression,
    )


def test_should_raise_training_exception_when_training_fails():
    """
    Verifica que los errores durante el entrenamiento
    sean encapsulados en TrainingException.
    """
    trainer = LogisticRegressionTrainer()

    with pytest.raises(TrainingException):
        trainer.train(
            None,
            None,
        )