# Git Development Workflow

**Proyecto:** TechMind – Organización Inteligente del Conocimiento Técnico

**Versión:** 1.0

**Estado:** Aprobado

---

# 1. Objetivo

Establecer un flujo de trabajo estándar para el uso de Git y GitHub durante el desarrollo del proyecto, garantizando la trazabilidad, la colaboración y la calidad del código.

---

# 2. Estrategia de Ramas

Se adopta una estrategia basada en una rama principal y ramas de trabajo por funcionalidad.

main
│
├── feature/backend-*
├── feature/frontend-*
├── feature/data-science-*
└── hotfix/*

## main

Contiene únicamente versiones estables y aprobadas del proyecto.

No se permite el desarrollo directo sobre esta rama.

---

# 3. Convención de Nombres

## Backend

feature/backend-api
feature/backend-auth
feature/backend-classifier

## Frontend

feature/frontend-ui
feature/frontend-dashboard

## Data Science

feature/data-science-dataset
feature/data-science-cleaning
feature/data-science-training

## Correcciones

hotfix/nombre-del-error

---

# 4. Flujo de Trabajo

1. Crear una nueva rama desde `main`.
2. Implementar los cambios.
3. Ejecutar pruebas locales.
4. Actualizar la documentación correspondiente.
5. Realizar commit.
6. Publicar la rama en GitHub.
7. Crear Pull Request.
8. Revisar el código.
9. Aprobar.
10. Realizar Merge hacia `main`.

---

# 5. Commits

Los mensajes de commit seguirán el estándar Conventional Commits.

## Convención de Commits

El proyecto adopta el estándar **Conventional Commits** para mantener un historial de cambios claro, consistente y fácilmente trazable.

### Tabla de referencia

| Prefijo | Significado | Ejemplo |
|---------|-------------|----------|
| **feat** | Nueva funcionalidad | `feat: implementar clasificador de documentos` |
| **fix** | Corrección de errores | `fix: corregir validación de etiquetas` |
| **docs** | Cambios en la documentación | `docs: actualizar Sprint DS-03` |
| **test** | Incorporación o actualización de pruebas | `test: agregar pruebas del módulo de entrenamiento` |
| **refactor** | Reestructuración del código sin cambiar su comportamiento | `refactor: reorganizar componente de Ciencia de Datos` |
| **chore** | Tareas de mantenimiento | `chore: actualizar dependencias` |
| **style** | Cambios de formato (sin modificar la lógica) | `style: aplicar formato con Black` |
| **perf** | Mejoras de rendimiento | `perf: optimizar carga del Dataset Maestro` |
| **ci** | Cambios en integración o despliegue continuo | `ci: actualizar flujo de GitHub Actions` |
| **build** | Cambios en compilación o empaquetado | `build: actualizar configuración de Docker` |

### Recomendaciones

- Mantener los **prefijos en inglés**, siguiendo el estándar *Conventional Commits*.
- Escribir la **descripción en español**, utilizando verbos en modo imperativo (por ejemplo: *implementar*, *corregir*, *actualizar*, *agregar*).
- Realizar commits pequeños, frecuentes y enfocados en un único cambio.
- Relacionar cada commit con el Sprint o la funcionalidad correspondiente cuando sea posible.

## Ejemplos

feat: implementar integración del dataset

fix: corregir error en el analizador de archivos CSV

docs: actualizar documentación del Sprint DS-03

test: agregar pruebas de validación del dataset

refactor: simplificar el pipeline de preprocesamiento

chore: actualizar dependencias del proyecto


Nota: El uso de Conventional Commits facilita la revisión del historial del proyecto, mejora la trazabilidad de los cambios y permite integrar herramientas de automatización para la generación de versiones (versioning) y registros de cambios (CHANGELOG).

---

# 6. Pull Requests

Todo Pull Request deberá incluir:

- Objetivo del cambio.
- Sprint asociado.
- Archivos modificados.
- Evidencia de pruebas (si aplica).
- Documentación actualizada.

---

# 7. Revisión de Código

Antes de aprobar un Pull Request se verificará:

- Cumplimiento de estándares.
- Código funcional.
- Ausencia de errores evidentes.
- Documentación actualizada.
- Pruebas ejecutadas.
- No existen conflictos con `main`.

---

# 8. Relación con los Sprints

Cada Sprint deberá generar:

- Código.
- Documentación.
- Artefactos.
- Commits asociados.

No se cerrará un Sprint sin que los cambios estén integrados en la rama principal.

---

# 9. Buenas Prácticas

- Realizar commits pequeños y frecuentes.
- Mantener las ramas actualizadas con `main`.
- No subir archivos temporales.
- No subir credenciales o información sensible.
- Mantener el `.gitignore` actualizado.
- Documentar los cambios relevantes.

---

# 10. Criterios de Aceptación

El flujo de trabajo se considerará correctamente aplicado cuando:

- Todas las funcionalidades se desarrollen en ramas independientes.
- No existan commits directos sobre `main`.
- Todos los cambios sean revisados mediante Pull Request.
- La documentación se mantenga sincronizada con el código.