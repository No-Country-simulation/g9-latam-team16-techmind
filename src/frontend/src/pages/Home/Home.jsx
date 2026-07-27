import "./Home.css";
import { useNavigate } from "react-router-dom";
import { Box, Typography, Button } from "@mui/material";
import FeatureCard from "../home/FeatureCard";
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
          className="home-icon"
        />

        <Typography variant="h2" className="home-title">
          AyniKortex
        </Typography>

        <Typography variant="h6" className="home-description">
          Biblioteca inteligente para organizar, clasificar y consultar
          contenido técnico mediante Inteligencia Artificial.
        </Typography>

        <Button
          className="home-cta"
          variant="contained"
          size="large"
          onClick={() => navigate("/register")}
        >
          Comenzar
        </Button>

        <Box className="home-features">
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
        </Box>
      </Box>
    </Box>
  );
}

export default Home;
