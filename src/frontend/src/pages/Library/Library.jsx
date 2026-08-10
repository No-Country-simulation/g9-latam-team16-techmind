import { useEffect, useMemo, useState } from "react";
import {
  Box,
  Container,
  Typography,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Grid,
  InputAdornment,
} from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";

import ContentCard from "../../components/library/ContentCard";
import EmptyState from "../../components/common/EmptyState";
import { getContents } from "../../services/contentService";

function Library() {
  const [contents, setContents] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("");
  const [subcategoryFilter, setSubcategoryFilter] = useState("");
  const [typeFilter, setTypeFilter] = useState("");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Cargar contenidos desde el backend
  useEffect(() => {
    const loadContents = async () => {
      try {
        setLoading(true);
        setError("");

        const data = await getContents();
        setContents(data);
      } catch (err) {
        console.error("Error al cargar contenidos:", err);
        setError("No fue posible cargar la biblioteca.");
      } finally {
        setLoading(false);
      }
    };

    loadContents();
  }, []);

  // Obtener categorías a partir de los contenidos reales
  const categories = useMemo(() => {
    return [...new Set(contents.map((item) => item.category).filter(Boolean))];
  }, [contents]);

  // Obtener subcategorías según la categoría seleccionada
  const subcategories = useMemo(() => {
    if (!categoryFilter) {
      return [];
    }

    return [
      ...new Set(
        contents
          .filter((item) => item.category === categoryFilter)
          .map((item) => item.subcategory)
          .filter(Boolean),
      ),
    ];
  }, [contents, categoryFilter]);

  // Obtener tipos de contenido disponibles
  const contentTypes = useMemo(() => {
    return [
      ...new Set(contents.map((item) => item.contentType).filter(Boolean)),
    ];
  }, [contents]);

  // Filtrar contenidos
  const filteredContent = useMemo(() => {
    const normalizedSearch = searchTerm.toLowerCase().trim();

    return contents.filter((item) => {
      const matchesSearch =
        normalizedSearch === "" ||
        item.title?.toLowerCase().includes(normalizedSearch) ||
        item.summary?.toLowerCase().includes(normalizedSearch) ||
        item.category?.toLowerCase().includes(normalizedSearch) ||
        item.subcategory?.toLowerCase().includes(normalizedSearch) ||
        item.keywords?.some((keyword) =>
          keyword.toLowerCase().includes(normalizedSearch),
        );

      const matchesCategory =
        categoryFilter === "" || item.category === categoryFilter;

      const matchesSubcategory =
        subcategoryFilter === "" || item.subcategory === subcategoryFilter;

      const matchesType = typeFilter === "" || item.contentType === typeFilter;

      return (
        matchesSearch && matchesCategory && matchesSubcategory && matchesType
      );
    });
  }, [contents, searchTerm, categoryFilter, subcategoryFilter, typeFilter]);

  const handleCategoryChange = (event) => {
    setCategoryFilter(event.target.value);
    setSubcategoryFilter("");
  };

  return (
    <Box
      sx={{
        bgcolor: "background.default",
        minHeight: "100vh",
        py: { xs: 3, md: 5 },
      }}
    >
      <Container maxWidth="lg">
        {/* Encabezado */}
        <Box sx={{ mb: 4, textAlign: "center" }}>
          <Typography
            variant="h3"
            sx={{
              fontWeight: 700,
              color: "text.primary",
              mb: 1,
            }}
          >
            Biblioteca AyniKortex
          </Typography>

          <Typography variant="body1" color="text.secondary">
            Explora nuestra biblioteca de conocimiento técnico. Encuentra
            contenidos clasificados, filtra por categoría y descubre nuevas
            perspectivas.
          </Typography>
        </Box>

        {/* Barra de búsqueda y filtros */}
        <Box sx={{ mb: 4 }}>
          {/* Búsqueda */}
          <TextField
            fullWidth
            placeholder="Buscar por título, palabra clave o categoría..."
            value={searchTerm}
            onChange={(event) => setSearchTerm(event.target.value)}
            variant="outlined"
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon color="action" />
                </InputAdornment>
              ),
            }}
            sx={{
              mb: 3,
              "& .MuiOutlinedInput-root": {
                borderRadius: 2,
              },
            }}
          />

          {/* Filtros */}
          <Grid container spacing={2}>
            {/* Categoría */}
            <Grid item xs={12} sm={6} md={4}>
              <FormControl fullWidth variant="outlined">
                <InputLabel>Categoría</InputLabel>

                <Select
                  value={categoryFilter}
                  onChange={handleCategoryChange}
                  label="Categoría"
                  sx={{ borderRadius: 2 }}
                >
                  <MenuItem value="">Todas las categorías</MenuItem>

                  {categories.map((category) => (
                    <MenuItem key={category} value={category}>
                      {category}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            {/* Subcategoría */}
            <Grid item xs={12} sm={6} md={4}>
              <FormControl
                fullWidth
                variant="outlined"
                disabled={!categoryFilter}
              >
                <InputLabel>Subcategoría</InputLabel>

                <Select
                  value={subcategoryFilter}
                  onChange={(event) => setSubcategoryFilter(event.target.value)}
                  label="Subcategoría"
                  sx={{ borderRadius: 2 }}
                >
                  <MenuItem value="">Todas las subcategorías</MenuItem>

                  {subcategories.map((subcategory) => (
                    <MenuItem key={subcategory} value={subcategory}>
                      {subcategory}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            {/* Tipo de contenido */}
            <Grid item xs={12} sm={12} md={4}>
              <FormControl fullWidth variant="outlined">
                <InputLabel>Tipo de contenido</InputLabel>

                <Select
                  value={typeFilter}
                  onChange={(event) => setTypeFilter(event.target.value)}
                  label="Tipo de contenido"
                  sx={{ borderRadius: 2 }}
                >
                  <MenuItem value="">Todos los tipos</MenuItem>

                  {contentTypes.map((type) => (
                    <MenuItem key={type} value={type}>
                      {type}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
          </Grid>
        </Box>

        {/* Cargando */}
        {loading && (
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              py: 6,
            }}
          >
            <Typography color="text.secondary">
              Cargando contenidos...
            </Typography>
          </Box>
        )}

        {/* Error */}
        {!loading && error && (
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              py: 6,
            }}
          >
            <Typography color="error">{error}</Typography>
          </Box>
        )}

        {/* Resultados */}
        {!loading && !error && filteredContent.length > 0 && (
          <Box
            sx={{
              display: "grid",
              gridTemplateColumns: {
                xs: "1fr",
                sm: "repeat(2, 1fr)",
                md: "repeat(3, 1fr)",
              },
              gap: 3,
            }}
          >
            {filteredContent.map((content) => (
              <ContentCard key={content.id} content={content} />
            ))}
          </Box>
        )}

        {/* Sin resultados */}
        {!loading && !error && filteredContent.length === 0 && (
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              py: 6,
            }}
          >
            <EmptyState
              title="No hay resultados"
              message="No encontramos contenidos que coincidan con tu búsqueda. Intenta con otros filtros."
            />
          </Box>
        )}
      </Container>
    </Box>
  );
}

export default Library;
