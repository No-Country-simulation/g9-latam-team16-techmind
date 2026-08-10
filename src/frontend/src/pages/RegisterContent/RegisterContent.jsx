import { useState } from "react";
import { Box, Card, Container, Typography } from "@mui/material";

import UploadPanel from "../../components/register/panels/UploadPanel";
import ResultPanel from "../../components/register/panels/ResultPanel";
import { analyzeContent } from "../../services/contentService";

const createInitialForm = () => ({
  title: "",
  description: "",
  contentType: "TEXT",
  textContent: "",
  file: null,
  fileName: "",
});

function RegisterContent() {
  const [contentType, setContentType] = useState("TEXT");
  const [formData, setFormData] = useState(createInitialForm);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    try {
      setLoading(true);

      const response = await analyzeContent({
        contentType,
        formData,
      });

      setAnalysis(response);
    } catch (error) {
      console.error("Error al registrar el contenido:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setContentType("TEXT");
    setFormData(createInitialForm());
    setAnalysis(null);
  };

  const handleContentTypeChange = (newValue) => {
    setContentType(newValue);
  };

  return (
    <Box
      className="register-page"
      sx={{
        bgcolor: "background.default",
        minHeight: "100vh",
        py: {
          xs: 3,
          md: 5,
        },
      }}
    >
      <Container
        maxWidth="lg"
        sx={{
          px: {
            xs: 2,
            sm: 3,
          },
        }}
      >
        {/* Encabezado */}
        <Box
          sx={{
            mb: {
              xs: 3,
              md: 4,
            },
            textAlign: "center",
          }}
        >
          <Typography
            variant="h3"
            sx={{
              fontWeight: 700,
              color: "text.primary",
              mb: 1,
              fontSize: {
                xs: "2rem",
                sm: "2.5rem",
                md: "3rem",
              },
            }}
          >
            Registrar contenido
          </Typography>

          <Typography
            variant="body1"
            color="text.secondary"
            sx={{
              maxWidth: 800,
              mx: "auto",
            }}
          >
            Centraliza la evaluación de texto y archivos en una experiencia
            clara, rápida y visualmente consistente.
          </Typography>
        </Box>

        <Box
          sx={{
            display: "grid",
            gridTemplateColumns: {
              xs: "1fr",
              md: "7fr 5fr",
            },
            gap: {
              xs: 2,
              md: 3,
            },
            alignItems: "stretch",
          }}
        >
          {/* Panel de carga */}
          <Card
            elevation={0}
            sx={{
              height: "100%",
              borderRadius: 3,
              border: "1px solid",
              borderColor: "divider",
              p: {
                xs: 2,
                sm: 2.5,
                md: 3,
              },
              bgcolor: "background.paper",
            }}
          >
            <UploadPanel
              contentType={contentType}
              onContentTypeChange={handleContentTypeChange}
              formData={formData}
              setFormData={setFormData}
              loading={loading}
              analysis={analysis}
              onAnalyze={handleSubmit}
              onReset={handleReset}
            />
          </Card>

          {/* Panel de resultado */}
          <Card
            elevation={0}
            sx={{
              height: "100%",
              borderRadius: 3,
              border: "1px solid",
              borderColor: "divider",
              p: {
                xs: 2,
                sm: 2.5,
                md: 3,
              },
              bgcolor: "background.paper",
            }}
          >
            <ResultPanel analysis={analysis} loading={loading} />
          </Card>
        </Box>
      </Container>
    </Box>
  );
}

export default RegisterContent;
