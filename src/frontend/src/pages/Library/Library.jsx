import { useState, useMemo } from "react";
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
  Stack,
} from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";
import ContentCard from "../../components/library/ContentCard";
import EmptyState from "../../components/common/EmptyState";
import {
  libraryMock,
  getCategoriesFromMock,
  getSubcategoriesFromMock,
  getContentTypesFromMock,
} from "../../mocks/libraryMock";

function Library() {
  const [searchTerm, setSearchTerm] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("");
  const [subcategoryFilter, setSubcategoryFilter] = useState("");
  const [typeFilter, setTypeFilter] = useState("");

  const categories = useMemo(() => getCategoriesFromMock(), []);
  const contentTypes = useMemo(() => getContentTypesFromMock(), []);

  const subcategories = useMemo(() => {
    if (!categoryFilter) return [];
    return getSubcategoriesFromMock(categoryFilter);
  }, [categoryFilter]);

  // Filtrar contenidos basado en búsqueda y filtros
  const filteredContent = useMemo(() => {
    return libraryMock.filter((item) => {
      const matchesSearch =
        searchTerm === "" ||
        item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.summary.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.keywords.some((kw) =>
          kw.toLowerCase().includes(searchTerm.toLowerCase()),
        );

      const matchesCategory =
        categoryFilter === "" || item.category === categoryFilter;
      const matchesSubcategory =
        subcategoryFilter === "" || item.subcategory === subcategoryFilter;
      const matchesType = typeFilter === "" || item.type === typeFilter;

      return (
        matchesSearch && matchesCategory && matchesSubcategory && matchesType
      );
    });
  }, [searchTerm, categoryFilter, subcategoryFilter, typeFilter]);

  const handleCategoryChange = (e) => {
    setCategoryFilter(e.target.value);
    setSubcategoryFilter(""); // Reset subcategory cuando cambia la categoría
  };

  return (
    <Box
      sx={{
        bgcolor: "background.default",
        minHeight: "100vh",
        py: { xs: 3, md: 5 },
      }}
    >
      <Container maxWidth="xl">
        {/* Encabezado */}
        <Box sx={{ mb: 4, textAlign: "center" }}>
          <Typography
            variant="h3"
            sx={{ fontWeight: 700, color: "text.primary", mb: 1 }}
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
            placeholder="Search by title, keyword or category..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            variant="outlined"
            InputProps={{
              startAdornment: (
                <SearchIcon sx={{ mr: 1, color: "action.active" }} />
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
                  {categories.map((cat) => (
                    <MenuItem key={cat} value={cat}>
                      {cat}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12} sm={6} md={4}>
              <FormControl
                fullWidth
                variant="outlined"
                disabled={!categoryFilter}
              >
                <InputLabel>Subcategoría</InputLabel>
                <Select
                  value={subcategoryFilter}
                  onChange={(e) => setSubcategoryFilter(e.target.value)}
                  label="Subcategoría"
                  sx={{ borderRadius: 2 }}
                >
                  <MenuItem value="">Todas las subcategorías</MenuItem>
                  {subcategories.map((subcat) => (
                    <MenuItem key={subcat} value={subcat}>
                      {subcat}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12} sm={12} md={4}>
              <FormControl fullWidth variant="outlined">
                <InputLabel>Tipo de contenido</InputLabel>
                <Select
                  value={typeFilter}
                  onChange={(e) => setTypeFilter(e.target.value)}
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

        {/* Resultados */}
        {filteredContent.length > 0 ? (
          <Grid container spacing={3}>
            {filteredContent.map((content) => (
              <Grid item xs={12} sm={6} md={4} key={content.id}>
                <ContentCard content={content} />
              </Grid>
            ))}
          </Grid>
        ) : (
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
