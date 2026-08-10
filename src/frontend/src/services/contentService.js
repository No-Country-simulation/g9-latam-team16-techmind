import { API_BASE_URL } from "../api/apiClient";

export async function getContents() {
  const response = await fetch(`${API_BASE_URL}/contents`);

  if (!response.ok) {
    throw new Error(`Error al obtener contenidos: ${response.status}`);
  }

  return response.json();
}

export async function registerText(request) {
  const response = await fetch(`${API_BASE_URL}/contents/text`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error(`Error al registrar contenido: ${response.status}`);
  }

  return response.json();
}

export async function registerFile(formData) {
  const response = await fetch(`${API_BASE_URL}/contents/file`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`Error al registrar archivo: ${response.status}`);
  }

  return response.json();
}

export async function analyzeContent({ contentType, formData }) {
  if (contentType === "TEXT") {
    return registerText({
      title: formData.title,
      text: formData.textContent,
      metadata: formData.metadata || {},
    });
  }

  const multipartData = new FormData();

  multipartData.append("title", formData.title || "");
  multipartData.append("file", formData.file);

  if (formData.metadata) {
    multipartData.append("metadata", JSON.stringify(formData.metadata));
  }

  return registerFile(multipartData);
}
