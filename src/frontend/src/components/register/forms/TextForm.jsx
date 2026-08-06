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
    <Card sx={{ borderRadius: 3, p: { xs: 2, md: 3 }, boxShadow: 1 }}>
      <Typography variant="h5" sx={{ fontWeight: 700, mb: 2 }}>
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
          sx={{ borderRadius: 2, textTransform: "none", fontWeight: 600 }}
          onClick={onSubmit}
          disabled={!formData.textContent.trim() || loading}
        >
          {loading ? "Analizando..." : "Analizar contenido"}
        </Button>

        {classification && (
          <Button
            variant="outlined"
            sx={{ borderRadius: 2, textTransform: "none", fontWeight: 600 }}
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
