import "./Home.css";

import { useNavigate } from "react-router-dom";

import { Box, Typography, Button, Stack, Chip } from "@mui/material";

import PsychologyIcon from "@mui/icons-material/Psychology";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";
import MenuBookIcon from "@mui/icons-material/MenuBook";

function Home() {
  const navigate = useNavigate();

  return (
    <Box className="home">
      <Box className="home-content">
        <PsychologyIcon className="home-icon" />

        <Typography variant="h2" className="home-title">
          AyniKortex
        </Typography>

        <Typography variant="h6" className="home-description">
          Biblioteca inteligente para organizar, clasificar y consultar
          contenido técnico mediante Inteligencia Artificial.
        </Typography>

        <Button
          variant="contained"
          size="large"
          onClick={() => navigate("/register")}
        >
          Comenzar
        </Button>

        <Stack
          direction="row"
          spacing={2}
          justifyContent="center"
          className="home-features"
        >
          <Chip icon={<PsychologyIcon />} label="IA" />

          <Chip icon={<MenuBookIcon />} label="Biblioteca" />

          <Chip icon={<AutoAwesomeIcon />} label="Organización" />
        </Stack>
      </Box>
    </Box>
  );
}

export default Home;
