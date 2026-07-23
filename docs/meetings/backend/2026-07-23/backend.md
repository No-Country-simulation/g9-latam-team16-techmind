# Propuesta de Arquitectura Backend (MVP)

> **Estado:** Borrador – Pendiente de validación por el equipo Backend.
>
> Este documento propone la arquitectura inicial del backend para el MVP de TechMind.
> Su objetivo es establecer una base común antes de comenzar el desarrollo para evitar retrabajos y facilitar la integración con el equipo de Ciencia de Datos.

---

# 1. Alcance del MVP

El backend soportará las siguientes funcionalidades:

- Gestión de usuarios.
- Registro de contenido.
- Clasificación automática mediante el servicio de Ciencia de Datos.
- Consulta de contenidos.
- Búsqueda por categoría y palabras clave.
- Simulación de roles (ADMIN / USER).

## Fuera del alcance del MVP

Las siguientes funcionalidades podrán implementarse en una versión futura:

- Autenticación.
- Spring Security.
- JWT.
- Recuperación de contraseña.
- Control de permisos basado en autenticación.

---

# 2. Modelo del Dominio

Para mantener el MVP simple se propone persistir únicamente dos entidades:

- User
- Content

La clasificación realizada por el modelo de Machine Learning **no se considera una entidad del dominio**, sino información proveniente de un servicio externo.

---

## Relación entre entidades

```text
User (1)
   │
   │
   └───────────────< Content (N)
```

Un usuario puede registrar múltiples contenidos.

Cada contenido pertenece a un único usuario.

---

# 3. Modelo de Persistencia

## Entidad User

| Campo     | Tipo Java     | Tipo MySQL           | Restricciones                            |
| --------- | ------------- | -------------------- | ---------------------------------------- |
| id        | UUID          | CHAR(36)             | PK                                       |
| name      | String        | VARCHAR(100)         | NOT NULL                                 |
| email     | String        | VARCHAR(150)         | UNIQUE, NOT NULL                         |
| password  | String        | VARCHAR(255)         | NULL _(hasta implementar autenticación)_ |
| role      | Enum<Role>    | ENUM('ADMIN','USER') | NOT NULL                                 |
| createdAt | LocalDateTime | TIMESTAMP            | NOT NULL                                 |

### Relaciones

- Un **User** puede tener múltiples **Content**.

---

## Entidad Content

| Campo        | Tipo Java         | Tipo MySQL          | Restricciones                                    |
| ------------ | ----------------- | ------------------- | ------------------------------------------------ |
| id           | UUID              | CHAR(36)            | PK                                               |
| title        | String            | VARCHAR(200)        | NOT NULL                                         |
| description  | String            | VARCHAR(1000)       | NULL                                             |
| contentType  | Enum<ContentType> | ENUM('TEXT','FILE') | NOT NULL                                         |
| textContent  | String            | LONGTEXT            | NULL _(Contenido cuando es texto libre)_         |
| fileName     | String            | VARCHAR(255)        | NULL _(Nombre original del archivo)_             |
| filePath     | String            | VARCHAR(500)        | NULL _(Ruta o URL donde se almacena el archivo)_ |
| category     | String            | VARCHAR(100)        | NULL _(Generada por Modelo IA)_                  |
| subcategory  | String            | VARCHAR(100)        | NULL _(Generada por Modelo IA)_                  |
| confidence   | BigDecimal        | DECIMAL(4,3)        | NULL                                             |
| modelVersion | String            | VARCHAR(20)         | NULL                                             |
| keywords     | JSON              | JSON                | NULL _(Palabras clave generadas por Modelo IA)_  |
| createdAt    | LocalDateTime     | TIMESTAMP           | NOT NULL                                         |
| updatedAt    | LocalDateTime     | TIMESTAMP           | NOT NULL                                         |
| user_id      | UUID              | CHAR(36)            | FK → users(id), NOT NULL                         |

### Relaciones

Cada **Content** pertenece a un único **User**.

---

# 4. Enumeraciones

## Role

```java
public enum Role {

    ADMIN,

    USER

}
```

---

## ContentType

```java
public enum ContentType {

    TEXT,

    FILE

}

}
```

---

# 5. Integración con Ciencia de Datos

El equipo de Ciencia de Datos será responsable de desarrollar y mantener la API REST en FastAPI.

Backend **únicamente consumirá dicha API**, sin conocer la implementación interna del modelo de Machine Learning.

---

## Flujo de integración

```text
Frontend
    │
    ▼
Backend (Spring Boot)
    │
    ▼
DataScienceClient
    │
    │ HTTP
    ▼
API FastAPI (Data Science)
    │
    ▼
ClassificationResponse
    │
    ▼
Mapeo a Content
    │
    ▼
Base de Datos
```

---

# 6. Modelos de Integración

Los siguientes modelos **NO serán entidades de base de datos**.

Se utilizarán únicamente para comunicarse con la API de Ciencia de Datos.

```text
integration/
│
├── client/
│      DataScienceClient
│
├── dto/
│      FileClassificationRequest
│      TextClassificationRequest
│      ClassificationResponse
│      Classification
│      Keyword
│      Metadata
│      ErrorResponse
│      HealthResponse
│
└── service/
```

---

# 7. ¿Por qué Classification NO es una entidad?

La API de Ciencia de Datos responde con un objeto como el siguiente:

```json
{
  "classification": {
    "category": "...",
    "subcategory": "...",
    "confidence": 0.97,
    "keywords": []
  }
}
```

Este objeto forma parte del **contrato de integración** entre Backend y Ciencia de Datos.

No representa una entidad propia del dominio de TechMind.

Por ello, el backend únicamente utilizará esta respuesta para actualizar la entidad **Content**.

El proceso será el siguiente:

```text
ClassificationResponse

↓

category

↓

Content.category

------------------------

subcategory

↓

Content.subcategory

------------------------

confidence

↓

Content.confidence

------------------------

keywords

↓

Content.keywords

------------------------

modelVersion

↓

Content.modelVersion
```

Una vez realizado el mapeo, el objeto `ClassificationResponse` deja de utilizarse y no se almacena en la base de datos.

---

# 8. Organización del Proyecto

Se propone organizar el backend por módulos (feature-based).

```text
src/main/java/com/techmind/backend

config/

exception/

integration/
│
├── client/
├── dto/
└── service/

user/
│
├── controller/
├── dto/
├── entity/
├── mapper/
├── repository/
└── service/

content/
│
├── controller/
├── dto/
├── entity/
├── mapper/
├── repository/
└── service/
```

Esta estructura permite que cada módulo tenga encapsulada toda su funcionalidad.

---

# 9. Responsabilidad de cada capa

## Controller

Responsabilidades:

- Recibir solicitudes HTTP.
- Validar parámetros de entrada.
- Invocar al Service.
- Retornar DTOs de respuesta.

No debe contener lógica de negocio.

---

## Service

Responsabilidades:

- Implementar la lógica de negocio.
- Coordinar llamadas a repositorios.
- Consumir servicios externos.
- Aplicar reglas de negocio.

---

## Repository

Responsabilidades:

- Acceso a la base de datos mediante Spring Data JPA.

---

## Entity

Responsabilidades:

- Representar el modelo persistente de la base de datos.

---

## DTO

Responsabilidades:

- Representar los objetos de entrada y salida de la API del Backend.

---

## Mapper

Responsabilidades:

- Convertir entre DTOs y Entities.

---

## Integration

Responsabilidades:

- Consumir la API REST del equipo de Ciencia de Datos.
- Mapear los modelos de integración hacia el dominio del backend.

---

# 10. Simulación de Roles

Para el MVP se propone simular los roles.

Roles disponibles:

- ADMIN
- USER

En esta versión:

- No habrá Login.
- No habrá JWT.
- No habrá Spring Security.

El Frontend simulará el rol seleccionado para efectos de demostración.

La implementación de autenticación podrá incorporarse posteriormente sin modificar las entidades principales.

---

# 11. Propuesta de Distribución de Backend

## Developer 1

### Módulo User + Consultas de Content

Responsable de:

### User

- Entity
- DTOs
- Repository
- Service
- Controller
- Mapper
- Validaciones
- Documentación Swagger de los endpoints del módulo

### Consultas de Content

Responsable de:

- GET /contents
- GET /contents/{id}
- Búsqueda por categoría
- Búsqueda por keywords
- Búsqueda por usuario
- Paginación
- Filtros

---

## Developer 2

### Módulo Content (CRUD)

Responsable de:

- Entity
- DTOs
- Repository
- Service
- Controller
- Mapper

Funcionalidades:

- POST /contents
- PUT /contents/{id}
- DELETE /contents/{id}
- Validaciones del módulo Content
- Manejo de excepciones del módulo
- Documentación Swagger de los endpoints del módulo

---

## Developer 3 (Arquitectura e Integración)

### Configuración base del proyecto

Responsable de:

- Creación inicial del proyecto Spring Boot
- Estructura general del backend
- Configuración de JPA / Hibernate
- Dependencias principales
- Variables de entorno
- Convenciones del proyecto
- Revisión de integración entre módulos

### Integración con Ciencia de Datos

Responsable de:

- Definir el contrato de comunicación con Data Science
- DataScienceClient
- Consumo de la API externa
- DTOs de integración
- Mapeo de la respuesta del modelo
- Integración con el módulo Content para almacenar la clasificación
- Manejo de errores de comunicación con el servicio de Data Science

### Frontend React

Responsable de:

- Creación del proyecto frontend
- Diseño de las vistas principales
- Integración con la API Backend
- Consumo de endpoints

# 12. Decisiones pendientes

Antes de comenzar el desarrollo deberán validarse los siguientes puntos:

- Catálogo definitivo de `SourceType`.
- Estrategia para almacenar `keywords` (JSON o Converter).
- Validaciones de cada endpoint.
- Contrato definitivo entre Frontend y Backend.
- Definición de las respuestas de la API del Backend.

---

# 13. Principio de Diseño

> **Separar el dominio del negocio de la capa de integración.**

Esto implica que:

- Las **Entities** representan únicamente la información persistida por TechMind.
- Los **DTOs** representan la comunicación entre componentes.
- El Backend es responsable de traducir la información recibida desde la API de Ciencia de Datos hacia su propio modelo de dominio.

De esta forma, cualquier cambio futuro en la API de Ciencia de Datos tendrá un impacto mínimo sobre el resto del sistema.
