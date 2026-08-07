import sys
from pathlib import Path

# Asegurar path de Python para los módulos del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.data_science.ml.persistence.repositories.filesystem_artifact_repository import FilesystemArtifactRepository

def main():
    models_dir = PROJECT_ROOT / "models"
    repo = FilesystemArtifactRepository(root_directory=models_dir)
    
    # Identificador del modelo que acabamos de guardar
    model_id = "aynikortex_classifier-v1.0.0"
    
    if not repo.exists(model_id):
        print(f"[ERROR] No se encontro el modelo: {model_id} en {models_dir}")
        return
        
    print("[INFO] Cargando modelo desde el disco...")
    bundle = repo.load(model_id)
    
    model = bundle.model
    vectorizer = bundle.vectorizer
    label_encoder = bundle.label_encoder
    
    print("\n[OK] Modelo cargado con exito.")
    print("=====================================================")
    print(" AyniKortex - Consola de Prueba Interactiva")
    print("=====================================================")
    print("Escribe un texto tecnico o de prueba y presiona Enter.")
    print("Escribe 'salir' para terminar.\n")
    
    while True:
        try:
            texto = input("Ingresa un texto: ")
            if texto.lower().strip() == 'salir':
                break
            if not texto.strip():
                continue
                
            # Preprocesar e inferir
            x_test = vectorizer.transform([texto])
            pred_encoded = model.predict(x_test)
            
            try:
                # Obtener probabilidad de confianza
                probabilidades = model.predict_proba(x_test)[0]
                confianza = max(probabilidades) * 100
                confianza_str = f" (Confianza: {confianza:.2f}%)"
            except AttributeError:
                confianza_str = ""
            
            # Decodificar categoria
            categoria = label_encoder.inverse_transform(pred_encoded)[0]
            
            print(f"-> Prediccion: {categoria}{confianza_str}\n")
            
        except KeyboardInterrupt:
            break
            
    print("\n[FIN] Prueba terminada!")

if __name__ == "__main__":
    main()
