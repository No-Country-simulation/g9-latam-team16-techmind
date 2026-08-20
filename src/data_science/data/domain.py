"""
==========================================================
TechMind
Data Science Component

Module:
    domain.py

Description:
    Defines the domain models shared by the Data Science
    preprocessing and inference pipelines.

==========================================================
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class DocumentRecord:
    """
    Represents a technical document before entering the
    preprocessing pipeline.
    """

    document_id: str
    source: str
    title: str
    text: str
    category: str
    language: str

    source_id: str | None = None
    tags: list[str] = field(default_factory=list)
    author: str | None = None
    created_date: str | None = None
    url: str | None = None


@dataclass(slots=True)
class ProcessedDocument:
    """
    Represents a document after completing the
    preprocessing pipeline.
    """

    document: DocumentRecord
    processed_text: str = ""
    tokens: list[str] = field(default_factory=list)
    lemmas: list[str] = field(default_factory=list)