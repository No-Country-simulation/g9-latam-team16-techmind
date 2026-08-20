# 🏛️ ADR-003 — Integración mediante llamadas directas a funciones

> **Versión:** 1.1  
> **Estado:** Reemplazado  
> **Proyecto:** AyniKortex – Organización Inteligente del Conocimiento Técnico  
> **Decisión original:** Julio 2026

---

## ⚠️ Estado de la decisión

Esta decisión arquitectónica corresponde a una etapa anterior del desarrollo de AyniKortex.

En la decisión original se estableció una integración directa entre Backend y Ciencia de Datos mediante la función:

```python
predict(title, text)
```

Posteriormente, durante la implementación del MVP, la arquitectura evolucionó hacia un servicio independiente de Data Science utilizando **FastAPI** y comunicación mediante API HTTP.

### Arquitectura actual

La integración vigente utiliza:

```text
Backend
   │
   │ HTTP / API REST
   ▼
Data Science
   │
   ▼
Modelo de Machine Learning
```

La arquitectura actual se encuentra documentada en:

👉 [Arquitectura de AyniKortex](../Architecture/Architecture.md)

> **Nota:** Este ADR se conserva como registro histórico de la decisión original y no debe utilizarse como referencia de la integración vigente.

---

# 1. Contexto

Durante la etapa inicial de desarrollo de AyniKortex se definió una arquitectura compuesta por un componente Backend y un componente de Ciencia de Datos.

Era necesario establecer un mecanismo de integración que permitiera intercambiar información entre ambos componentes de forma simple, eficiente y con un bajo nivel de acoplamiento.

Esta decisión debía facilitar el desarrollo del MVP y permitir que Backend y Ciencia de Datos evolucionaran de manera independiente.

---

# 2. Problema

Era necesario establecer un mecanismo de integración que permitiera:

- Intercambiar información entre Backend y Ciencia de Datos.
- Reducir la complejidad de la solución.
- Evitar infraestructura adicional durante la etapa inicial.
- Facilitar el desarrollo y las pruebas.
- Mantener un contrato estable entre componentes.

---

# 3. Decisión original

Se adoptó una integración mediante llamadas directas a funciones.

El componente de Ciencia de Datos expuso una única interfaz pública:

```python
predict(title, text)
```

El Backend invocaba directamente esta función durante el procesamiento de cada solicitud.

Como parte de esta decisión, no se utilizarían protocolos HTTP, RPC, colas de mensajes ni otros mecanismos de comunicación entre procesos para la integración interna del sistema.

---

# 4. Justificación

La integración mediante llamadas directas reducía significativamente la complejidad de la arquitectura inicial.

Esta decisión eliminaba la necesidad de mantener múltiples servicios en ejecución, simplificaba el despliegue y reducía el número de puntos de fallo durante la operación del sistema.

Además, permitía que Backend y Ciencia de Datos trabajaran de forma independiente mientras mantenían un contrato de integración claramente definido.

---

# 5. Alternativas evaluadas

## API REST entre componentes

**Resultado:** No seleccionada en la decisión original.

Aunque permitía desacoplar físicamente los componentes, introducía un segundo servicio HTTP, mayor complejidad operativa y latencia adicional que no se consideraban necesarias para el MVP inicial.

> **Evolución posterior:** Esta alternativa fue adoptada durante la implementación del MVP, dando lugar al servicio actual de Data Science basado en FastAPI.

---

## Arquitectura basada en microservicios

**Resultado:** No seleccionada.

Requería mecanismos adicionales para despliegue, monitoreo y comunicación entre servicios, aumentando la complejidad del sistema sin un beneficio proporcional para el MVP.

---

## Comunicación mediante colas de mensajes

**Resultado:** No seleccionada.

Este mecanismo estaba orientado a arquitecturas distribuidas y procesamiento asíncrono, escenarios que no formaban parte del alcance del MVP inicial.

---

# 6. Consecuencias de la decisión original

## Positivas

- Integración simple.
- Bajo nivel de complejidad operativa.
- Fácil mantenimiento.
- Menor latencia de comunicación.
- Despliegue simplificado.
- Menor consumo de recursos.
- Pruebas de integración más sencillas.

## Negativas

- Backend y Ciencia de Datos dependían del mismo proceso de ejecución.
- La separación física entre componentes era limitada.
- La escalabilidad independiente de Ciencia de Datos requería revisar esta decisión.

---

# 7. Evolución de la integración

Durante la implementación del MVP, la solución evolucionó respecto de la decisión original.

La integración mediante llamadas directas fue reemplazada por un servicio independiente de Data Science basado en **FastAPI**.

El flujo actual es:

```mermaid
flowchart LR
    "⚙️ Backend" -->|"API HTTP / REST"| "🤖 Data Science mediante FastAPI"
    "🤖 Data Science mediante FastAPI" -->|"Inferencia"| "🧠 Modelo de Machine Learning"
```

Esta evolución permite separar operacionalmente Backend y Data Science y facilita su despliegue, mantenimiento y evolución independiente.

La implementación actual del servicio se encuentra dentro del componente:

```text
src/data_science/
```

La documentación de la integración vigente se encuentra en:

👉 [Documentación de API](../api/README.md)

👉 [Contrato Backend–Data Science](../api/Backend-Data-Contract.md)

---

# 8. Estado de la decisión

**Reemplazado.**

La integración mediante llamadas directas a `predict()` dejó de representar la arquitectura implementada en el MVP.

La arquitectura vigente utiliza un servicio FastAPI para Data Science y comunicación mediante API HTTP.

Este ADR se conserva como **registro histórico de la evolución de la arquitectura de integración de AyniKortex**.

---

# 9. Referencias

- [Arquitectura actual de AyniKortex](../Architecture/Architecture.md)
- [Documentación de API](../api/README.md)
- [Contrato Backend–Data Science](../api/Backend-Data-Contract.md)
- [ADR-001 — Arquitectura Backend–Ciencia de Datos](ADR-001%20%E2%80%93%20Arquitectura%20Backend%E2%80%93Ciencia%20de%20Datos.md)

---

