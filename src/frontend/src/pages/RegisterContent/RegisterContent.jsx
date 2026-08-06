import { useState } from "react";
import { Box, Card, Container, Grid, Typography } from "@mui/material";

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
      const response = await analyzeContent({ contentType, formData });
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
        py: { xs: 3, md: 5 },
      }}
    >
      <Container maxWidth="xl" sx={{ width: "100%" }}>
        <Box sx={{ mb: 4, textAlign: "center" }}>
          <Typography
            variant="h3"
            sx={{ fontWeight: 700, color: "text.primary", mb: 1 }}
          >
            Registrar contenido
          </Typography>
          <Typography variant="body1" color="text.secondary">
            Centraliza la evaluación de texto y archivos en una experiencia
            clara, rápida y visualmente consistente.
          </Typography>
        </Box>

        <Grid container spacing={3}>
          <Grid item xs={12} md={5}>
            <Card
              elevation={0}
              sx={{
                height: "100%",
                borderRadius: 3,
                border: "1px solid",
                borderColor: "divider",
                p: { xs: 2, md: 3 },
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
          </Grid>

          <Grid item xs={12} md={7}>
            <Card
              elevation={0}
              sx={{
                height: "100%",
                borderRadius: 3,
                border: "1px solid",
                borderColor: "divider",
                p: { xs: 2, md: 3 },
                bgcolor: "background.paper",
              }}
            >
              <ResultPanel analysis={analysis} loading={loading} />
            </Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}

export default RegisterContent;
