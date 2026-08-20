# ☁️ ADR-004 — Adopción de Oracle Cloud Infrastructure para el MVP

> **Versión:** 1.1  
> **Estado:** Aceptado  
> **Proyecto:** AyniKortex – Organización Inteligente del Conocimiento Técnico  
> **Decisión original:** Julio 2026

---

## 📚 Registro de decisiones relacionadas

| ADR | Decisión | Estado |
|---|---|---|
| ADR-001 | Arquitectura Backend–Ciencia de Datos | Reemplazado |
| ADR-002 | Adopción de Machine Learning Clásico para el MVP | Aceptado |
| ADR-003 | Integración mediante llamadas directas a funciones | Reemplazado |
| ADR-004 | Adopción de Oracle Cloud Infrastructure para el MVP | **Aceptado** |
| ADR-005 | Exclusión de IA Generativa | Aceptado |

---

# 1. Contexto

AyniKortex requiere una infraestructura que permita ejecutar y publicar el MVP desarrollado durante el Hackathon ONE – Oracle Next Education.

Además, el Hackathon establece como requisito la integración con al menos un servicio de Oracle Cloud Infrastructure (OCI).

Durante el desarrollo se evaluó una infraestructura que permitiera mantener una arquitectura sencilla, facilitar el despliegue de los componentes y disponer de un entorno funcional para demostración.

Oracle Cloud Infrastructure fue seleccionada como plataforma de infraestructura para el MVP.

---

# 2. Problema

Era necesario definir una infraestructura que permitiera:

- Desplegar los componentes funcionales del MVP.
- Cumplir con los requisitos de integración con Oracle Cloud Infrastructure.
- Mantener una infraestructura sencilla y adecuada al alcance del proyecto.
- Facilitar la publicación de una versión funcional para demostración.
- Permitir la evolución gradual de la solución.
- Gestionar los artefactos y recursos asociados al componente de Ciencia de Datos.

---

# 3. Decisión

Se adopta **Oracle Cloud Infrastructure (OCI)** como plataforma de infraestructura para AyniKortex.

OCI se utiliza como entorno de despliegue del MVP, permitiendo disponer de una versión funcional de la solución accesible para demostración.

La infraestructura mantiene separados los componentes de aplicación y permite desplegar los servicios necesarios para el funcionamiento de:

- Frontend.
- Backend.
- Data Science.
- Modelo de Machine Learning.

Adicionalmente, se utiliza almacenamiento de objetos de OCI para gestionar recursos asociados al proyecto, como datasets y artefactos de Ciencia de Datos, mediante procesos automatizados cuando corresponde.

La incorporación de nuevos servicios de OCI deberá justificarse en función de las necesidades reales del proyecto y del valor que aporten a la solución.

---

## ☁️ Arquitectura de despliegue

La utilización de OCI permite disponer de los principales componentes del MVP en un entorno de infraestructura cloud.

```mermaid
flowchart LR
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "⚙️ Backend" --> "🗄️ MySQL"
    "🤖 Data Science" --> "🧠 Modelo de Machine Learning"

    "☁️ Oracle Cloud Infrastructure" -. "Infraestructura" .-> "🌐 Frontend"
    "☁️ Oracle Cloud Infrastructure" -. "Infraestructura" .-> "⚙️ Backend"
    "☁️ Oracle Cloud Infrastructure" -. "Infraestructura" .-> "🤖 Data Science"
```

El detalle de configuración y procedimientos de despliegue se encuentra en:

👉 [Guía de despliegue](../Deployment-Guide/Deployment-Guide.md)

---

# 4. Justificación

Oracle Cloud Infrastructure permite cumplir los requerimientos del Hackathon y proporciona una plataforma adecuada para desplegar el MVP.

La utilización de OCI permite:

- Disponer de un entorno cloud para demostración.
- Integrar los componentes desplegados de la solución.
- Gestionar recursos asociados al proyecto.
- Mantener una infraestructura proporcional al alcance del MVP.
- Permitir futuras ampliaciones de infraestructura sin modificar necesariamente la lógica de negocio.

La adopción de OCI también mantiene alineada la solución con el ecosistema tecnológico definido para el Hackathon.

---

# 5. Alternativas evaluadas

## Infraestructura completamente local

**Resultado:** No seleccionada.

Aunque simplifica el desarrollo inicial, no permite cumplir con el requisito de integración con Oracle Cloud Infrastructure establecido por el Hackathon ni proporciona un entorno cloud para la demostración del MVP.

---

## Otros proveedores Cloud

**Resultado:** No seleccionados.

Servicios como AWS, Microsoft Azure o Google Cloud Platform ofrecen capacidades equivalentes, pero no satisfacen el requisito específico del Hackathon de utilizar Oracle Cloud Infrastructure.

---

## Uso intensivo de múltiples servicios OCI

**Resultado:** No seleccionado.

Se decidió utilizar únicamente los recursos de OCI necesarios para el funcionamiento y soporte del MVP, evitando incorporar servicios adicionales que no aportaran valor directo a la solución.

---

# 6. Consecuencias

## Positivas

- Cumplimiento de los requisitos del Hackathon.
- MVP funcional desplegado en infraestructura cloud.
- Infraestructura alineada con la arquitectura de la solución.
- Posibilidad de demostrar la solución fuera del entorno local.
- Gestión centralizada de recursos cloud.
- Posibilidad de ampliar progresivamente la infraestructura.
- Integración con servicios de OCI para soportar los recursos del proyecto.

## Negativas

- Dependencia de Oracle Cloud Infrastructure para el entorno desplegado.
- Posibles limitaciones asociadas a disponibilidad de recursos, cuotas o capacidad del entorno.
- La administración de infraestructura cloud introduce responsabilidades operativas adicionales frente a una ejecución exclusivamente local.

---

# 7. Impacto arquitectónico

La adopción de OCI establece la infraestructura cloud utilizada para el MVP de AyniKortex.

La lógica de negocio y los componentes de la aplicación mantienen separación respecto de la infraestructura, permitiendo que futuras modificaciones de la plataforma cloud puedan evaluarse sin rediseñar necesariamente la solución.

La infraestructura puede evolucionar de acuerdo con las necesidades de escalabilidad, disponibilidad, almacenamiento y operación del sistema.

---

# 8. Referencias

- [Arquitectura de AyniKortex](../Architecture/Architecture.md)
- [Guía de despliegue](../Deployment-Guide/Deployment-Guide.md)
- [Roadmap técnico](../ROADMAP/Technical-Roadmap.md)

---

---

## Estado

**Aceptado**

Oracle Cloud Infrastructure constituye la plataforma de infraestructura cloud adoptada para el desarrollo, soporte y despliegue del MVP de AyniKortex.

La decisión permanece vigente mientras OCI continúe proporcionando los recursos necesarios para la operación y demostración del MVP.

---