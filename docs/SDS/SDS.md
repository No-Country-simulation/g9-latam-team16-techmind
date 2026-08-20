# Software Design Specification (SDS)

## AyniKortex — Organización Inteligente del Conocimiento Técnico

> **Versión:** 2.0  
> **Estado:** Vigente  
> **Proyecto:** AyniKortex  
> **Última actualización:** Agosto 2026

---

## Control del documento

| Campo | Valor |
|---|---|
| **Documento** | Software Design Specification |
| **Proyecto** | AyniKortex |
| **Versión** | 2.0 |
| **Estado** | Vigente |
| **Tipo** | Especificación de Diseño de Software |
| **Alcance** | MVP funcional |
| **Infraestructura** | Oracle Cloud Infrastructure (OCI) |

---

# 1. Propósito

Este documento define el diseño de alto nivel de **AyniKortex**, una plataforma orientada a la organización y clasificación de documentación técnica mediante técnicas de Inteligencia Artificial y Machine Learning.

El objetivo del SDS es proporcionar una visión coherente de la estructura del sistema, sus principales componentes, responsabilidades, relaciones e integración.

El documento representa el estado actual del diseño del MVP y sirve como referencia para comprender cómo se integran sus principales componentes.

Los detalles específicos de implementación se mantienen en documentos especializados para evitar duplicidad y facilitar su mantenimiento.

---

# 2. Alcance

El presente documento cubre el diseño general del MVP de AyniKortex, incluyendo:

- Arquitectura general del sistema.
- Componentes principales.
- Responsabilidades de cada componente.
- Flujo de información.
- Uso de Machine Learning para clasificación.
- Integración entre Frontend, Backend y Data Science.
- Persistencia de información.
- Infraestructura y despliegue en Oracle Cloud Infrastructure.
- Principales consideraciones de diseño.
- Estado actual y evolución prevista del MVP.

Este documento **no sustituye** la documentación especializada del proyecto.

| Tema | Documento de referencia |
|---|---|
| Arquitectura detallada | `docs/Architecture/Architecture.md` |
| Decisiones arquitectónicas | `docs/ADR/` |
| Contrato de integración | `docs/api/Backend-Data-Contract.md` |
| API | `docs/api/aynikortex-api.yaml` |
| Modelo de datos | `docs/api/Backend-Data-Model.md` |
| Data Science | `docs/SPRINTS/data-science/` |
| Despliegue | `docs/Deployment-Guide/Deployment-Guide.md` |
| Roadmap | `docs/ROADMAP/Technical-Roadmap.md` |

---

# 3. Contexto del proyecto

Los equipos tecnológicos generan y utilizan grandes cantidades de documentación técnica: especificaciones, decisiones arquitectónicas, manuales, guías, registros y otros documentos asociados al desarrollo de software.

A medida que esta información crece, identificar y organizar el conocimiento disponible puede convertirse en una tarea manual, lenta y difícil de mantener.

AyniKortex surge como una solución orientada a **organizar y clasificar automáticamente documentación técnica**, utilizando técnicas de procesamiento de texto y Machine Learning.

El proyecto fue desarrollado como un MVP dentro del Hackathon ONE – Oracle Next Education, priorizando una solución funcional, sencilla de mantener y desplegable en infraestructura cloud.

---

# 4. Problema

La documentación técnica puede encontrarse distribuida entre diferentes archivos y fuentes, dificultando su organización y clasificación.

El problema principal consiste en disponer de un mecanismo que permita analizar el contenido de un documento y determinar automáticamente la categoría a la que pertenece.

AyniKortex busca reducir esta tarea manual mediante un flujo automatizado de análisis y clasificación.

---

# 5. Objetivos del sistema

## 5.1 Objetivo general

Desarrollar un MVP capaz de **analizar documentación técnica y generar automáticamente una clasificación**, proporcionando información complementaria que facilite la interpretación del resultado.

## 5.2 Objetivos específicos

- Recibir contenido técnico mediante la aplicación.
- Procesar texto proveniente de diferentes tipos de archivos.
- Analizar el contenido utilizando un modelo de Machine Learning.
- Asignar una categoría y subcategoría al contenido.
- Obtener un nivel de confianza asociado a la clasificación.
- Identificar palabras relevantes del contenido.
- Generar un resumen del contenido procesado.
- Registrar la información necesaria para el funcionamiento de la plataforma.
- Disponer de una solución integrada y desplegada en Oracle Cloud Infrastructure.

---

# 6. Alcance del MVP

El MVP se concentra en demostrar el flujo completo de:

```mermaid
flowchart LR
    "👤 Usuario" --> "📄 Documento"
    "📄 Documento" --> "🔍 Procesamiento"
    "🔍 Procesamiento" --> "🧠 Clasificación"
    "🧠 Clasificación" --> "📊 Resultado"
    "📊 Resultado" --> "👤 Usuario"
```

El alcance incluye la recepción del contenido, su procesamiento, clasificación mediante Machine Learning y presentación del resultado.

Las funcionalidades adicionales que no forman parte del alcance actual podrán evaluarse en futuras versiones de AyniKortex.

---

# 7. Principios de diseño

El diseño de AyniKortex se basa en los siguientes principios:

- **Separación de responsabilidades:** cada componente tiene una función claramente definida.
- **Modularidad:** los componentes pueden evolucionar de forma independiente.
- **Simplicidad:** la arquitectura se mantiene proporcional al alcance del MVP.
- **Bajo acoplamiento:** la comunicación entre componentes se realiza mediante contratos definidos.
- **Reproducibilidad:** el procesamiento y la clasificación deben producir resultados consistentes bajo las mismas condiciones.
- **Evolución incremental:** la arquitectura permite incorporar nuevas capacidades sin modificar innecesariamente los componentes existentes.
- **Despliegue cloud:** el MVP se encuentra preparado para ejecutarse en Oracle Cloud Infrastructure.

---

# 8. Arquitectura del sistema

AyniKortex está compuesto por cuatro elementos funcionales principales:

- **Frontend:** interfaz mediante la cual el usuario interactúa con la plataforma.
- **Backend:** gestiona las solicitudes, la lógica de negocio, la persistencia y la integración con Data Science.
- **Data Science:** procesa el contenido y ejecuta el modelo de Machine Learning para obtener la clasificación.
- **Base de datos:** almacena la información necesaria para el funcionamiento de la plataforma.

La arquitectura se complementa con Oracle Cloud Infrastructure como plataforma de despliegue.

## 8.1 Vista general

```mermaid
flowchart LR
    "👤 Usuario" --> "🌐 Frontend"
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" -->|"HTTP / API"| "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo de Machine Learning"
    "⚙️ Backend" --> "🗄️ Base de Datos"

    "☁️ Oracle Cloud Infrastructure" -.-> "🌐 Frontend"
    "☁️ Oracle Cloud Infrastructure" -.-> "⚙️ Backend"
    "☁️ Oracle Cloud Infrastructure" -.-> "🤖 Data Science"
```

## 8.2 Flujo principal

El procesamiento de una solicitud sigue el siguiente flujo:

```mermaid
flowchart LR
    "📄 Contenido" --> "🌐 Frontend"
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo"
    "🧠 Modelo" --> "📊 Clasificación"
    "📊 Clasificación" --> "⚙️ Backend"
    "⚙️ Backend" --> "🌐 Frontend"
    "🌐 Frontend" --> "👤 Usuario"
```

La arquitectura actual utiliza **Data Science como un servicio independiente**, expuesto mediante FastAPI. Esta integración reemplaza la decisión arquitectónica inicial basada en llamadas directas a funciones.

Para conocer el detalle de la evolución arquitectónica, consultar:

- `docs/ADR/ADR-001 – Arquitectura Backend–Ciencia de Datos.md`
- `docs/ADR/ADR-003 – Integración mediante Llamadas Directas a Funciones.md`
- `docs/Architecture/Architecture.md`

---

# 9. Componentes del sistema

AyniKortex está organizado en componentes especializados. Cada uno cumple una responsabilidad específica dentro del flujo general de la plataforma.

## 9.1 Frontend

El Frontend proporciona la interfaz web mediante la cual el usuario interactúa con AyniKortex.

Sus principales responsabilidades son:

- Permitir el ingreso o selección del contenido a procesar.
- Enviar las solicitudes al Backend.
- Mostrar el resultado de la clasificación.
- Presentar al usuario la información generada por el sistema.

**Tecnologías principales:** React y Vite.

---

## 9.2 Backend

El Backend constituye la capa central de la aplicación.

Sus principales responsabilidades son:

- Recibir las solicitudes provenientes del Frontend.
- Gestionar la lógica de negocio.
- Validar y procesar las solicitudes.
- Coordinar la comunicación con Data Science.
- Gestionar la persistencia de información.
- Devolver los resultados al Frontend.

**Tecnologías principales:** Java y Spring Boot.

La especificación detallada del contrato y modelo de datos se encuentra en:

[📄 Contrato Backend–Data Science](../api/Backend-Data-Contract.md)

[📄 Modelo de datos](../api/Backend-Data-Model.md)

---

## 9.3 Data Science

Data Science es el componente responsable del procesamiento inteligente del contenido.

Sus principales responsabilidades son:

- Recibir el contenido enviado para análisis.
- Procesar el texto.
- Transformar el contenido en características utilizables por el modelo.
- Ejecutar el modelo de Machine Learning.
- Generar la clasificación.
- Calcular el nivel de confianza.
- Identificar palabras relevantes.
- Generar un resumen del contenido.
- Devolver el resultado al Backend.

Data Science funciona como un servicio independiente mediante **FastAPI**.

La documentación específica del componente se mantiene en:

[🤖 Documentación de Data Science](../SPRINTS/data-science/)

> **Nota:** La documentación de Data Science será actualizada para reflejar el estado final del componente implementado en el MVP.

---

## 9.4 Base de datos

La Base de Datos permite almacenar y gestionar la información necesaria para el funcionamiento de la plataforma.

**Tecnología principal:** MySQL.

La definición detallada del modelo de datos se encuentra en:

[🗄️ Modelo de datos](../api/Backend-Data-Model.md)

---

## 9.5 Relación entre componentes

Los componentes colaboran mediante un flujo definido de responsabilidades:

```mermaid
flowchart LR
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo de Machine Learning"
    "⚙️ Backend" --> "🗄️ Base de Datos"
    "🧠 Modelo de Machine Learning" --> "📊 Resultado"
    "📊 Resultado" --> "⚙️ Backend"
    "⚙️ Backend" --> "🌐 Frontend"
```

Esta separación permite que cada componente pueda evolucionar de manera independiente manteniendo definidos sus puntos de integración.

---

# 10. Inteligencia Artificial y Machine Learning

AyniKortex utiliza técnicas de **Machine Learning (aprendizaje automático)** para analizar el contenido de documentación técnica y asignarlo automáticamente a una categoría.

El objetivo del componente de Inteligencia Artificial no es generar contenido nuevo, sino **analizar información existente y clasificarla** de acuerdo con los patrones aprendidos durante el entrenamiento.

## 10.1 Enfoque utilizado

El MVP utiliza **Machine Learning clásico**, basado en técnicas de procesamiento de texto y algoritmos de `scikit-learn`.

El flujo general es:

```mermaid
flowchart LR
    "📄 Texto" --> "🔤 Procesamiento"
    "🔤 Procesamiento" --> "📊 Representación numérica"
    "📊 Representación numérica" --> "🧠 Modelo entrenado"
    "🧠 Modelo entrenado" --> "🏷️ Categoría"
    "🧠 Modelo entrenado" --> "📈 Confianza"
```

En términos sencillos:

> El sistema transforma el contenido de un documento en información que el modelo puede analizar y utiliza los patrones aprendidos previamente para determinar la categoría más probable.

---

## 10.2 Clasificación automática

La clasificación automática permite que AyniKortex determine una **categoría y subcategoría** para el contenido recibido.

El resultado incluye información adicional que ayuda a interpretar la predicción:

- Categoría.
- Subcategoría.
- Nivel de confianza.
- Palabras relevantes.
- Resumen del contenido.
- Versión del modelo.
- Tiempo de procesamiento.

El proceso puede representarse de la siguiente manera:

```mermaid
flowchart LR
    "📄 Documento" --> "🔍 Análisis del contenido"
    "🔍 Análisis del contenido" --> "🧠 Modelo"
    "🧠 Modelo" --> "🏷️ Categoría"
    "🧠 Modelo" --> "📈 Confianza"
    "🔍 Análisis del contenido" --> "🔑 Palabras relevantes"
    "🔍 Análisis del contenido" --> "📝 Resumen"
    "🏷️ Categoría" --> "📦 Resultado"
    "📈 Confianza" --> "📦 Resultado"
    "🔑 Palabras relevantes" --> "📦 Resultado"
    "📝 Resumen" --> "📦 Resultado"
```

---

## 10.3 Tecnologías utilizadas

El componente utiliza principalmente:

| Tecnología | Función |
|---|---|
| **Python** | Desarrollo del componente de Data Science |
| **scikit-learn** | Procesamiento y entrenamiento del modelo |
| **TF-IDF** | Representación numérica del texto |
| **Logistic Regression** | Clasificación del contenido |
| **Joblib** | Persistencia de los artefactos del modelo |
| **FastAPI** | Exposición del servicio de inferencia |

---

## 10.4 Alcance de Inteligencia Artificial del MVP

La Inteligencia Artificial de AyniKortex está orientada específicamente a la **clasificación automática de documentación técnica**.

El MVP no utiliza:

- Modelos de Lenguaje de Gran Escala (LLM).
- Inteligencia Artificial Generativa.
- Arquitecturas RAG.
- Bases de datos vectoriales.
- Agentes de Inteligencia Artificial.

Esta decisión está documentada en:

[📄 ADR-002 — Machine Learning clásico](../ADR/ADR-002%20%E2%80%93%20Adopci%C3%B3n%20de%20Machine%20Learning%20Cl%C3%A1sico%20para%20el%20MVP.md)

[📄 ADR-005 — Exclusión de IA Generativa](../ADR/ADR-005%20%E2%80%93%20Exclusi%C3%B3n%20de%20IA%20Generativa.md)

---

## 10.5 Documentación especializada

Los detalles sobre dataset, preprocesamiento, entrenamiento, evaluación, persistencia, inferencia y pruebas se mantienen en la documentación específica de Data Science.

[🤖 Documentación de Data Science](../SPRINTS/data-science/)

---

# 11. Integración y flujo de información

La integración de AyniKortex permite que los diferentes componentes colaboren para procesar una solicitud y devolver el resultado al usuario.

El Backend actúa como punto central de coordinación entre la interfaz, el componente de Data Science y la persistencia de información.

## 11.1 Flujo general

El flujo principal de una solicitud es:

```mermaid
flowchart LR
    "👤 Usuario" --> "🌐 Frontend"
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo"
    "🧠 Modelo" --> "📊 Clasificación"
    "📊 Clasificación" --> "🤖 Data Science"
    "🤖 Data Science" --> "⚙️ Backend"
    "⚙️ Backend" --> "🗄️ Base de Datos"
    "⚙️ Backend" --> "🌐 Frontend"
    "🌐 Frontend" --> "👤 Usuario"
```

El flujo permite separar claramente las responsabilidades:

1. El usuario proporciona el contenido.
2. El Frontend envía la solicitud al Backend.
3. El Backend valida y coordina el procesamiento.
4. Data Science analiza el contenido.
5. El modelo genera la clasificación.
6. Data Science devuelve el resultado.
7. El Backend gestiona el resultado y la persistencia correspondiente.
8. El Frontend presenta la información al usuario.

---

## 11.2 Integración Frontend–Backend

El Frontend se comunica con el Backend mediante servicios HTTP.

El Backend proporciona las operaciones necesarias para que la aplicación pueda enviar información y recibir los resultados correspondientes.

El detalle de las operaciones disponibles, estructuras de solicitud y respuestas se encuentra definido en la documentación de API:

[📄 Especificación de API](../api/aynikortex-api.yaml)

[📄 Contrato Backend–Data Science](../api/Backend-Data-Contract.md)

---

## 11.3 Integración Backend–Data Science

El Backend se comunica con el componente de Data Science mediante **HTTP**, utilizando el servicio de inferencia desarrollado con FastAPI.

Esta integración permite mantener Data Science como un componente independiente y facilita su despliegue y evolución.

El flujo de integración es:

```mermaid
flowchart LR
    "⚙️ Backend" -->|"Solicitud HTTP"| "🤖 Data Science"
    "🤖 Data Science" -->|"Procesamiento"| "🧠 Modelo"
    "🧠 Modelo" -->|"Predicción"| "🤖 Data Science"
    "🤖 Data Science" -->|"Resultado HTTP"| "⚙️ Backend"
```

La definición detallada del contrato de comunicación se encuentra en:

[📄 Contrato Backend–Data Science](../api/Backend-Data-Contract.md)

---

## 11.4 Procesamiento de contenido

AyniKortex permite procesar contenido textual y archivos compatibles con el servicio de Data Science.

El contenido recibido es transformado en texto cuando es necesario y posteriormente enviado al proceso de inferencia.

El flujo conceptual es:

```mermaid
flowchart LR
    "📄 Archivo o texto" --> "🔍 Extracción de contenido"
    "🔍 Extracción de contenido" --> "📝 Texto"
    "📝 Texto" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo"
    "🧠 Modelo" --> "📊 Resultado"
```

El detalle de los formatos soportados y del procesamiento interno corresponde a la documentación específica de Data Science.

---

## 11.5 Contratos de integración

La comunicación entre los componentes se basa en contratos definidos para evitar dependencias innecesarias entre sus implementaciones internas.

Los contratos y estructuras de datos oficiales se mantienen en:

- [📄 Especificación de API](../api/aynikortex-api.yaml)
- [📄 Contrato Backend–Data Science](../api/Backend-Data-Contract.md)
- [📄 Modelo de datos](../api/Backend-Data-Model.md)

El SDS presenta únicamente la relación entre los componentes; los detalles técnicos de cada contrato deben mantenerse en su documentación especializada.

---

# 12. Infraestructura y despliegue

AyniKortex utiliza **Oracle Cloud Infrastructure (OCI)** como plataforma cloud para el despliegue del MVP.

La infraestructura permite disponer de una versión funcional de la solución fuera del entorno local y soportar los principales componentes de la aplicación.

## 12.1 Infraestructura cloud

La arquitectura de despliegue contempla los componentes principales de la solución:

```mermaid
flowchart LR
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "⚙️ Backend" --> "🗄️ MySQL"
    "🤖 Data Science" --> "🧠 Modelo de Machine Learning"

    "☁️ Oracle Cloud Infrastructure" -. "Infraestructura cloud" .-> "🌐 Frontend"
    "☁️ Oracle Cloud Infrastructure" -. "Infraestructura cloud" .-> "⚙️ Backend"
    "☁️ Oracle Cloud Infrastructure" -. "Infraestructura cloud" .-> "🤖 Data Science"
```

OCI forma parte de la solución como plataforma de infraestructura y no modifica las responsabilidades funcionales de los componentes de AyniKortex.

---

## 12.2 Despliegue

El MVP cuenta con una versión funcional desplegada en Oracle Cloud Infrastructure.

El despliegue permite:

- Ejecutar los componentes principales de la aplicación.
- Integrar Frontend, Backend y Data Science.
- Disponer de un entorno cloud para demostración.
- Gestionar los recursos necesarios para la operación del MVP.
- Mantener una infraestructura proporcional al alcance del proyecto.

El detalle de configuración, procedimientos y validaciones de OCI se encuentra en:

[☁️ Guía de despliegue](../Deployment-Guide/Deployment-Guide.md)

---

## 12.3 Gestión de artefactos

Los datasets y artefactos asociados al componente de Data Science pueden gestionarse mediante almacenamiento de objetos de OCI.

La sincronización de determinados recursos se encuentra automatizada mediante **GitHub Actions**, permitiendo mantener los artefactos utilizados por el componente de Data Science asociados al flujo de desarrollo.

El detalle de esta configuración se mantiene en la documentación específica de despliegue y operación.

---

## 12.4 Estado de infraestructura

La infraestructura del MVP se encuentra en estado **funcional para demostración**.

La configuración utilizada durante el Hackathon responde a las necesidades actuales del MVP y puede evolucionar posteriormente de acuerdo con requerimientos de:

- Escalabilidad.
- Disponibilidad.
- Seguridad.
- Capacidad.
- Automatización.
- Operación continua.

Las futuras modificaciones de infraestructura deberán mantener la separación entre la lógica de aplicación y los recursos de la plataforma cloud.

---

# 13. Seguridad y consideraciones operativas

La seguridad de AyniKortex se aborda considerando la separación de responsabilidades entre los componentes y la protección de los recursos utilizados durante el despliegue.

## 13.1 Principios de seguridad

La solución considera los siguientes principios:

- Separación entre componentes de aplicación e infraestructura.
- Validación de las solicitudes recibidas por los servicios.
- Uso de variables de entorno y mecanismos de configuración para información sensible.
- Exclusión de credenciales y secretos del código fuente.
- Gestión controlada de accesos a los recursos cloud.
- Uso de repositorios y mecanismos de control de versiones para mantener trazabilidad de los cambios.

## 13.2 Protección de credenciales

Las credenciales, claves privadas y demás información sensible utilizada durante el desarrollo o despliegue no deben almacenarse directamente en el repositorio.

Los procesos automatizados utilizan mecanismos de configuración segura, como los **Secrets de GitHub Actions**, para proporcionar las credenciales necesarias durante la ejecución de los flujos correspondientes.

## 13.3 Configuración de servicios

Los parámetros de conexión y configuración de los componentes deben gestionarse mediante mecanismos externos a la lógica de aplicación cuando contengan información específica del entorno.

Esto permite separar la configuración del código y facilita la utilización del mismo componente en diferentes entornos.

## 13.4 Consideraciones operativas

La infraestructura utilizada corresponde al alcance del MVP y está orientada principalmente a desarrollo, validación y demostración.

Por esta razón, aspectos como:

- Alta disponibilidad.
- Escalabilidad horizontal.
- Balanceo de carga.
- Recuperación ante desastres.
- Monitoreo avanzado.
- Gestión empresarial de secretos.

podrán ser considerados en futuras evoluciones de la plataforma.

La guía con los procedimientos concretos de despliegue y operación se encuentra en:

[☁️ Guía de despliegue](../Deployment-Guide/Deployment-Guide.md)

---

# 14. Estado actual del MVP

AyniKortex cuenta actualmente con un **MVP funcional de extremo a extremo**, integrando los principales componentes de la solución.

El sistema permite recibir contenido técnico, procesarlo mediante el componente de Data Science, ejecutar el modelo de Machine Learning y presentar el resultado de la clasificación al usuario.

## 14.1 Componentes implementados

```mermaid
flowchart LR
    "🌐 Frontend" --> "⚙️ Backend"
    "⚙️ Backend" --> "🤖 Data Science"
    "🤖 Data Science" --> "🧠 Modelo ML"
    "⚙️ Backend" --> "🗄️ MySQL"
    "🧠 Modelo ML" --> "📊 Clasificación"
    "📊 Clasificación" --> "⚙️ Backend"
    "⚙️ Backend" --> "🌐 Frontend"
```

Los principales elementos implementados son:

- Interfaz web para interacción con el usuario.
- Backend para gestión de solicitudes y lógica de negocio.
- Servicio de Data Science para procesamiento e inferencia.
- Modelo de Machine Learning para clasificación.
- Procesamiento de contenido textual y archivos compatibles.
- Persistencia de información.
- Integración entre los componentes.
- Despliegue del MVP en Oracle Cloud Infrastructure.

## 14.2 Estado de integración

Los principales componentes se encuentran integrados y permiten ejecutar el flujo completo de la solución.

La arquitectura actual refleja la evolución realizada durante el desarrollo del MVP y reemplaza las decisiones arquitectónicas iniciales que fueron modificadas durante la implementación.

Las decisiones históricas y su evolución se encuentran documentadas en:

[📚 Architecture Decision Records](../ADR/)

---

# 15. Evolución futura

La arquitectura de AyniKortex permite continuar evolucionando el sistema sin modificar necesariamente su estructura fundamental.

Entre las posibles líneas de evolución se consideran:

- Mejorar el modelo de clasificación mediante nuevos datos y procesos de entrenamiento.
- Ampliar las categorías y tipos de documentación soportados.
- Incrementar la cobertura de pruebas.
- Mejorar la observabilidad y monitoreo.
- Fortalecer los mecanismos de seguridad.
- Optimizar el despliegue y la automatización.
- Incorporar capacidades de escalabilidad.
- Evaluar nuevas técnicas de Inteligencia Artificial cuando aporten valor al producto.

Cualquier incorporación tecnológica que modifique significativamente la arquitectura deberá ser evaluada mediante la documentación arquitectónica correspondiente.

---

# 16. Referencias

La documentación de AyniKortex se encuentra organizada por área y nivel de detalle.

## Arquitectura

[🏗️ Arquitectura del sistema](../Architecture/Architecture.md)

Documento de referencia para la descripción detallada de la arquitectura vigente.

## Decisiones arquitectónicas

[📚 Architecture Decision Records](../ADR/)

Registro de las principales decisiones arquitectónicas y su evolución durante el desarrollo.

## API e integración

[🔗 Documentación de API](../api/README.md)

[📄 Especificación OpenAPI](../api/aynikortex-api.yaml)

[📄 Contrato Backend–Data Science](../api/Backend-Data-Contract.md)

[🗄️ Modelo de datos](../api/Backend-Data-Model.md)

## Data Science

[🤖 Documentación de Data Science](../SPRINTS/data-science/)

Documentación relacionada con dataset, procesamiento, entrenamiento, evaluación, persistencia, inferencia y pruebas del componente de Ciencia de Datos.

## Despliegue

[☁️ Guía de despliegue](../Deployment-Guide/Deployment-Guide.md)

Documentación relacionada con el despliegue y configuración de la solución en Oracle Cloud Infrastructure.

## Roadmap

[🗺️ Roadmap técnico](../ROADMAP/Technical-Roadmap.md)

Documento de referencia para la evolución técnica del proyecto.

## Estándares

[📐 Engineering Standards](../Standards/Engineering-Standards.md)

Lineamientos técnicos y de desarrollo utilizados durante la construcción del proyecto.

---

# 17. Trazabilidad documental

El SDS constituye el documento de diseño de alto nivel y se relaciona con los documentos especializados mediante la siguiente estructura:

```mermaid
flowchart LR
    "📘 SDS 2.0" --> "🏗️ Arquitectura"
    "📘 SDS 2.0" --> "📚 Decisiones arquitectónicas"
    "📘 SDS 2.0" --> "🔗 API e integración"
    "📘 SDS 2.0" --> "🤖 Data Science"
    "📘 SDS 2.0" --> "☁️ Despliegue"
    "📘 SDS 2.0" --> "🗺️ Roadmap"
    "📘 SDS 2.0" --> "📐 Estándares"
```

Esta organización permite mantener una única fuente de información para cada área y reducir la duplicación entre documentos.

Cuando una decisión, contrato o detalle técnico cambie, deberá actualizarse el documento especializado correspondiente y, cuando sea necesario, reflejar el cambio en este SDS.

---

# 18. Estado del documento

**Versión 2.0 — Vigente**

Este documento representa el diseño de alto nivel de la versión actual del MVP de AyniKortex.

La documentación podrá evolucionar junto con el proyecto. Los cambios que modifiquen decisiones arquitectónicas relevantes deberán quedar registrados mediante los mecanismos de documentación establecidos en el repositorio.

---
