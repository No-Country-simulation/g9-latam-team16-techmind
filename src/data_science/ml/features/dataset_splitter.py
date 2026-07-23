"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    DatasetSplitter

Descripción:
    Divide la matriz de características (X) y la variable
    objetivo (y) en conjuntos de entrenamiento y prueba.

Autor:
    Equipo Data Science

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

from __future__ import annotations

from typing import Any

from sklearn.model_selection import train_test_split


class DatasetSplitter:
    """
    Responsable de dividir el dataset para entrenamiento
    y evaluación.
    """

    def __init__(
        self,
        test_size: float = 0.2,
        random_state: int = 42,
        shuffle: bool = True,
    ) -> None:
        """
        Inicializa el divisor del dataset.

        Parameters
        ----------
        test_size : float
            Proporción del conjunto de prueba.

        random_state : int
            Semilla utilizada para garantizar la
            reproducibilidad de la división.

        shuffle : bool
            Indica si los datos deben mezclarse antes
            de realizar la división.
        """

        self._test_size = test_size
        self._random_state = random_state
        self._shuffle = shuffle

    def split(
        self,
        X: Any,
        y: Any,
    ) -> tuple[Any, Any, Any, Any]:
        """
        Divide X e y en conjuntos de entrenamiento y prueba.

        Parameters
        ----------
        X : Any
            Matriz de características.

        y : Any
            Variable objetivo.

        Returns
        -------
        tuple[Any, Any, Any, Any]
            Tupla con:
            (X_train, X_test, y_train, y_test).
        """

        return train_test_split(
            X,
            y,
            test_size=self._test_size,
            random_state=self._random_state,
            shuffle=self._shuffle,
        )