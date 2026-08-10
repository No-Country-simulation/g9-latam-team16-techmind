import { Stack, Typography } from "@mui/material";

function ResultHeader({ title }) {
  return (
    <Stack spacing={0.5}>
      <Typography
        variant="overline"
        color="text.secondary"
        sx={{ fontWeight: 600, letterSpacing: 1 }}
      >
        Resultado del análisis
      </Typography>

      <Typography variant="h5" sx={{ fontWeight: 700 }}>
        {title || "Contenido analizado"}
      </Typography>
    </Stack>
  );
}

export default ResultHeader;
