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
  Collapse,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  DialogActions,
} from "@mui/material";

import {
  Download as DownloadIcon,
  ExpandMore as ExpandMoreIcon,
  ExpandLess as ExpandLessIcon,
  Delete as DeleteIcon,
} from "@mui/icons-material";

function ContentCard({ content, onDelete }) {
  const [expanded, setExpanded] = useState(false);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [deleting, setDeleting] = useState(false);

  const confidence = Number(content.confidence ?? 0);
  const confidencePercentage = confidence * 100;

  // =========================================================
  // DESCARGAR
  // =========================================================

  const handleDownload = () => {
    if (content.contentType === "TEXT") {
      downloadAsText();
    } else if (content.contentType === "FILE") {
      downloadFile();
    }
  };

  // Descargar el CONTENIDO COMPLETO como .txt
  const downloadAsText = () => {
    const fileContent = `
TÍTULO: ${content.title}

CATEGORÍA: ${content.category}
SUBCATEGORÍA: ${content.subcategory}
TIPO: ${content.contentType}
CONFIANZA DE IA: ${confidencePercentage.toFixed(0)}%

KEYWORDS: ${content.keywords?.join(", ") ?? ""}

---

CONTENIDO:
${content.textContent ?? ""}

---

Contenido descargado desde AyniKortex
Fecha: ${new Date().toLocaleString("es-ES")}
`.trim();

    const blob = new Blob([fileContent], {
      type: "text/plain;charset=utf-8",
    });

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;
    link.download = `${
      content.title?.toLowerCase().replace(/\s+/g, "_") || "contenido"
    }.txt`;

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    URL.revokeObjectURL(url);

    console.log(`✓ Descargado: ${content.title}`);
  };

  // Pendiente del endpoint real de descarga de archivos
  const downloadFile = () => {
    console.log(
      `[PENDING] Descargar archivo: ${content.title} (ID: ${content.id})`,
    );
  };

  // =========================================================
  // ELIMINAR
  // =========================================================

  const handleDeleteClick = () => {
    setDeleteDialogOpen(true);
  };

  const handleCancelDelete = () => {
    if (!deleting) {
      setDeleteDialogOpen(false);
    }
  };

  const handleConfirmDelete = async () => {
    try {
      setDeleting(true);

      // El ID viene directamente del registro de BD
      await onDelete(content.id);

      setDeleteDialogOpen(false);
    } catch (error) {
      console.error("Error al eliminar contenido:", error);
    } finally {
      setDeleting(false);
    }
  };

  return (
    <>
      <Card
        elevation={0}
        sx={{
          height: "100%",
          width: "100%",
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
              overflow: "hidden",
              minHeight: "3.6em",
            }}
          >
            {content.summary}
          </Typography>

          {/* Contenido expandible */}
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <Box
              sx={{
                pt: 2,
                borderTop: "1px solid",
                borderColor: "divider",
              }}
            >
              {/* Categorías */}
              <Box sx={{ mb: 2 }}>
                <Typography
                  variant="caption"
                  sx={{
                    fontWeight: 600,
                    color: "text.secondary",
                  }}
                >
                  CATEGORÍA
                </Typography>

                <Box
                  sx={{
                    display: "flex",
                    gap: 1,
                    mt: 0.5,
                    flexWrap: "wrap",
                  }}
                >
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

              {/* Tipo */}
              <Box sx={{ mb: 2 }}>
                <Typography
                  variant="caption"
                  sx={{
                    fontWeight: 600,
                    color: "text.secondary",
                  }}
                >
                  TIPO
                </Typography>

                <Box sx={{ mt: 0.5 }}>
                  <Chip
                    label={content.contentType}
                    size="small"
                    color={content.contentType === "TEXT" ? "success" : "info"}
                    variant="filled"
                  />
                </Box>
              </Box>

              {/* Confianza */}
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
                    sx={{
                      fontWeight: 600,
                      color: "text.secondary",
                    }}
                  >
                    CONFIANZA DE IA
                  </Typography>

                  <Typography
                    variant="caption"
                    sx={{
                      fontWeight: 700,
                      color: "primary.main",
                    }}
                  >
                    {confidencePercentage.toFixed(0)}%
                  </Typography>
                </Box>

                <LinearProgress
                  variant="determinate"
                  value={confidencePercentage}
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
                  sx={{
                    fontWeight: 600,
                    color: "text.secondary",
                  }}
                >
                  KEYWORDS
                </Typography>

                <Box
                  sx={{
                    display: "flex",
                    gap: 0.5,
                    flexWrap: "wrap",
                    mt: 0.5,
                  }}
                >
                  {content.keywords?.map((keyword, index) => (
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
        <CardActions
          sx={{
            pt: 1,
            gap: 1,
            flexWrap: "wrap",
          }}
        >
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

          <Button
            fullWidth
            variant="outlined"
            color="error"
            size="small"
            startIcon={<DeleteIcon />}
            onClick={handleDeleteClick}
            sx={{
              textTransform: "none",
              fontWeight: 600,
              borderRadius: 2,
            }}
          >
            Delete
          </Button>
        </CardActions>
      </Card>

      {/* =====================================================
          CONFIRMACIÓN DE ELIMINACIÓN
      ===================================================== */}
      <Dialog
        open={deleteDialogOpen}
        onClose={handleCancelDelete}
        fullWidth
        maxWidth="xs"
        margin="dense"
        slotProps={{
          paper: {
            sx: {
              width: "100%",
              maxWidth: "400px",
              margin: { xs: "16px", sm: "32px" },
              borderRadius: 3,
              boxSizing: "border-box",
            },
          },
        }}
      >
        <DialogTitle
          sx={{
            px: { xs: 2, sm: 3 },
            py: 2,
            fontSize: { xs: "1.1rem", sm: "1.25rem" },
            fontWeight: 700,
            wordBreak: "break-word",
          }}
        >
          Eliminar contenido
        </DialogTitle>

        <DialogContent
          sx={{
            px: { xs: 2, sm: 3 },
            py: 1,
            minWidth: 0,
            overflowX: "hidden",
          }}
        >
          <DialogContentText
            component="div"
            sx={{
              fontSize: { xs: "0.9rem", sm: "0.95rem" },
              lineHeight: 1.6,
              overflowWrap: "anywhere",
              wordBreak: "break-word",
            }}
          >
            ¿Estás seguro/a de que deseas eliminar{" "}
            <Box
              component="strong"
              sx={{
                overflowWrap: "anywhere",
                wordBreak: "break-word",
              }}
            >
              {content.title || "este contenido"}
            </Box>
            ?
            <br />
            <br />
            Esta acción no se puede deshacer.
          </DialogContentText>
        </DialogContent>

        <DialogActions
          sx={{
            px: { xs: 2, sm: 3 },
            py: { xs: 2, sm: 3 },
            gap: 1,
            flexDirection: { xs: "column", sm: "row" },
            "& > button": {
              width: { xs: "100%", sm: "auto" },
              minHeight: 42,
            },
          }}
        >
          <Button
            onClick={handleCancelDelete}
            disabled={deleting}
            sx={{
              textTransform: "none",
              fontWeight: 600,
            }}
          >
            Cancelar
          </Button>

          <Button
            onClick={handleConfirmDelete}
            color="error"
            variant="contained"
            disabled={deleting}
            sx={{
              textTransform: "none",
              fontWeight: 600,
            }}
          >
            {deleting ? "Eliminando..." : "Eliminar"}
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default ContentCard;
