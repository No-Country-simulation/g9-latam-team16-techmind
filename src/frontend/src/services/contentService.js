import { createRegisterTextRequest } from "../dto/request/RegisterTextRequest";
import { registerTextMock } from "../mocks/contentMock";

const mockRegisterFile = async ({ fileName }) => ({
  title: fileName || "Archivo recibido",
  category: "Pendiente de integración",
  confidence: 0.5,
});

export async function registerText(request) {
  return registerTextMock(request);
}

export async function registerFile({ fileName }) {
  return mockRegisterFile({ fileName });
}

export async function analyzeContent({ contentType, formData }) {
  if (contentType === "TEXT") {
    const request = createRegisterTextRequest(
      formData.title,
      formData.textContent,
    );

    return registerText(request);
  }

  return registerFile({ fileName: formData.fileName });
}
