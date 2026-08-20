# 🏛️ ADR-001 — Arquitectura Backend–Ciencia de Datos

> **Versión:** 1.2  
> **Estado:** Reemplazado  
> **Proyecto:** AyniKortex – Organización Inteligente del Conocimiento Técnico  
> **Decisión original:** Julio 2026

---

## ⚠️ Estado de la decisión

Esta decisión arquitectónica corresponde a una etapa anterior del desarrollo de AyniKortex.

En la decisión original se estableció una integración directa entre el Backend y el componente de Ciencia de Datos mediante la función:

```python
predict(title, text)
```

La arquitectura evolucionó posteriormente durante la implementación del MVP.

### Arquitectura actual

La implementación vigente utiliza **Data Science como un servicio independiente mediante FastAPI**, permitiendo que el Backend se comunique con el componente de Ciencia de Datos mediante una API HTTP.

La arquitectura actual se encuentra documentada en:

👉 [Arquitectura de AyniKortex](../Architecture/Architecture.md)

La documentación de la integración actual se encuentra en:

👉 [Documentación de API](../api/README.md)

> **Nota:** Este ADR se conserva como registro histórico de la decisión original y no debe utilizarse como referencia de la arquitectura vigente.

---

## 📚 Registro de decisiones relacionadas

| ADR | Decisión | Estado |
|---|---|---|
| ADR-001 | Arquitectura Backend–Ciencia de Datos | **Reemplazado** |
| ADR-002 | Adopción de Machine Learning Clásico para el MVP | Aceptado |
| ADR-003 | Integración mediante llamadas directas a funciones | **Reemplazado** |
| ADR-004 | Adopción de Oracle Cloud Infrastructure para el MVP | Aceptado |
| ADR-005 | Exclusión de IA Generativa | Aceptado |

---

# 1. Contexto

AyniKortex se desarrolla como un Producto Mínimo Viable (MVP) para el Hackathon ONE – Oracle Next Education.

Durante una etapa inicial del proyecto se planteó integrar un componente Backend y un componente de Ciencia de Datos para procesar contenido técnico mediante técnicas de Machine Learning clásico.

Debido al tiempo limitado del Hackathon y a la necesidad de facilitar el trabajo paralelo del equipo, era necesario definir una arquitectura simple, modular y fácil de mantener.

---

# 2. Problema

Era necesario definir una arquitectura que permitiera:

- Separar claramente las responsabilidades de cada componente.
- Facilitar el desarrollo paralelo entre Backend y Ciencia de Datos.
- Reducir el acoplamiento entre los componentes.
- Simplificar la integración del sistema.
- Facilitar el despliegue del MVP.
- Permitir futuras evoluciones sin modificar completamente la solución.

---

# 3. Decisión original

En la etapa inicial del proyecto se adoptó una arquitectura compuesta por:

- Backend.
- Ciencia de Datos.
- Oracle Cloud Infrastructure (OCI).

El Backend constituía el punto de acceso al sistema mediante una API REST.

El componente de Ciencia de Datos era responsable del procesamiento del contenido y de la ejecución del modelo de Machine Learning.

La integración inicialmente definida entre Backend y Ciencia de Datos se realizaría mediante una llamada directa a la función pública:

```python
predict(title, text)
```

Bajo esta decisión, el componente de Ciencia de Datos no expondría servicios HTTP ni APIs independientes.

---

# 4. Justificación

La decisión original fue seleccionada porque proporcionaba un equilibrio adecuado entre simplicidad, modularidad y mantenibilidad para el alcance inicial del MVP.

La separación entre Backend y Ciencia de Datos permitía que ambos componentes evolucionaran de manera independiente mientras se mantenía un contrato de integración estable.

Asimismo, esta decisión reducía la complejidad de la solución y evitaba incorporar infraestructura adicional durante la etapa inicial del Hackathon.

La arquitectura también permitía incorporar futuras mejoras en el modelo de Machine Learning sin afectar directamente la lógica del Backend.

---

# 5. Alternativas evaluadas

## Arquitectura basada en microservicios

**Resultado:** No seleccionada en la etapa inicial.

Aunque proporciona una alta independencia entre componentes, introduce complejidad adicional en aspectos como despliegue, comunicación, monitoreo y mantenimiento, lo cual no aportaba un beneficio proporcional para el MVP inicial.

---

## Exponer Ciencia de Datos mediante una API independiente

**Resultado:** No seleccionada en la decisión original.

Esta alternativa requería mantener un servicio HTTP adicional y gestionar la comunicación entre los componentes, incrementando la complejidad operativa y de despliegue.

> **Nota:** Esta alternativa fue posteriormente adoptada durante la evolución de la implementación del MVP.

---

## Arquitectura monolítica

**Resultado:** Parcialmente considerada.

Aunque simplifica el despliegue, dificulta la separación de responsabilidades entre Backend y Ciencia de Datos y limita la evolución independiente de ambos componentes.

---

# 6. Consecuencias de la decisión original

## Positivas

- Arquitectura simple y fácil de comprender.
- Separación clara de responsabilidades.
- Bajo acoplamiento conceptual entre componentes.
- Desarrollo paralelo entre Backend y Ciencia de Datos.
- Integración sencilla mediante una interfaz estable.
- Menor complejidad operativa para el MVP inicial.

## Negativas

- Backend y Ciencia de Datos dependían de una integración directa.
- La solución tenía menor independencia operativa entre ambos componentes.
- La evolución hacia un despliegue independiente requeriría una modificación arquitectónica.

---

# 7. Evolución de la arquitectura

Durante la implementación del MVP, la solución evolucionó respecto de la decisión original.

La arquitectura actual utiliza **FastAPI** para exponer el componente de Data Science como un servicio independiente.

El flujo vigente es:

```mermaid
flowchart LR
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science mediante FastAPI"
    "🤖 Data Science mediante FastAPI" --> "🧠 Modelo de Machine Learning"
```

Esta evolución permite separar operacionalmente el Backend y Data Science, facilitando su despliegue y evolución independiente.

La arquitectura vigente se encuentra documentada en:

👉 [Architecture.md](../Architecture/Architecture.md)

La definición de los contratos de integración se encuentra en:

👉 [Backend-Data-Contract.md](../api/Backend-Data-Contract.md)

---

# 8. Estado de la decisión

**Reemplazado.**

La decisión original de integrar Backend y Ciencia de Datos mediante una llamada directa a `predict()` dejó de representar la arquitectura implementada en el MVP.

La arquitectura vigente utiliza un servicio FastAPI para Data Science y comunicación mediante API HTTP.

Este ADR se conserva como **registro histórico de la evolución arquitectónica del proyecto**.

---

# 9. Referencias

- [Arquitectura actual de AyniKortex](../Architecture/Architecture.md)
- [Documentación de API](../api/README.md)
- [Contrato Backend–Data Science](../api/Backend-Data-Contract.md)
- [Modelo de datos](../api/Backend-Data-Model.md)
- [ADR-003 — Integración mediante llamadas directas a funciones](ADR-003%20%E2%80%93%20Integraci%C3%B3n%20mediante%20Llamadas%20Directas%20a%20Funciones.md)

---

