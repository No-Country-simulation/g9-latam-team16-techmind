# 🚀 TechMind – Organización Inteligente del Conocimiento Técnico

> TechMind es una plataforma inteligente diseñada para organizar, clasificar y facilitar el acceso al conocimiento técnico mediante técnicas de Machine Learning. El proyecto integra un componente Backend y un componente de Ciencia de Datos para construir un sistema escalable, modular y preparado para evolucionar hacia capacidades avanzadas de búsqueda y recomendación de información técnica.

Desarrollado por el equipo **G9 – LATAM Team 16** para el **Hackathon Oracle Next Education (ONE)**.


> Estado del proyecto (Julio 2026)

✅ Sprint DS-06 finalizado

✅ Arquitectura estable

✅ 138 pruebas automatizadas exitosas

🚀 Preparado para iniciar DS-07


# Estado del Proyecto

Versión MVP: 0.2

## Estado General

🟢 Arquitectura estable

🟢 Dataset Maestro construido

🟢 Pipeline de preprocesamiento validado

🟢 Ingeniería de características completada

🟢 Arquitectura de entrenamiento implementada

🟢 138/138 pruebas aprobadas

🟡 Backend en desarrollo

🟡 Frontend en desarrollo

🔵 Próxima etapa: Persistencia del modelo e inferencia

---

| Componente | Estado | Observaciones |
|------------|:------:|---------------|
| Arquitectura | ✅ | Definida y validada |
| Backend | 🚧 | Desarrollo en progreso |
| Data Science | ✅ | Dataset, Feature Engineering y Training completados |
| Frontend | 🚧 | Desarrollo en progreso |
| Integración | ⏳ | Pendiente |
| Infraestructura | ⏳ | Pendiente |
| Despliegue | ⏳ | Pendiente |


# Descripción

TechMind es una plataforma diseñada para centralizar, organizar y clasificar documentación técnica proveniente de diferentes fuentes de información.

El objetivo del proyecto es facilitar el acceso al conocimiento técnico mediante técnicas de Machine Learning, permitiendo clasificar documentos y servir como base para futuras funcionalidades de búsqueda inteligente y asistencia técnica.

La solución está organizada en componentes independientes que facilitan el desarrollo colaborativo, la mantenibilidad y la evolución del sistema.

# Arquitectura General

```mermaid
flowchart LR

    User["Usuario"]

    Backend["Backend"]

    DataScience["Componente Data Science"]

    MachineLearningModel["Modelo de Machine Learning"]

    User --> Backend

    Backend -->|"Solicita predicción"| DataScience

    DataScience --> MachineLearningModel

    MachineLearningModel --> DataScience

    DataScience --> Backend

    Backend --> User
```

El Backend constituye el único punto de acceso al sistema y coordina la comunicación con el componente de Ciencia de Datos, responsable del procesamiento y clasificación de documentos.

# Componentes del Proyecto

## Backend

El componente Backend es responsable de:

- Exponer la API REST.
- Gestionar las solicitudes de los usuarios.
- Validar la información recibida.
- Integrar el componente de Ciencia de Datos.
- Documentar la API mediante Swagger/OpenAPI.

📄 Documentación específica:

- `src/backend/README.md`

---

## Ciencia de Datos

El componente de Ciencia de Datos actualmente implementa un pipeline completo que cubre:

- Construcción del dataset.
- Preprocesamiento de datos.
- Entrenamiento del modelo.
- Evaluación.
- Predicción de categorías.
- Construcción del Dataset Maestro.
- Validación.
- Limpieza.
- Preprocesamiento.
- Ingeniería de Características.
- Entrenamiento del modelo.
- Evaluación del modelo.


📄 Documentación específica:

- `src/data_science/README.md`


## Estado del Componente Data Science

### Completado

- Arquitectura del componente
- Dataset Maestro
- Readers
- Loaders
- Validación del Dataset
- Pipeline de Preprocesamiento
- Ingeniería de Características
- Entrenamiento del Modelo
- Evaluación del Modelo
- Arquitectura desacoplada de Machine Learning
- Suite automatizada de pruebas (138/138)

### En desarrollo

- Persistencia del modelo
- Motor de inferencia
- Integración con Backend


# Estructura del Repositorio

```text
TechMind/
│
├── docs/
│   ├── ADR/
│   ├── Architecture/
│   ├── Roadmap/
│   ├── SDS/
│   └── Standards/
│
├── src/
│   ├── backend/
│   └── data_science/
│
├── tests/
│
├── datasets/
│
├── artifacts/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
└── requirements.txt
```

La estructura detallada del proyecto se encuentra documentada en:

- `docs/Architecture/RepositoryStructure.md`

# Stack Tecnológico

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## Ciencia de Datos

- Pandas
- NumPy
- Scikit-Learn
- Joblib

## DevOps y Herramientas

- Git
- GitHub
- GitHub Projects
- GitHub Actions *(próximamente)*

## Infraestructura

- Oracle Cloud Infrastructure (OCI)

# Instalación

## Clonar el repositorio

```bash
git clone <https://github.com/No-Country-simulation/g9-latam-team16-techmindO>
```

## Ingresar al proyecto

```bash
cd TechMind
```

## Crear un entorno virtual

```bash
python -m venv .venv
```

## Activar el entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

# Testing

Ejecutar todas las pruebas del proyecto:

```bash
python -m pytest
```

Generar el reporte de cobertura:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

## Estado actual

| Métrica | Valor |
|----------|------:|
| Tests automatizados | 138 |
| Cobertura del componente Data Science | En crecimiento  |

> La suite de pruebas valida la arquitectura completa del componente Data Science, incluyendo adquisición de datos, preprocesamiento, ingeniería de características y entrenamiento del modelo.

> La cobertura corresponde al módulo de adquisición de datos del componente de Ciencia de Datos.

# Documentación

La documentación del proyecto está organizada para facilitar la navegación y el mantenimiento.

| Documento | Descripción |
|------------|-------------|
| `README.md` | Visión general del proyecto. |
| `src/backend/README.md` | Documentación del componente Backend. |
| `src/data_science/README.md` | Documentación del componente de Ciencia de Datos. |
| `docs/Architecture/` | Arquitectura del sistema y del repositorio. |
| `docs/SDS/` | Software Design Specification. |
| `docs/ADR/` | Architecture Decision Records. |
| `docs/Roadmap/` | Plan de evolución del proyecto. |
| `docs/Standards/` | Estándares de desarrollo y documentación. |

# Roadmap

## Arquitectura

- ✅ Arquitectura General
- ✅ Diseño Técnico

## Backend

- 🚧 API REST
- 🚧 Integración con Ciencia de Datos
- ⏳ Persistencia
- ⏳ Despliegue

## Ciencia de Datos

| Sprint | Estado |
|---------|--------|
| DS-01 | ✅ Arquitectura |
| DS-02 | ✅ Investigación del Dataset |
| DS-03 | ✅ Construcción del Dataset Maestro |
| DS-04 | ✅ Limpieza y Preprocesamiento |
| DS-05 | ✅ Ingeniería de Características |
| DS-06 | ✅ Entrenamiento del Modelo |
| DS-07 | ⏳ Persistencia del Modelo |
| DS-08 | ⏳ Motor de Inferencia |
| DS-09 | ⏳ Integración Backend |
| DS-10 | ⏳ Optimización |



## Características

- Clasificación automática de documentación técnica.
- Construcción de un Dataset Maestro a partir de múltiples fuentes.
- Pipeline de validación y preprocesamiento.
- Arquitectura modular Backend + Ciencia de Datos.
- Integración mediante una interfaz estable (`predict(title, text)`).
- Documentación técnica basada en SDS y ADR.
- Infraestructura preparada para Oracle Cloud Infrastructure (OCI).
- Validación automática del dataset.
- Pipeline de preprocesamiento.
- Arquitectura basada en DocumentRecord.
- Suite de pruebas automatizadas.
- Readers y Loaders para múltiples formatos (si ya están implementados).
- Arquitectura desacoplada para entrenamiento.
- Pipeline de entrenamiento.
- Evaluación del modelo.
- Strategy Pattern para algoritmos de Machine Learning.
- Dependency Injection en el módulo de entrenamiento.


# Contribución

Las contribuciones al proyecto deberán respetar:

- La arquitectura definida para el sistema.
- Los estándares de desarrollo del equipo.
- La documentación técnica vigente.
- El flujo de trabajo basado en Git y Pull Requests.

Antes de proponer cambios arquitectónicos, estos deberán ser discutidos y aprobados por el equipo.

---

# Estado del Desarrollo

Actualmente el proyecto cuenta con:

- Arquitectura modular basada en Clean Architecture.
- Pipeline completo de adquisición y preparación de datos.
- Pipeline de Ingeniería de Características.
- Arquitectura desacoplada para entrenamiento.
- Evaluación del modelo.
- 138 pruebas unitarias exitosas.
- Cero regresiones entre sprints.

El proyecto se encuentra preparado para iniciar el desarrollo del módulo de persistencia e inferencia del modelo.

---

# Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

Para más información, consultar el archivo `LICENSE`.