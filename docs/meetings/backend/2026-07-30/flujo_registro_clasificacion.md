```
Frontend (React)
│
▼
Spring Boot (ContentController)
POST /contents
│
├── Texto libre:
│     Recibe:
│     • TextContentRequest DTO
│
│     Contiene:
│     - title (opcional)
│     - text (obligatorio)
│     - metadata (opcional)
│
│
├── Archivo:
│     Recibe:
│     • FileContentRequest DTO
│
│     Contiene:
│     - file (obligatorio)
│     - metadata (opcional)
│
▼
ContentService
│
├── Si es archivo:
│     • Guardar archivo en OCI File Storage.
│     • Obtener filePath.
│
├── Crear entidad Content con información inicial:
│
│     Para texto:
│     - title
│     - textContent
│     - contentType = TEXT
│     - createdAt
│
│     Para archivo:
│     - title
│     - fileName
│     - filePath
│     - fileFormat
│     - contentType = FILE
│     - createdAt
│
├──ContentRepository.save()
|    (Persistencia inicial)
│
├── Construir DTO para Ciencia de Datos:
│
│     Texto:
│     • TextClassificationRequest DTO
│
│     Archivo:
│     • FileClassificationRequest DTO
│
├──────────────► DataScienceClient
│                    │
│                    ▼
│              FastAPI (Data Science)
│                    │
│              Clasifica texto o archivo
│                    │
│              Devuelve:
│              • ClassificationResponse DTO
│                    │
│◄───────────────────┘
│
├── Recibir:
│     • ClassificationResponse DTO
│
├── Validar:
│     - status = SUCCESS
│
│
├──  Mapear a:
│     • ContentClassification DTO (Con los datos que nos interesa persistir)
│
├── Completar entidad Content:
│
│     - category
│     - subcategory
│     - confidence
│     - keywords
│     - resume
│
▼
ContentRepository.save(content)
(Actualización del registro)
│
▼
MySQL
│
▼
Construir:
│     • ContentResponse DTO
│
▼
Frontend
```
