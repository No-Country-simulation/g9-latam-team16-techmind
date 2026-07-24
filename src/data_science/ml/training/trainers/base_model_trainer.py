"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    base_model_trainer.py

Descripción:
    Define el contrato base para todos los entrenadores
    de modelos de Machine Learning.

    Esta clase establece la interfaz común que deberán
    implementar todos los algoritmos de entrenamiento y
    administra el estado del proceso de entrenamiento.
==========================================================
"""

from abc import ABC, abstractmethod
from typing import Any

from data_science.ml.exceptions.training_exception import (
    TrainingException,
)


class BaseModelTrainer(ABC):
    """
    Define el contrato base para todos los entrenadores
    de modelos de Machine Learning.

    Las clases derivadas deberán implementar el proceso
    de entrenamiento del algoritmo correspondiente.

    La clase también administra el estado del entrenamiento
    y proporciona acceso controlado al modelo entrenado.
    """

    def __init__(self) -> None:
        """
        Inicializa el estado del entrenador.

        El entrenador comienza sin un modelo entrenado.
        """
        self._model: Any | None = None
        self._trained: bool = False

    @abstractmethod
    def train(
        self,
        features: Any,
        target: Any,
    ) -> None:
        """
        Entrena el modelo utilizando las características
        y etiquetas proporcionadas.

        Args:
            features:
                Conjunto de características utilizado
                para el entrenamiento.

            target:
                Etiquetas asociadas al conjunto de
                entrenamiento.
        """
        raise NotImplementedError

    def get_model(self) -> Any:
        """
        Retorna el modelo entrenado.

        Returns:
            Modelo entrenado.

        Raises:
            TrainingException:
                Si el modelo aún no ha sido entrenado.
        """
        if not self._trained or self._model is None:
            raise TrainingException(
                "El modelo aún no ha sido entrenado."
            )

        return self._model

    def is_trained(self) -> bool:
        """
        Indica si el entrenador ya cuenta con un modelo
        entrenado.

        Returns:
            True si el modelo fue entrenado;
            False en caso contrario.
        """
        return self._trained