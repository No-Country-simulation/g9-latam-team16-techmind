import "./Navbar.css";
import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import { NavLink } from "react-router-dom";

function Navbar() {
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
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
