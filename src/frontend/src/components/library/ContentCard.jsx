import { useState } from "react";
import {
  Card,
  CardContent,
  CardActions,
  Typography,
  Box,
  Chip,
  LinearProgress,
  Button,
  Stack,
  Collapse,
} from "@mui/material";
import {
  Download as DownloadIcon,
  ExpandMore as ExpandMoreIcon,
  ExpandLess as ExpandLessIcon,
} from "@mui/icons-material";

function ContentCard({ content }) {
  const [expanded, setExpanded] = useState(false);

  // Función para descargar contenido
  const handleDownload = () => {
    if (content.type === "Text") {
      downloadAsText();
    } else if (content.type === "File") {
      downloadFile();
    }
  };

  // Descargar contenido tipo Text como archivo .txt
  const downloadAsText = () => {
    const fileContent = `
TÍTULO: ${content.title}

CATEGORÍA: ${content.category}
SUBCATEGORÍA: ${content.subcategory}
TIPO: ${content.type}
CONFIANZA DE IA: ${content.confidence}%

RESUMEN:
${content.summary}

KEYWORDS: ${content.keywords.join(", ")}

---
Contenido descargado desde AyniKortex
Fecha: ${new Date().toLocaleString("es-ES")}
    `.trim();

    const blob = new Blob([fileContent], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);

    link.setAttribute("href", url);
    link.setAttribute(
      "download",
      `${content.title.toLowerCase().replace(/\s+/g, "_")}.txt`,
    );
    link.style.visibility = "hidden";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    console.log(`✓ Descargado: ${content.title}`);
  };

  // Para descargar archivos, preparado para backend
  const downloadFile = () => {
    // TODO: Implementar con endpoint del backend
    // GET /api/contents/{id}/download
    console.log(
      `[PENDING] Descargar archivo: ${content.title} (ID: ${content.id})`,
    );
    console.log(`Preparado para: GET /api/contents/${content.id}/download`);
  };

  return (
    <Card
      elevation={0}
      sx={{
        height: "100%",
        width: "100%",
        maxWidth: 420,
        display: "flex",
        flexDirection: "column",
        borderRadius: 3,
        padding: 2,
        border: "1px solid",
        borderColor: "divider",
        transition: "all 0.3s ease",
        "&:hover": {
          boxShadow: 4,
          borderColor: "primary.main",
        },
      }}
    >
      <CardContent sx={{ flexGrow: 1, pb: 1 }}>
        {/* Título */}
        <Typography
          variant="h6"
          sx={{
            fontWeight: 700,
            color: "text.primary",
            mb: 1,
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {content.title}
        </Typography>

        {/* Resumen */}
        <Typography
          variant="body2"
          color="text.secondary"
          sx={{
            mb: 2,
            display: "-webkit-box",
            WebkitLineClamp: 3,
            WebkitBoxOrient: "vertical",
            overflow: "auto",
            minHeight: "3.6em",
          }}
        >
          {content.summary}
        </Typography>

        {/* Contenido expandible */}
        <Collapse in={expanded} timeout="auto" unmountOnExit>
          <Box sx={{ pt: 2, borderTop: "1px solid", borderColor: "divider" }}>
            {/* Categorías */}
            <Box sx={{ mb: 2 }}>
              <Typography
                variant="caption"
                sx={{ fontWeight: 600, color: "text.secondary" }}
              >
                CATEGORÍA
              </Typography>
              <Box sx={{ display: "flex", gap: 1, mt: 0.5, flexWrap: "wrap" }}>
                <Chip
                  label={content.category}
                  size="small"
                  sx={{
                    bgcolor: "primary.light",
                    color: "primary.dark",
                    fontWeight: 600,
                  }}
                />
                <Chip
                  label={content.subcategory}
                  size="small"
                  variant="outlined"
                  sx={{ fontWeight: 500 }}
                />
              </Box>
            </Box>

            {/* Tipo de contenido */}
            <Box sx={{ mb: 2 }}>
              <Typography
                variant="caption"
                sx={{ fontWeight: 600, color: "text.secondary" }}
              >
                TIPO
              </Typography>
              <Box sx={{ mt: 0.5 }}>
                <Chip
                  label={content.type}
                  size="small"
                  color={content.type === "Text" ? "success" : "info"}
                  variant="filled"
                />
              </Box>
            </Box>

            {/* Nivel de confianza */}
            <Box sx={{ mb: 2 }}>
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  mb: 0.5,
                }}
              >
                <Typography
                  variant="caption"
                  sx={{ fontWeight: 600, color: "text.secondary" }}
                >
                  CONFIANZA DE IA
                </Typography>
                <Typography
                  variant="caption"
                  sx={{ fontWeight: 700, color: "primary.main" }}
                >
                  {content.confidence}%
                </Typography>
              </Box>
              <LinearProgress
                variant="determinate"
                value={content.confidence}
                sx={{
                  height: 6,
                  borderRadius: 3,
                  backgroundColor: "divider",
                  "& .MuiLinearProgress-bar": {
                    borderRadius: 3,
                  },
                }}
              />
            </Box>

            {/* Keywords */}
            <Box>
              <Typography
                variant="caption"
                sx={{ fontWeight: 600, color: "text.secondary" }}
              >
                KEYWORDS
              </Typography>
              <Box
                sx={{ display: "flex", gap: 0.5, flexWrap: "wrap", mt: 0.5 }}
              >
                {content.keywords.map((keyword, index) => (
                  <Chip
                    key={index}
                    label={keyword}
                    size="small"
                    variant="outlined"
                    sx={{ fontSize: "0.7rem" }}
                  />
                ))}
              </Box>
            </Box>
          </Box>
        </Collapse>
      </CardContent>

      {/* Acciones */}
      <CardActions sx={{ pt: 1, gap: 1 }}>
        <Button
          fullWidth
          variant="contained"
          size="small"
          endIcon={expanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
          onClick={() => setExpanded(!expanded)}
          sx={{
            textTransform: "none",
            fontWeight: 600,
            borderRadius: 2,
          }}
        >
          {expanded ? "Hide Details" : "Show Details"}
        </Button>
        <Button
          fullWidth
          variant="outlined"
          size="small"
          startIcon={<DownloadIcon />}
          onClick={handleDownload}
          sx={{
            textTransform: "none",
            fontWeight: 600,
            borderRadius: 2,
          }}
        >
          Download
        </Button>
      </CardActions>
    </Card>
  );
}

export default ContentCard;
