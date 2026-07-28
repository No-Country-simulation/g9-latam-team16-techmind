"""
==========================================================
TechMind - Data Science
Script: generate_gold_test_set.py

Descripción:
    Genera el Gold Test Set con 70 documentos independientes
    con un ALTO NIVEL DE DETALLE Y CONTEXTO para AyniKortex,
    distribuidos equitativamente (10 documentos x 7 tipos):
    1. corto (10)
    2. mediano (10)
    3. largo (10)
    4. tecnico_especializado (10)
    5. ambiguo (10)
    6. errores_ortograficos (10)
    7. casos_limite (10)
==========================================================
"""

import sys
import shutil
from pathlib import Path
import pandas as pd

# Importar los datasets enriquecidos
from gold_data.cortos import CORTOS
from gold_data.medianos import MEDIANOS
from gold_data.largos import LARGOS
from gold_data.tecnico_especializado import TECNICO_ESPECIALIZADO
from gold_data.ambiguo import AMBIGUO
from gold_data.errores_ortograficos import ERRORES_ORTOGRAFICOS
from gold_data.casos_limite import CASOS_LIMITE

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GOLD_DIR = PROJECT_ROOT / "datasets" / "gold_test_set"

TEST_DOCUMENTS = CORTOS + MEDIANOS + LARGOS + TECNICO_ESPECIALIZADO + AMBIGUO + ERRORES_ORTOGRAFICOS + CASOS_LIMITE

def main():
    print(f"[INFO] Generando Gold Test Set con extenso nivel de detalle ({len(TEST_DOCUMENTS)} documentos)...")

    # Limpiar directorio si existe
    if GOLD_DIR.exists():
        shutil.rmtree(GOLD_DIR)
    
    GOLD_DIR.mkdir(parents=True, exist_ok=True)

    for doc in TEST_DOCUMENTS:
        type_dir = GOLD_DIR / doc["test_type"]
        type_dir.mkdir(parents=True, exist_ok=True)
        file_path = type_dir / f"{doc['doc_id']}.txt"
        
        # Eliminar dobles retornos de carro escapados por si los hay
        content = doc['content'].replace('\\\\n', '\\n')
        
        file_content = f"TITULO: {doc['title']}\nCATEGORIA_ESPERADA: {doc['expected_category']}\n\n{content}"
        file_path.write_text(file_content, encoding="utf-8")

    df_gold = pd.DataFrame(TEST_DOCUMENTS)
    # Limpiar saltos de linea dobles para CSV si es necesario
    df_gold['content'] = df_gold['content'].apply(lambda x: x.replace('\\\\n', '\\n'))
    
    csv_path = GOLD_DIR / "gold_test_set.csv"
    df_gold.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"[SUCCESS] Gold Test Set generado exitosamente en {GOLD_DIR}:")
    print(f"  - 70 archivos individuales .txt detallados en carpetas por tipologia.")
    print(f"  - Consolidado: gold_test_set.csv ({len(df_gold)} filas).")

if __name__ == "__main__":
    main()
