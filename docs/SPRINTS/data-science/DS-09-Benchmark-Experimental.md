# 📊 DS-09 – Benchmark Experimental del Modelo

> **Proyecto:** AyniKortex  
> **Componente:** Data Science  
> **Sprint:** DS-09  
> **Estado:** 🚧 En planificación

---

# 🎯 Objetivo

Diseñar y ejecutar un proceso de evaluación comparativa (Benchmark Experimental) para analizar el desempeño del modelo de Machine Learning bajo diferentes tamaños de entrenamiento y determinar la configuración que ofrece el mejor equilibrio entre precisión, rendimiento y costo computacional para el MVP.

---

# 📌 Alcance

Este documento define la metodología, métricas y criterios que se utilizarán para evaluar los modelos entrenados.

El Benchmark permitirá comparar objetivamente distintas configuraciones del modelo antes de su validación final e integración definitiva al MVP.

---

# 🧪 Metodología

El Benchmark se desarrollará en dos fases.

## Fase A – Diseño del Benchmark

Durante esta fase se definirán:

- Objetivos del Benchmark.
- Diseño experimental.
- Métricas de evaluación.
- Criterios de selección.
- Plantillas de tablas.
- Plantillas de gráficos.
- Conjunto de pruebas (Gold Test Set).

---

## Fase B – Ejecución del Benchmark

Durante esta fase se realizarán las pruebas experimentales.

Actividades:

- Entrenamiento de los modelos.
- Evaluación mediante el Gold Test Set.
- Registro de resultados.
- Comparación de métricas.
- Elaboración de gráficos.
- Selección del modelo recomendado.

---

# 📚 Diseño Experimental

Se propone entrenar diferentes modelos utilizando conjuntos de datos de distintos tamaños para evaluar el impacto del volumen de información sobre el rendimiento del modelo.

## Experimentos

| Experimento | Dataset | Estado |
|-------------|---------|:------:|
| EXP-01 | 1,000 registros | ⏳ |
| EXP-02 | 2,500 registros | ⏳ |
| EXP-03 | 5,000 registros | ⏳ |
| EXP-04 | 7,500 registros | ⏳ |
| EXP-05 | 10,000 registros | ⏳ |

---

# 🏆 Gold Test Set

Todos los modelos serán evaluados utilizando exactamente el mismo conjunto de pruebas.

Este conjunto permanecerá fijo durante todo el Benchmark para garantizar resultados comparables.

## Objetivo

Evaluar todos los modelos bajo las mismas condiciones.

## Estado

⏳ Pendiente de construcción.

---

# 📏 Métricas de Evaluación

Cada modelo será evaluado utilizando las siguientes métricas.

| Métrica | Descripción |
|----------|-------------|
| Accuracy | Exactitud global del modelo |
| Precision | Precisión por clase |
| Recall | Cobertura de clasificación |
| F1-Score | Balance entre Precision y Recall |
| Tiempo de entrenamiento | Tiempo requerido para entrenar el modelo |
| Tiempo de inferencia | Tiempo promedio de respuesta |
| Tamaño del modelo | Espacio ocupado en disco |
| Uso de memoria | Consumo durante la inferencia |

---

# 📊 Plantilla de Resultados

| Modelo | Accuracy | Precision | Recall | F1 | Tiempo Entrenamiento | Tiempo Inferencia |
|---------|----------|-----------|--------|----|----------------------|-------------------|
| 1K | - | - | - | - | - | - |
| 2.5K | - | - | - | - | - | - |
| 5K | - | - | - | - | - | - |
| 7.5K | - | - | - | - | - | - |
| 10K | - | - | - | - | - | - |

---

# 📈 Visualización de Resultados

Al finalizar el Benchmark se generarán gráficos comparativos para facilitar el análisis de los resultados.

Gráficos previstos:

- Accuracy vs Tamaño del Dataset.
- Precision vs Tamaño del Dataset.
- Recall vs Tamaño del Dataset.
- F1-Score vs Tamaño del Dataset.
- Tiempo de entrenamiento.
- Tiempo de inferencia.
- Comparativa general de métricas.

---

# ✅ Criterios de Selección

El modelo recomendado para el MVP deberá cumplir con los siguientes criterios:

- Alcanzar el mayor F1-Score posible.
- Mantener un tiempo de inferencia adecuado para un sistema interactivo.
- Presentar un equilibrio entre rendimiento y costo computacional.
- Ser estable frente a diferentes tipos de documentos.
- Integrarse correctamente con el componente Backend mediante la interfaz `predict(title, text)`.

---

# 📋 Resultados

> Esta sección será completada durante la ejecución del Benchmark.

Se documentarán:

- Resultados obtenidos por cada modelo.
- Tablas comparativas.
- Gráficos.
- Observaciones relevantes.

---

# 🔍 Análisis

En esta sección se realizará el análisis comparativo de todos los experimentos.

Se evaluarán aspectos como:

- Evolución del rendimiento.
- Impacto del tamaño del dataset.
- Beneficios y limitaciones de cada configuración.
- Relación entre precisión y tiempo de respuesta.

---

# 🏁 Conclusiones

Al finalizar el Benchmark se documentarán las conclusiones obtenidas.

Entre ellas:

- Modelo recomendado.
- Justificación técnica de la selección.
- Limitaciones encontradas.
- Posibles mejoras futuras.

---

# 📌 Estado del Documento

| Actividad | Estado |
|------------|:------:|
| Diseño del Benchmark | ✅ |
| Definición de métricas | ✅ |
| Diseño experimental | ✅ |
| Construcción del Gold Test Set | ⏳ |
| Entrenamiento de modelos | ⏳ |
| Ejecución del Benchmark | ⏳ |
| Análisis de resultados | ⏳ |
| Conclusiones | ⏳ |

---

# 📖 Referencias

- Documentación técnica del proyecto AyniKortex.
- DS-06 – Entrenamiento del Modelo.
- DS-07 – Integración del Modelo.
- DS-08 – Persistencia del Modelo.
- Project Master Roadmap.