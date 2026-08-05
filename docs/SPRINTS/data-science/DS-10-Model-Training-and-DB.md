# Sprint DS-10: Entrenamiento Definitivo del Modelo y Despliegue de Base de Datos Local (MySQL)

## Objetivo del Sprint
1. Entrenar el modelo de Machine Learning definitivo utilizando el dataset óptimo identificado en el Sprint DS-09 (10,000 registros).
2. Persistir el modelo en disco (`.joblib`) siguiendo la arquitectura definida en DS-07 utilizando `FilesystemArtifactRepository`.
3. Proveer una infraestructura de Base de Datos relacional (MySQL) contenerizada con Docker para habilitar el desarrollo y pruebas locales del equipo de Backend.

## 1. Entrenamiento y Persistencia del Modelo (Data Science)

Se completó el entrenamiento del modelo MVP final de clasificación de contenido técnico. 
- **Dataset:** 10K registros (Pruebas de estrés superadas).
- **Algoritmo:** `LogisticRegression (SAGA)` + `TfidfVectorizer (unigramas y bigramas)`.
- **Artefactos:** Se utilizó el módulo de persistencia local para serializar y guardar los componentes requeridos por el Backend.

### Estructura de Artefactos Generados
Los binarios fueron almacenados en el directorio `/models` bajo un identificador versionado:
- `models/aynikortex_classifier-v1.0.0/model.joblib`: Modelo clasificador entrenado (~640 KB).
- `models/aynikortex_classifier-v1.0.0/vectorizer.joblib`: Vectorizador TF-IDF (~414 KB).
- `models/aynikortex_classifier-v1.0.0/label_encoder.joblib`: Mapeo de categorías.
- `models/aynikortex_classifier-v1.0.0/metadata.json`: Archivo de trazabilidad con versión, hiperparámetros y checksum criptográfico.

> **CLI de Pruebas:** Se creó el script interactivo `scripts/test_model_cli.py` para realizar inferencias manuales directamente en la terminal. Carga los artefactos desde `/models` y devuelve predicciones con porcentaje de confianza.

## 2. Infraestructura de Base de Datos Local (Backend)

Con base en la arquitectura definida por el equipo de Backend (uso de JPA, Spring Data, y migraciones Flyway), se habilitó el entorno de desarrollo local.
- **Docker Compose:** Se integró un archivo `docker-compose.yml` en la raíz del proyecto.
- **Motor:** MySQL 8.0.
- **Propósito:** Proveer a los desarrolladores backend de una instancia de base de datos inmediata que coincida con las necesidades de las migraciones SQL existentes en `src/backend/src/main/resources/db_migration/`.

### Credenciales de Acceso
El contenedor inicializa automáticamente la siguiente configuración, la cual debe ser mapeada en el archivo `application.properties` de Spring Boot:
- **URL (JDBC):** `jdbc:mysql://localhost:3306/aynikortex_db`
- **Usuario:** `ayni_user`
- **Contraseña:** `ayni_password`

## Siguientes Pasos
- Conexión real desde `DataScienceIntegrationService` (Java) hacia el modelo serializado.
- Despliegue de los artefactos `.joblib` en OCI Object Storage.
- Migración de la base de datos MySQL local hacia MySQL HeatWave Database Service en Oracle Cloud (OCI).
