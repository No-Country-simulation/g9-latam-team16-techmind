import "./ContentTypeSelector.css";

import { useState } from "react";

import DescriptionIcon from "@mui/icons-material/Description";
import NotesIcon from "@mui/icons-material/Notes";

import { Card, Typography, Box } from "@mui/material";

import TextContentForm from "./TextContentForm";
import FileContentForm from "./FileContentForm";

function ContentTypeSelector() {
  const [contentType, setContentType] = useState(null);

  return (
    <>
      <Box className="content-selector">
        <Card
          className={`content-card ${contentType === "text" ? "selected" : ""}`}
          onClick={() => setContentType("text")}
        >
          <NotesIcon className="content-icon" />

          <Typography variant="h6">Texto libre</Typography>

          <Typography variant="body2">
            Escribe el contenido manualmente.
          </Typography>
        </Card>

        <Card
          className={`content-card ${contentType === "file" ? "selected" : ""}`}
          onClick={() => setContentType("file")}
        >
          <DescriptionIcon className="content-icon" />

          <Typography variant="h6">Archivo</Typography>

          <Typography variant="body2">PDF, DOCX, TXT o Markdown.</Typography>
        </Card>
      </Box>

      {contentType === "text" && <TextContentForm />}

      {contentType === "file" && <FileContentForm />}
    </>
  );
}

export default ContentTypeSelector;
