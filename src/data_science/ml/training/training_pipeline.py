"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    Machine Learning

Archivo:
    training_pipeline.py

Descripción:
    Orquesta el proceso completo de entrenamiento de un
    modelo de Machine Learning.

Autor:
    Equipo Data Science

Sprint:
    DS-06 - Model Training
==========================================================
"""

from __future__ import annotations

from time import perf_counter

import pandas as pd

from data_science.ml.evaluation.evaluators.model_evaluator import (
    ModelEvaluator,
)
from data_science.ml.features.feature_pipeline import (
    FeaturePipeline,
)
from data_science.ml.training.training_result import (
    TrainingResult,
)
from data_science.ml.training.trainers.base_model_trainer import (
    BaseModelTrainer,
)


class TrainingPipeline:
    """
    Orquesta el proceso completo de entrenamiento
    de un modelo de Machine Learning.
    """

    def __init__(
        self,
        feature_pipeline: FeaturePipeline,
        trainer: BaseModelTrainer,
        evaluator: ModelEvaluator,
    ) -> None:
        """
        Inicializa el pipeline de entrenamiento.

        Parameters
        ----------
        feature_pipeline : FeaturePipeline
            Pipeline de Ingeniería de Características.

        trainer : BaseModelTrainer
            Entrenador del modelo.

        evaluator : ModelEvaluator
            Evaluador del modelo entrenado.
        """

        self._feature_pipeline = feature_pipeline
        self._trainer = trainer
        self._evaluator = evaluator

    def train(
        self,
        dataset: pd.DataFrame,
    ) -> TrainingResult:
        """
        Ejecuta el proceso completo de entrenamiento.

        Parameters
        ----------
        dataset : pd.DataFrame
            Dataset Maestro.

        Returns
        -------
        TrainingResult
            Resultado del entrenamiento.
        """

        (
            x_train,
            x_test,
            y_train,
            y_test,
        ) = self._feature_pipeline.build(dataset)

        start_time = perf_counter()

        self._trainer.train(
            x_train,
            y_train,
        )

        training_time = perf_counter() - start_time

        model = self._trainer.get_model()

        metrics = self._evaluator.evaluate(
            model,
            x_test,
            y_test,
        )

        return TrainingResult(
            model=model,
            accuracy=metrics["accuracy"],
            precision=metrics["precision"],
            recall=metrics["recall"],
            f1_score=metrics["f1_score"],
            training_time=training_time,
        )