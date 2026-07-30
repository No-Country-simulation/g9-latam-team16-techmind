import "./ContentTypeSelector.css";

import DescriptionIcon from "@mui/icons-material/Description";
import NotesIcon from "@mui/icons-material/Notes";

import { Card, Typography, Box } from "@mui/material";

import TextContentForm from "./TextContentForm";
import FileContentForm from "./FileContentForm";

function ContentTypeSelector({
  formData,
  setFormData,
  loading,
  classification,
  onSubmit,
  onReset,
}) {
  const selectedType = formData?.contentType?.toUpperCase();

  const handleSelectType = (type) => {
    setFormData((prev) => ({
      ...prev,
      contentType: type,
    }));
  };

  return (
    <>
      <Box className="content-selector">
        <Card
          className={`content-card ${selectedType === "TEXT" ? "selected" : ""}`}
          onClick={() => handleSelectType("TEXT")}
        >
          <NotesIcon className="content-icon" />

          <Typography variant="h6">Texto libre</Typography>

          <Typography variant="body2">
            Escribe el contenido manualmente.
          </Typography>
        </Card>

        <Card
          className={`content-card ${selectedType === "FILE" ? "selected" : ""}`}
          onClick={() => handleSelectType("FILE")}
        >
          <DescriptionIcon className="content-icon" />

          <Typography variant="h6">Archivo</Typography>

          <Typography variant="body2">PDF, DOCX, TXT o Markdown.</Typography>
        </Card>
      </Box>

      {selectedType === "TEXT" && (
        <TextContentForm
          formData={formData}
          setFormData={setFormData}
          loading={loading}
          classification={classification}
          onSubmit={onSubmit}
          onReset={onReset}
        />
      )}

      {selectedType === "FILE" && (
        <FileContentForm
          formData={formData}
          setFormData={setFormData}
          loading={loading}
          classification={classification}
          onSubmit={onSubmit}
          onReset={onReset}
        />
      )}
    </>
  );
}

export default ContentTypeSelector;
