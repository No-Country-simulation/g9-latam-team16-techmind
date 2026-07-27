"""
----------------------------------------------------------
Proyecto : TechMind
Sprint   : DS-08 - Motor de Inferencia
Módulo   : Data Science
Archivo  : predict.py
----------------------------------------------------------
"""

from data_science.ml.inference.inference_engine import (
    InferenceEngine,
)

from data_science.ml.inference.prediction_result import (
    PredictionResult,
)

from data_science.ml.persistence.contracts.artifact_repository import (
    ArtifactRepository,
)

from data_science.ml.persistence.services.artifact_loader import (
    ArtifactLoader,
)


def predict(
    identifier: str,
    title: str,
    content: str,
    repository: ArtifactRepository,
) -> PredictionResult:
    """
    Punto de entrada público del Motor de Inferencia.
    """

    loader = ArtifactLoader(
        repository=repository,
    )

    engine = InferenceEngine(
        loader=loader,
    )

    return engine.predict(
        identifier=identifier,
        title=title,
        content=content,
    )