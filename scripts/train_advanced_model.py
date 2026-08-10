import sys
import os
import itertools
import random
from pathlib import Path
from datetime import datetime
import hashlib

# Añadir el src al path para poder importar módulos del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

from src.data_science.ml.persistence.repositories.filesystem_artifact_repository import FilesystemArtifactRepository
from src.data_science.ml.persistence.domain.artifact_bundle import ArtifactBundle
from src.data_science.ml.persistence.domain.model_metadata import ModelMetadata


def generate_synthetic_sentences():
    # Estructura: (Acción, Tecnología, Contexto) -> Frase
    actions_fix = ["Necesitamos arreglar", "Hay un bug en", "Se reportó un fallo en", "Hay que optimizar", "Debemos corregir", "El cliente se queja de", "Urge refactorizar"]
    actions_create = ["Tenemos que implementar", "Se requiere desarrollar", "Vamos a construir", "Hay que agregar", "El product owner pidió", "Es necesario integrar"]
    
    domains = {
        "Frontend_UI/UX": {
            "techs": ["los estilos CSS", "los componentes de React", "la vista de Vue.js", "el responsive design", "el HTML semántico", "el grid layout", "Tailwind CSS", "Bootstrap", "la interfaz de usuario", "la landing page"],
            "contexts": ["para móviles", "en producción", "para mejorar el SEO", "en el navegador", "para el sprint actual", "para mejorar la experiencia de usuario"]
        },
        "Frontend_General": {
            "techs": ["el estado de Redux", "el framework Next.js", "el código de Angular", "el DOM virtual", "los hooks de React", "la arquitectura frontend", "Webpack", "Vite", "el store de Vuex"],
            "contexts": ["para acelerar la carga", "en el lado del cliente", "en el server side rendering", "en el proyecto", "urgentemente"]
        },
        "Backend_Databases": {
            "techs": ["las consultas SQL", "la base de datos MySQL", "el cluster de PostgreSQL", "las colecciones de MongoDB", "las tablas de Redis", "el ORM Prisma", "Entity Framework", "los índices de la base de datos"],
            "contexts": ["para reducir latencia", "en el servidor", "para evitar bloqueos", "para el panel de control", "en la nube"]
        },
        "Backend_APIs": {
            "techs": ["el endpoint REST", "la API GraphQL", "los microservicios en Java", "el servidor Node.js Express", "el controlador de Spring Boot", "el webhook", "la integración con Stripe", "la API de Django"],
            "contexts": ["para procesar los pagos", "en el backend", "para los clientes externos", "en el servidor de staging", "para soportar más tráfico"]
        },
        "Security_General": {
            "techs": ["los tokens JWT", "el sistema de autenticación", "la encriptación AES", "las políticas CORS", "el firewall WAF", "OAuth2", "Single Sign-On SSO", "la protección contra inyección SQL", "los certificados SSL"],
            "contexts": ["para evitar hackeos", "para cumplir normativas", "en todos los endpoints", "en producción", "para proteger datos sensibles"]
        },
        "DevOps_CI/CD": {
            "techs": ["el pipeline de GitHub Actions", "las tareas de Jenkins", "el despliegue en GitLab CI", "el archivo de Docker Compose", "las imágenes de Docker", "el despliegue Blue/Green"],
            "contexts": ["para automatizar pases a producción", "en el repositorio", "porque los tests fallaron", "para acelerar el deploy"]
        },
        "DevOps_Infrastructure": {
            "techs": ["los pods de Kubernetes", "el clúster K8s", "la infraestructura como código en Terraform", "las instancias EC2 de AWS", "los balanceadores de carga", "los logs de Nginx", "el monitoreo de Prometheus"],
            "contexts": ["para soportar el tráfico", "en la nube", "para evitar caídas", "en el entorno de desarrollo"]
        },
        "AI/ML_Data Science": {
            "techs": ["el modelo de machine learning", "la red neuronal de TensorFlow", "el script de Python pandas", "la regresión logística de Scikit-Learn", "los embeddings de NLP", "el LLM", "el pipeline de datos"],
            "contexts": ["para mejorar la precisión", "para predecir ventas", "en el Jupyter Notebook", "para análisis de sentimiento", "para evitar el sobreajuste"]
        },
        "Cloud_Serverless": {
            "techs": ["las funciones de AWS Lambda", "los buckets de Amazon S3", "el servicio API Gateway", "las Azure Functions", "los recursos de Google Cloud", "el almacenamiento en la nube"],
            "contexts": ["para reducir costos", "en la cuenta de AWS", "para el despliegue serverless", "en producción"]
        },
        "QA_Testing": {
            "techs": ["los unit tests de Jest", "las pruebas end-to-end de Cypress", "la cobertura de SonarQube", "los mocks de JUnit", "las pruebas de integración", "el TDD"],
            "contexts": ["para evitar bugs en producción", "antes del pase a producción", "en el pipeline", "para garantizar calidad"]
        },
        "Agile_Scrum": {
            "techs": ["el backlog de Jira", "los tickets del sprint", "las user stories", "el tablero Kanban", "la estimación de story points", "la retrospectiva"],
            "contexts": ["con el Product Owner", "en la reunión diaria", "para la planificación", "antes de que termine el sprint"]
        }
    }
    
    generated_data = []
    
    # Generar permutaciones combinando (Action + Tech + Context)
    for label, components in domains.items():
        techs = components["techs"]
        contexts = components["contexts"]
        
        # Mezclar combinaciones de acciones de "arreglo" y de "creación"
        for action in actions_fix + actions_create:
            for tech in techs:
                for context in contexts:
                    sentence = f"{action} {tech} {context}."
                    generated_data.append((sentence, label))
                    
    # Mezclar el orden de las frases
    generated_data = shuffle(generated_data, random_state=42)
    return generated_data

def main():
    print("Iniciando Generador Programático de Datos...")
    dataset = generate_synthetic_sentences()
    
    print(f"¡Se han generado {len(dataset)} frases técnicas perfectamente categorizadas!")
    
    texts = [row[0] for row in dataset]
    labels = [row[1] for row in dataset]

    print("Entrenando modelo de Machine Learning con el gran volumen de datos...")
    
    # 1. Label Encoder
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    
    # 2. Vectorizer
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=3000, sublinear_tf=True)
    X = vectorizer.fit_transform(texts)
    
    # 3. Model - C más alto y más iteraciones para ajustarse mejor a los miles de datos
    model = LogisticRegression(C=2.0, max_iter=2000, random_state=42)
    model.fit(X, y)
    
    print("Modelo entrenado con éxito.")
    
    # Computar un checksum real para el modelo
    model_bytes = str(model.get_params()).encode('utf-8')
    checksum = hashlib.sha256(model_bytes).hexdigest()

    metadata = ModelMetadata(
        model_name="aynikortex_classifier",
        version="v1.4.0",
        algorithm="LogisticRegression",
        created_at=datetime.now(),
        training_dataset="programmatic_synthetic_dataset",
        feature_count=3000,
        label_count=len(label_encoder.classes_),
        checksum=checksum,
        description="Modelo Junior entrenado con miles de frases programaticamente generadas mediante combinatoria logica.",
        author="Data Science Team"
    )
    
    bundle = ArtifactBundle(
        model=model,
        vectorizer=vectorizer,
        metadata=metadata,
        label_encoder=label_encoder,
        model_filename="model.joblib",
        vectorizer_filename="vectorizer.joblib",
        label_encoder_filename="label_encoder.joblib"
    )
    
    models_dir = PROJECT_ROOT / "models"
    repo = FilesystemArtifactRepository(root_directory=models_dir)
    
    saved_id = repo.save(bundle)
    print(f"Modelo avanzado guardado exitosamente en: models/{saved_id}")

if __name__ == "__main__":
    main()
