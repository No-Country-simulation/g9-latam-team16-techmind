# 📖 Guía de Estilo de Documentación

> **Proyecto:** AyniKortex  
> **Estado:** Vigente

La documentación es una parte esencial de AyniKortex.

Esta guía define los estándares utilizados para crear, mantener y evolucionar la documentación del proyecto, con el objetivo de garantizar claridad, consistencia y facilidad de mantenimiento.

Todos los documentos oficiales deberán seguir estas recomendaciones.

---

# 🎯 Objetivo

Esta guía establece las convenciones de documentación utilizadas en AyniKortex.

Su propósito es asegurar que todos los documentos compartan una estructura uniforme, un lenguaje consistente y una presentación clara para cualquier persona que participe en el proyecto.

---

# 🌟 Filosofía de la Documentación

En AyniKortex entendemos la documentación como parte del producto, no como un complemento.

Una buena documentación debe:

- Facilitar el aprendizaje.
- Explicar antes de detallar.
- Evolucionar junto con el proyecto.
- Evitar información duplicada.
- Ser accesible para perfiles técnicos y no técnicos.

Cada documento debe aportar valor y mantenerse actualizado conforme evoluciona el proyecto.

---

# 📝 Principios de Escritura

Toda la documentación deberá seguir los siguientes principios:

- Escribir con un lenguaje claro y profesional.
- Explicar primero el propósito y después los detalles técnicos.
- Utilizar títulos descriptivos.
- Priorizar ejemplos y tablas cuando faciliten la comprensión.
- Mantener un tono cercano y colaborativo.
- Evitar párrafos excesivamente largos.

---

# 📚 Un Documento, Un Propósito

Cada documento oficial de AyniKortex debe responder una única pregunta principal.

Este principio evita la duplicación de información, facilita el mantenimiento y permite que cada documento tenga un propósito claramente definido.

| Documento | Pregunta que responde |
|-----------|------------------------|
| README.md | ¿Qué es AyniKortex? |
| ARCHITECTURE.md | ¿Cómo funciona el sistema? |
| CONTRIBUTING.md | ¿Cómo puedo colaborar? |
| ROADMAP.md | ¿Hacia dónde evoluciona el proyecto? |
| CODE_OF_CONDUCT.md | ¿Cómo convivimos en la comunidad? |
| SECURITY.md | ¿Cómo reportar una vulnerabilidad? |
| SUPPORT.md | ¿Dónde puedo obtener ayuda? |

Cuando un documento requiera información adicional, deberá enlazar al documento correspondiente en lugar de duplicar su contenido.

---

# 📑 Convenciones de Markdown

Toda la documentación deberá escribirse utilizando Markdown y seguir las siguientes convenciones:

- Utilizar títulos jerárquicos (`#`, `##`, `###`).
- Separar las secciones principales mediante líneas horizontales (`---`).
- Utilizar listas para describir procesos, recomendaciones o pasos.
- Emplear tablas cuando permitan presentar información de manera más clara.
- Utilizar bloques de código indicando el lenguaje correspondiente cuando sea posible.
- Mantener una estructura uniforme en todos los documentos.

---

# 📊 Uso de Tablas

Las tablas deben utilizarse cuando faciliten la lectura y comparación de información.

Se recomienda su uso para:

- Comparar componentes.
- Mostrar estados del proyecto.
- Definir responsabilidades.
- Presentar cronogramas o roadmaps.
- Documentar contratos e interfaces.

Evita utilizar tablas cuando un listado simple resulte más claro.

---

# 💻 Bloques de Código

Todo bloque de código deberá indicar el lenguaje correspondiente para aprovechar el resaltado de sintaxis.

Ejemplo:

```java
public class DocumentoService {

}
```


---

# ✍️ Sección 9: Diagramas Mermaid

Esta sección incorpora una de las convenciones más representativas del proyecto.

```markdown
---

# 📈 Diagramas Mermaid

Los diagramas Mermaid deberán utilizar nombres descriptivos para identificar los nodos.

## ✔ Recomendado

- Usuario
- Frontend
- Backend
- CienciaDatos
- ModeloClasificacion
- BaseDatos

## ✘ Evitar

- A
- B
- C
- FE
- BE
- DS
- DB
- ML

Los nombres descriptivos facilitan la comprensión del diagrama sin necesidad de consultar una leyenda adicional.

---

# 🔗 Enlaces entre Documentos

La documentación de AyniKortex está organizada como un conjunto de documentos relacionados entre sí.

Cuando un tema sea tratado en otro documento oficial, se recomienda crear una referencia hacia ese documento en lugar de duplicar la información.

Ejemplos:

- README.md → ARCHITECTURE.md
- CONTRIBUTING.md → DOCUMENTATION_STYLE_GUIDE.md
- SECURITY.md → SUPPORT.md (cuando corresponda)
- ROADMAP.md → ARCHITECTURE.md

Este enfoque mantiene una única fuente de verdad y facilita el mantenimiento de la documentación.

---

# 📂 Organización de la Documentación

La documentación oficial del proyecto se organiza de la siguiente manera:

## Documentación de la Comunidad

Ubicada en la raíz del repositorio.

- README.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- SUPPORT.md

## Documentación Técnica

Ubicada en el directorio `docs/`.

- Arquitectura
- Roadmap
- Guías de documentación
- Especificaciones técnicas

Esta organización facilita la navegación y permite diferenciar claramente la documentación dirigida a la comunidad de aquella orientada al desarrollo técnico.

---

# 🚫 Qué Evitar

Para mantener una documentación consistente y fácil de mantener, evita:

- Duplicar información entre documentos.
- Crear documentos sin un propósito definido.
- Utilizar nombres ambiguos en títulos o diagramas.
- Mantener información desactualizada.
- Escribir párrafos excesivamente largos.
- Incluir detalles técnicos en documentos cuyo objetivo es introductorio.
- Romper la estructura y el estilo definidos en esta guía.

---

# ✅ Lista de Verificación

Antes de publicar o actualizar un documento, verifica que:

- [ ] El documento tiene un objetivo claramente definido.
- [ ] Responde a una única pregunta principal.
- [ ] Sigue la estructura oficial de AyniKortex.
- [ ] Utiliza títulos descriptivos.
- [ ] No duplica información existente.
- [ ] Incluye tablas o diagramas cuando aportan claridad.
- [ ] Los diagramas Mermaid utilizan nombres descriptivos.
- [ ] Se enlaza con otros documentos cuando corresponde.
- [ ] Ha sido revisado antes de publicarse.

---

# 💙 Nuestra Filosofía

La documentación evoluciona junto con el proyecto.

En AyniKortex creemos que documentar no significa únicamente describir el software, sino compartir conocimiento, facilitar el aprendizaje y promover una colaboración efectiva.

Cada documento representa una oportunidad para mejorar la experiencia de quienes desarrollan, mantienen o utilizan el proyecto.

Una documentación clara, actualizada y consistente también es una forma de construir software de calidad.

¡Gracias por contribuir a mantener vivo este conocimiento! 🚀
