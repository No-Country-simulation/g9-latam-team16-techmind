"""
artifact_loader.py

Servicio encargado de cargar los artefactos del modelo
utilizando el repositorio de persistencia.
"""

from src.data_science.ml.persistence.contracts.artifact_repository import (
    ArtifactRepository,
)
from src.data_science.ml.persistence.domain.artifact_bundle import (
    ArtifactBundle,
)


class ArtifactLoader:
    """
    Servicio responsable de recuperar un conjunto de artefactos
    persistidos para el proceso de inferencia.
    """

    def __init__(
        self,
        repository: ArtifactRepository,
    ) -> None:
        self._repository = repository

    def load(
        self,
        identifier: str,
    ) -> ArtifactBundle:
        """
        Recupera los artefactos asociados al identificador indicado.
        """

        return self._repository.load(
            identifier,
        )