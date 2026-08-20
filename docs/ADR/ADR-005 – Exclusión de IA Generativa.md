# 🚫 ADR-005 — Exclusión de IA Generativa y Arquitecturas Avanzadas del MVP

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
| ADR-004 | Adopción de Oracle Cloud Infrastructure para el MVP | Aceptado |
| ADR-005 | Exclusión de IA Generativa | **Aceptado** |

---

# 1. Contexto

Durante la etapa de diseño arquitectónico de AyniKortex se evaluó la posibilidad de incorporar tecnologías de Inteligencia Artificial Generativa y arquitecturas avanzadas para el procesamiento de contenido técnico.

Estas tecnologías ofrecen capacidades importantes para aplicaciones basadas en lenguaje natural, pero también introducen dependencias, infraestructura y complejidad adicionales.

Era necesario determinar si dichas tecnologías aportaban un valor proporcional a los objetivos definidos para el MVP del Hackathon ONE.

---

# 2. Problema

Era necesario establecer el alcance tecnológico del MVP para:

- Mantener una arquitectura simple.
- Reducir la complejidad técnica.
- Cumplir los objetivos funcionales definidos.
- Facilitar el desarrollo dentro del tiempo disponible.
- Minimizar dependencias externas.
- Favorecer el mantenimiento y la comprensión del sistema.

---

# 3. Decisión

Se excluye del alcance del MVP el uso de tecnologías de Inteligencia Artificial Generativa y arquitecturas orientadas a generación y recuperación avanzada de información.

Entre las tecnologías y enfoques excluidos se encuentran:

- Modelos de Lenguaje de Gran Escala (LLM).
- Arquitecturas Retrieval-Augmented Generation (RAG).
- LangChain.
- LangGraph.
- CrewAI.
- AutoGen.
- Agentes de Inteligencia Artificial.
- Bases de datos vectoriales.
- Frameworks de orquestación para IA Generativa.

El sistema utiliza técnicas de Machine Learning clásico, de acuerdo con la decisión establecida en el ADR-002.

---

# 4. Justificación

La evaluación técnica concluyó que las funcionalidades requeridas por el MVP pueden implementarse mediante algoritmos tradicionales de Machine Learning.

La incorporación de tecnologías de IA Generativa aumentaría significativamente la complejidad de la arquitectura sin proporcionar un beneficio proporcional al alcance definido para esta versión.

Esta decisión permite mantener una solución más sencilla, reproducible, de menor complejidad operativa y más fácil de comprender y mantener.

Asimismo, reduce la dependencia de servicios externos y facilita el despliegue del sistema.

---

# 5. Alternativas evaluadas

## Modelos de Lenguaje de Gran Escala (LLM)

**Resultado:** No seleccionados para el MVP.

Se descartaron porque incrementarían la complejidad del sistema y excederían las necesidades funcionales definidas para esta versión.

---

## Arquitecturas RAG

**Resultado:** No seleccionadas para el MVP.

Requieren componentes adicionales, como mecanismos de recuperación y almacenamiento vectorial, que no aportan un beneficio proporcional al alcance actual.

---

## Frameworks para IA Generativa

**Resultado:** No seleccionados para el MVP.

Herramientas como LangChain, LangGraph, CrewAI y AutoGen fueron consideradas dentro de las alternativas tecnológicas, pero se concluyó que introducirían una complejidad innecesaria para el alcance definido.

---

# 6. Consecuencias

## Positivas

- Arquitectura más simple.
- Menor complejidad de desarrollo.
- Reducción de dependencias externas.
- Menor consumo de recursos.
- Mayor facilidad de mantenimiento.
- Resultados reproducibles.
- Menor riesgo técnico durante el Hackathon.

## Negativas

- El MVP no cuenta con capacidades generativas propias de los LLM.
- Algunas funcionalidades avanzadas deberán evaluarse como parte de futuras versiones del proyecto.

---

# 7. Impacto arquitectónico

Esta decisión establece el límite tecnológico del MVP y orienta el diseño de sus componentes hacia el uso de Machine Learning clásico.

La arquitectura mantiene la simplicidad y separación de responsabilidades definidas para la solución.

La incorporación futura de tecnologías de Inteligencia Artificial Generativa requerirá una nueva evaluación arquitectónica y, de ser necesario, la emisión de un nuevo ADR que modifique o complemente esta decisión.

---

# 8. Referencias

- [Arquitectura de AyniKortex](../Architecture/Architecture.md)
- [ADR-002 — Adopción de Machine Learning Clásico para el MVP](ADR-002%20%E2%80%93%20Adopci%C3%B3n%20de%20Machine%20Learning%20Cl%C3%A1sico%20para%20el%20MVP.md)
- [Documentación de Data Science](../SPRINTS/data-science/)

---

---

## Estado

**Aceptado**

La exclusión de Inteligencia Artificial Generativa y arquitecturas RAG permanece vigente para el MVP de AyniKortex.

Esta decisión define el alcance tecnológico de la versión actual y no impide que futuras versiones evalúen nuevas tecnologías mediante la correspondiente revisión arquitectónica.

---



