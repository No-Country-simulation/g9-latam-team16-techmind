import "./Navbar.css";
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
} from "@mui/material";
import Brightness4Icon from "@mui/icons-material/Brightness4";
import Brightness7Icon from "@mui/icons-material/Brightness7";
import { useContext } from "react";
import { NavLink } from "react-router-dom";
import { ThemeContext } from "../../context/ThemeContext";

function Navbar() {
  const { mode, toggleTheme } = useContext(ThemeContext);

  return (
    <AppBar position="sticky" className="navbar">
      <Toolbar className="navbar-content">
        <Box component={NavLink} to="/" className="navbar-logo">
          <Box
            component="img"
            src="/aynikortex-logo.png"
            alt="AyniKortex"
            className="navbar-icon"
          />

          <Typography variant="h6" className="navbar-title">
            AyniKortex
          </Typography>
        </Box>

        <Box className="navbar-links">
          <Button component={NavLink} to="/register" className="navbar-link">
            Registrar contenido
          </Button>

          <Button component={NavLink} to="/library" className="navbar-link">
            Biblioteca
          </Button>

          <IconButton
            onClick={toggleTheme}
            color="inherit"
            aria-label="toggle theme"
          >
            {mode === "dark" ? <Brightness7Icon /> : <Brightness4Icon />}
          </IconButton>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
