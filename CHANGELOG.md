# Changelog

Todos los cambios importantes del proyecto **TechMind** se documentan en este archivo.

El formato sigue la especificación de **Keep a Changelog** y el proyecto utiliza **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Backend

- En desarrollo.

### Data Science

- Preparación del Sprint DS-04 – Preprocesamiento del Dataset.

---

## [0.3.0] - 2026-07-19

### Added

#### Data Science

##### Readers

- Implementación de `BaseReader`.
- Implementación de `TextReader`.
- Implementación de `JsonReader`.
- Implementación de `CsvReader`.
- Implementación de `PdfReader`.
- Implementación de `ReaderFactory`.

##### Dataset Acquisition

- Implementación de `BaseLoader`.
- Implementación de `GitHubLoader`.
- Implementación de `TechnicalDocsLoader`.
- Implementación de `StackExchangeLoader`.
- Implementación de `HuggingFaceLoader`.
- Implementación de `MockLoader`.
- Implementación de `LoaderFactory`.

##### Domain

- Implementación del modelo `DocumentRecord`.

##### Testing

- Suite completa de pruebas para Readers.
- Suite completa de pruebas para Loaders.
- Suite completa de pruebas para Factories.
- 61 pruebas automatizadas.
- Cobertura del 98%.

### Changed

#### Data Science

- Se consolidó la arquitectura de adquisición de datos basada en Readers y Loaders.
- Se reorganizó la documentación del componente mediante un `README.md` independiente.

---

## [0.2.0] - 2026-07-15

### Added

#### Proyecto

- Arquitectura general aprobada.
- Organización inicial del repositorio.
- Definición de estándares de documentación.
- Inicio del componente Data Science.
- Inicio del componente Backend.

---

## [0.1.0] - 2026-07-14

### Added

#### Proyecto

- Creación del repositorio.
- Configuración inicial del proyecto.
- Definición de la estructura base.
- Configuración del entorno de desarrollo.