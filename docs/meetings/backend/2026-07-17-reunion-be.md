# Acta de Reunión - Backend

## Información General

| Campo | Información |
|--------|-------------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **Equipo** | Backend |
| **Sprint** | BE-01 |
| **Fecha** | 17 de julio de 2026 |
| **Hora** |10:00 am |
| **Modalidad** | Discord |

---

# Participantes

- Equipo Backend

>* Giselle
>* Rodrigo 
>* José


---

# Objetivo de la reunión

Definir las bases técnicas para el desarrollo del Backend del proyecto TechMind, incluyendo arquitectura, tecnologías, convenciones de desarrollo y próximos pasos.

---

# Temas tratados

## 1. Roles de usuario

Se definieron los roles iniciales para el MVP.

### Administrator

Acceso completo (CRUD):

- POST `/contents`
- GET `/contents`
- GET `/contents/{id}`
- PUT `/contents/{id}`
- DELETE `/contents/{id}`

### General User

Acceso de consulta:

- GET `/contents`
- GET `/contents/{id}`

**Pendiente**

- Definir si el MVP implementará autenticación real o si los roles serán simulados.

---

## 2. Tecnologías

Se acordó utilizar:

- Java 21 LTS
- Spring Boot
- Base de datos (pendiente de definir)

---

## 3. Convenciones de desarrollo

Se acordó utilizar el idioma inglés para:

- Paquetes
- Clases
- Entidades
- Atributos
- Carpetas
- Ramas
- Commits

Con el objetivo de mantener consistencia y alinearse con buenas prácticas internacionales.

---

## 4. Arquitectura

Se propuso una arquitectura por capas compuesta por:

- Controller
- Service
- Repository
- Model

Estructura inicial del proyecto:

```text
controller/
service/
repository/
model/
config/
exception/
dto/        (por confirmar)
mapper/     (por confirmar)
```

---

## 5. Frontend

Se discutieron las siguientes alternativas para la interfaz de usuario:

- Thymeleaf
- Streamlit
- Frontend independiente desarrollado en React

La decisión queda pendiente.

---

# Acuerdos

| Nº | Acuerdo | Responsable |
|----|----------|-------------|
| 1 | Implementar arquitectura por capas. | Equipo Backend |
| 2 | Utilizar Java 21 LTS y Spring Boot. | Equipo Backend |
| 3 | Mantener nomenclatura en inglés en todo el proyecto. | Equipo Backend |
| 4 | Definir posteriormente la base de datos. | Equipo Backend |
| 5 | Evaluar la estrategia de autenticación del MVP. | Equipo Backend |
| 6 | Evaluar la tecnología del Frontend. | Equipo Técnico |

---

# Tareas

| Tarea | Responsable | Estado |
|--------|-------------|--------|
| Definir estrategia de ramas en Git. | Equipo Backend | 🟡 Pendiente |
| Definir la integración con Data Science. | Backend + Data Science | 🟡 Pendiente |
| Definir entidades y relaciones. | Equipo Backend | 🟡 Pendiente |
| Definir el motor de base de datos. | Equipo Backend | 🟡 Pendiente |
| Diseñar la API REST. | Equipo Backend | 🟡 Pendiente |

---

# Estado del Sprint

| Actividad | Estado |
|-----------|--------|
| Definición de tecnologías | ✅ Completado |
| Arquitectura inicial | ✅ Completado |
| Convenciones de desarrollo | ✅ Completado |
| Definición de entidades | 🟡 En progreso |
| Diseño API REST | ⏳ Pendiente |
| Definición Base de Datos | ⏳ Pendiente |
| Estrategia Git | ⏳ Pendiente |

---

# Riesgos identificados

- La decisión tardía del motor de base de datos puede afectar el desarrollo.
- La integración con Data Science requiere definir un contrato de comunicación.
- La decisión del Frontend puede impactar el diseño de la API.

---

# Bloqueos

No se identificaron bloqueos técnicos durante la reunión.

---

# Próximos pasos

1. Definir la estrategia de ramas en Git.
2. Definir la base de datos del proyecto.
3. Diseñar el modelo de dominio.
4. Diseñar la API REST.
5. Definir el contrato de integración con Data Science.
6. Seleccionar la tecnología definitiva para el Frontend.

---

# Próxima reunión

**Fecha:** Pendiente de definir.

**Objetivo:**

- Revisar el modelo de dominio.
- Validar la arquitectura.
- Definir la estrategia de integración con Data Science.
- Avanzar en el diseño de la API REST.

---

# Observaciones

- La arquitectura propuesta sigue un modelo por capas, favoreciendo la mantenibilidad y escalabilidad del proyecto.
- Se acordó utilizar inglés como estándar para todo el código fuente.
- La definición del contrato entre Backend y Data Science será una prioridad para facilitar la integración entre ambos equipos.

---

# Control del documento

| Versión | Fecha | Autor | Descripción |
|---------|--------|--------|-------------|
| 1.0 | 2026-07-17 | Equipo Backend | Creación del acta de la reunión inicial del equipo Backend. |