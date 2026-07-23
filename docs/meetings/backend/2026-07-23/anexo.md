# Anexo A. Glosario del Modelo de Datos

## Entidad User

| Campo         | Descripción                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------- |
| **id**        | Identificador único del usuario. Se genera automáticamente mediante UUID.                     |
| **name**      | Nombre del usuario que registra contenido dentro de la plataforma.                            |
| **email**     | Correo electrónico del usuario. Debe ser único dentro del sistema.                            |
| **password**  | Contraseña del usuario. En el MVP podrá permanecer nula hasta implementar autenticación.      |
| **role**      | Rol del usuario dentro del sistema. Determina las funcionalidades disponibles (ADMIN o USER). |
| **createdAt** | Fecha y hora en que el usuario fue creado dentro del sistema.                                 |

---

## Entidad Content

| Campo            | Descripción                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **id**           | Identificador único del contenido. Se genera mediante UUID.                                                                                        |
| **title**        | Nombre o título del contenido registrado por el usuario.                                                                                           |
| **description**  | un resumen corto escrito por el usuario (máximo unos cientos de caracteres), útil para mostrar en listados                                         |
| **contentType**  | Tipo de contenido registrado. Define cómo será procesado por el backend y qué endpoint de Ciencia de Datos se utilizará.                           |
| **textContent**  | Contenido escrito por el usuario cuando el tipo es **TEXT**. Se almacena para futuras consultas y búsquedas.                                       |
| **fileName**     | Nombre original del archivo cargado por el usuario. Solo aplica cuando el contenido es un archivo.                                                 |
| **filePath**     | Ruta o URL donde se almacena físicamente el archivo. Permite recuperarlo posteriormente sin guardar el archivo dentro de la base de datos.         |
| **category**     | Categoría principal asignada automáticamente por el modelo de Machine Learning.                                                                    |
| **subcategory**  | Subcategoría asignada automáticamente por el modelo de Machine Learning.                                                                           |
| **confidence**   | Nivel de confianza de la clasificación realizada por el modelo. Su valor estará entre 0.0 y 1.0.                                                   |
| **modelVersion** | Versión del modelo de Machine Learning utilizada para generar la clasificación.                                                                    |
| **keywords**     | Lista de palabras clave identificadas por el modelo de IA junto con su relevancia. Se almacena para facilitar búsquedas y contenidos relacionados. |
| **createdAt**    | Fecha y hora en que el contenido fue registrado en TechMind.                                                                                       |
| **updatedAt**    | Fecha y hora de la última modificación realizada sobre el contenido.                                                                               |
| **user_id**      | Referencia al usuario propietario del contenido. Establece la relación entre User y Content.                                                       |

---

# Enumeraciones

## Role

Define el tipo de usuario dentro del sistema.

| Valor     | Descripción                                                                     |
| --------- | ------------------------------------------------------------------------------- |
| **ADMIN** | Puede administrar el contenido y gestionar usuarios (según el alcance del MVP). |
| **USER**  | Puede registrar y consultar sus propios contenidos.                             |

---

## ContentType

Define el tipo de contenido registrado por el usuario.

| Valor    | Descripción                                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------- |
| **TEXT** | El usuario escribe directamente el contenido en la aplicación. El backend consumirá el endpoint `/api/v1/predict/text`. |
| **FILE** | El usuario carga un archivo (PDF, DOCX, TXT, MD). El backend consumirá el endpoint `/api/v1/predict/file`.              |

---

# Campos generados por Inteligencia Artificial

Los siguientes atributos **no son capturados por el usuario**.

Son generados automáticamente por el componente de Ciencia de Datos.

| Campo        | Generado por               |
| ------------ | -------------------------- |
| category     | Modelo de Machine Learning |
| subcategory  | Modelo de Machine Learning |
| confidence   | Modelo de Machine Learning |
| modelVersion | API de Ciencia de Datos    |
| keywords     | Modelo de Machine Learning |

---

# Flujo de almacenamiento

## Cuando el contenido es texto

Usuario

↓

Escribe texto

↓

Backend guarda:

- title
- description
- textContent

↓

Backend envía el texto a Ciencia de Datos

↓

Recibe:

- category
- subcategory
- confidence
- keywords
- modelVersion

↓

Actualiza el registro en la base de datos

---

## Cuando el contenido es un archivo

Usuario

↓

Sube un archivo

↓

Backend almacena el archivo

↓

Guarda:

- fileName
- filePath

↓

Envía el archivo a Ciencia de Datos

↓

Recibe la clasificación

↓

Actualiza:

- category
- subcategory
- confidence
- keywords
- modelVersion
