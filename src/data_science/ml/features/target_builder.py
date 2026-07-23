"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    TargetBuilder

Descripción:
    Construye el vector objetivo (y) a partir del
    Dataset Maestro.

Autor:
    Equipo Data Science

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

from __future__ import annotations

import pandas as pd


class TargetBuilder:
    """
    Responsable de construir la variable objetivo
    utilizada durante el entrenamiento.
    """

    TARGET_COLUMN = "category"

    def build(self, dataset: pd.DataFrame) -> pd.Series:
        """
        Construye el vector objetivo.

        Parameters
        ----------
        dataset : pd.DataFrame
            Dataset Maestro.

        Returns
        -------
        pd.Series
            Variable objetivo.
        """

        if self.TARGET_COLUMN not in dataset.columns:
            raise ValueError(
                f"La columna '{self.TARGET_COLUMN}' no existe en el dataset."
            )

        return dataset[self.TARGET_COLUMN].copy()