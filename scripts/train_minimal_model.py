import sys
import os
import json
from pathlib import Path
import numpy as np

# Añadir el src al path para poder importar módulos del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

from src.data_science.ml.persistence.repositories.filesystem_artifact_repository import FilesystemArtifactRepository
from src.data_science.ml.persistence.domain.artifact_bundle import ArtifactBundle
from src.data_science.ml.persistence.domain.model_metadata import ModelMetadata

def main():
    print("Preparando el mini-dataset tecnológico...")
    
    # Dataset manual con frases técnicas reales
    dataset = [
        # FRONTEND
        ("Necesitamos ajustar los estilos de los componentes en React y optimizar el CSS de la landing page principal.", "Frontend_General"),
        ("El estado global de Vuex está causando renders innecesarios, hay que refactorizar los reducers.", "Frontend_General"),
        ("Agreguemos animaciones con Tailwind CSS y Framer Motion para mejorar la UX.", "Frontend_UI/UX"),
        ("Hay un problema en el formulario de login, el token JWT no se guarda en el local storage.", "Frontend_Authentication"),
        ("Migraremos la web de Angular a Next.js para mejorar el SEO y el server side rendering.", "Frontend_General"),
        ("El responsive design está fallando en móviles, arregla los media queries del grid.", "Frontend_UI/UX"),
        
        # BACKEND
        ("La base de datos MySQL tiene bloqueos, necesitamos optimizar las consultas SQL.", "Backend_Databases"),
        ("Hay que crear un endpoint REST en Node.js Express para procesar los pagos de Stripe.", "Backend_APIs"),
        ("El microservicio de Java con Spring Boot se queda sin memoria, ajustemos el heap de la JVM.", "Backend_General"),
        ("Implementaremos GraphQL para evitar hacer overfetching en la API de productos.", "Backend_APIs"),
        ("Tenemos que migrar de PostgreSQL a MongoDB para manejar mejor los JSON anidados.", "Backend_Databases"),
        ("Se necesita un job programado en Python para limpiar los registros temporales cada medianoche.", "Backend_General"),
        
        # SECURITY
        ("Es urgente implementar encriptación de datos sensibles y configurar tokens JWT para evitar vulnerabilidades de inyección SQL en los endpoints.", "Security_General"),
        ("Se detectó un intento de inyección SQL en el formulario de búsqueda, sanitiza los inputs.", "Security_General"),
        ("Actualiza las políticas CORS del backend porque está aceptando peticiones de orígenes desconocidos.", "Security_General"),
        ("Instala un WAF y habilita el rate limiting para mitigar los ataques de denegación de servicio DDoS.", "Security_General"),
        
        # DEVOPS
        ("El pipeline de CI/CD en GitHub Actions falló porque la imagen de Docker no compiló.", "DevOps_CI/CD"),
        ("Hay que escalar los pods en Kubernetes usando un Horizontal Pod Autoscaler.", "DevOps_Infrastructure"),
        ("Configura Terraform para provisionar tres instancias EC2 y un balanceador de carga en AWS.", "DevOps_Infrastructure"),
        ("Se nos llenó el disco del servidor, configura la rotación de logs de Nginx.", "DevOps_Infrastructure"),
        ("La subida a producción será automatizada con Jenkins y despliegue Blue/Green.", "DevOps_CI/CD"),
        
        # AI/ML
        ("El modelo de machine learning está sobreajustado, hay que hacer regularización y cross validation.", "AI/ML_Data Science"),
        ("Entrenaremos una red neuronal profunda con TensorFlow para clasificación de imágenes.", "AI/ML_Data Science"),
        ("El accuracy del modelo de regresión logística bajó mucho, revisa las métricas f1 y precision.", "AI/ML_Data Science"),
        ("Usaremos modelos de lenguaje natural LLM y embeddings para análisis de sentimiento.", "AI/ML_Data Science"),
        
        # MOBILE
        ("La aplicación en React Native se crashea en Android 12, necesitamos revisar los logs en Logcat.", "Mobile_Android"),
        ("Hay que actualizar los pods de CocoaPods para el nuevo SDK en iOS con Swift.", "Mobile_iOS"),
        ("Los widgets en Flutter no se están reconstruyendo cuando cambia el State.", "Mobile_General"),
        
        # CLOUD
        ("Hay que configurar los permisos de lectura en el bucket de Amazon S3.", "Cloud_Storage"),
        ("El costo de Google Cloud subió, revisa si tenemos funciones Serverless encendidas por error.", "Cloud_Compute"),
        ("Crearemos una arquitectura de microservicios usando AWS Lambda y API Gateway.", "Cloud_Serverless"),
        
        # QA / TESTING
        ("Agrega pruebas End-to-End con Cypress para verificar el flujo de compras en el carrito.", "QA_Automation"),
        ("El unit test en Jest está fallando porque no estamos mockeando bien la respuesta de Axios.", "QA_Testing"),
        ("El coverage de SonarQube nos pide al menos 80% de cobertura de código en JUnit.", "QA_Testing"),
        
        # DATA ENGINEERING
        ("El proceso ETL con Apache Spark tarda demasiado, hay que particionar mejor los datos.", "Data_Engineering"),
        ("El pipeline de datos en Airflow falló al conectar con Snowflake, revisa las credenciales.", "Data_Engineering"),
        
        # AGILE / PRODUCT
        ("Hay que cerrar el sprint en Jira y mover los tickets no terminados al Backlog.", "Agile_Scrum"),
        ("El product owner necesita refinar las user stories para la próxima planificacion.", "Agile_Product"),
        
        # WEB3 / BLOCKCHAIN
        ("Hay que hacer deploy del smart contract en Solidity a la red principal de Ethereum.", "Web3_Blockchain"),
        ("Optimiza el consumo de gas en las transacciones de minteo de NFTs.", "Web3_Blockchain"),
        
        # EMBEDDED / IOT
        ("El sensor de temperatura en la Raspberry Pi dejó de publicar mensajes por MQTT.", "IoT_Hardware"),
        ("Actualiza el firmware del microcontrolador Arduino escrito en C++.", "IoT_Hardware"),
        
        # NETWORKING
        ("El firewall de Cisco está bloqueando los paquetes del protocolo BGP en el router.", "Networking_Infrastructure"),
        ("Necesitamos configurar una VPN IPsec site-to-site con la nueva oficina.", "Networking_Infrastructure"),
        
        # GAME DEVELOPMENT
        ("Hay un bug en los shaders de la tarjeta gráfica y los FPS en Unity cayeron a 20.", "GameDev_Graphics"),
        ("El motor de físicas en Unreal Engine no detecta bien las colisiones del personaje.", "GameDev_Physics"),
        
        # ERP / CRM
        ("El workflow de automatización de ventas en Salesforce está enviando correos dobles.", "ERP_CRM"),
        ("Desarrolla una integración ABAP en SAP para sincronizar el inventario de Odoo.", "ERP_CRM"),
        
        # ARCHITECTURE
        ("El patrón Event-Driven con Kafka está perdiendo mensajes si el consumidor muere.", "Architecture_Microservices"),
        ("Refactorizar el monolito a Domain-Driven Design para desacoplar los servicios.", "Architecture_Design"),
        
        # CYBERSECURITY ADVANCED
        ("El pentesting reportó una vulnerabilidad crítica de Cross-Site Scripting XSS.", "Cybersecurity_Pentesting"),
        ("Integra Single Sign-On SSO y OAuth2 usando Active Directory IAM.", "Cybersecurity_IAM")
    ]
    
    texts = [row[0] for row in dataset]
    labels = [row[1] for row in dataset]

    print("Entrenando modelo...")
    # 1. Label Encoder
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    
    # 2. Vectorizer
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=2000, sublinear_tf=True)
    X = vectorizer.fit_transform(texts)
    
    # 3. Model
    model = LogisticRegression(C=1.5, max_iter=1000, random_state=42)
    model.fit(X, y)
    
    print("Modelo entrenado con éxito.")
    
    from datetime import datetime
    import hashlib

    # Computar un checksum falso para este ejemplo
    model_bytes = str(model.get_params()).encode('utf-8')
    checksum = hashlib.sha256(model_bytes).hexdigest()

    metadata = ModelMetadata(
        model_name="aynikortex_classifier",
        version="v1.3.0",
        algorithm="LogisticRegression",
        created_at=datetime.now(),
        training_dataset="tech_dataset_mini_in_memory",
        feature_count=1000,
        label_count=len(label_encoder.classes_),
        checksum=checksum,
        description="Modelo clasificador entrenado con un mini dataset tecnico real.",
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
    print(f"Modelo guardado exitosamente en: models/{saved_id}")

if __name__ == "__main__":
    main()
