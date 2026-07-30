import "./RegisterContent.css";

import { useState } from "react";
import { Box, Typography } from "@mui/material";

import ContentTypeSelector from "../../components/register/ContentTypeSelector";
import ClassificationResult from "../../components/register/ClassificationResult";
import { createRegisterTextRequest } from "../../dto/request/RegisterTextRequest";
import { registerText } from "../../services/contentService";

const initialForm = {
  title: "",
  description: "",
  contentType: "TEXT",
  textContent: "",
  file: null,
  fileName: "",
};

function RegisterContent() {
  const [formData, setFormData] = useState(initialForm);
  const [loading, setLoading] = useState(false);
  const [classification, setClassification] = useState(null);

  const handleSubmit = async () => {
    try {
      setLoading(true);

      if (formData.contentType === "TEXT") {
        const request = createRegisterTextRequest(
          formData.title,
          formData.textContent,
        );
        const response = await registerText(request);
        setClassification(response);
      } else {
        setClassification({
          title: formData.fileName || "Archivo recibido",
          category: "Pendiente de integración",
          confidence: 0.5,
        });
      }
    } catch (error) {
      console.error("Error al registrar el contenido:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFormData(initialForm);
    setClassification(null);
  };

  return (
    <Box className="register-page">
      <Typography variant="h3" className="register-title">
        Registrar contenido
      </Typography>

      <Typography variant="body1" className="register-subtitle">
        ¿Qué deseas registrar?
      </Typography>

      <ContentTypeSelector
        formData={formData}
        setFormData={setFormData}
        loading={loading}
        classification={classification}
        onSubmit={handleSubmit}
        onReset={handleReset}
      />

      {classification && (
        <Box sx={{ mt: 3 }}>
          <ClassificationResult classification={classification} />
        </Box>
      )}
    </Box>
  );
}

export default RegisterContent;
