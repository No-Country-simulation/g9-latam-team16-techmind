# 🧠 AyniKortex – Componente Data Science

> Componente responsable del procesamiento de datos, entrenamiento e inferencia de modelos de Machine Learning para la clasificación inteligente de documentación técnica dentro de la plataforma **AyniKortex**.

---

## Estado del Componente

| Información | Valor |
|--------------|-------|
| Proyecto | AyniKortex |
| Componente | Data Science |
| Estado | ✅ DS-08 Completado |
| Arquitectura | Modular |
| Lenguaje | Python |
| Modelo | Machine Learning Clásico |
| Integración | Backend (DS-09) |
| Pruebas | ✅ 212 / 212 exitosas |

---

## Descripción

El componente **Data Science** de **AyniKortex** implementa el ciclo de vida completo del modelo de Machine Learning utilizado para la clasificación automática de documentación técnica.

Su responsabilidad comprende la adquisición de datos, construcción del Dataset Maestro, preprocesamiento, ingeniería de características, entrenamiento, persistencia e inferencia del modelo, proporcionando una interfaz estable para su integración con el componente Backend.

La arquitectura del componente ha sido diseñada siguiendo principios de modularidad, escalabilidad y mantenibilidad, permitiendo la incorporación de nuevas fuentes de información, técnicas de procesamiento y modelos de clasificación con un impacto mínimo sobre el resto del sistema.

---

# Objetivos

## Objetivo General

Desarrollar y mantener el componente **Data Science** de **AyniKortex**, responsable del procesamiento de datos y del ciclo de vida completo del modelo de Machine Learning para la clasificación inteligente de documentación técnica, proporcionando resultados confiables y una integración estable con el componente Backend.

## Objetivos Específicos

- Adquirir e integrar información proveniente de múltiples fuentes de datos.
- Construir y mantener un **Dataset Maestro** estructurado y de alta calidad.
- Validar la integridad, consistencia y calidad de los datos antes de su procesamiento.
- Implementar un pipeline de preprocesamiento que transforme los documentos en información apta para el entrenamiento del modelo.
- Generar representaciones numéricas mediante técnicas de ingeniería de características.
- Entrenar, evaluar y seleccionar modelos de Machine Learning para la clasificación documental.
- Persistir los artefactos del modelo para garantizar inferencias reproducibles.
- Ejecutar predicciones mediante un motor de inferencia optimizado.
- Proporcionar una interfaz estable que facilite la integración con el componente Backend.

---

# Estado del Componente

El componente **Data Science** de **AyniKortex** ha completado las funcionalidades planificadas hasta el **Sprint DS-08**, consolidando una arquitectura modular y un pipeline de Machine Learning capaz de procesar documentos técnicos desde su adquisición hasta la generación de predicciones.

## Estado de Desarrollo

| Área | Estado | Observaciones |
|------|:------:|---------------|
| Arquitectura del Componente | ✅ | Diseño modular implementado |
| Adquisición de Datos | ✅ | Readers y Loaders implementados |
| Dataset Maestro | ✅ | Integración y validación completadas |
| Preprocesamiento | ✅ | Pipeline implementado y validado |
| Ingeniería de Características | ✅ | Pipeline de transformación implementado |
| Entrenamiento del Modelo | ✅ | Modelo de clasificación entrenado |
| Persistencia del Modelo | ✅ | Artefactos serializados y validados |
| Motor de Inferencia | ✅ | Pipeline de predicción implementado |
| API REST | ⏳ | Planificada para DS-09 |
| Integración con Backend | ⏳ | Planificada para DS-09 |
| Optimización | ⏳ | Planificada para DS-10 |

## Indicadores del Componente

| Indicador | Estado |
|-----------|:------:|
| Dataset Maestro | ✅ |
| Modelo Entrenado | ✅ |
| Modelo Persistido | ✅ |
| Motor de Inferencia | ✅ |
| Arquitectura Modular | ✅ |
| Pruebas Automatizadas | ✅ 212 / 212 |

> **Estado actual:** El componente se encuentra listo para iniciar la implementación de la API REST y su integración con el componente Backend durante el Sprint **DS-09**.

---

# Arquitectura General

El componente **Data Science** de **AyniKortex** implementa una arquitectura modular basada en responsabilidades específicas, donde cada módulo participa en una etapa del ciclo de vida del modelo de Machine Learning.

Desde la adquisición de documentos hasta la generación de predicciones, cada componente opera de forma independiente, facilitando la mantenibilidad, reutilización y evolución del sistema.

La arquitectura permite incorporar nuevas fuentes de información, técnicas de procesamiento y modelos de clasificación sin afectar el funcionamiento del resto del pipeline.

## Arquitectura del Componente

```mermaid
flowchart LR

Fuentes_de_Datos["Fuentes de Datos"]
    --> Readers["Readers"]

Readers
    --> Dataset_Maestro["Dataset Maestro"]

Dataset_Maestro
    --> Preprocesamiento["Preprocesamiento"]

Preprocesamiento
    --> Ingenieria_de_Caracteristicas["Ingeniería de Características"]

Ingenieria_de_Caracteristicas
    --> Entrenamiento["Entrenamiento"]

Entrenamiento
    --> Persistencia["Persistencia del Modelo"]

Persistencia
    --> Motor_de_Inferencia["Motor de Inferencia"]

Motor_de_Inferencia
    --> Backend["Backend"]
```

## Componentes de la Arquitectura

### Fuentes de Datos

Representan el origen de la información utilizada para construir el Dataset Maestro. El componente puede incorporar documentos provenientes de múltiples fuentes sin modificar el resto del pipeline.

### Readers

Interpretan el contenido de los documentos según su formato (TXT, CSV, JSON, PDF, entre otros) y generan una representación uniforme para su procesamiento.

### Dataset Maestro

Integra la información proveniente de todas las fuentes en una estructura única, validada y consistente, que sirve como base para el entrenamiento del modelo.

### Preprocesamiento

Ejecuta las tareas de limpieza, normalización y transformación del texto para preparar los documentos antes de la extracción de características.

### Ingeniería de Características

Convierte el texto procesado en representaciones numéricas que pueden ser utilizadas por los algoritmos de Machine Learning.

### Entrenamiento

Construye el modelo de clasificación documental utilizando el Dataset Maestro preparado y las características generadas.

### Persistencia del Modelo

Almacena los artefactos generados durante el entrenamiento, garantizando que puedan reutilizarse durante la inferencia sin necesidad de volver a entrenar el modelo.

### Motor de Inferencia

Carga los artefactos persistidos, ejecuta el pipeline de predicción y genera la categoría y el nivel de confianza para cada documento procesado.

### Backend

Consume el motor de inferencia mediante una interfaz estable para ofrecer las funcionalidades de clasificación al resto de la plataforma.

---

## Principios de Arquitectura

La arquitectura del componente se fundamenta en los siguientes principios:

- **Arquitectura Modular:** cada módulo implementa una responsabilidad claramente definida.
- **Responsabilidad Única (SRP):** cada componente realiza una única función dentro del pipeline.
- **Bajo Acoplamiento:** los módulos interactúan mediante interfaces bien definidas.
- **Alta Cohesión:** funcionalidades relacionadas permanecen agrupadas.
- **Extensibilidad:** nuevas fuentes, algoritmos o técnicas pueden incorporarse sin modificar el núcleo del sistema.
- **Reutilización:** los componentes pueden utilizarse tanto durante el entrenamiento como durante la inferencia.
- **Mantenibilidad:** la organización del código facilita la evolución del proyecto y la incorporación de nuevas funcionalidades.

---

# Estructura del Proyecto

El componente **Data Science** de **AyniKortex** está organizado siguiendo una arquitectura modular, donde cada directorio representa una responsabilidad específica dentro del ciclo de vida del modelo de Machine Learning.

Esta organización facilita la mantenibilidad, reutilización del código y escalabilidad del componente, permitiendo incorporar nuevas funcionalidades sin afectar el resto del sistema.

## Estructura General

```text
src/
└── data_science/
    ├── adapters/
    ├── data/
    ├── loaders/
    ├── ml/
    │   ├── evaluation/
    │   ├── exceptions/
    │   ├── features/
    │   ├── inference/
    │   ├── persistence/
    │   └── training/
    ├── preprocessing/
    ├── readers/
    ├── services/
    ├── utils/
    ├── config.py
    ├── README.md
    └── __init__.py
```

## Descripción de los Directorios

| Directorio | Responsabilidad |
|------------|-----------------|
| **adapters/** | Adaptadores que facilitan la conversión de estructuras de datos entre los distintos componentes del sistema. |
| **data/** | Construcción, integración y validación del Dataset Maestro utilizado durante el entrenamiento y la inferencia. |
| **loaders/** | Obtención y carga de documentos desde las diferentes fuentes de información soportadas por el sistema. |
| **readers/** | Lectura e interpretación de archivos en distintos formatos (TXT, CSV, JSON, PDF, entre otros). |
| **preprocessing/** | Limpieza, normalización y preparación del texto antes de la extracción de características. |
| **ml/features/** | Implementación de la ingeniería de características y transformación del texto en representaciones numéricas para el modelo de Machine Learning. |
| **ml/training/** | Entrenamiento, validación y selección del modelo de clasificación documental. |
| **ml/evaluation/** | Evaluación del desempeño del modelo mediante métricas y procesos de validación. |
| **ml/persistence/** | Persistencia y recuperación de los artefactos generados durante el entrenamiento del modelo. |
| **ml/inference/** | Implementación del motor de inferencia encargado de generar predicciones utilizando el modelo persistido. |
| **ml/exceptions/** | Definición de excepciones personalizadas utilizadas por los módulos de Machine Learning para el manejo controlado de errores. |
| **services/** | Servicios de alto nivel encargados de orquestar procesos del componente. |
| **utils/** | Funciones auxiliares y utilidades compartidas entre los diferentes módulos. |
| **config.py** | Configuración centralizada del componente Data Science. |

## Organización de las Pruebas

La estructura de pruebas mantiene la misma organización modular del componente principal, permitiendo validar cada módulo de forma independiente.

```text
tests/
└── data_science/
    ├── fixtures/
    ├── readers/
    ├── preprocessing/
    ├── ml/
    │   ├── features/
    │   ├── training/
    │   ├── evaluation/
    │   ├── persistence/
    │   └── inference/
```

Esta organización favorece la trazabilidad entre el código fuente y sus pruebas automatizadas, facilitando el mantenimiento, la depuración y la incorporación de nuevas funcionalidades.

---

# Pipeline de Machine Learning

El componente **Data Science** implementa un pipeline secuencial que transforma documentos técnicos en predicciones mediante un proceso estructurado de preparación de datos, entrenamiento e inferencia.

Cada etapa del pipeline recibe la salida de la etapa anterior, garantizando un flujo consistente y reproducible durante el entrenamiento y la clasificación de documentos.

## Flujo General

```mermaid
flowchart LR

Fuentes_de_Datos["Fuentes de Datos"]
    --> Readers["Readers"]

Readers
    --> Dataset_Maestro["Dataset Maestro"]

Dataset_Maestro
    --> Preprocesamiento["Preprocesamiento"]

Preprocesamiento
    --> Caracteristicas["Ingeniería de Características"]

Caracteristicas
    --> Entrenamiento["Entrenamiento"]

Entrenamiento
    --> Evaluacion["Evaluación"]

Evaluacion
    --> Persistencia["Persistencia del Modelo"]

Persistencia
    --> Inferencia["Motor de Inferencia"]

Inferencia
    --> Prediccion["Predicción"]
```

## Etapas del Pipeline

### Adquisición de Datos

Los documentos son obtenidos desde diferentes fuentes de información mediante los módulos **Loaders** y **Readers**, proporcionando una representación uniforme para el resto del proceso.

### Construcción del Dataset Maestro

La información recopilada se integra en un único conjunto de datos estructurado y validado, que constituye la base para el entrenamiento del modelo.

### Preprocesamiento

Los documentos son limpiados, normalizados y preparados para garantizar la calidad de la información utilizada por el modelo de Machine Learning.

### Ingeniería de Características

El texto preprocesado se transforma en representaciones numéricas que permiten al modelo identificar patrones y realizar el proceso de clasificación.

### Entrenamiento

Se construye y ajusta el modelo de clasificación utilizando el conjunto de datos preparado durante las etapas anteriores.

### Evaluación

El modelo entrenado es evaluado mediante métricas de desempeño para verificar su capacidad de generalización y precisión.

### Persistencia del Modelo

Los artefactos generados durante el entrenamiento se almacenan para que puedan reutilizarse posteriormente durante la inferencia.

### Motor de Inferencia

El motor de inferencia carga los artefactos persistidos, procesa nuevos documentos y genera la categoría predicha junto con el nivel de confianza asociado.

## Beneficios del Pipeline

- Arquitectura modular y escalable.
- Separación clara de responsabilidades.
- Reutilización de componentes entre entrenamiento e inferencia.
- Facilidad para incorporar nuevas fuentes de datos y algoritmos.
- Flujo reproducible para el entrenamiento y la generación de predicciones.

---

# Integración con Backend

El componente **Data Science** se integra con el componente **Backend** de **AyniKortex** para proporcionar funcionalidades de clasificación automática de documentación técnica.

Durante el **Sprint DS-09**, el motor de inferencia será expuesto mediante una API REST, permitiendo que el Backend solicite predicciones utilizando documentos proporcionados por los usuarios.

## Flujo de Integración

```mermaid
flowchart LR

Frontend["Frontend"]
    --> Backend["Backend"]

Backend
    --> API["API REST"]

API
    --> Inferencia["Motor de Inferencia"]

Inferencia
    --> Modelo["Modelo Persistido"]

Modelo
    --> Resultado["Predicción"]

Resultado
    --> Backend
```

## Responsabilidades

### Backend

- Recibir las solicitudes de clasificación.
- Validar la información recibida.
- Invocar el componente Data Science.
- Procesar la respuesta y entregarla al Frontend.

### Data Science

- Cargar el modelo entrenado.
- Ejecutar el pipeline de inferencia.
- Generar la categoría predicha.
- Calcular el nivel de confianza de la predicción.
- Devolver un resultado estructurado al Backend.

## Estado de la Integración

| Componente | Estado |
|------------|:------:|
| Contrato de integración | ✅ Definido |
| Motor de inferencia | ✅ Implementado |
| API REST | ⏳ DS-09 |
| Integración Backend | ⏳ DS-09 |

---

# Roadmap

El desarrollo del componente **Data Science** sigue una estrategia incremental, donde cada Sprint incorpora nuevas capacidades hasta completar el ciclo de vida del modelo de Machine Learning.

## Estado de los Sprints

| Sprint | Descripción | Estado |
|---------|-------------|:------:|
| DS-01 | Arquitectura del Componente | ✅ |
| DS-02 | Investigación y Adquisición del Dataset | ✅ |
| DS-03 | Construcción del Dataset Maestro | ✅ |
| DS-04 | Preprocesamiento del Dataset | ✅ |
| DS-05 | Ingeniería de Características | ✅ |
| DS-06 | Entrenamiento del Modelo | ✅ |
| DS-07 | Persistencia del Modelo | ✅ |
| DS-08 | Motor de Inferencia | ✅ |
| DS-09 | API REST e Integración | ⏳ |
| DS-10 | Optimización del Modelo | ⏳ |

## Próximas Etapas

Las siguientes actividades estarán enfocadas en:

- Implementación de la API REST para exponer el motor de inferencia.
- Integración completa con el componente Backend.
- Optimización del rendimiento del modelo y del proceso de inferencia.
- Validación del sistema integrado.

---

# Instalación y Ejecución

## Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd aynikortex
```

## Crear un Entorno Virtual

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar las Pruebas

```bash
pytest
```

Para obtener un reporte detallado:

```bash
pytest -v
```

---

# Documentación Relacionada

La documentación técnica del componente se encuentra organizada en el directorio **docs/**.

## Documentación Principal

- Software Design Specification (SDS)
- Architecture
- Technical Roadmap
- Engineering Standards

## Sprints de Data Science

- DS-01 – Arquitectura del Componente
- DS-02 – Investigación y Adquisición del Dataset
- DS-03 – Construcción del Dataset Maestro
- DS-04 – Preprocesamiento del Dataset
- DS-05 – Ingeniería de Características
- DS-06 – Entrenamiento del Modelo
- DS-07 – Persistencia del Modelo
- DS-08 – Motor de Inferencia

## Arquitectura y Decisiones

- Architecture Decision Records (ADR)
- Contrato de Integración con Backend
- Modelo de Datos para Backend

---

# Próximos Pasos

El componente **Data Science** ha completado las funcionalidades planificadas hasta el **Sprint DS-08**, consolidando un pipeline de Machine Learning capaz de procesar documentos técnicos desde su adquisición hasta la generación de predicciones.

Las siguientes etapas estarán orientadas a la exposición del motor de inferencia mediante una API REST, su integración con el componente Backend y la optimización del rendimiento del sistema.

El desarrollo continuará siguiendo los principios de arquitectura modular, calidad del código, pruebas automatizadas y documentación continua, garantizando la evolución sostenible del componente dentro de la plataforma **AyniKortex**.