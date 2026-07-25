"""
-----------------------------------------------------------------------
Proyecto : AyniKortex
Sprint   : DS-07 - Persistencia del Modelo
Módulo   : Data Science
Archivo  : test_hash_utils.py

Descripción:
Pruebas unitarias para HashUtils.
-----------------------------------------------------------------------
"""

from pathlib import Path

from src.data_science.ml.persistence.utils.hash_utils import HashUtils


def test_calculate_bytes_hash() -> None:
    """Debe calcular correctamente el hash de un bloque de bytes."""

    hash_value = HashUtils.calculate_bytes_hash(b"Hola Mundo")

    assert len(hash_value) == 64


def test_calculate_file_hash(tmp_path: Path) -> None:
    """Debe calcular el hash de un archivo."""

    file_path = tmp_path / "archivo.txt"

    file_path.write_text("Hola Mundo", encoding="utf-8")

    hash_value = HashUtils.calculate_file_hash(file_path)

    assert len(hash_value) == 64


def test_same_content_same_hash(tmp_path: Path) -> None:
    """Dos archivos con el mismo contenido deben tener el mismo hash."""

    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"

    file1.write_text("AyniKortex", encoding="utf-8")
    file2.write_text("AyniKortex", encoding="utf-8")

    assert (
        HashUtils.calculate_file_hash(file1)
        == HashUtils.calculate_file_hash(file2)
    )


def test_different_content_different_hash(tmp_path: Path) -> None:
    """Archivos diferentes deben generar hashes diferentes."""

    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"

    file1.write_text("Uno", encoding="utf-8")
    file2.write_text("Dos", encoding="utf-8")

    assert (
        HashUtils.calculate_file_hash(file1)
        != HashUtils.calculate_file_hash(file2)
    )


def test_verify_checksum_true() -> None:
    """Debe devolver True cuando los hashes coinciden."""

    checksum = HashUtils.calculate_bytes_hash(b"Ayni")

    assert HashUtils.verify_checksum(checksum, checksum)


def test_verify_checksum_false() -> None:
    """Debe devolver False cuando los hashes son diferentes."""

    checksum1 = HashUtils.calculate_bytes_hash(b"Ayni")

    checksum2 = HashUtils.calculate_bytes_hash(b"Kortex")

    assert not HashUtils.verify_checksum(
        checksum1,
        checksum2,
    )