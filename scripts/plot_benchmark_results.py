"""
==========================================================
TechMind - Data Science
Script: plot_benchmark_results.py

Descripción:
    Genera los 7 gráficos comparativos para el Benchmark
    Experimental (Sprint DS-09) a partir de los resultados
    de `datasets/benchmark/benchmark_results.json`:
    1. Accuracy vs Tamaño del Dataset
    2. Precision vs Tamaño del Dataset
    3. Recall vs Tamaño del Dataset
    4. F1-Score vs Tamaño del Dataset
    5. Tiempo de Entrenamiento
    6. Tiempo de Inferencia (Latencia)
    7. Comparativa General de Métricas
==========================================================
"""

import sys
import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_JSON = PROJECT_ROOT / "datasets" / "benchmark" / "benchmark_results.json"
IMAGES_DIR = PROJECT_ROOT / "docs" / "SPRINTS" / "data-science" / "images"


def main():
    if not RESULTS_JSON.exists():
        print(f"[ERROR] No se encontro {RESULTS_JSON}. Ejecuta primero run_benchmark_experiments.py.")
        return

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    with open(RESULTS_JSON, "r", encoding="utf-8") as f:
        results = json.load(f)

    df = pd.DataFrame(results)

    # Estilo general
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    colors = ["#2b5c8f", "#4682b4", "#5c9ded", "#7fb3d5", "#a9cce3"]

    sizes_labels = [f"{s // 1000}K" if s >= 1000 else str(s) for s in df["dataset_size"]]

    # 1. Accuracy vs Tamaño del Dataset
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(sizes_labels, df["accuracy"] * 100, marker="o", color="#2b5c8f", linewidth=2.5, markersize=8)
    ax.set_title("Accuracy vs Tamaño del Dataset de Entrenamiento", fontsize=12, fontweight="bold")
    ax.set_xlabel("Tamaño del Dataset", fontsize=10)
    ax.set_ylabel("Accuracy (%)", fontsize=10)
    ax.set_ylim(0, 105)
    for i, v in enumerate(df["accuracy"] * 100):
        ax.text(i, v + 2, f"{v:.1f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "accuracy_vs_dataset_size.png", dpi=300)
    plt.close()

    # 2. Precision vs Tamaño del Dataset
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(sizes_labels, df["precision"] * 100, marker="s", color="#27ae60", linewidth=2.5, markersize=8)
    ax.set_title("Precision vs Tamaño del Dataset de Entrenamiento", fontsize=12, fontweight="bold")
    ax.set_xlabel("Tamaño del Dataset", fontsize=10)
    ax.set_ylabel("Precision (%)", fontsize=10)
    ax.set_ylim(0, 105)
    for i, v in enumerate(df["precision"] * 100):
        ax.text(i, v + 2, f"{v:.1f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "precision_vs_dataset_size.png", dpi=300)
    plt.close()

    # 3. Recall vs Tamaño del Dataset
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(sizes_labels, df["recall"] * 100, marker="^", color="#e67e22", linewidth=2.5, markersize=8)
    ax.set_title("Recall vs Tamaño del Dataset de Entrenamiento", fontsize=12, fontweight="bold")
    ax.set_xlabel("Tamaño del Dataset", fontsize=10)
    ax.set_ylabel("Recall (%)", fontsize=10)
    ax.set_ylim(0, 105)
    for i, v in enumerate(df["recall"] * 100):
        ax.text(i, v + 2, f"{v:.1f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "recall_vs_dataset_size.png", dpi=300)
    plt.close()

    # 4. F1-Score vs Tamaño del Dataset
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(sizes_labels, df["f1_score"] * 100, marker="D", color="#8e44ad", linewidth=2.5, markersize=8)
    ax.set_title("F1-Score vs Tamaño del Dataset de Entrenamiento", fontsize=12, fontweight="bold")
    ax.set_xlabel("Tamaño del Dataset", fontsize=10)
    ax.set_ylabel("F1-Score (%)", fontsize=10)
    ax.set_ylim(0, 105)
    for i, v in enumerate(df["f1_score"] * 100):
        ax.text(i, v + 2, f"{v:.1f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "f1_score_vs_dataset_size.png", dpi=300)
    plt.close()

    # 5. Tiempo de Entrenamiento
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(sizes_labels, df["training_time_sec"], color="#34495e", width=0.5)
    ax.set_title("Tiempo de Entrenamiento por Tamaño de Dataset", fontsize=12, fontweight="bold")
    ax.set_xlabel("Tamaño del Dataset", fontsize=10)
    ax.set_ylabel("Tiempo (segundos)", fontsize=10)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height + 0.1, f"{height:.2f}s", ha="center", va="bottom", fontweight="bold")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "training_time_vs_dataset_size.png", dpi=300)
    plt.close()

    # 6. Tiempo de Inferencia (Latencia por documento)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(sizes_labels, df["avg_inference_latency_ms"], color="#16a085", width=0.5)
    ax.set_title("Latencia Promedio de Inferencia por Documento", fontsize=12, fontweight="bold")
    ax.set_xlabel("Tamaño del Dataset de Entrenamiento", fontsize=10)
    ax.set_ylabel("Latencia (ms / documento)", fontsize=10)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height + 0.05, f"{height:.2f} ms", ha="center", va="bottom", fontweight="bold")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "inference_latency_vs_dataset_size.png", dpi=300)
    plt.close()

    # 7. Comparativa General de Métricas
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(df))
    width = 0.2
    ax.bar([p - 1.5 * width for p in x], df["accuracy"] * 100, width, label="Accuracy", color="#2b5c8f")
    ax.bar([p - 0.5 * width for p in x], df["precision"] * 100, width, label="Precision", color="#27ae60")
    ax.bar([p + 0.5 * width for p in x], df["recall"] * 100, width, label="Recall", color="#e67e22")
    ax.bar([p + 1.5 * width for p in x], df["f1_score"] * 100, width, label="F1-Score", color="#8e44ad")

    ax.set_title("Comparativa General de Métricas de Evaluación", fontsize=13, fontweight="bold")
    ax.set_xlabel("Experimento (Tamaño del Dataset)", fontsize=11)
    ax.set_ylabel("Porcentaje (%)", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(df["experiment"])
    ax.set_ylim(0, 110)
    ax.legend(loc="upper left")
    plt.tight_layout()
    fig.savefig(IMAGES_DIR / "general_metrics_comparison.png", dpi=300)
    plt.close()

    print(f"[SUCCESS] Se generaron exitosamente las 7 graficas del benchmark en {IMAGES_DIR}:")
    print("  - accuracy_vs_dataset_size.png")
    print("  - precision_vs_dataset_size.png")
    print("  - recall_vs_dataset_size.png")
    print("  - f1_score_vs_dataset_size.png")
    print("  - training_time_vs_dataset_size.png")
    print("  - inference_latency_vs_dataset_size.png")
    print("  - general_metrics_comparison.png")


if __name__ == "__main__":
    main()
