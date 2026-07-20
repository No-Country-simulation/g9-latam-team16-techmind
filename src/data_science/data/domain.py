"""
==========================================================
TechMind
Data Science Component

Module:
    domain.py

Description:
    Defines the domain models shared across the Data Science
    pipeline.

Sprint:
    DS-03 - Dataset Construction
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from dataclasses import dataclass, field
#from typing import Literal, TypedDict
from typing import NotRequired, TypedDict

# ==========================================================
# Domain Models
# ==========================================================

class DocumentRecord(TypedDict):

    document_id: str
    source: str
    title: str
    text: str
    category: str
    language: str

    source_id: NotRequired[str]
    tags: NotRequired[list[str]]
    author: NotRequired[str]
    created_date: NotRequired[str]
    url: NotRequired[str]


@dataclass(slots=True)
class ValidationIssue:
    """
    Represents a single validation issue detected during
    dataset validation.
    """

    level: Literal["ERROR", "WARNING"]
    message: str
    column: str | None = None
    row: int | None = None


@dataclass(slots=True)
class ValidationResult:
    """
    Aggregates all validation issues found during dataset
    validation.
    """

    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """
        Returns True if no validation errors exist.
        """
        return not any(
            issue.level == "ERROR"
            for issue in self.issues
        )

    @property
    def errors(self) -> list[ValidationIssue]:
        """
        Returns only validation errors.
        """
        return [
            issue
            for issue in self.issues
            if issue.level == "ERROR"
        ]

    @property
    def warnings(self) -> list[ValidationIssue]:
        """
        Returns only validation warnings.
        """
        return [
            issue
            for issue in self.issues
            if issue.level == "WARNING"
        ]