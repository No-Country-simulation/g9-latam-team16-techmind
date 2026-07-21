# **Propuesta de desarrollo: `AyniKortex`**

## Visión General del Proyecto

AyniKortex es una solución diseñada para la organización inteligente del conocimiento técnico. Su propósito principal es recibir textos técnicos (como descripciones de artículos, documentación, notas de estudio o tutoriales) y aprovechar modelos de Ciencia de Datos para automatizar su clasificación temática, extracción de palabras clave y estructuración en una base de conocimiento reutilizable.

## Arquitectura de la Solución: Diagrama General de Componentes y Flujo

```
 ┌─────────────┐
 │   Usuario   │
 └──────┬──────┘
        │ 1. Ingresa contenido (Título y Texto)
        ▼
 ┌─────────────┐
 │  Frontend   │
 │   (React)   │
 └──────┬──────┘
        │ 2. HTTP POST /content (JSON Payload)
        ▼
 ┌────────────────────────────────────────────────────────┐
 │            Backend Principal (Java / Spring Boot)      │
 │  - Recibe y valida DTOs de entrada                     │
 │  - Gestiona transacciones de base de datos             │
 └──────┬──────────────────────────────────────────┬──────┘
        │                                          │
        │ 3. HTTP POST (Envía texto a procesar)    │ 5. Guarda o consulta
        ▼                                          ▼
 ┌──────────────┐                          ┌──────────────┐
 │   FastAPI    │                          │     MySQL    │
 │   (Python)   │                          │   Database   │
 └──────┬───────┘                          └──────┬───────┘
        │                                         │
        │ 4. HTTP Response (JSON IA:              │ 6. Confirma
        │    Categoría, Probabilidad, Tags) │    persistencia
        ▼                                         ▼
 ┌────────────────────────────────────────────────────────┐
 │            Backend Principal (Java / Spring Boot)      │
 │  - Enriquece datos y construye la respuesta final      │
 └──────────────────────┬─────────────────────────────────┘
                        │
                        │ 7. HTTP Response (JSON Final consolidado)
                        ▼
                 ┌─────────────┐
                 │  Frontend   │
                 │   (React)   │
                 └──────┬──────┘
                        │
                        │ 8. Renderiza resultados visuales al usuario
                        ▼
                 ┌─────────────┐
                 │   Usuario   │
                 └─────────────┘

```

### Diagrama simplificado

```
          React

POST /api/contents
        │
        ▼
   Spring Boot
        │
        │ POST /analyze
        ▼
     FastAPI
        │
   Modelo IA
        │
        ▼
 JSON resultado
        │
        ▼
 Spring Boot
        │
 Guarda en BD
        │
        ▼
 Devuelve respuesta
        │
        ▼
      React
```

### Flujo detallado de Operación

1.  **Petición Inicial**: El usuario interactúa con la interfaz de React, escribe el título y el texto técnico del artículo/curso y hace clic en enviar.

2.  **Entrada al Backend Core**: El Backend en Java (Spring Boot) recibe una petición HTTP POST hacia su endpoint `/content` (o el endpoint que definamos). Spring Boot valida automáticamente que los campos no estén vacíos y que cumplan con la estructura del DTO.

3.  **Delegación a la IA**: Como Java por sí mismo no ejecuta modelos de Machine Learning entrenados en archivos .pkl o .joblib de forma nativa tan limpia como Python, Spring Boot empaqueta el texto recibido y hace una petición HTTP interna (usando RestClient o WebClient) hacia el microservicio de `FastAPI (Python)`.

4.  **Procesamiento Analítico y Retorno parcial**: FastAPI recibe el texto, lo pasa por su modelo de Scikit-Learn (TF-IDF, clasificación, etc.) y regresa una respuesta estructurada en JSON a Java con campos como: categoria, probabilidad, informacion_adicional (palabras clave), etc.

5.  **Persistencia**: El backend de Java toma ese resultado devuelto por FastAPI y, utilizando Spring Data JPA, lo almacena en MySQL para cumplir con la creación de la base de conocimiento reutilizable.

6.  **Construcción de la Respuesta Final**: El backend de Java toma el control absoluto, unifica la respuesta de la IA (y opcionalmente le inyecta metadatos de base de datos como ID o fecha de registro).

7.  **Respuesta al Cliente**: Spring Boot serializa todo en un objeto JSON limpio y se lo devuelve al Frontend cerrando el ciclo HTTP.

8.  **Renderizado**: React recibe el JSON y pinta las tarjetas con la categoría detectada y las palabras clave para que el usuario las visualice de forma intuitiva.

## Responsabilidades

### `Frontend (React)`

Se encarga únicamente de:

- Mostrar pantallas
- Enviar formularios
- Mostrar resultados
- Consumir la API Java

<ins> Nota: El Frontend nunca se comunica directamente con FastAPI. </ins>

### `Backend (Spring Boot)`

Es el cerebro de la aplicación. Debe encargarse de:

- Exponer la API REST principal del sistema.
- Gestionar operaciones CRUD y transacciones de base de datos.
- Aplicar validaciones estrictas de DTOs.
- Autenticación (si se llega a agregar)
- Persistencia
- Comunicación con FastAPI: Gestionar la comunicación HTTP con el servicio de FastAPI.
- Manejo de errores
- Devolver respuestas al frontend

### `Ciencia de Datos`

Se encarga de:

- Dataset
- Entrenamiento
- Evaluación
- Modelo
- Inferencia

## Estructura de carpetas

```
src/

frontend/ <-- React

backend/ <-- Spring Boot

data_science/ <-- Modelo + FastAPI
```

Se propone estructurar y alojar la API de FastAPI dentro del directorio **data_science/** porque su responsabilidad principal y única es servir como el puente de exposición del modelo de Machine Learning. Aunque técnicamente utiliza un framework web, este componente pertenece de manera natural al dominio de Ciencia de Datos y no al backend principal en Spring Boot. Su propósito en esta arquitectura no es manejar la lógica de negocio ni la base de datos de la aplicación (de eso se encarga Java), sino actuar como un conector rápido que envuelve el modelo de Machine Learning creado por el equipo de datos para facilitar su consumo en formato JSON.
