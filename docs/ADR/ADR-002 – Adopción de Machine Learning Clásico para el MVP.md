# 🧠 ADR-002 — Adopción de Machine Learning Clásico para el MVP

> **Versión:** 1.1  
> **Estado:** Aceptado  
> **Proyecto:** AyniKortex – Organización Inteligente del Conocimiento Técnico  
> **Decisión original:** Julio 2026

---

## 📚 Registro de decisiones relacionadas

| ADR | Decisión | Estado |
|---|---|---|
| ADR-001 | Arquitectura Backend–Ciencia de Datos | Reemplazado |
| ADR-002 | Adopción de Machine Learning Clásico para el MVP | **Aceptado** |
| ADR-003 | Integración mediante llamadas directas a funciones | Reemplazado |
| ADR-004 | Adopción de Oracle Cloud Infrastructure para el MVP | Aceptado |
| ADR-005 | Exclusión de IA Generativa | Aceptado |

---

# 1. Contexto

AyniKortex tiene como objetivo organizar y clasificar contenido técnico mediante técnicas de procesamiento de texto y aprendizaje automático.

Durante la etapa de diseño se evaluaron diferentes enfoques para resolver el problema, incluyendo modelos tradicionales de Machine Learning y tecnologías basadas en Inteligencia Artificial Generativa.

La solución debía satisfacer los objetivos funcionales del MVP, respetar el tiempo disponible del Hackathon y mantener una arquitectura simple, mantenible y de bajo costo operativo.

---

# 2. Problema

Era necesario seleccionar una estrategia de procesamiento de texto que permitiera:

- Clasificar contenido técnico.
- Identificar palabras relevantes del contenido.
- Obtener resultados reproducibles.
- Generar información complementaria para facilitar la interpretación del resultado.
- Reducir la complejidad del sistema.
- Facilitar el desarrollo, evaluación y mantenimiento del MVP.

---

# 3. Decisión

Se adopta un enfoque basado en **Machine Learning clásico** utilizando herramientas de `scikit-learn`.

El componente de Ciencia de Datos utiliza principalmente:

- **TF-IDF** para representar el contenido textual como características numéricas.
- **Logistic Regression** para realizar la clasificación.
- **Label Encoding** para gestionar las categorías utilizadas por el modelo.
- **Joblib** para la persistencia de los artefactos del modelo.

El modelo constituye el núcleo de la capacidad de clasificación automática de AyniKortex.

Durante la inferencia, el sistema genera una clasificación acompañada de información complementaria como nivel de confianza, palabras clave, resumen, versión del modelo y tiempo de procesamiento.

---

# 4. Justificación

Las técnicas de Machine Learning clásico permiten resolver los objetivos principales del MVP sin incorporar infraestructura adicional ni dependencias asociadas a modelos generativos.

La solución facilita la evaluación mediante métricas tradicionales y simplifica los procesos de entrenamiento, persistencia e inferencia.

Asimismo, este enfoque reduce los requerimientos computacionales y evita depender de servicios externos de Inteligencia Artificial Generativa durante la ejecución del sistema.

La elección también permite mantener una arquitectura adecuada al alcance y los recursos disponibles durante el Hackathon.

---

# 5. Alternativas evaluadas

## Modelos de Inteligencia Artificial Generativa (LLM)

**Resultado:** No seleccionados para el MVP.

Aunque ofrecen capacidades avanzadas de comprensión y generación de lenguaje, exceden los requerimientos funcionales definidos para el MVP e incrementarían la complejidad técnica y operativa de la solución.

---

## Arquitecturas RAG

**Resultado:** No seleccionadas para el MVP.

Requieren componentes adicionales, como mecanismos de recuperación de información y almacenamiento vectorial, que no aportan un beneficio proporcional al alcance definido para esta versión.

---

## Modelos basados en Deep Learning

**Resultado:** No seleccionados para el MVP.

Su entrenamiento y mantenimiento requieren mayores recursos computacionales y un volumen de datos superior al disponible para el alcance actual del proyecto.

---

# 6. Consecuencias

## Positivas

- Arquitectura más simple.
- Entrenamiento y evaluación accesibles.
- Resultados reproducibles.
- Bajo consumo de recursos.
- Despliegue sencillo.
- Independencia de servicios externos de IA generativa.
- Menor complejidad de mantenimiento.

## Negativas

- Menor capacidad para comprender relaciones semánticas complejas frente a modelos de lenguaje más avanzados.
- El rendimiento depende directamente de la calidad y representatividad del dataset.
- La ampliación hacia casos de uso más complejos podría requerir evaluar otros enfoques de Inteligencia Artificial.

---

# 7. Impacto arquitectónico

Esta decisión define el núcleo tecnológico del componente de Ciencia de Datos para el MVP.

Los procesos de entrenamiento, persistencia e inferencia fueron diseñados considerando un enfoque de Machine Learning clásico.

La utilización de este enfoque permite mantener el componente de Data Science ligero y adecuado para su despliegue como servicio independiente mediante FastAPI.

La adopción de modelos generativos o arquitecturas diferentes en futuras versiones requerirá revisar esta decisión y evaluar su impacto sobre la arquitectura, infraestructura y procesos de entrenamiento.

---

# 8. Referencias

- [Arquitectura de AyniKortex](../Architecture/Architecture.md)
- [Documentación de Data Science](../SPRINTS/data-science/)
- [ADR-005 — Exclusión de IA Generativa](ADR-005%20%E2%80%93%20Exclusi%C3%B3n%20de%20IA%20Generativa.md)

---

---

## Estado

**Aceptado**

La decisión de utilizar Machine Learning clásico permanece vigente para el MVP de AyniKortex y constituye la base tecnológica del componente de Ciencia de Datos.

Cualquier cambio hacia modelos generativos, Deep Learning u otros enfoques deberá evaluarse mediante una nueva decisión arquitectónica o una actualización de este ADR.

---

