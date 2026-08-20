"""
----------------------------------------------------------
Proyecto : TechMind
Sprint   : DS-08 - Motor de Inferencia
MÃ³dulo   : Data Science
Archivo  : predict_pipeline.py
----------------------------------------------------------
"""

from src.data_science.data.domain import DocumentRecord

from src.data_science.ml.inference.prediction_result import PredictionResult

from src.data_science.ml.persistence.domain.artifact_bundle import ArtifactBundle

from src.data_science.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)


class PredictPipeline:
    """
    Ejecuta el pipeline completo de inferencia utilizando
    los artefactos previamente cargados.
    """

    def __init__(self) -> None:

        self._preprocessing = PreprocessingPipeline()

    def predict(
        self,
        title: str,
        content: str,
        artifacts: ArtifactBundle,
    ) -> PredictionResult:
        """
        Ejecuta el proceso completo de inferencia.
        """

        document = DocumentRecord(
            document_id="inference",
            source="api",
            title=title,
            text=f"{title}\n{content}",
            category="",
            language="es",
        )

        processed = self._preprocessing.process(
            document,
        )

        vector = artifacts.vectorizer.transform(
            [
                processed.processed_text,
            ]
        )

        prediction = artifacts.model.predict(
            vector,
        )[0]

        confidence = max(
            artifacts.model.predict_proba(
                vector,
            )[0]
        )

        if artifacts.label_encoder is not None:

            prediction = artifacts.label_encoder.inverse_transform(
                [
                    prediction,
                ]
            )[0]

        return PredictionResult(
            category=prediction,
            confidence=float(confidence),
        )

