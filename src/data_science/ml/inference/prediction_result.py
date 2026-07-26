"""
prediction_result.py

Define la estructura del resultado generado por el Motor de Inferencia.
"""

from dataclasses import dataclass


@dataclass
class PredictionResult:
    """
    Representa el resultado de una predicción realizada por el modelo.
    """

    category: str
    confidence: float