"""
==========================================================
TechMind

Módulo:
    Machine Learning

Archivo:
    training_result.py

Descripción:
    Define el objeto de dominio que representa el resultado
    de un proceso de entrenamiento de un modelo de Machine
    Learning.
==========================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass(
    frozen=True,
    slots=True,
)
class TrainingResult:
    """
    Representa el resultado de un proceso de entrenamiento.

    Esta clase encapsula la información generada durante el
    entrenamiento de un modelo, incluyendo las métricas de
    evaluación y el modelo entrenado.

    Al ser un Value Object, su estado es inmutable una vez
    creado.
    """

    model: Any

    accuracy: float

    precision: float

    recall: float

    f1_score: float

    training_time: float