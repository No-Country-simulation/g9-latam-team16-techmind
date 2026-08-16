import "./Home.css";
import { useNavigate } from "react-router-dom";
import { Box, Typography, Button, Stack } from "@mui/material";
import FeatureCard from "./FeatureCard";
import PsychologyIcon from "@mui/icons-material/Psychology";
import MenuBookIcon from "@mui/icons-material/MenuBook";
import BoltIcon from "@mui/icons-material/Bolt";

function Home() {
  const navigate = useNavigate();

  return (
    <Box className="home">
      <Box className="home-content">
        <Box
          component="img"
          src="/aynikortex-logo.png"
          alt="AyniKortex"
          sx={{
            width: { xs: 140, md: 164 },
            height: "auto",
            objectFit: "contain",
            mb: 3,
          }}
        />

        <Typography
          variant="h2"
          sx={{
            fontWeight: 800,
            mb: 2,
            color: "common.white",
            letterSpacing: -0.04,
          }}
        >
          AyniKortex
        </Typography>

        <Typography
          variant="h6"
          sx={{
            mx: "auto",
            mb: 3,
            maxWidth: 680,
            color: "common.white",
            opacity: 0.9,
          }}
        >
          Biblioteca inteligente para organizar, clasificar y consultar
          contenido técnico mediante Inteligencia Artificial.
        </Typography>

        <Button
          variant="contained"
          size="large"
          onClick={() => navigate("/register")}
          sx={{
            textTransform: "none",
            px: 3,
            py: 1.25,
            borderRadius: 999,
            fontWeight: 700,
            background: "linear-gradient(135deg, #8b5cf6, #3b82f6)",
            boxShadow: "0 18px 30px rgba(59, 130, 246, 0.24)",
            "&:hover": {
              background: "linear-gradient(135deg, #7c3aed, #2563eb)",
            },
          }}
        >
          Comenzar
        </Button>

        <Stack
          direction={{ xs: "column", md: "row" }}
          spacing={2}
          sx={{
            justifyContent: "center",
            alignItems: "stretch",
            mt: 4,
            flexWrap: "wrap",
          }}
          className="home-features"
        >
          <FeatureCard
            icon={<PsychologyIcon />}
            title="IA Inteligente"
            description="Clasifica y entiende tu contenido técnico automáticamente."
          />

          <FeatureCard
            icon={<MenuBookIcon />}
            title="Biblioteca"
            description="Organiza y consulta toda la información en un solo lugar."
          />

          <FeatureCard
            icon={<BoltIcon />}
            title="Organización"
            description="Encuentra rápidamente el contenido que necesitas."
          />
        </Stack>
      </Box>
    </Box>
  );
}

export default Home;
