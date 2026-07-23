"""
==========================================================
AyniKortex
Data Science Component

Módulo:
    FeatureBuilder

Descripción:
    Construye la matriz de características (X) a partir
    del Dataset Maestro utilizando un BaseVectorizer.

Autor:
    Equipo Data Science

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

from __future__ import annotations

from typing import Sequence

import pandas as pd
from scipy.sparse import csr_matrix

from data_science.ml.features.base_vectorizer import BaseVectorizer


class FeatureBuilder:
    """
    Responsable de construir la matriz de características (X)
    utilizada durante el entrenamiento del modelo.
    """

    DEFAULT_TEXT_COLUMNS = (
        "title",
        "description",
        "content",
    )

    def __init__(
        self,
        vectorizer: BaseVectorizer,
        text_columns: Sequence[str] | None = None,
    ) -> None:
        """
        Inicializa el constructor de características.

        Parameters
        ----------
        vectorizer : BaseVectorizer
            Estrategia de vectorización.

        text_columns : Sequence[str] | None
            Columnas que serán utilizadas para construir
            el documento de entrenamiento.
        """

        self._vectorizer = vectorizer
        self._text_columns = tuple(
            text_columns or self.DEFAULT_TEXT_COLUMNS
        )

    def build(
        self,
        dataset: pd.DataFrame,
    ) -> csr_matrix:
        """
        Construye la matriz de características.

        Parameters
        ----------
        dataset : pd.DataFrame
            Dataset Maestro.

        Returns
        -------
        csr_matrix
            Matriz de características.
        """

        missing_columns = [
            column
            for column in self._text_columns
            if column not in dataset.columns
        ]

        if missing_columns:
            raise ValueError(
                "Faltan columnas requeridas: "
                + ", ".join(missing_columns)
            )

        documents = (
            dataset[list(self._text_columns)]
            .fillna("")
            .astype(str)
            .agg("\n".join, axis=1)
        )

        X = self._vectorizer.fit_transform(documents)

        return X