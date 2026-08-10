import { Button, Card, Stack, Typography } from "@mui/material";

import DynamicContentForm from "../forms/DynamicContentForm";

function UploadPanel({
  contentType,
  onContentTypeChange,
  formData,
  setFormData,
  loading,
  analysis,
  onAnalyze,
  onReset,
}) {
  return (
    <Card
      variant="outlined"
      sx={{
        height: "100%",
        borderRadius: 3,
        p: { xs: 2, md: 3 },
        bgcolor: "background.paper",
      }}
    >
      <Stack spacing={1} sx={{ mb: 3 }}>
        <Typography
          variant="h5"
          sx={{ fontWeight: 700, color: "text.primary" }}
        >
          Analizar contenido
        </Typography>

        <Typography variant="body1" color="text.secondary">
          Ingresa un texto o carga un archivo para obtener su clasificación.
        </Typography>
      </Stack>

      <DynamicContentForm
        contentType={contentType}
        onContentTypeChange={onContentTypeChange}
        formData={formData}
        setFormData={setFormData}
        loading={loading}
        analysis={analysis}
        onSubmit={onAnalyze}
        onReset={onReset}
      />
    </Card>
  );
}

export default UploadPanel;
