"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    model_evaluator.py

Descripción:
    Implementa la evaluación de modelos de Machine Learning
    mediante métricas de clasificación.
==========================================================
"""

from typing import Any

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)

from data_science.ml.exceptions.training_exception import (
    TrainingException,
)


class ModelEvaluator:
    """
    Servicio encargado de evaluar un modelo entrenado.
    """

    def evaluate(
        self,
        model: Any,
        features: Any,
        target: Any,
    ) -> dict[str, float]:
        """
        Evalúa un modelo entrenado y calcula las principales
        métricas de clasificación.

        Args:
            model:
                Modelo entrenado.

            features:
                Características utilizadas para la evaluación.

            target:
                Etiquetas reales.

        Returns:
            Diccionario con las métricas calculadas.
        """
        try:
            predictions = model.predict(features)

            return {
                "accuracy": accuracy_score(
                    target,
                    predictions,
                ),
                "precision": precision_score(
                    target,
                    predictions,
                    average="weighted",
                    zero_division=0,
                ),
                "recall": recall_score(
                    target,
                    predictions,
                    average="weighted",
                    zero_division=0,
                ),
                "f1_score": f1_score(
                    target,
                    predictions,
                    average="weighted",
                    zero_division=0,
                ),
            }

        except Exception as error:
            raise TrainingException(
                "Ocurrió un error durante la evaluación del modelo."
            ) from error