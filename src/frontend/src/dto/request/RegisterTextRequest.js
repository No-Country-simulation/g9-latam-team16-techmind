/**
 * Crea el cuerpo de la petición para registrar contenido de texto.
 *
 * @param {string} title
 * @param {string} content
 * @returns {Object}
 */
export function createRegisterTextRequest(title, content) {
  return {
    title: title?.trim() || null,
    content: content.trim(),
  };
}
