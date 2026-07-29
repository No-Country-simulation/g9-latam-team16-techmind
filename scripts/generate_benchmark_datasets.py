"""
==========================================================
TechMind - Data Science
Script: generate_benchmark_datasets.py

Descripción:
    Genera los 5 datasets de entrenamiento para el Benchmark
    Experimental (Sprint DS-09) a partir del dataset maestro:
    - train_1k.csv   (1,000 registros)
    - train_2.5k.csv (2,500 registros)
    - train_5k.csv   (5,000 registros)
    - train_7.5k.csv (7,500 registros)
    - train_10k.csv  (10,000 registros)

    Utiliza muestreo estratificado por 'category' para garantizar
    el balance de clases en todas las escalas.
==========================================================
"""

import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MASTER_DATASET_PATH = PROJECT_ROOT / "datasets" / "raw" / "master_dataset_v1.csv"
OUTPUT_DIR = PROJECT_ROOT / "datasets" / "benchmark"

DATASET_SIZES = {
    "train_1k.csv": 1000,
    "train_2.5k.csv": 2500,
    "train_5k.csv": 5000,
    "train_7.5k.csv": 7500,
    "train_10k.csv": 10000,
}


def main():
    print(f"[INFO] Cargando dataset maestro desde {MASTER_DATASET_PATH}...")
    df_master = pd.read_csv(MASTER_DATASET_PATH)
    total_master = len(df_master)
    print(f"[OK] Dataset maestro cargado: {total_master} registros.")
    print(f"[STATS] Categorias detectadas: {df_master['category'].value_counts().to_dict()}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename, target_size in DATASET_SIZES.items():
        output_path = OUTPUT_DIR / filename
        if target_size == total_master:
            df_subset = df_master.copy()
        else:
            fraction = target_size / total_master
            df_subset, _ = train_test_split(
                df_master,
                train_size=fraction,
                stratify=df_master["category"],
                random_state=42,
            )

        df_subset.to_csv(output_path, index=False)
        print(f"[SAVED] {filename} -> {len(df_subset)} registros | Distribución: {df_subset['category'].value_counts().to_dict()}")

    print("\n[SUCCESS] Generación de los 5 datasets de entrenamiento completada con éxito.")


if __name__ == "__main__":
    main()
