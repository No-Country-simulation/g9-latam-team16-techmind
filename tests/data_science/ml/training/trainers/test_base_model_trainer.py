"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    test_base_model_trainer.py

Descripción:
    Pruebas unitarias para la clase BaseModelTrainer.
==========================================================
"""

import pytest

from data_science.ml.exceptions.training_exception import (
    TrainingException,
)
from data_science.ml.training.trainers.base_model_trainer import (
    BaseModelTrainer,
)


class DummyTrainer(BaseModelTrainer):
    """
    Implementación mínima utilizada únicamente para
    validar el comportamiento de BaseModelTrainer.
    """

    def train(self, features, target) -> None:
        """
        Simula el entrenamiento de un modelo.
        """
        self._model = "dummy-model"
        self._trained = True


class IncompleteTrainer(BaseModelTrainer):
    """
    Implementación incompleta utilizada para validar
    que las clases abstractas no pueden instanciarse.
    """

    pass


def test_should_not_instantiate_base_model_trainer():
    """
    Verifica que no sea posible instanciar
    la clase abstracta BaseModelTrainer.
    """
    with pytest.raises(TypeError):
        BaseModelTrainer()


def test_should_not_instantiate_incomplete_trainer():
    """
    Verifica que una implementación incompleta
    tampoco pueda instanciarse.
    """
    with pytest.raises(TypeError):
        IncompleteTrainer()


def test_should_initialize_as_not_trained():
    """
    Verifica que el entrenador inicie
    en estado no entrenado.
    """
    trainer = DummyTrainer()

    assert trainer.is_trained() is False


def test_should_raise_exception_when_model_is_not_trained():
    """
    Verifica que se lance una excepción cuando
    se intenta obtener un modelo sin entrenarlo.
    """
    trainer = DummyTrainer()

    with pytest.raises(TrainingException):
        trainer.get_model()


def test_should_change_training_status_after_train():
    """
    Verifica que el estado del entrenador cambie
    correctamente después del entrenamiento.
    """
    trainer = DummyTrainer()

    trainer.train(None, None)

    assert trainer.is_trained() is True


def test_should_return_trained_model():
    """
    Verifica que se retorne el modelo entrenado.
    """
    trainer = DummyTrainer()

    trainer.train(None, None)

    assert trainer.get_model() == "dummy-model"