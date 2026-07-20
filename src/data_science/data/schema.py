"""
==========================================================
TechMind
Data Science Component

Module:
    schema.py

Description:
    Defines the Canonical Schema and business rules used
    throughout the Data Science pipeline.

Sprint:
    DS-03 - Dataset Construction
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from typing import Final

# ==========================================================
# Canonical Schema
# ==========================================================

REQUIRED_COLUMNS: Final[tuple[str, ...]] = (
    "document_id",
    "source",
    "title",
    "text",
    "category",
    "language",
)

OPTIONAL_COLUMNS: Final[tuple[str, ...]] = (
    "source_id",
    "tags",
    "author",
    "created_date",
    "url",
)

CANONICAL_SCHEMA: Final[tuple[str, ...]] = (
    *REQUIRED_COLUMNS,
    *OPTIONAL_COLUMNS,
)

# ==========================================================
# Metadata Columns
# ==========================================================

OPTIONAL_METADATA_COLUMNS: Final[tuple[str, ...]] = (
    "source_id",
    "tags",
    "author",
    "created_date",
    "url",
)

# ==========================================================
# Allowed Values
# ==========================================================

VALID_SOURCES: Final[tuple[str, ...]] = (
    "stack_exchange",
    "github",
    "huggingface",
    "technical_docs",
)

VALID_LANGUAGES: Final[tuple[str, ...]] = (
    "en",
    "es",
)

# ==========================================================
# Expected Data Types
# ==========================================================

COLUMN_TYPE_MAPPING: Final[dict[str, type]] = {
    "document_id": str,
    "source": str,
    "source_id": str,
    "title": str,
    "text": str,
    "category": str,
    "language": str,
    "tags": list,
    "author": str,
    "created_date": str,
    "url": str,
}

# ==========================================================
# Public Functions
# ==========================================================

def get_required_columns() -> tuple[str, ...]:
    """
    Returns the required columns of the Canonical Schema.
    """
    return REQUIRED_COLUMNS


def get_optional_columns() -> tuple[str, ...]:
    """
    Returns the optional columns of the Canonical Schema.
    """
    return OPTIONAL_COLUMNS


def get_canonical_schema() -> tuple[str, ...]:
    """
    Returns the complete Canonical Schema.
    """
    return CANONICAL_SCHEMA