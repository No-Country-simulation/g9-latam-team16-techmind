"""
==========================================================
TechMind
Data Science Component

Module:
    test_artifact_loader.py

Description:
    Unit tests for the ArtifactLoader service.

Sprint:
    DS-08 - Inference Engine
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from unittest.mock import Mock

from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)

from src.data_science.ml.persistence.services.artifact_loader import (
    ArtifactLoader,
)

# ==========================================================
# Unit Tests
# ==========================================================


def test_artifact_loader_returns_artifact_bundle():
    """
    Verifies that ArtifactLoader retrieves the expected
    ArtifactBundle from the repository.
    """

    # ------------------------------------------------------
    # Arrange
    # ------------------------------------------------------

    repository = Mock()

    expected_bundle = Mock(spec=ArtifactBundle)

    repository.load.return_value = expected_bundle

    loader = ArtifactLoader(
        repository=repository,
    )

    # ------------------------------------------------------
    # Act
    # ------------------------------------------------------

    result = loader.load(
        "modelo_prueba",
    )

    # ------------------------------------------------------
    # Assert
    # ------------------------------------------------------

    assert result is expected_bundle

    repository.load.assert_called_once_with(
        "modelo_prueba",
    )