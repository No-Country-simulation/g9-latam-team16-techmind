import { Box, Card, Skeleton, Stack, Typography } from "@mui/material";

import EmptyState from "../common/EmptyState";
import ClassificationResult from "../results/ClassificationResult";

function ResultPanel({ analysis, loading }) {
  const renderContent = () => {
    if (loading) {
      return (
        <Box>
          <Stack spacing={2} sx={{ mb: 3 }}>
            <Typography
              variant="h5"
              sx={{ fontWeight: 700, color: "text.primary" }}
            >
              Resultado
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Clasificando tu contenido. Esto tomará unos segundos.
            </Typography>
          </Stack>
          <Skeleton
            variant="rectangular"
            height={140}
            sx={{ mb: 2, borderRadius: 3 }}
          />
          <Skeleton variant="text" width="60%" />
          <Skeleton variant="text" width="40%" />
        </Box>
      );
    }

    if (!analysis) {
      return (
        <Box>
          <Stack spacing={1} sx={{ mb: 3 }}>
            <Typography
              variant="h5"
              sx={{ fontWeight: 700, color: "text.primary" }}
            >
              Resultado
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Aquí aparecerá la clasificación una vez completes el análisis.
            </Typography>
          </Stack>
          <EmptyState />
        </Box>
      );
    }

    return (
      <Box>
        <Stack spacing={1} sx={{ mb: 3 }}>
          <Typography
            variant="h5"
            sx={{ fontWeight: 700, color: "text.primary" }}
          >
            Resultado
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Vista previa de la clasificación generada para el contenido.
          </Typography>
        </Stack>
        <ClassificationResult classification={analysis} />
      </Box>
    );
  };

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
      {renderContent()}
    </Card>
  );
}

export default ResultPanel;
