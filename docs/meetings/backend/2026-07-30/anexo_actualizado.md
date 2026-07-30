# Anexo A. Glosario del Modelo de Datos

## Entidad Content

| Campo            | Descripción                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **id**           | Identificador único del contenido. Se genera mediante UUID.                                                                                        |
| **title**        | Nombre o título del contenido registrado por el usuario.                                                                                           |
| **resume**       | un resumen corto proveniente de DS (máximo unos cientos de caracteres), útil para mostrar en listados                                              |
| **contentType**  | Tipo de contenido registrado. Define cómo será procesado por el backend y qué endpoint de Ciencia de Datos se utilizará. ENUM Text, File           |
| **fileFormat**   | Formato del archivo ENUM (pdf, docx, txt, md).                                                                                                     |
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

---

# Enumeraciones

## fileFormat

Define el formato del archivo que se sube para su procesamiento.

| Valor        | Descripción                            |
| ------------ | -------------------------------------- |
| **PDF**      | Documento en formato PDF (`.pdf`).     |
| **TXT**      | Archivo de texto plano (`.txt`).       |
| **DOCX**     | Documento de Microsoft Word (`.docx`). |
| **MARKDOWN** | Documento en formato Markdown (`.md`). |

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

Son generados automáticamente por el componente de Ciencia de Datos durante el proceso de clasificación del contenido.

| Campo            | Generado por               | Descripción                                                                                                 |
| ---------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `category`       | Modelo de Machine Learning | Categoría principal asignada al contenido.                                                                  |
| `subcategory`    | Modelo de Machine Learning | Subcategoría específica dentro de la categoría principal.                                                   |
| `confidence`     | Modelo de Machine Learning | Nivel de confianza de la clasificación, expresado como un valor decimal entre `0` y `1`.                    |
| `keywords`       | Modelo de Machine Learning | Lista de palabras clave relevantes identificadas en el contenido, cada una con su puntuación de relevancia. |
| `modelVersion`   | API de Ciencia de Datos    | Versión del modelo de Machine Learning que realizó la clasificación.                                        |
| `processingTime` | API de Ciencia de Datos    | Tiempo empleado para procesar la solicitud, expresado en milisegundos.                                      |
| `requestId`      | API de Ciencia de Datos    | Identificador único de la solicitud de clasificación generado por la API.                                   |
| `timestamp`      | API de Ciencia de Datos    | Fecha y hora en que se completó el procesamiento de la clasificación.                                       |

---

# Transformación de la respuesta de Ciencia de Datos

La API de Ciencia de Datos devuelve un objeto `ClassificationResponse` con información relacionada tanto con la clasificación como con la ejecución del proceso.

El backend transforma dicha respuesta y utiliza únicamente los atributos necesarios para el dominio de la aplicación.

| Campo recibido   | Persistido | Observación                                                                              |
| ---------------- | :--------: | ---------------------------------------------------------------------------------------- |
| `category`       |     ✅     | Categoría asignada al contenido.                                                         |
| `subcategory`    |     ✅     | Subcategoría asignada al contenido.                                                      |
| `confidence`     |     ✅     | Nivel de confianza de la clasificación.                                                  |
| `keywords`       |     ✅     | Palabras clave detectadas.                                                               |
| `modelVersion`   |     ✅     | Versión del modelo utilizada.                                                            |
| `requestId`      |     ❌     | Utilizado únicamente para trazabilidad de la integración.                                |
| `processingTime` |     ❌     | Información de monitoreo y rendimiento.                                                  |
| `timestamp`      |     ❌     | Marca temporal generada por la API de Ciencia de Datos.                                  |
| `status`         |     ❌     | Se utiliza para validar el resultado de la clasificación antes de procesar la respuesta. |

# Flujo de almacenamiento

## Cuando el contenido es texto

```
Usuario

↓

Escribe texto

↓

Backend guarda:

- title
- textContent
- contentType
- createdAt

↓

Backend envía el texto a Ciencia de Datos

↓

Recibe:

- category
- subcategory
- confidence
- keywords
- resume

↓

Actualiza el registro en la base de datos
```

---

## Cuando el contenido es un archivo

```
Usuario

↓

Sube un archivo

↓

Backend almacena el archivo

↓

Guarda:

- fileName
- filePath
- contentType
- fileFormat
- createdAt

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
- resume
```
