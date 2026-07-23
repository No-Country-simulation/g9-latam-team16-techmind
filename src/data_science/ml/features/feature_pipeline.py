"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    FeaturePipeline

Descripción:
    Orquesta el proceso de Ingeniería de Características.

Autor:
    Equipo Data Science

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from data_science.ml.features.dataset_splitter import DatasetSplitter
from data_science.ml.features.feature_builder import FeatureBuilder
from data_science.ml.features.target_builder import TargetBuilder


class FeaturePipeline:
    """
    Orquesta el proceso completo de construcción
    de características.
    """

    def __init__(
        self,
        feature_builder: FeatureBuilder,
        target_builder: TargetBuilder,
        dataset_splitter: DatasetSplitter,
    ) -> None:
        """
        Inicializa el pipeline de Ingeniería de Características.

        Parameters
        ----------
        feature_builder : FeatureBuilder
            Responsable de construir la matriz de características (X).

        target_builder : TargetBuilder
            Responsable de construir la variable objetivo (y).

        dataset_splitter : DatasetSplitter
            Responsable de dividir el dataset en entrenamiento
            y prueba.
        """

        self._feature_builder = feature_builder
        self._target_builder = target_builder
        self._dataset_splitter = dataset_splitter

    def build(
        self,
        dataset: pd.DataFrame,
    ) -> tuple[Any, Any, Any, Any]:
        """
        Ejecuta el pipeline completo de Feature Engineering.

        Parameters
        ----------
        dataset : pd.DataFrame
            Dataset Maestro.

        Returns
        -------
        tuple[Any, Any, Any, Any]
            Tupla con:
            (X_train, X_test, y_train, y_test).
        """

        X = self._feature_builder.build(dataset)

        y = self._target_builder.build(dataset)

        return self._dataset_splitter.split(X, y)