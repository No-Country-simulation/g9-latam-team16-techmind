import { createTheme } from "@mui/material/styles";

const colors = {
  primary: "#7c3aed",
  primaryHover: "#6d28d9",
  secondary: "#2563eb",
  backgroundLight: "#f8fafc",
  backgroundDark: "#020617",
  surfaceLight: "#ffffff",
  surfaceDark: "#0f172a",
  textLight: "#0f172a",
  textDark: "#f8fafc",
  textSecondaryLight: "#475569",
  textSecondaryDark: "rgba(248, 250, 252, 0.72)",
  borderLight: "#e2e8f0",
  borderDark: "rgba(255, 255, 255, 0.08)",
};

export const getThemeTokens = (mode) => ({
  primary: colors.primary,
  primaryHover: colors.primaryHover,
  secondary: colors.secondary,
  background: mode === "dark" ? colors.backgroundDark : colors.backgroundLight,
  surface: mode === "dark" ? colors.surfaceDark : colors.surfaceLight,
  text: mode === "dark" ? colors.textDark : colors.textLight,
  textSecondary:
    mode === "dark" ? colors.textSecondaryDark : colors.textSecondaryLight,
  border: mode === "dark" ? colors.borderDark : colors.borderLight,
});

const createAppTheme = (mode) => {
  const tokens = getThemeTokens(mode);

  return createTheme({
    palette: {
      mode,
      primary: {
        main: tokens.primary,
        dark: colors.primaryHover,
        light: "#8b5cf6",
      },
      secondary: {
        main: tokens.secondary,
      },
      background: {
        default: tokens.background,
        paper: tokens.surface,
      },
      text: {
        primary: tokens.text,
        secondary: tokens.textSecondary,
      },
      divider: tokens.border,
    },
    typography: {
      fontFamily: ["Inter", "Roboto", "Arial", "sans-serif"].join(","),
      h1: { fontWeight: 700 },
      h2: { fontWeight: 700 },
      h3: { fontWeight: 700 },
      h4: { fontWeight: 700 },
      h5: { fontWeight: 700 },
      h6: { fontWeight: 700 },
    },
    shape: {
      borderRadius: 16,
    },
    components: {
      MuiButton: {
        defaultProps: {
          disableElevation: true,
        },
      },
      MuiCard: {
        styleOverrides: {
          root: {
            boxShadow:
              mode === "dark"
                ? "0 12px 32px rgba(2, 6, 23, 0.45)"
                : "0 10px 30px rgba(15, 23, 42, 0.08)",
          },
        },
      },
    },
  });
};

export const lightTheme = createAppTheme("light");
export const darkTheme = createAppTheme("dark");
