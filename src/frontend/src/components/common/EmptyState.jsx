import { Box, Typography, Stack } from "@mui/material";
import { InboxOutlined as EmptyIcon } from "@mui/icons-material";

function EmptyState({
  title = "Sin contenido",
  message = "No hay datos para mostrar en este momento.",
  icon: Icon = EmptyIcon,
}) {
  return (
    <Stack
      spacing={2}
      sx={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        py: 6,
        textAlign: "center",
      }}
    >
      <Icon
        sx={{
          fontSize: 80,
          color: "text.disabled",
          opacity: 0.5,
        }}
      />
      <Stack spacing={1}>
        <Typography
          variant="h6"
          sx={{
            fontWeight: 700,
            color: "text.primary",
          }}
        >
          {title}
        </Typography>
        <Typography
          variant="body2"
          sx={{
            color: "text.secondary",
            maxWidth: 400,
          }}
        >
          {message}
        </Typography>
      </Stack>
    </Stack>
  );
}

export default EmptyState;
