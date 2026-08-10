from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List
import traceback
import sys
import os
import numpy as np

# Añadir src al path por si acaso para las importaciones
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.data_science.ml.persistence.repositories.filesystem_artifact_repository import FilesystemArtifactRepository

# Variables globales para los modelos
model_bundle = None

# Lifespan context manager para cargar el modelo al arrancar
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_bundle
    print("Cargando modelo de Machine Learning...")
    try:
        repo = FilesystemArtifactRepository(root_directory=os.path.join(os.path.dirname(__file__), "models"))
        model_bundle = repo.load("aynikortex_classifier-v1.4.0")
        print("Modelo cargado exitosamente.")
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
    yield
    print("Apagando API...")

app = FastAPI(title="TechMind ML API", version="1.0", lifespan=lifespan)

# --- Modelos Pydantic (CONTRATO) ---
class TextRequest(BaseModel):
    text: str

class Keyword(BaseModel):
    term: str
    score: float

class PredictionResponse(BaseModel):
    category: str
    subcategory: str
    confidence: float
    modelVersion: str
    keywords: List[Keyword]

# --- Funciones Auxiliares ---
def _extract_keywords(text: str, vectorizer, top_n: int = 3) -> List[Keyword]:
    try:
        # Transformamos el texto
        tfidf_matrix = vectorizer.transform([text])
        # Obtenemos los nombres de las caracteristicas (palabras)
        feature_names = vectorizer.get_feature_names_out()
        
        # Obtenemos los indices de los valores no nulos y sus puntuaciones
        nonzero_indices = tfidf_matrix.nonzero()[1]
        scores = tfidf_matrix.data
        
        # Ordenamos los indices por score de mayor a menor
        sorted_indices = np.argsort(scores)[::-1]
        
        keywords = []
        for idx in sorted_indices[:top_n]:
            term = feature_names[nonzero_indices[idx]]
            score = float(scores[idx])
            keywords.append(Keyword(term=term, score=score))
            
        return keywords
    except Exception as e:
        print(f"Error extrayendo keywords: {e}")
        return []

def _process_prediction(text: str) -> PredictionResponse:
    if not model_bundle:
        raise HTTPException(status_code=503, detail="Modelo no cargado. Revisa los logs del servidor.")
    
    # 1. Extraer caracteristicas
    X = model_bundle.vectorizer.transform([text])
    
    # 2. Predecir
    probabilities = model_bundle.model.predict_proba(X)[0]
    max_prob_index = np.argmax(probabilities)
    confidence = float(probabilities[max_prob_index])
    
    # 3. Decodificar etiqueta (Ej. Backend_Base de datos)
    encoded_label = model_bundle.model.classes_[max_prob_index]
    decoded_label = model_bundle.label_encoder.inverse_transform([encoded_label])[0]
    
    # Separar en categoria y subcategoria
    if "_" in decoded_label:
        parts = decoded_label.split("_", 1)
        category = parts[0]
        subcategory = parts[1]
    else:
        category = decoded_label
        subcategory = "General"
        
    # 4. Extraer keywords
    keywords = _extract_keywords(text, model_bundle.vectorizer)
    
    return PredictionResponse(
        category=category,
        subcategory=subcategory,
        confidence=float(round(confidence, 4)),
        modelVersion=model_bundle.metadata.version,
        keywords=keywords
    )

# --- Endpoints ---
@app.post("/api/v1/predict/text", response_model=PredictionResponse)
async def predict_text(request: TextRequest):
    try:
        return _process_prediction(request.text)
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/predict/file", response_model=PredictionResponse)
async def predict_file(request: Request):
    try:
        form = await request.form()
        file_item = form.get("file") or form.get("files") or form.get("document")
        
        if file_item and hasattr(file_item, "read"):
            # Validacion basica: solo texto
            filename = getattr(file_item, "filename", "archivo.txt")
            if not filename.endswith(".txt") and not filename.endswith(".md") and not filename.endswith(".csv"):
                raise HTTPException(status_code=400, detail="Solo se permiten archivos de texto plano (.txt, .md, .csv)")
                
            content_bytes = await file_item.read()
            text = content_bytes.decode('utf-8', errors='ignore')
        else:
            content_bytes = await request.body()
            text = content_bytes.decode('utf-8', errors='ignore')

        if not text.strip():
            raise HTTPException(status_code=400, detail="El texto está vacío.")

        return _process_prediction(text)
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "TechMind API is running", "model_loaded": model_bundle is not None}