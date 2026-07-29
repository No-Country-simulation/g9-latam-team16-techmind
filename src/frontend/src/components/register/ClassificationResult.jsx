import "./ClassificationResult.css";

import PsychologyIcon from "@mui/icons-material/Psychology";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";

import {
  Card,
  Typography,
  Stack,
  Chip,
  LinearProgress,
  Box,
} from "@mui/material";

function ClassificationResult({ classification }) {
  if (!classification) return null;

  const confidence = classification.confidence * 100;

  const progressColor =
    confidence >= 90 ? "success" : confidence >= 70 ? "warning" : "error";

  return (
    <Card className="classification-card">
      <Stack
        direction="row"
        spacing={2}
        alignItems="center"
        className="classification-header"
      >
        <PsychologyIcon className="classification-icon" />

        <Box>
          <Typography variant="h5" className="classification-title">
            Resultado del análisis
          </Typography>

          <Typography className="classification-subtitle">
            El contenido fue procesado correctamente por el modelo de IA.
          </Typography>
        </Box>
      </Stack>

      <Box className="classification-divider" />

      <Box className="classification-section">
        <Typography className="classification-label">Categoría</Typography>

        <Typography className="classification-value">
          {classification.category}
        </Typography>
      </Box>

      <Box className="classification-section">
        <Typography className="classification-label">Subcategoría</Typography>

        <Typography className="classification-value">
          {classification.subcategory}
        </Typography>
      </Box>

      <Box className="classification-section">
        <Typography className="classification-label">
          Confianza del modelo
        </Typography>

        <LinearProgress
          variant="determinate"
          value={confidence}
          color={progressColor}
          className="classification-progress"
        />

        <Typography className="classification-confidence">
          {confidence.toFixed(1)} %
        </Typography>
      </Box>

      <Box className="classification-section">
        <Typography className="classification-label">Palabras clave</Typography>

        <Stack direction="row" spacing={1} useFlexGap flexWrap="wrap">
          {classification.keywords.map((keyword) => (
            <Chip
              key={keyword}
              label={keyword}
              color="primary"
              variant="filled"
            />
          ))}
        </Stack>
      </Box>

      <Stack
        direction="row"
        spacing={1}
        alignItems="center"
        className="classification-footer"
      >
        <CheckCircleIcon color="success" />

        <Typography>Clasificación finalizada correctamente.</Typography>
      </Stack>
    </Card>
  );
}

export default ClassificationResult;
