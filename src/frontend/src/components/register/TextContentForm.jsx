import "./TextContentForm.css";
import { useRef } from "react";
import { Card, TextField, Typography, Button, Stack } from "@mui/material";

function TextContentForm({
  formData,
  setFormData,
  loading,
  classification,
  onSubmit,
  onReset,
}) {
  const titleInputRef = useRef(null);

  const handleReset = () => {
    onReset();
    titleInputRef.current?.focus();
  };

  return (
    <Card className="text-form-card">
      <Typography variant="h5" className="text-form-title">
        Texto libre
      </Typography>

      <Stack spacing={3}>
        <TextField
          inputRef={titleInputRef}
          label="Título (opcional)"
          variant="outlined"
          fullWidth
          value={formData.title}
          onChange={(event) =>
            setFormData((prev) => ({ ...prev, title: event.target.value }))
          }
        />

        <TextField
          label="Contenido"
          multiline
          rows={8}
          fullWidth
          required
          value={formData.textContent}
          onChange={(event) =>
            setFormData((prev) => ({
              ...prev,
              textContent: event.target.value,
            }))
          }
        />

        <Button
          variant="contained"
          className="text-form-button"
          onClick={onSubmit}
          disabled={!formData.textContent.trim() || loading}
        >
          {loading ? "Clasificando..." : "Clasificar contenido"}
        </Button>

        {classification && (
          <Button
            variant="outlined"
            className="text-form-clear-button"
            onClick={handleReset}
          >
            Limpiar formulario
          </Button>
        )}
      </Stack>
    </Card>
  );
}

export default TextContentForm;
