"""
==========================================================
AyniKortex
Data Science Component

Tests:
    FeaturePipeline

Sprint:
    DS-05 - Feature Engineering
==========================================================
"""

import pandas as pd

from data_science.ml.features.dataset_splitter import DatasetSplitter
from data_science.ml.features.feature_builder import FeatureBuilder
from data_science.ml.features.feature_pipeline import FeaturePipeline
from data_science.ml.features.target_builder import TargetBuilder
from data_science.ml.features.tfidf_vectorizer import (
    TfidfVectorizerAdapter,
)


def test_build_executes_complete_pipeline():
    """
    Debe ejecutar correctamente todo el pipeline
    de Ingeniería de Características.
    """

    # Arrange
    dataset = pd.DataFrame(
        {
            "title": [
                "Python",
                "Java",
                "Docker",
                "Kubernetes",
            ],
            "description": [
                "Lenguaje",
                "Lenguaje",
                "Contenedores",
                "Orquestación",
            ],
            "content": [
                "Python es popular.",
                "Java es robusto.",
                "Docker facilita despliegues.",
                "Kubernetes administra contenedores.",
            ],
            "category": [
                "Backend",
                "Backend",
                "DevOps",
                "DevOps",
            ],
        }
    )

    pipeline = FeaturePipeline(
        feature_builder=FeatureBuilder(
            TfidfVectorizerAdapter()
        ),
        target_builder=TargetBuilder(),
        dataset_splitter=DatasetSplitter(),
    )

    # Act
    X_train, X_test, y_train, y_test = pipeline.build(dataset)

    # Assert
    assert X_train.shape[0] == 3
    assert X_test.shape[0] == 1

    assert len(y_train) == 3
    assert len(y_test) == 1