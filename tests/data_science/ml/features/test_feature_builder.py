"""
==========================================================
AyniKortex
Data Science Component

Tests:
    FeatureBuilder

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

import pandas as pd
import pytest
from scipy.sparse import csr_matrix

from data_science.ml.features.feature_builder import FeatureBuilder
from data_science.ml.features.tfidf_vectorizer import (
    TfidfVectorizerAdapter,
)


def test_build_returns_feature_matrix():
    """
    Debe construir correctamente la matriz de características.
    """

    # Arrange
    dataset = pd.DataFrame(
        {
            "title": [
                "Python",
                "Java",
            ],
            "description": [
                "Lenguaje interpretado",
                "Lenguaje orientado a objetos",
            ],
            "content": [
                "Python es ampliamente utilizado.",
                "Java se utiliza en aplicaciones empresariales.",
            ],
        }
    )

    builder = FeatureBuilder(
        vectorizer=TfidfVectorizerAdapter(),
    )

    # Act
    X = builder.build(dataset)

    # Assert
    assert isinstance(X, csr_matrix)
    assert X.shape[0] == len(dataset)
    assert X.shape[1] > 0
    assert X.nnz > 0


def test_build_raises_error_when_required_columns_are_missing():
    """
    Debe lanzar una excepción cuando falta alguna
    columna requerida.
    """

    # Arrange
    dataset = pd.DataFrame(
        {
            "title": ["Python"],
            "content": ["Contenido"],
        }
    )

    builder = FeatureBuilder(
        vectorizer=TfidfVectorizerAdapter(),
    )

    # Act / Assert
    with pytest.raises(ValueError):
        builder.build(dataset)


def test_build_handles_null_values():
    """
    Debe soportar valores nulos sin lanzar excepciones.
    """

    # Arrange
    dataset = pd.DataFrame(
        {
            "title": [
                "Python",
            ],
            "description": [
                None,
            ],
            "content": [
                "Lenguaje de programación",
            ],
        }
    )

    builder = FeatureBuilder(
        vectorizer=TfidfVectorizerAdapter(),
    )

    # Act
    X = builder.build(dataset)

    # Assert
    assert isinstance(X, csr_matrix)
    assert X.shape[0] == 1
    assert X.shape[1] > 0