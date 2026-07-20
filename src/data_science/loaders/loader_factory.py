"""
==========================================================
TechMind
Componente Data Science

Módulo:
    loader_factory.py

Descripción:
    Fábrica para la creación de loaders.

Sprint:
    DS-03
==========================================================
"""

from .base_loader import BaseLoader
from .github_loader import GitHubLoader
from .huggingface_loader import HuggingFaceLoader
from .mock_loader import MockLoader
from .stackexchange_loader import StackExchangeLoader
from .technical_docs_loader import TechnicalDocsLoader


class LoaderFactory:

    _LOADERS = {

        "github": GitHubLoader,

        "stack_exchange": StackExchangeLoader,

        "technical_docs": TechnicalDocsLoader,

        "huggingface": HuggingFaceLoader,

        "mock": MockLoader,
    }

    @classmethod
    def create(
        cls,
        loader_name: str,
        **kwargs,
    ) -> BaseLoader:

        try:

            loader = cls._LOADERS[loader_name]

        except KeyError as exc:

            raise ValueError(
                f"Loader no soportado: {loader_name}"
            ) from exc

        return loader(**kwargs)