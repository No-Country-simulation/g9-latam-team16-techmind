# 📋 Project Master Roadmap

> **Proyecto:** AyniKortex  
> **Versión:** 1.0  
> **Estado:** En ejecución

---

# 🎯 Objetivo

El **Project Master Roadmap** proporciona una visión integral del estado del proyecto AyniKortex.

A diferencia del **Technical Roadmap**, este documento no describe la evolución funcional del producto, sino el avance de su implementación, permitiendo conocer el estado actual de cada equipo, las dependencias entre componentes y los próximos hitos necesarios para completar el MVP.

Este documento servirá como referencia principal para el seguimiento del proyecto durante el Hackathon.

---

# 📊 Estado General del Proyecto

**Estado del MVP**

```
███████████████████░░░░░░░░░░

70 %
```

> El porcentaje representa el avance general del MVP y será actualizado al finalizar cada Sprint o hito importante.

---

# 📈 Dashboard Ejecutivo

| Área | Estado | Responsable | Avance |
|------|:------:|-------------|:------:|
| 📄 Documentación | ✅ | Equipo | 95 % |
| 🤖 Data Science | ✅ | DS | 100 % |
| ⚙️ Backend | 🟡 | Backend | 60 %* |
| 🎨 Frontend | ⚪ | Frontend | 15 %* |
| 🔗 Integración | ⚪ | Equipo | 20 %* |
| 🧪 QA | ⚪ | Equipo | 0 % |
| ☁️ Deploy | ⚪ | DevOps | 0 % |

> (*) Avance estimado. Se actualizará conforme cada equipo reporte su progreso.

---

# 🗺️ Roadmap del MVP

```text
Preparación
      │
      ▼
Data Science
      │
      ▼
Backend
      │
      ▼
Frontend
      │
      ▼
Integración
      │
      ▼
Optimización y Hardening
      │
      ▼
Despliegue
      │
      ▼
Entrega Final
```

---

# 🚀 Estado por Equipos

## 🤖 Data Science

### Estado

✅ Alcance principal del MVP completado.

### Entregables

- Arquitectura del componente
- Dataset Maestro
- Preprocesamiento
- EDA
- Entrenamiento del modelo
- Evaluación
- Persistencia del modelo
- Integración mediante `predict(title, text)`
- Documentación técnica

### Próximas actividades

- Benchmark Experimental
- Validación Integral del MVP
- Soporte durante la integración con Backend y Frontend

---

## ⚙️ Backend

### Estado

🟡 En desarrollo

### Actividades

- API REST
- Persistencia
- Validaciones
- Swagger / OpenAPI
- Integración con Data Science
- Manejo de errores

---

## 🎨 Frontend

### Estado

⚪ Inicio de desarrollo

### Actividades

- Diseño UI
- Consumo de API
- Visualización de resultados
- Experiencia de usuario

---

## 🔗 Integración

### Objetivo

Integrar todos los componentes del MVP.

### Alcance

- Frontend ↔ Backend
- Backend ↔ Data Science
- Flujo completo del sistema
- Validaciones
- Persistencia
- Comunicación entre componentes

---

# 🔄 Dependencias

```text
Data Science
        │
        ▼
Backend
        │
        ▼
Frontend
        │
        ▼
QA
        │
        ▼
Deploy
```

| Dependencia | Estado |
|--------------|:------:|
| DS → Backend | ✅ |
| Backend → Frontend | 🟡 |
| Frontend → QA | ⏳ |
| QA → Deploy | ⏳ |

---

# 🎯 Próximos Hitos

| Prioridad | Actividad | Responsable |
|-----------|------------|-------------|
| 🔴 Alta | Finalizar API REST | Backend |
| 🔴 Alta | Integración Backend ↔ Data Science | Backend + DS |
| 🔴 Alta | Inicio del Frontend | Frontend |
| 🟡 Media | Benchmark Experimental | Data Science |
| 🟡 Media | Validación End-to-End | Equipo |
| 🟢 Baja | Optimización y Hardening | Equipo |

---

# 🛡️ Optimización y Hardening

Una vez completada la integración del MVP, el proyecto entrará en una fase de estabilización y mejora continua.

## Actividades

- Benchmark del modelo
- Optimización del rendimiento
- Refactor del código
- Logging
- Validación de entradas
- Manejo de errores
- Casos límite
- Pruebas End-to-End
- Documentación técnica final

---

# 🚀 Despliegue

## Objetivo

Preparar el MVP para su presentación y evaluación.

### Alcance

- Docker
- Oracle Cloud Infrastructure (OCI)
- Variables de entorno
- Configuración final
- Validaciones de despliegue

---

# 🏁 Entrega Final

La última fase del proyecto contempla la preparación de todos los entregables del Hackathon.

### Entregables

- MVP funcional
- Video demostrativo
- Pitch
- README final
- Documentación actualizada
- Presentación del proyecto

---

# 🌟 Visión del Proyecto

AyniKortex se desarrolla de forma incremental mediante la colaboración entre los equipos de Data Science, Backend y Frontend.

El propósito de este documento es proporcionar una visión compartida del estado del proyecto, facilitar la coordinación entre equipos y apoyar la toma de decisiones durante el desarrollo del MVP.

Este Roadmap será actualizado conforme el proyecto avance y se alcancen nuevos hitos.