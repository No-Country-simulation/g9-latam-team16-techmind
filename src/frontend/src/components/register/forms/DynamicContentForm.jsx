import { Box, ToggleButton, ToggleButtonGroup } from "@mui/material";

import FileForm from "./FileForm";
import TextForm from "./TextForm";

function DynamicContentForm({
  contentType,
  onContentTypeChange,
  formData,
  setFormData,
  loading,
  analysis,
  onSubmit,
  onReset,
}) {
  const handleContentTypeChange = (_event, newValue) => {
    if (newValue !== null) {
      onContentTypeChange(newValue);
    }
  };

  return (
    <Box>
      <ToggleButtonGroup
        color="primary"
        exclusive
        value={contentType}
        onChange={handleContentTypeChange}
        aria-label="tipo de contenido"
        sx={{ mb: 3 }}
      >
        <ToggleButton value="TEXT">Texto</ToggleButton>
        <ToggleButton value="FILE">Archivo</ToggleButton>
      </ToggleButtonGroup>

      {contentType === "TEXT" ? (
        <TextForm
          formData={formData}
          setFormData={setFormData}
          loading={loading}
          analysis={analysis}
          onSubmit={onSubmit}
          onReset={onReset}
        />
      ) : (
        <FileForm
          formData={formData}
          setFormData={setFormData}
          loading={loading}
          analysis={analysis}
          onSubmit={onSubmit}
          onReset={onReset}
        />
      )}
    </Box>
  );
}

export default DynamicContentForm;
