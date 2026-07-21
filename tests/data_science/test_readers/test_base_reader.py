"""
==========================================================
TechMind
Componente Data Science

Módulo:
    test_base_reader.py

Descripción:
    Pruebas unitarias para BaseReader.

Sprint:
    DS-03 - Construcción del Dataset
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import pytest

from data_science.readers.base_reader import BaseReader


# ==========================================================
# Tests
# ==========================================================

def test_base_reader_cannot_be_instantiated() -> None:
    """
    Verifica que BaseReader no pueda instanciarse
    directamente al ser una clase abstracta.
    """

    with pytest.raises(TypeError):
        BaseReader()