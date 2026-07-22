"""
==========================================================
TechMind
Data Science Component

Script:
    validar_dataset_pipeline.py

Description:
    Validates the preprocessing pipeline using a sample
    dataset and generates a validation report.

Sprint:
    DS-04.5 - Pipeline Hardening
==========================================================
"""

# ==========================================================
# Validation Configuration
# ==========================================================

VALIDATION_SIZE = 100

# ==========================================================
# Imports
# ==========================================================

import sys
from pathlib import Path
from time import perf_counter

# ----------------------------------------------------------
# Configure project path
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# ----------------------------------------------------------
# Imports
# ----------------------------------------------------------

from validation.dataset_validator import DatasetValidator
from validation.report import Report

from data_science.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)

from validation.benchmark import BenchmarkResult


# ==========================================================
# Dataset
# ==========================================================

DATASET_PATH = (
    PROJECT_ROOT
    / "datasets"
    / "raw"
<<<<<<< HEAD
    / "master_dataset_v1.csv"
=======
    / "documents_prueba_data_generada_data.csv"
>>>>>>> 6b0afd4 (refactor(ds): migración de DocumentRecord a dataclass y estabilización del pipeline de preprocesamiento)
)


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("VALIDACIÓN DEL COMPONENTE DATA SCIENCE")
    print("=" * 60)

    # ------------------------------------------------------
    # Dataset
    # ------------------------------------------------------

    validator = DatasetValidator()

    dataframe = validator.load(DATASET_PATH)

    validator.validate_columns(dataframe)

    documents = validator.build_documents(
        dataframe=dataframe,
        limit=VALIDATION_SIZE,
    )

    document = documents[0]

    # ------------------------------------------------------
    # Pipeline
    # ------------------------------------------------------

    pipeline = PreprocessingPipeline()

    start = perf_counter()

    processed = pipeline.process(document)

    total = perf_counter() - start

    # ------------------------------------------------------
    # Benchmark
    # ------------------------------------------------------

    benchmark = BenchmarkResult(
        documents=len(documents),
        success=1,
        failed=0,
        success_rate=100.0,
        total_time=total,
        average_time=total,
        min_time=total,
        max_time=total,
        documents_per_second=1 / total if total else 0,
        errors=[],
    )

    # ------------------------------------------------------
    # Validaciones
    # ------------------------------------------------------

    assert processed.processed_text

    assert processed.tokens

    assert processed.lemmas

    # ------------------------------------------------------
    # Report
    # ------------------------------------------------------

    report = Report()

    report.show_dataset(
        str(DATASET_PATH),
        dataframe,
    )

    report.show_document(
        document,
    )

    report.show_preprocessing(
        document,
        processed,
    )

    report.show_benchmark(
        benchmark,
    )

    report.show_success()


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()