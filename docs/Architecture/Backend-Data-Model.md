# Backend-Data-Model

| Proyecto | AyniKortex |
|-----------|------------|
| Documento | Backend-Data-Model |
| Versión | 1.0 |
| Estado | En Diseño |
| Responsable | Equipo Data Science |
| Consumidor | Equipo Backend |

---

# Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|-------|--------|-------------|
| 1.0 | YYYY-MM-DD | Equipo Data Science | Versión inicial del Modelo de Datos para la integración entre Backend y Data Science. |

---

# 1. Introducción

Este documento define los modelos de datos utilizados para el intercambio de información entre los componentes **Backend** y **Data Science** del proyecto **AyniKortex**.

Su propósito es establecer una estructura común para las solicitudes y respuestas intercambiadas durante la ejecución de las capacidades descritas en el documento **Backend-Data-Contract.md**, garantizando que ambos equipos implementen la integración utilizando un contrato único, consistente e independiente de la tecnología utilizada.

Los modelos aquí definidos representan únicamente la estructura de los datos intercambiados entre componentes. La implementación técnica (REST, gRPC, mensajería, etc.) queda fuera del alcance de este documento.

---

# 2. Objetivo

Definir los modelos de datos que utilizarán los componentes **Backend** y **Data Science** para garantizar una integración consistente, desacoplada y compatible durante el intercambio de información.

Este documento constituye la referencia oficial para:

- definir las estructuras de solicitud (Request);
- definir las estructuras de respuesta (Response);
- establecer los modelos reutilizables compartidos entre ambos componentes;
- asegurar la compatibilidad entre futuras versiones del contrato.

---

# 3. Convenciones

Las siguientes convenciones aplican a todos los modelos definidos en este documento.

| Convención | Valor |
|------------|-------|
| Codificación | UTF-8 |
| Formato de Fechas | ISO-8601 |
| Zona Horaria | UTC |
| Identificadores | UUID |
| Enumeraciones | Valores en MAYÚSCULAS |
| Valores Opcionales | Se omiten cuando no existan |
| Formato de Texto | UTF-8 |

> [!IMPORTANT]
>
> Las convenciones definidas en este documento deberán ser respetadas por Backend y Data Science para garantizar la compatibilidad del contrato de integración.
>
> Cualquier modificación deberá reflejarse mediante el mecanismo de versionado definido en este documento.

---

# 4. Modelos de Solicitud

Este capítulo describe los modelos utilizados por Backend para solicitar la ejecución de las capacidades expuestas por el componente Data Science.

Los modelos de este capítulo reutilizan los objetos compartidos definidos en el **Capítulo 6**, evitando duplicidad de definiciones y facilitando la evolución del contrato.

---

## 4.1 ProcessDocumentRequest

Representa la solicitud enviada por Backend para incorporar un documento a la Base de Conocimiento.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| projectId | UUID | Sí | Identificador del proyecto al que pertenece el documento. |
| document | Document | Sí | Información del documento que será procesado. |
| uploadedAt | DateTime | Sí | Fecha y hora en que el documento fue incorporado por Backend. |
| metadata | RequestMetadata | No | Información adicional asociada a la solicitud. |

### Observaciones

- Backend es el propietario del documento.
- Data Science utilizará únicamente la información contenida en el objeto `Document`.
- La ubicación física del documento es transparente para Data Science; únicamente utilizará el atributo `uri` para acceder al recurso.

### Ejemplo

```json
{
  "projectId": "c3fa5d86-8a77-41b4-bc4c-8b3f9e95a2d1",
  "document": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "uri": "/documents/api-authentication.pdf",
    "type": "PDF"
  },
  "uploadedAt": "2026-07-21T15:20:00Z",
  "metadata": {
    "uploadedBy": "USR-1001",
    "source": "WEB",
    "language": "es"
  }
}
```

---

## 4.2 AnswerQuestionRequest

Representa la solicitud enviada por Backend para obtener una respuesta basada en la Base de Conocimiento.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| projectId | UUID | Sí | Proyecto sobre el cual se realizará la consulta. |
| question | String | Sí | Pregunta realizada por el usuario. |
| conversationId | UUID | No | Identificador de la conversación asociada a la consulta. |
| metadata | RequestMetadata | No | Información adicional proporcionada por Backend. |

### Observaciones

- Todas las consultas deberán ejecutarse dentro del contexto de un proyecto.
- El atributo `conversationId` permitirá mantener continuidad conversacional en futuras versiones del sistema.
- El contenido de `metadata` es opcional y podrá ampliarse sin romper la compatibilidad del contrato.

### Ejemplo

```json
{
  "projectId": "c3fa5d86-8a77-41b4-bc4c-8b3f9e95a2d1",
  "question": "¿Cómo funciona el proceso de autenticación?",
  "conversationId": "9d27a4f2-f4f4-4567-9e18-f55f3b0d12aa",
  "metadata": {
    "language": "es",
    "source": "WEB"
  }
}
```

---

# 5. Modelos de Respuesta

Este capítulo describe los modelos utilizados por el componente **Data Science** para responder las solicitudes realizadas por **Backend**.

Cada modelo representa el resultado de una capacidad definida en el documento **Backend-Data-Contract.md**.

Los modelos de este capítulo reutilizan los objetos compartidos definidos en el **Capítulo 6**, evitando la duplicidad de definiciones y facilitando la evolución del contrato.

---

## 5.1 ProcessDocumentResponse

Representa el resultado del procesamiento de un documento incorporado a la Base de Conocimiento.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| document | Document | Sí | Documento procesado. |
| status | Status | Sí | Estado del procesamiento. |
| processedAt | DateTime | Sí | Fecha y hora de finalización del procesamiento. |
| processingTime | Integer | Sí | Tiempo total empleado para procesar el documento, expresado en milisegundos. |
| message | String | No | Mensaje descriptivo del resultado del procesamiento. |
| statistics | Statistics | No | Estadísticas generadas durante el procesamiento. |

### Observaciones

- El atributo `status` representa el resultado general del procesamiento.
- El atributo `statistics` tiene únicamente fines informativos y no deberá utilizarse como parte de la lógica de negocio de Backend.
- La estructura del documento almacenado continúa siendo responsabilidad exclusiva de Backend.

### Ejemplo

```json
{
  "document": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "uri": "/documents/api-authentication.pdf",
    "type": "PDF"
  },
  "status": "SUCCESS",
  "processedAt": "2026-07-21T15:24:31Z",
  "processingTime": 3821,
  "message": "Documento incorporado correctamente a la Base de Conocimiento.",
  "statistics": {
    "pagesProcessed": 18,
    "chunksGenerated": 154,
    "detectedLanguage": "es",
    "documentCategory": "Arquitectura"
  }
}
```

---

## 5.2 AnswerQuestionResponse

Representa la respuesta generada por el componente Data Science a partir de la Base de Conocimiento.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| status | Status | Sí | Estado de la consulta realizada. |
| answer | String | Sí | Respuesta generada para el usuario. |
| generatedAt | DateTime | Sí | Fecha y hora de generación de la respuesta. |
| processingTime | Integer | Sí | Tiempo empleado para generar la respuesta, expresado en milisegundos. |
| message | String | No | Información adicional relacionada con la respuesta. |
| metadata | ResponseMetadata | No | Información complementaria generada durante la consulta. |

### Observaciones

- La respuesta corresponde únicamente a la información obtenida desde la Base de Conocimiento.
- El atributo `metadata` contiene información complementaria que podrá ampliarse en futuras versiones sin romper la compatibilidad del contrato.
- Backend es responsable de presentar la respuesta al usuario final.

### Ejemplo

```json
{
  "status": "SUCCESS",
  "answer": "La autenticación del sistema utiliza JWT para validar las solicitudes entre componentes.",
  "generatedAt": "2026-07-21T17:10:30Z",
  "processingTime": 842,
  "message": "Consulta procesada correctamente.",
  "metadata": {
    "confidence": 0.96,
    "references": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "title": "Guía de Arquitectura"
      },
      {
        "id": "66af7813-a48b-4894-8d95-8216cb3d85aa",
        "title": "Manual Backend"
      }
    ]
  }
}
```

---

# 6. Modelos Compartidos

Los modelos definidos en este capítulo representan estructuras de datos reutilizables por múltiples solicitudes y respuestas del contrato de integración entre **Backend** y **Data Science**.

Su propósito es evitar la duplicidad de definiciones, facilitar el mantenimiento del contrato y garantizar la consistencia entre las capacidades actuales y futuras del sistema.

Cada modelo describe únicamente la información necesaria para cumplir su propósito dentro del proceso de integración.

---

## 6.1 DocumentDescriptor

Representa la información mínima requerida por el componente **Data Science** para localizar y procesar un documento administrado por **Backend**.

Este modelo será utilizado únicamente en las solicitudes de procesamiento documental.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| id | UUID | Sí | Identificador único del documento. |
| uri | String | Sí | Ubicación física o lógica del documento administrada por Backend. |
| type | Enum | Sí | Tipo de documento que será procesado. |

### Enumeración type

| Valor | Descripción |
|--------|-------------|
| PDF | Documento PDF |
| DOCX | Documento Microsoft Word |
| TXT | Documento de texto plano |
| MD | Documento Markdown |

### Observaciones

- Backend es el propietario del documento.
- Data Science utilizará únicamente el atributo **uri** para acceder al contenido.
- La ubicación física del documento es transparente para Data Science.
- Nuevos formatos podrán incorporarse ampliando la enumeración **type** sin afectar la compatibilidad del contrato.

### Ejemplo

```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "uri": "/documents/api-authentication.pdf",
    "type": "PDF"
}
```

---

## 6.2 DocumentReference

Representa una referencia a un documento previamente conocido por Backend.

Este modelo será utilizado en las respuestas cuando únicamente sea necesario identificar el documento sobre el cual se ejecutó una operación.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| id | UUID | Sí | Identificador único del documento. |

### Observaciones

- No contiene información de ubicación ni de tipo documental.
- Backend ya dispone de dicha información.
- Su objetivo es reducir el tamaño de los mensajes y evitar redundancia.

### Ejemplo

```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

## 6.3 Status

Representa el estado de ejecución de una operación realizada por el componente Data Science.

Este modelo será reutilizado por todas las respuestas del contrato de integración.

### Valores

| Valor | Descripción |
|--------|-------------|
| SUCCESS | La operación finalizó correctamente. |
| FAILED | La operación no pudo completarse. |

### Observaciones

- Todos los modelos de respuesta reutilizarán esta enumeración.
- Nuevos estados deberán incorporarse manteniendo compatibilidad con versiones anteriores.

---

## 6.4 RequestMetadata

Representa información adicional enviada por Backend para complementar una solicitud.

Su contenido es opcional y podrá evolucionar sin modificar la estructura principal del contrato.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| uploadedBy | String | No | Usuario responsable de la incorporación del documento. |
| source | String | No | Origen desde el cual se generó la solicitud. |
| language | String | No | Idioma preferido asociado a la solicitud. |

### Observaciones

- Todos los atributos son opcionales.
- Backend podrá incorporar nuevos atributos compatibles sin afectar las operaciones existentes.

### Ejemplo

```json
{
    "uploadedBy": "USR-1001",
    "source": "WEB",
    "language": "es"
}
```

---

## 6.5 ResponseMetadata

Representa información adicional generada durante la ejecución de una consulta sobre la Base de Conocimiento.

Su objetivo es proporcionar información complementaria sin afectar el resultado principal de la operación.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| confidence | Decimal | No | Nivel estimado de confianza de la respuesta. |
| references | Reference[] | No | Documentos utilizados para construir la respuesta. |

### Observaciones

- Los atributos son opcionales.
- Nuevos campos podrán incorporarse en futuras versiones sin romper la compatibilidad del contrato.

### Ejemplo

```json
{
    "confidence": 0.96,
    "references": [
        {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "title": "Guía de Arquitectura"
        }
    ]
}
```

---

## 6.6 Statistics

Representa información estadística generada durante el procesamiento documental.

Estos datos tienen fines informativos y no deberán utilizarse como parte de la lógica funcional del sistema.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| pagesProcessed | Integer | No | Número de páginas procesadas. |
| chunksGenerated | Integer | No | Cantidad de fragmentos generados. |
| detectedLanguage | String | No | Idioma identificado automáticamente. |
| documentCategory | String | No | Categoría detectada para el documento. |

### Observaciones

- La disponibilidad de los atributos dependerá del tipo de documento procesado.
- Backend no deberá asumir que todos los valores estarán presentes.

### Ejemplo

```json
{
    "pagesProcessed": 18,
    "chunksGenerated": 154,
    "detectedLanguage": "es",
    "documentCategory": "Arquitectura"
}
```

---

## 6.7 Reference

Representa una referencia a uno de los documentos utilizados por Data Science para generar una respuesta.

Su propósito es permitir que Backend conozca el origen de la información presentada al usuario.

### Atributos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| id | UUID | Sí | Identificador del documento utilizado. |
| title | String | Sí | Título del documento. |

### Observaciones

- No representa el documento completo.
- Su finalidad es facilitar la trazabilidad de las respuestas generadas.

### Ejemplo

```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Guía de Arquitectura"
}
```

---

# 7. Reglas de Validación y Compatibilidad

Este capítulo define las reglas que deberán cumplirse durante el intercambio de información entre los componentes **Backend** y **Data Science**.

Las validaciones descritas buscan garantizar la consistencia de los modelos, reducir errores durante la integración y establecer claramente la responsabilidad de cada componente.

> [!IMPORTANT]
>
> El cumplimiento de estas reglas forma parte del contrato de integración.
> Cada componente será responsable únicamente de las validaciones que le correspondan según este documento.

---

## 7.1 Reglas Generales

| Código | Regla | Responsable |
|---------|--------|-------------|
| RV-01 | Todos los identificadores deberán cumplir el formato UUID. | Backend |
| RV-02 | Todas las fechas deberán utilizar el estándar ISO-8601 en UTC. | Backend |
| RV-03 | Los atributos opcionales podrán omitirse cuando no exista información disponible. | Ambos |
| RV-04 | Todos los modelos deberán respetar las convenciones definidas en este documento. | Ambos |

---

## 7.2 Validación de ProcessDocumentRequest

| Código | Regla | Responsable |
|---------|--------|-------------|
| RV-10 | projectId es obligatorio. | Backend |
| RV-11 | document.id es obligatorio. | Backend |
| RV-12 | document.uri es obligatorio. | Backend |
| RV-13 | document.type deberá corresponder a un formato soportado. | Backend |
| RV-14 | El documento deberá existir en la ubicación indicada por document.uri. | Backend |
| RV-15 | uploadedAt deberá corresponder a una fecha válida cuando sea informado. | Backend |

### Observaciones

- Data Science asumirá que Backend realizó estas validaciones antes de iniciar el procesamiento.
- La inexistencia del documento durante el procesamiento deberá reportarse como un error de ejecución y no como un error de validación.

---

## 7.3 Validación de AnswerQuestionRequest

| Código | Regla | Responsable |
|---------|--------|-------------|
| RV-20 | projectId es obligatorio. | Backend |
| RV-21 | question no podrá ser nula ni vacía. | Backend |
| RV-22 | conversationId deberá cumplir el formato UUID cuando sea informado. | Backend |

### Observaciones

- Backend será responsable de validar la estructura de la solicitud antes de invocar a Data Science.

---

## 7.4 Validaciones durante el Procesamiento

Las siguientes validaciones corresponden al componente Data Science y serán ejecutadas durante el procesamiento de las solicitudes.

| Código | Regla |
|---------|--------|
| RV-30 | Verificar que el tipo de documento pueda ser procesado. |
| RV-31 | Verificar que el contenido del documento pueda ser leído correctamente. |
| RV-32 | Verificar que el documento pueda ser incorporado a la Base de Conocimiento. |
| RV-33 | Verificar que el proyecto exista dentro del contexto de la Base de Conocimiento. |
| RV-34 | Verificar que exista información suficiente para responder una consulta. |

### Observaciones

El incumplimiento de estas reglas deberá generar una respuesta con estado **FAILED**, utilizando el modelo de respuesta definido en este documento.

---

## 7.5 Reglas de Compatibilidad

Con el fin de preservar la estabilidad del contrato de integración, deberán respetarse las siguientes reglas.

| Código | Regla |
|---------|--------|
| RV-40 | Los nuevos atributos deberán ser opcionales cuando sea posible. |
| RV-41 | No deberán eliminarse atributos existentes sin incrementar la versión mayor del contrato. |
| RV-42 | Los nuevos valores de una enumeración deberán mantener compatibilidad con versiones anteriores. |
| RV-43 | Los modelos compartidos definidos en el Capítulo 6 constituyen la única fuente oficial de definición de estructuras reutilizables. |

---

# 8. Escenarios de Integración

Este capítulo presenta ejemplos completos del intercambio de información entre los componentes **Backend** y **Data Science**.

Su objetivo es ilustrar la utilización de los modelos definidos en este documento dentro de los principales escenarios de integración.

Los ejemplos aquí presentados tienen fines ilustrativos y utilizan datos ficticios.

---

## 8.1 Incorporación de Documento

Este escenario representa el proceso mediante el cual Backend solicita la incorporación de un documento a la Base de Conocimiento administrada por Data Science.

### Flujo

Backend

↓

ProcessDocumentRequest

↓

Data Science

↓

ProcessDocumentResponse

---

### Solicitud

```json
{
  "projectId": "c3fa5d86-8a77-41b4-bc4c-8b3f9e95a2d1",
  "document": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "uri": "/documents/api-authentication.pdf",
    "type": "PDF"
  },
  "uploadedAt": "2026-07-21T15:20:00Z",
  "metadata": {
    "uploadedBy": "USR-1001",
    "source": "WEB",
    "language": "es"
  }
}
```

### Respuesta

```json
{
  "document": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  },
  "status": "SUCCESS",
  "processedAt": "2026-07-21T15:24:31Z",
  "processingTime": 3821,
  "message": "Documento incorporado correctamente a la Base de Conocimiento.",
  "statistics": {
    "pagesProcessed": 18,
    "chunksGenerated": 154,
    "detectedLanguage": "es",
    "documentCategory": "Arquitectura"
  }
}
```

### Observaciones

- Backend mantiene la propiedad del documento durante todo el proceso.
- Data Science procesa el contenido y actualiza la Base de Conocimiento.
- El documento no es modificado por Data Science.
- La respuesta devuelve únicamente una referencia al documento procesado.

## 8.2 Consulta a la Base de Conocimiento

Este escenario representa el proceso mediante el cual Backend solicita una respuesta basada en la Base de Conocimiento.

### Flujo

Backend

↓

AnswerQuestionRequest

↓

Data Science

↓

AnswerQuestionResponse

---

### Solicitud

```json
{
  "projectId": "c3fa5d86-8a77-41b4-bc4c-8b3f9e95a2d1",
  "question": "¿Cómo funciona el proceso de autenticación?",
  "conversationId": "9d27a4f2-f4f4-4567-9e18-f55f3b0d12aa",
  "metadata": {
    "language": "es",
    "source": "WEB"
  }
}
```

### Respuesta

```json
{
  "status": "SUCCESS",
  "answer": "La autenticación del sistema utiliza JWT para validar las solicitudes entre componentes.",
  "generatedAt": "2026-07-21T17:10:30Z",
  "processingTime": 842,
  "message": "Consulta procesada correctamente.",
  "metadata": {
    "confidence": 0.96,
    "references": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "title": "Guía de Arquitectura"
      },
      {
        "id": "66af7813-a48b-4894-8d95-8216cb3d85aa",
        "title": "Manual Backend"
      }
    ]
  }
}
```

### Observaciones

- La respuesta es generada utilizando la Base de Conocimiento del proyecto.
- Backend es responsable de presentar la respuesta al usuario.
- Las referencias permiten identificar los documentos utilizados durante la generación de la respuesta.

---

# 9. Versionado

La evolución de los modelos definidos en este documento deberá mantener compatibilidad con el documento **Backend-Data-Contract.md**.

El versionado seguirá el esquema de **Versionado Semántico (Semantic Versioning)**.

| Versión | Alcance |
|----------|---------|
| Major | Cambios incompatibles con versiones anteriores. |
| Minor | Incorporación de nuevos modelos o atributos compatibles. |
| Patch | Corrección de errores o mejoras que no modifican el contrato. |

## Reglas de Compatibilidad

- Los nuevos atributos deberán ser opcionales siempre que sea posible.
- No deberán eliminarse atributos existentes sin incrementar la versión mayor.
- Los modelos compartidos definidos en el Capítulo 6 constituyen la fuente oficial de estructuras reutilizables.
- Toda modificación deberá actualizar el historial de cambios del documento.

> [!IMPORTANT]
>
> Cualquier cambio en los modelos definidos en este documento deberá evaluarse conjuntamente por los equipos Backend y Data Science antes de su implementación.


# Anexo A – Glosario

| Término                | Definición                                                                  |
| ---------------------- | --------------------------------------------------------------------------- |
| **DocumentDescriptor** | Modelo que describe un documento que será procesado por Data Science.       |
| **DocumentReference**  | Modelo que identifica un documento previamente conocido por Backend.        |
| **Knowledge Base**     | Repositorio de conocimiento administrado exclusivamente por Data Science.   |
| **RequestMetadata**    | Información adicional enviada por Backend junto con una solicitud.          |
| **ResponseMetadata**   | Información complementaria generada por Data Science durante una respuesta. |
| **Statistics**         | Información estadística derivada del procesamiento documental.              |
| **Reference**          | Referencia a un documento utilizado para generar una respuesta.             |
| **Status**             | Estado de ejecución de una operación del componente Data Science.           |
