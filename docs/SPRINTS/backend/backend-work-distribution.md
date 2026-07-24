# Distribución de tareas Backend - TechMind (MVP)

## 👨‍💻 Desarrollador 1: Rodrigo – Módulo Content (Persistencia)

### Objetivo

Implementar el núcleo del módulo `Content` y la persistencia en base de datos.

### Responsabilidades

#### Modelo de dominio

```text
content/entity/

Content.java
ContentType.java
```

- Definir la entidad `Content`.
- Configurar anotaciones JPA.
- Implementar UUID como identificador.
- Crear el enum `ContentType`.
- Configurar los campos `createdAt` y `updatedAt`.

---

#### Repositorio

```text
content/repository/

ContentRepository.java
```

Responsabilidades:

- Extender `JpaRepository`.
- Implementar consultas básicas.
- Agregar consultas necesarias para búsqueda (si aplica).

---

#### Servicio de persistencia

```text
content/service/

ContentService.java
ContentServiceImpl.java
```

Implementar la lógica para:

- Guardar contenido.
- Obtener contenido por ID.
- Listar contenidos.
- Eliminar contenido.

---

### Entregables

- Entidad `Content`.
- Enum `ContentType`.
- Repositorio JPA.
- Servicio de persistencia.
- CRUD básico funcionando con MySQL.

---

# 👨‍💻 Desarrollador 2: Jose – API Content (DTOs + Validaciones + Consultas)

### Objetivo

Construir la capa de comunicación entre el backend y el frontend.

### Responsabilidades

#### DTOs

```text
content/dto/

ContentRequestDTO
ContentResponseDTO
```

---

#### Mapper

```text
content/mapper/

ContentMapper.java
```

Conversión entre:

```
DTO ↔ Entity
```

---

#### Validaciones

Aplicar Bean Validation.

Ejemplos:

- `@NotBlank` para `title`.
- Validar `contentType`.
- Validar `textContent` cuando el tipo sea `TEXT`.
- Validar `fileName` y `filePath` cuando el tipo sea `FILE`.

---

#### Controller

```text
content/controller/

ContentController.java
```

Implementar endpoints de consulta:

```
GET /contents
GET /contents/{id}
GET /contents/search
DELETE /contents/{id}
```

---

#### Búsquedas

Implementar filtros por:

- category
- subcategory
- keywords
- contentType

---

### Entregables

- DTOs.
- Mapper.
- Validaciones.
- Endpoints de consulta.
- Búsqueda de contenidos.

---

# 👩‍💻 Desarrolladora 3: Giselle – Integración con Data Science + Arquitectura Backend

### Objetivo

Implementar la comunicación con la API de Data Science y coordinar el flujo completo del sistema.

### Responsabilidades

#### Configuración

```text
config/

RestClientConfig.java
CorsConfig.java
OpenApiConfig.java
```

---

#### Integración

```text
integration/

client/
    DataScienceClient.java

dto/
    ClassificationRequest.java
    ClassificationResponse.java
    DataScienceErrorResponse.java
    HealthResponse.java

service/
    DataScienceService.java
```

---

#### Cliente HTTP

Consumir los endpoints de Data Science:

```
POST /predict/text

POST /predict/file
```

---

#### Manejo de errores

Implementar:

```text
exception/

GlobalExceptionHandler.java

DataScienceException.java

ExternalServiceException.java

ResourceNotFoundException.java
```

Mapear correctamente los errores enviados por Data Science.

Ejemplo:

```json
{
  "requestId": "...",
  "status": 422,
  "error": "DOCUMENT_PROCESSING_ERROR",
  "code": "DS-422-001",
  "message": "...",
  "path": "/api/v1/predict/file"
}
```

---

#### Health Check

Preparar el consumo del endpoint de estado del servicio utilizando:

```
HealthResponse.java
```

---

#### Flujo principal del sistema

Implementar el endpoint:

```
POST /contents
```

El flujo será:

```
Frontend
      │
      ▼
POST /contents
      │
      ▼
DataScienceService
      │
      ▼
FastAPI
      │
      ▼
ClassificationResponse
      │
      ▼
Guardar Content
      │
      ▼
Respuesta al Frontend
```

---

### Entregables

- Cliente HTTP.
- Integración con FastAPI.
- DTOs de integración.
- Manejo de errores.
- Health Check.
- Flujo completo de clasificación y almacenamiento.

---

# Tareas compartidas

Estas actividades pueden realizarse entre todos durante la configuración inicial del proyecto.

## Infraestructura

- Configuración inicial de Spring Boot.
- Configuración de MySQL.
- Variables de entorno.
- Dependencias.
- `.gitignore`.

---

## Documentación

- Swagger/OpenAPI.
- README.
- Documentación del contrato con Data Science.

---

# Dependencias entre tareas

```text
Developer 1
(Entity + Repository)
        │
        ▼
Developer 2
(DTO + Controller + Mapper)
        │
        ▼
Developer 3
(Integración con IA)
```

---

# Cronograma sugerido (2 semanas)

## Semana 1

### 👨‍💻 Rodrigo – Persistencia

- Crear la entidad `Content`.
- Crear el enum `ContentType`.
- Configurar JPA para la entidad.
- Crear `ContentRepository`.
- Implementar el servicio de persistencia (`save`, `findById`, `findAll`, `delete`).
- Configurar la conexión con MySQL.
- Realizar pruebas de persistencia.

---

### 👨‍💻 Jose 2 – API Content

- Crear `ContentRequestDTO` y `ContentResponseDTO`.
- Implementar `ContentMapper`.
- Implementar validaciones con Bean Validation.
- Crear `ContentController`.
- Implementar los endpoints:
  - `POST /contents`
  - `GET /contents`
  - `GET /contents/{id}`
  - `GET /contents/search`
  - `DELETE /contents/{id}`

> **Nota:** El endpoint `POST /contents` únicamente recibirá la petición y delegará la lógica al servicio correspondiente.

---

### 👩‍💻 Giselle – Integración con Data Science

- Configurar `RestClient`.
- Crear `DataScienceClient`.
- Crear los DTOs de integración:
  - `ClassificationRequest`
  - `ClassificationResponse`
  - `DataScienceErrorResponse`
  - `HealthResponse`
- Implementar el manejo de excepciones:
  - `GlobalExceptionHandler`
  - `DataScienceException`
  - `ExternalServiceException`
- Preparar la comunicación con FastAPI.

---

## Semana 2

### 👨‍💻 Rodrigo – Persistencia

- Completar el CRUD de persistencia.
- Ajustar consultas necesarias.
- Optimizar la capa de persistencia.
- Realizar pruebas del módulo.
- Corregir incidencias detectadas.

---

### 👨‍💻 Jose – API Content

- Implementar filtros de búsqueda:
  - categoría
  - subcategoría
  - tipo de contenido
  - palabras clave
- Ajustar validaciones.
- Integrar el Controller con la lógica del servicio.
- Realizar pruebas de los endpoints.
- Apoyar las pruebas con Frontend.

---

### 👩‍💻 Giselle – Integración con Data Science

- Implementar la comunicación con FastAPI.
- Procesar la respuesta de clasificación.
- Implementar la orquestación del flujo:

```text
POST /contents
        │
        ▼
Recibir contenido
        │
        ▼
Enviar a Data Science
        │
        ▼
Recibir clasificación
        │
        ▼
Completar Content
        │
        ▼
Guardar en Base de Datos
        │
        ▼
Responder al Frontend
```

- Manejar errores provenientes de Data Science.
- Implementar el consumo del endpoint `Health`.
- Realizar pruebas de integración.

---

## Al finalizar la segunda semana

- ✅ CRUD del módulo `Content` funcionando.
- ✅ API REST del módulo `Content` completa.
- ✅ Integración con la API de Data Science.
- ✅ Clasificación automática de contenido.
- ✅ Almacenamiento de la información clasificada.
- ✅ Endpoints de consulta y búsqueda funcionando.
- ✅ Manejo de errores de integración.
- ✅ Backend listo para integrarse con Frontend y comenzar las pruebas del MVP.
