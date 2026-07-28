"""
==========================================================
TechMind - Data Science
Script: run_benchmark_experiments.py

Descripción:
    Ejecuta la Fase B del Benchmark Experimental (Sprint DS-09).
    Entrena y evalúa los 5 modelos (1K, 2.5K, 5K, 7.5K, 10K) sobre:
    1. Pruebas de validación del dataset de entrenamiento.
    2. Evaluación independiente sobre el Gold Test Set (70 documentos).

    Guarda los resultados tabulares en JSON y CSV dentro de `datasets/benchmark/`.
==========================================================
"""

import sys
import os
import json
import time
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Asegurar path de Python para los módulos del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BENCHMARK_DIR = PROJECT_ROOT / "datasets" / "benchmark"
GOLD_TEST_PATH = PROJECT_ROOT / "datasets" / "gold_test_set" / "gold_test_set.csv"

DATASETS = [
    ("EXP-01 (1K)", BENCHMARK_DIR / "train_1k.csv"),
    ("EXP-02 (2.5K)", BENCHMARK_DIR / "train_2.5k.csv"),
    ("EXP-03 (5K)", BENCHMARK_DIR / "train_5k.csv"),
    ("EXP-04 (7.5K)", BENCHMARK_DIR / "train_7.5k.csv"),
    ("EXP-05 (10K)", BENCHMARK_DIR / "train_10k.csv"),
]


def main():
    print("[INFO] Cargando Gold Test Set de 70 documentos...")
    df_gold = pd.read_csv(GOLD_TEST_PATH)
    print(f"[OK] Gold Test Set cargado: {len(df_gold)} documentos de prueba.")

    results = []

    for exp_id, dataset_path in DATASETS:
        print(f"\n==========================================")
        print(f"🚀 Ejecutando {exp_id} -> {dataset_path.name}")
        print(f"==========================================")

        df_train = pd.read_csv(dataset_path)

        # Preprocesar textos combinando título y contenido/texto
        if "text" in df_train.columns and "title" in df_train.columns:
            train_texts = df_train["title"].fillna("") + " " + df_train["text"].fillna("")
        elif "content" in df_train.columns and "title" in df_train.columns:
            train_texts = df_train["title"].fillna("") + " " + df_train["content"].fillna("")
        else:
            train_texts = df_train["text"].fillna("")

        train_labels = df_train["category"]

        # Label Encoder
        label_encoder = LabelEncoder()
        y_train = label_encoder.fit_transform(train_labels)

        # 1. Medición de Entrenamiento
        start_train_time = time.perf_counter()

        vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=10000, sublinear_tf=True)
        X_train = vectorizer.fit_transform(train_texts)

        model = LogisticRegression(C=1.5, max_iter=1000, random_state=42, solver="saga")
        model.fit(X_train, y_train)

        training_time = time.perf_counter() - start_train_time
        print(f"[METRICA] Tiempo de entrenamiento: {training_time:.4f} segundos.")

        # 2. Evaluación en Gold Test Set (70 documentos)
        gold_texts = df_gold["title"].fillna("") + " " + df_gold["content"].fillna("")
        gold_labels = df_gold["expected_category"]

        start_inf_time = time.perf_counter()
        X_gold = vectorizer.transform(gold_texts)
        gold_preds_encoded = model.predict(X_gold)
        total_inf_time = time.perf_counter() - start_inf_time

        gold_preds = label_encoder.inverse_transform(gold_preds_encoded)
        avg_inf_latency_ms = (total_inf_time / len(df_gold)) * 1000.0

        # Métricas Globales en Gold Test Set
        acc = accuracy_score(gold_labels, gold_preds)
        prec = precision_score(gold_labels, gold_preds, average="weighted", zero_division=0)
        rec = recall_score(gold_labels, gold_preds, average="weighted", zero_division=0)
        f1 = f1_score(gold_labels, gold_preds, average="weighted", zero_division=0)

        print(f"[GOLD TEST SET RESULTADOS]")
        print(f"  - Accuracy : {acc * 100:.2f}%")
        print(f"  - Precision: {prec * 100:.2f}%")
        print(f"  - Recall   : {rec * 100:.2f}%")
        print(f"  - F1-Score : {f1 * 100:.2f}%")
        print(f"  - Latencia Inferencia: {avg_inf_latency_ms:.3f} ms / doc")

        # 3. Desglose por tipo de prueba en Gold Test Set
        type_breakdown = {}
        for t_type in df_gold["test_type"].unique():
            mask = df_gold["test_type"] == t_type
            sub_labels = gold_labels[mask]
            sub_preds = gold_preds[mask]
            sub_acc = accuracy_score(sub_labels, sub_preds)
            sub_f1 = f1_score(sub_labels, sub_preds, average="weighted", zero_division=0)
            type_breakdown[t_type] = {
                "accuracy": round(float(sub_acc), 4),
                "f1_score": round(float(sub_f1), 4),
            }

        # Estimacion aproximada de tamaño del modelo
        vocab_size = len(vectorizer.vocabulary_)
        approx_size_mb = (X_train.data.nbytes + sys.getsizeof(model)) / (1024 * 1024) + (vocab_size * 0.0001)

        record = {
            "experiment": exp_id,
            "dataset_size": len(df_train),
            "accuracy": round(float(acc), 4),
            "precision": round(float(prec), 4),
            "recall": round(float(rec), 4),
            "f1_score": round(float(f1), 4),
            "training_time_sec": round(float(training_time), 4),
            "avg_inference_latency_ms": round(float(avg_inf_latency_ms), 3),
            "vocab_size": vocab_size,
            "approx_model_size_mb": round(float(approx_size_mb), 2),
            "test_type_breakdown": type_breakdown,
        }
        results.append(record)

    # Exportar resultados
    json_path = BENCHMARK_DIR / "benchmark_results.json"
    csv_path = BENCHMARK_DIR / "benchmark_results.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    df_res = pd.DataFrame(results)
    df_res_clean = df_res.drop(columns=["test_type_breakdown"])
    df_res_clean.to_csv(csv_path, index=False)

    print(f"\n🎉 Todos los experimentos completados exitosamente.")
    print(f"💾 Resultados guardados en:\n  - {json_path}\n  - {csv_path}")


if __name__ == "__main__":
    main()
