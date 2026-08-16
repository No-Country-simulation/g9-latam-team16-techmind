# 🚀 AyniKortex

### Organización Inteligente del Conocimiento Técnico

> **AyniKortex utiliza Inteligencia Artificial para analizar y clasificar documentación técnica, ayudando a transformar información dispersa en conocimiento organizado.**

---

## 🎯 ¿Qué es AyniKortex?

AyniKortex es una plataforma orientada a la **organización y clasificación de documentación técnica**.

La solución permite ingresar texto o documentos y analizar su contenido para obtener una clasificación automática basada en patrones aprendidos por un modelo de **Machine Learning (aprendizaje automático)**.

El proyecto busca reducir el esfuerzo manual asociado a la organización de grandes volúmenes de documentación y facilitar la gestión del conocimiento técnico dentro de los equipos.

---

## 💡 El problema

Los equipos tecnológicos generan continuamente documentación: especificaciones, decisiones de arquitectura, manuales, guías, reportes y otros contenidos técnicos.

Cuando esta información crece y se encuentra distribuida en diferentes fuentes, resulta más difícil:

- 🔎 Encontrar información relevante.
- 🗂️ Mantener la documentación organizada.
- 🏷️ Clasificar nuevos contenidos.
- 🔄 Reutilizar conocimiento existente.
- 🤝 Facilitar la transferencia de conocimiento entre equipos.

**AyniKortex aborda este problema mediante el análisis y clasificación automática del contenido.**

---

## ⚙️ ¿Cómo funciona?

El funcionamiento general de AyniKortex puede resumirse en el siguiente flujo:

```mermaid
flowchart LR
    "👤 Usuario" --> "📄 Ingreso de información"
    "📄 Ingreso de información" --> "🌐 Plataforma Web"
    "🌐 Plataforma Web" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Servicio de Data Science"
    "🤖 Servicio de Data Science" --> "🧠 Modelo de Machine Learning"
    "🧠 Modelo de Machine Learning" --> "🏷️ Clasificación automática"
    "🏷️ Clasificación automática" --> "📋 Resultado"
    "📋 Resultado" --> "🌐 Plataforma Web"
```

En términos simples:

1. El usuario proporciona texto o un documento.
2. La plataforma recibe y procesa la información.
3. El Backend coordina la solicitud.
4. Data Science analiza el contenido.
5. El modelo de Machine Learning determina la clasificación.
6. La plataforma presenta el resultado al usuario.

El resultado puede incluir la clasificación, nivel de confianza, palabras clave, resumen del contenido, versión del modelo y tiempo de procesamiento.

---

## 🏗️ Arquitectura

AyniKortex está compuesto por varios componentes especializados que trabajan de forma integrada:

```mermaid
flowchart LR
    "👤 Usuario" --> "🌐 Frontend"
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo de Machine Learning"
    "🧠 Modelo de Machine Learning" --> "🤖 Data Science"
    "🤖 Data Science" --> "⚙️ Backend"
    "⚙️ Backend" --> "🗄️ MySQL"
    "⚙️ Backend" --> "🌐 Frontend"
```

### 🌐 Frontend

Es la interfaz web mediante la cual el usuario interactúa con la plataforma.

**Tecnologías principales:**

- React
- Vite
- Nginx

### ⚙️ Backend

Gestiona la lógica de negocio, las solicitudes de la aplicación, la persistencia y la comunicación con Data Science.

**Tecnologías principales:**

- Java
- Spring Boot

### 🤖 Data Science

Procesa el contenido recibido y proporciona el servicio de inferencia del modelo.

**Tecnologías principales:**

- Python
- FastAPI
- scikit-learn
- pandas

### 🧠 Modelo de Machine Learning

El modelo analiza el contenido recibido y genera la clasificación correspondiente.

La documentación relacionada con el desarrollo, entrenamiento, evaluación, persistencia e integración del modelo se encuentra en:

👉 [Documentación de Data Science](docs/SPRINTS/data-science/)

### 🗄️ Base de Datos

MySQL se utiliza para la persistencia de la información gestionada por el Backend.

---

## 📊 Clasificación inteligente

AyniKortex utiliza **Machine Learning (aprendizaje automático)** para identificar patrones en la documentación.

El modelo genera una clasificación que puede incluir:

- **Categoría**
- **Subcategoría**
- **Nivel de confianza**
- **Palabras clave**
- **Resumen del contenido**
- **Versión del modelo**
- **Tiempo de procesamiento**

La solución permite analizar contenido textual y archivos compatibles con el servicio de Data Science.

La especificación de la API y los contratos de integración se encuentran en:

👉 [Documentación de API](docs/api/README.md)

👉 [Especificación OpenAPI](docs/api/aynikortex-api.yaml)

---

## 🧩 Componentes de la solución

| Componente | Responsabilidad |
|---|---|
| 🌐 **Frontend** | Interfaz de interacción con el usuario |
| ⚙️ **Backend** | Lógica de negocio e integración |
| 🤖 **Data Science** | Procesamiento e inferencia |
| 🧠 **Machine Learning** | Clasificación automática |
| 🗄️ **MySQL** | Persistencia de información |
| ☁️ **OCI** | Infraestructura para el despliegue |

---

## 🛠️ Tecnologías

| Área | Tecnologías |
|---|---|
| **Frontend** | React, Vite, Nginx |
| **Backend** | Java, Spring Boot |
| **Data Science** | Python, FastAPI, scikit-learn, pandas |
| **Base de datos** | MySQL |
| **Contenedores** | Docker, Docker Compose |
| **Cloud** | Oracle Cloud Infrastructure (OCI) |
| **Versionamiento** | Git, GitHub |
| **Automatización** | GitHub Actions |

---

## ☁️ Despliegue

AyniKortex cuenta con un **MVP funcional desplegado en Oracle Cloud Infrastructure (OCI)**.

La integración de los componentes principales puede representarse de la siguiente manera:

```mermaid
flowchart LR
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "⚙️ Backend" --> "🗄️ MySQL"
    "🤖 Data Science" --> "🧠 Modelo de Machine Learning"
```

La documentación detallada del proceso de despliegue se encuentra en:

👉 [Guía de despliegue](docs/Deployment-Guide/Deployment-Guide.md)

---

## 🐳 Ejecución local

El proyecto incluye configuración para ejecutar los principales servicios mediante Docker Compose.

```bash
docker compose up --build
```

La configuración se encuentra en:

👉 [docker-compose.yml](docker-compose.yml)

Para conocer los requisitos y procedimientos específicos de cada componente, consultar la documentación correspondiente.

---

## 📁 Estructura del repositorio

```text
aynikortex/
│
├── datasets/              # Datos utilizados durante el desarrollo
├── docs/                  # Documentación del proyecto
├── models/                # Modelos y artefactos de Machine Learning
├── scripts/               # Scripts y utilidades
├── tests/                 # Pruebas automatizadas
│
├── src/
│   ├── backend/           # Backend Spring Boot
│   ├── data_science/      # Componente de Ciencia de Datos
│   └── frontend/          # Aplicación web
│
├── .github/
│   └── workflows/         # Automatizaciones
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📚 Documentación

Este README proporciona una visión general del proyecto.

La documentación detallada se encuentra organizada por áreas:

### 🏗️ Arquitectura

- [Arquitectura de la solución](docs/Architecture/Architecture.md)
- [Pipeline de Data Science](docs/Architecture/DataScience-Pipeline.md)
- [Estructura del repositorio](docs/Architecture/Repository-Structure.md)

### 🔌 API e integración

- [Documentación de API](docs/api/README.md)
- [Contrato Backend–Data Science](docs/api/Backend-Data-Contract.md)
- [Modelo de datos](docs/api/Backend-Data-Model.md)
- [Especificación OpenAPI](docs/api/aynikortex-api.yaml)

### ☁️ Despliegue

- [Guía de despliegue](docs/Deployment-Guide/Deployment-Guide.md)

### 🤖 Ciencia de Datos

- [Documentación de Sprints de Data Science](docs/SPRINTS/data-science/)

### 📋 Decisiones y diseño

- [Architecture Decision Records (ADR)](docs/ADR/)
- [SDS — Software Design Specification](docs/SDS/SDS.md)
- [Roadmap técnico](docs/ROADMAP/Technical-Roadmap.md)

### 📐 Estándares

- [Engineering Standards](docs/Standards/Engineering-Standards.md)
- [Flujo de desarrollo Git](docs/Standards/git-development-workflow.md)

La documentación de reuniones y seguimiento del proyecto se encuentra disponible en [`docs/meetings/`](docs/meetings/).

---

## 🚀 Estado del proyecto

### MVP funcional

AyniKortex cuenta actualmente con:

- ✅ Plataforma web funcional.
- ✅ Backend integrado.
- ✅ Servicio de Data Science.
- ✅ Modelo de Machine Learning entrenado y versionado.
- ✅ Clasificación automática.
- ✅ Procesamiento de texto y documentos.
- ✅ Persistencia mediante MySQL.
- ✅ Integración entre los componentes.
- ✅ Contenedores Docker.
- ✅ Despliegue en OCI.

El proyecto queda preparado como base para continuar evolucionando las capacidades de organización, clasificación y gestión del conocimiento técnico.

---

## 👥 Equipo

AyniKortex fue desarrollado de manera colaborativa por **No Country – G9 LATAM Team 16**, integrando trabajo en las áreas de:

- Desarrollo Frontend
- Desarrollo Backend
- Ciencia de Datos e Inteligencia Artificial
- Arquitectura
- Integración y despliegue
- Documentación

---

## 🔗 Repositorio

**Repositorio oficial de AyniKortex:**

👉 [AyniKortex en GitHub](https://github.com/No-Country-simulation/aynikortex)

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

Consultar [LICENSE.md](LICENSE.md) para más información.

