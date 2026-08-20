# 🗺️ Roadmap

> **Proyecto:** AyniKortex  
> **Estado:** MVP funcional

El Roadmap de AyniKortex describe la evolución del proyecto desde la definición del MVP hasta las posibles capacidades futuras de la plataforma.

No representa un cronograma de trabajo ni una lista de tareas pendientes. Su propósito es mostrar los principales hitos alcanzados, el estado actual de la solución y las líneas de evolución previstas.

---

# 🎯 Objetivo

Este documento proporciona una visión estratégica de la evolución funcional y técnica de AyniKortex.

Su propósito es:

- Identificar los principales hitos alcanzados.
- Mostrar la evolución de los componentes de la plataforma.
- Establecer las principales líneas de evolución futura.
- Mantener una visión coherente entre arquitectura, implementación y producto.

El Roadmap se actualiza conforme evoluciona la plataforma y se alcanzan nuevos hitos relevantes.

---

# 🌟 Visión

AyniKortex busca facilitar la organización y clasificación inteligente de documentación técnica mediante técnicas de Machine Learning.

La evolución de la plataforma parte de un MVP funcional y contempla mejoras progresivas en:

- Inteligencia Artificial.
- Procesamiento de documentación.
- Integración entre componentes.
- Experiencia de usuario.
- Automatización.
- Infraestructura.
- Escalabilidad.

La evolución futura deberá mantener los principios de modularidad, mantenibilidad y separación de responsabilidades definidos en la arquitectura del sistema.

---

# 📅 Evolución del proyecto

```mermaid
timeline
    title Evolución de AyniKortex

    "Definición del MVP" : "Problema y alcance"
                         : "Arquitectura"
                         : "Diseño de componentes"

    "Construcción" : "Data Science"
                   : "Backend"
                   : "Frontend"
                   : "Base de datos"

    "Integración" : "Frontend ↔ Backend"
                  : "Backend ↔ Data Science"
                  : "Persistencia"
                  : "Validación funcional"

    "Despliegue" : "Contenedorización"
                 : "Oracle Cloud Infrastructure"
                 : "MVP funcional"

    "Evolución futura" : "Optimización"
                      : "Escalabilidad"
                      : "Nuevas capacidades"


---

# 🚀 Estado actual del MVP

AyniKortex cuenta con un **MVP funcional de extremo a extremo**, resultado de la integración progresiva de sus componentes principales.

La solución actual integra:

- Frontend web.
- Backend.
- Servicio de Data Science.
- Modelo de Machine Learning.
- Base de datos.
- Infraestructura en Oracle Cloud Infrastructure (OCI).

## Estado por componente

| Componente | Resultado actual | Estado |
|---|---|:---:|
| 📚 Documentación | Arquitectura, contratos, ADR, estándares y documentación técnica | ✅ |
| 🎨 Frontend | Interfaz web integrada con el Backend | ✅ |
| ⚙️ Backend | API REST, lógica de negocio y persistencia | ✅ |
| 🤖 Data Science | Procesamiento, modelo ML, inferencia y servicio FastAPI | ✅ |
| 🗄️ Base de datos | Persistencia mediante MySQL | ✅ |
| 🔗 Integración | Flujo Frontend → Backend → Data Science | ✅ |
| ☁️ Despliegue | Componentes preparados y desplegados en OCI | ✅ |

## Flujo actual

```mermaid
flowchart LR
    "👤 Usuario" --> "🌐 Frontend"
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo ML"
    "🧠 Modelo ML" --> "📊 Resultado"
    "📊 Resultado" --> "⚙️ Backend"
    "⚙️ Backend" --> "🗄️ MySQL"
    "⚙️ Backend" --> "🌐 Frontend"
    "🌐 Frontend" --> "👤 Usuario"
```

## Capacidades actuales

El MVP permite:

- Recibir contenido técnico para procesamiento.
- Procesar texto y archivos compatibles.
- Ejecutar inferencia mediante el modelo de Machine Learning.
- Generar una clasificación.
- Obtener un nivel de confianza asociado a la predicción.
- Identificar palabras relevantes.
- Generar un resumen del contenido.
- Persistir información mediante el Backend.
- Ejecutar la solución en infraestructura cloud.

La implementación detallada de cada componente se encuentra en la documentación técnica correspondiente.

---

# 🏆 Hitos alcanzados por componente

## 🤖 Data Science

El componente de Data Science evolucionó desde la construcción del dataset hasta la implementación del procesamiento, entrenamiento, evaluación, persistencia e inferencia del modelo de Machine Learning.

Actualmente incluye:

- Construcción y procesamiento del dataset.
- Preprocesamiento del contenido.
- Ingeniería de características.
- Entrenamiento del modelo de clasificación.
- Evaluación mediante métricas.
- Persistencia de artefactos del modelo.
- Motor de inferencia.
- Generación de resultados de predicción.
- Servicio de inferencia mediante FastAPI.
- Pruebas automatizadas del componente.
- Contenedorización para despliegue.

La documentación detallada de la evolución de Data Science se conserva en:

[🤖 Sprints de Data Science](../SPRINTS/data-science/)

---

## ⚙️ Backend

El Backend implementa la lógica de negocio y constituye el punto de integración de la aplicación.

Entre los principales resultados alcanzados se encuentran:

- Implementación de API REST.
- Gestión de las solicitudes de la aplicación.
- Integración con Data Science.
- Persistencia de información mediante MySQL.
- Gestión de entidades y DTOs.
- Validaciones de datos.
- Configuración de CORS.
- Preparación del componente para ejecución mediante contenedor.
- Integración con la infraestructura de despliegue.

La documentación específica de contratos, modelo de datos y API se encuentra en:

[🔗 Documentación de API e integración](../api/)

---

## 🎨 Frontend

El Frontend proporciona la interfaz web para la interacción con la plataforma.

Los principales resultados alcanzados incluyen:

- Implementación de la aplicación con React y Vite.
- Navegación entre las principales vistas.
- Integración con el Backend.
- Consumo de los endpoints de la aplicación.
- Presentación de los resultados al usuario.
- Preparación para despliegue mediante contenedor y Nginx.

---

## 🗄️ Base de datos

La solución incorpora MySQL como mecanismo de persistencia para la información gestionada por el Backend.

La base de datos forma parte del entorno de ejecución de la aplicación y se integra con el Backend mediante la configuración correspondiente.

---

## 🔗 Integración

La integración entre los componentes permitió completar el flujo funcional de la plataforma:

```mermaid
flowchart LR
    "👤 Usuario" --> "🌐 Frontend"
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo ML"
    "🧠 Modelo ML" --> "📊 Clasificación"
    "📊 Clasificación" --> "🤖 Data Science"
    "🤖 Data Science" --> "⚙️ Backend"
    "⚙️ Backend" --> "🗄️ MySQL"
    "⚙️ Backend" --> "🌐 Frontend"
```

Esta integración permite ejecutar el flujo principal de la solución de extremo a extremo.

---

## ☁️ Despliegue

La solución fue preparada para ejecución mediante contenedores y desplegada utilizando Oracle Cloud Infrastructure.

Los principales elementos considerados son:

- Contenedores Docker para los componentes.
- OCI como infraestructura cloud.
- OCI Object Storage para almacenamiento de artefactos.
- Configuración de variables de entorno.
- Automatización mediante GitHub Actions.
- Separación de configuración entre entornos.

La documentación operativa del despliegue se encuentra en:

[☁️ Deployment Guide](../Deployment-Guide/Deployment-Guide.md)

---

# 📈 Evolución del producto

La evolución de AyniKortex se plantea de manera incremental, partiendo del MVP funcional actual y priorizando mejoras que aporten valor al producto sin comprometer la simplicidad de la arquitectura.

## 🌱 Fase 1 — MVP funcional

**Estado: Completada**

Construcción e integración de los componentes fundamentales de la plataforma.

Principales resultados:

- Arquitectura definida.
- Frontend implementado.
- Backend implementado.
- Componente de Data Science implementado.
- Modelo de Machine Learning entrenado.
- Persistencia mediante MySQL.
- Integración entre componentes.
- Contenedorización.
- Despliegue en Oracle Cloud Infrastructure.
- Documentación técnica y arquitectónica.

---

## 🚀 Fase 2 — Optimización y estabilización

**Estado: Evolución futura**

La siguiente etapa se orienta a fortalecer el MVP y mejorar su comportamiento operativo.

Líneas principales:

- Optimización del modelo de Machine Learning.
- Ampliación y mejora del dataset.
- Mejora de métricas de clasificación.
- Optimización del tiempo de inferencia.
- Ampliación de cobertura de pruebas.
- Mejoras de experiencia de usuario.
- Fortalecimiento de validaciones.
- Mejoras de observabilidad.
- Automatización de procesos de despliegue.

---

## 📊 Fase 3 — Escalabilidad

**Estado: Evolución futura**

Una vez estabilizada la solución, podrán incorporarse capacidades orientadas a soportar un mayor volumen de información y usuarios.

Entre ellas:

- Optimización de recursos.
- Escalabilidad de los componentes.
- Automatización de procesos.
- Mejoras de infraestructura.
- Monitoreo y observabilidad avanzada.
- Gestión más robusta de artefactos y modelos.
- Optimización del procesamiento de documentos.

---

## 🌟 Fase 4 — Evolución avanzada

**Estado: Visión futura**

AyniKortex podrá evolucionar hacia una plataforma más amplia para la gestión inteligente del conocimiento técnico.

Las posibles líneas de evolución incluyen:

- Nuevos modelos de clasificación.
- Nuevas técnicas de procesamiento de lenguaje.
- Análisis y explotación avanzada del conocimiento.
- Nuevas capacidades de búsqueda y recomendación.
- Integraciones con fuentes externas de documentación.
- Capacidades avanzadas de Inteligencia Artificial.
- Nuevos servicios y funcionalidades orientados a la gestión del conocimiento.

Cualquier evolución que implique cambios significativos en la arquitectura deberá evaluarse mediante las decisiones arquitectónicas correspondientes.

---

# 🔮 Capacidades futuras

Las siguientes capacidades representan líneas potenciales de evolución de AyniKortex. Su incorporación dependerá de las necesidades del producto, los resultados obtenidos y la evaluación técnica correspondiente.

| Área | Posibles capacidades |
|---|---|
| 🤖 Inteligencia Artificial | Nuevos modelos de clasificación y mejora continua del modelo |
| 📚 Documentación | Mayor variedad de formatos y fuentes de documentación |
| 📊 Analítica | Métricas, indicadores y visualización del conocimiento procesado |
| ⚙️ Backend | Nuevos servicios, funcionalidades y capacidades de integración |
| 🎨 Frontend | Mejoras de experiencia de usuario y nuevas interfaces |
| ☁️ Infraestructura | Mayor automatización, observabilidad y escalabilidad |
| 🔗 Integraciones | Conexión con nuevas fuentes y sistemas externos |
| 🧠 Conocimiento | Nuevas capacidades para búsqueda, recomendación y organización |

---

# 🧭 Criterios para la evolución

Las futuras capacidades deberán evaluarse considerando:

- Valor funcional para los usuarios.
- Viabilidad técnica.
- Impacto sobre la arquitectura existente.
- Complejidad operativa.
- Costos de infraestructura.
- Seguridad.
- Mantenibilidad.
- Escalabilidad.

Las modificaciones que impliquen cambios significativos en la arquitectura deberán documentarse mediante los mecanismos establecidos en los Architecture Decision Records (ADR).

---

# 📚 Relación con la documentación del proyecto

El Roadmap mantiene una relación directa con los principales documentos técnicos del proyecto:

```mermaid
flowchart LR
    "🗺️ Roadmap" --> "📘 SDS"
    "🗺️ Roadmap" --> "🏗️ Arquitectura"
    "🗺️ Roadmap" --> "📚 ADR"
    "🗺️ Roadmap" --> "🤖 Data Science"
    "🗺️ Roadmap" --> "🔗 API"
    "🗺️ Roadmap" --> "☁️ Deployment"

Cada documento cumple una función diferente:

SDS: describe el diseño general del sistema.
Architecture: desarrolla la arquitectura con mayor detalle.
ADR: registra las decisiones arquitectónicas.
Data Science: documenta el componente de Ciencia de Datos.
API: define los contratos de integración.
Deployment: documenta el despliegue y la infraestructura.

El Roadmap no sustituye estos documentos ni duplica su contenido.

---

🌟 Estado del Roadmap

Estado: Vigente

El MVP funcional de AyniKortex constituye la primera etapa completada de la evolución del producto.

Las fases posteriores representan líneas de evolución y no compromisos de implementación.

El Roadmap será actualizado cuando se produzcan cambios relevantes en el producto, la arquitectura o las capacidades de la plataforma.

---


