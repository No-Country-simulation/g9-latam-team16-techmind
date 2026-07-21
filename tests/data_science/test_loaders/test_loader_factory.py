"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_loader_factory.py

Descripción:
    Pruebas unitarias para LoaderFactory.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

import pytest

from data_science.loaders.github_loader import GitHubLoader
from data_science.loaders.huggingface_loader import (
    HuggingFaceLoader,
)
from data_science.loaders.loader_factory import LoaderFactory
from data_science.loaders.mock_loader import MockLoader
from data_science.loaders.stackexchange_loader import (
    StackExchangeLoader,
)
from data_science.loaders.technical_docs_loader import (
    TechnicalDocsLoader,
)


def test_create_github_loader() -> None:
    loader = LoaderFactory.create("github")

    assert isinstance(loader, GitHubLoader)


def test_create_stackexchange_loader() -> None:
    loader = LoaderFactory.create("stack_exchange")

    assert isinstance(loader, StackExchangeLoader)


def test_create_technical_docs_loader() -> None:
    loader = LoaderFactory.create("technical_docs")

    assert isinstance(loader, TechnicalDocsLoader)


def test_create_huggingface_loader() -> None:
    loader = LoaderFactory.create("huggingface")

    assert isinstance(loader, HuggingFaceLoader)


def test_create_mock_loader() -> None:
    loader = LoaderFactory.create("mock")

    assert isinstance(loader, MockLoader)


def test_create_invalid_loader() -> None:
    with pytest.raises(ValueError):
        LoaderFactory.create("invalid_loader")
