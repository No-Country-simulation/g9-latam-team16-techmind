import "./TextContentForm.css";
import { useState } from "react";
import { createRegisterTextRequest } from "../../dto/request/RegisterTextRequest";
import { registerText } from "../../services/contentService";
import { Card, TextField, Typography, Button, Stack } from "@mui/material";
import ClassificationResult from "./ClassificationResult";

function TextContentForm() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const [loading, setLoading] = useState(false);
  const [classification, setClassification] = useState(null);

  const handleSubmit = async () => {
    try {
      setLoading(true);

      const request = createRegisterTextRequest(title, content);

      const response = await registerText(request);

      setClassification(response);
    } catch (error) {
      console.error("Error al registrar el contenido:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="text-form-card">
      <Typography variant="h5" className="text-form-title">
        Texto libre
      </Typography>

      <Stack spacing={3}>
        <TextField
          label="Título (opcional)"
          variant="outlined"
          fullWidth
          value={title}
          onChange={(event) => setTitle(event.target.value)}
        />

        <TextField
          label="Contenido"
          multiline
          rows={8}
          fullWidth
          required
          value={content}
          onChange={(event) => setContent(event.target.value)}
        />

        <Button
          variant="contained"
          className="text-form-button"
          onClick={handleSubmit}
          disabled={!content.trim() || loading}
        >
          {loading ? "Clasificando..." : "Clasificar contenido"}
        </Button>

        {classification && (
          <ClassificationResult classification={classification} />
        )}
      </Stack>
    </Card>
  );
}

export default TextContentForm;
