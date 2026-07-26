"""
----------------------------------------------------------
Proyecto : TechMind
Sprint   : DS-08 - Motor de Inferencia
Módulo   : Data Science
Archivo  : inference_engine.py
----------------------------------------------------------
"""

from data_science.ml.inference.predict_pipeline import (
    PredictPipeline,
)

from data_science.ml.inference.prediction_result import (
    PredictionResult,
)

from data_science.ml.persistence.services.artifact_loader import (
    ArtifactLoader,
)


class InferenceEngine:
    """
    Orquesta el proceso completo de inferencia.
    """

    def __init__(
        self,
        loader: ArtifactLoader,
    ) -> None:

        self._loader = loader

        self._pipeline = PredictPipeline()

    def predict(
        self,
        identifier: str,
        title: str,
        content: str,
    ) -> PredictionResult:
        """
        Ejecuta una predicción utilizando el modelo indicado.
        """

        artifacts = self._loader.load(
            identifier,
        )

        return self._pipeline.predict(
            title=title,
            content=content,
            artifacts=artifacts,
        )