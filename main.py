from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import traceback

app = FastAPI(title="TechMind ML API", version="1.0")

class TextRequest(BaseModel):
    text: str

@app.post("/api/v1/predict/text")
async def predict_text(request: TextRequest):
    try:
        return {
            "status": "success",
            "input_text": request.text,
            "prediction": "ejemplo_resultado"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/predict/file")
async def predict_file(request: Request):
    try:
        form = await request.form()
        file_item = form.get("file") or form.get("files") or form.get("document")
        
        if file_item and hasattr(file_item, "read"):
            content = await file_item.read()
            filename = getattr(file_item, "filename", "archivo.txt")
        else:
            content = await request.body()
            filename = "cuerpo_crudo.txt"

        return {
            "status": "success",
            "filename": filename,
            "size": len(content),
            "prediction": "resultado_analisis_archivo"
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "TechMind API is running"}