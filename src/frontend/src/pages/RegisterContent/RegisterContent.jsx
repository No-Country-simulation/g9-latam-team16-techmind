import "./RegisterContent.css";

import { Box, Typography } from "@mui/material";

import ContentTypeSelector from "../../components/register/ContentTypeSelector";

function RegisterContent() {
  return (
    <Box className="register-page">
      <Typography variant="h3" className="register-title">
        Registrar contenido
      </Typography>

      <Typography variant="body1" className="register-subtitle">
        ¿Qué deseas registrar?
      </Typography>

      <ContentTypeSelector />
    </Box>
  );
}

export default RegisterContent;
