"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    logistic_regression_trainer.py

Descripción:
    Implementa el entrenador basado en Regresión Logística
    utilizando scikit-learn.
==========================================================
"""

from typing import Any

from sklearn.linear_model import LogisticRegression

from data_science.ml.exceptions.training_exception import (
    TrainingException,
)
from data_science.ml.training.trainers.base_model_trainer import (
    BaseModelTrainer,
)


class LogisticRegressionTrainer(BaseModelTrainer):
    """
    Entrenador basado en Regresión Logística.
    """

    def __init__(
        self,
        random_state: int = 42,
        max_iter: int = 1000,
    ) -> None:
        """
        Inicializa el entrenador con una instancia de
        LogisticRegression.
        """
        super().__init__()

        self._model = LogisticRegression(
            random_state=random_state,
            max_iter=max_iter,
        )

    def train(
        self,
        features: Any,
        target: Any,
    ) -> None:
        """
        Entrena el modelo utilizando las características y
        etiquetas proporcionadas.
        """
        try:
            self._model.fit(features, target)
            self._trained = True

        except Exception as error:
            raise TrainingException(
                "Ocurrió un error durante el entrenamiento "
                "del modelo."
            ) from error

        