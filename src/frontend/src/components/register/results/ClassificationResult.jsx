import { Box, Card, CardContent, Chip, Stack, Typography } from "@mui/material";

function ClassificationResult({ classification }) {
  const title = classification?.title || "Resultado";
  const category = classification?.category || "Sin categoría";
  const confidence = classification?.confidence;

  return (
    <Card variant="outlined" sx={{ borderRadius: 3 }}>
      <CardContent>
        <Stack spacing={2}>
          <Typography variant="h6" sx={{ fontWeight: 700 }}>
            Clasificación
          </Typography>

          <Typography variant="h5" sx={{ fontWeight: 700 }}>
            {title}
          </Typography>

          <Chip
            label={category}
            color="primary"
            sx={{ alignSelf: "flex-start" }}
          />

          {confidence !== undefined && confidence !== null && (
            <Typography variant="body2" color="text.secondary">
              Confianza: {(confidence * 100).toFixed(0)}%
            </Typography>
          )}

          {classification?.summary && (
            <Box>
              <Typography variant="subtitle2" gutterBottom>
                Resumen
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {classification.summary}
              </Typography>
            </Box>
          )}
        </Stack>
      </CardContent>
    </Card>
  );
}

export default ClassificationResult;
