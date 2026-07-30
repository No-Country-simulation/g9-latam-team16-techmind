import { Box, Button, Typography, Paper } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

function FileContentForm({
  formData,
  setFormData,
  loading,
  classification,
  onSubmit,
  onReset,
}) {
  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      setFormData((prev) => ({
        ...prev,
        file: selectedFile,
        fileName: selectedFile.name,
      }));
    }
  };

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 4,
        borderRadius: 3,
        marginTop: 3,
      }}
    >
      <Typography variant="h6" gutterBottom>
        Subir archivo
      </Typography>

      <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
        Carga un documento técnico para ser clasificado automáticamente.
      </Typography>

      <Button
        component="label"
        variant="contained"
        startIcon={<CloudUploadIcon />}
      >
        Seleccionar archivo
        <input type="file" hidden onChange={handleFileChange} />
      </Button>

      {formData.file && (
        <Box sx={{ mt: 3 }}>
          <Typography>Archivo seleccionado:</Typography>

          <Typography fontWeight="bold">{formData.fileName}</Typography>

          <Typography variant="caption" color="text.secondary">
            {(formData.file.size / 1024).toFixed(2)} KB
          </Typography>
        </Box>
      )}

      <Button
        variant="contained"
        sx={{ mt: 3 }}
        onClick={onSubmit}
        disabled={!formData.file || loading}
      >
        {loading ? "Clasificando..." : "Clasificar contenido"}
      </Button>

      {classification && (
        <Button variant="outlined" sx={{ mt: 2 }} onClick={onReset}>
          Limpiar formulario
        </Button>
      )}
    </Paper>
  );
}

export default FileContentForm;
