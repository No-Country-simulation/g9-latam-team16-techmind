import { Box, Typography } from "@mui/material";
import DescriptionOutlinedIcon from "@mui/icons-material/DescriptionOutlined";

function EmptyState() {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        py: 6,
        px: 3,
        border: "1px dashed",
        borderColor: "divider",
        borderRadius: 3,
        bgcolor: "background.paper",
      }}
    >
      <DescriptionOutlinedIcon sx={{ fontSize: 48, mb: 2, color: "primary.main" }} />

      <Typography variant="h6" gutterBottom>
        Aún no hay resultados
      </Typography>

      <Typography variant="body2" color="text.secondary">
        Ingresa un contenido y presiona Analizar para visualizar la clasificación.
      </Typography>
    </Box>
  );
}

export default EmptyState;
