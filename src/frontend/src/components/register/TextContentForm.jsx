import "./TextContentForm.css";

import { Card, TextField, Typography, Button, Stack } from "@mui/material";

function TextContentForm() {
  return (
    <Card className="text-form-card">
      <Typography variant="h5" className="text-form-title">
        Texto libre
      </Typography>

      <Stack spacing={3}>
        <TextField label="Título (opcional)" variant="outlined" fullWidth />

        <TextField label="Contenido" multiline rows={8} fullWidth required />

        <Button variant="contained" className="text-form-button">
          Clasificar contenido
        </Button>
      </Stack>
    </Card>
  );
}

export default TextContentForm;
