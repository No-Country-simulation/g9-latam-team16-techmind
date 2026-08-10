import { useEffect, useMemo, useState } from "react";
import {
  Box,
  Button,
  Container,
  Typography,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  InputAdornment,
} from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";

import ContentCard from "../../components/library/ContentCard";
import EmptyState from "../../components/common/EmptyState";

import {
  getContents,
  searchByTitle,
  searchByKeyword,
  searchByCategory,
  deleteContent,
} from "../../services/contentService";

function Library() {
  const [allContents, setAllContents] = useState([]);

  const [contents, setContents] = useState([]);

  // Búsqueda
  const [searchTerm, setSearchTerm] = useState("");
  const [searchType, setSearchType] = useState("title");

  // Filtros
  const [categoryFilter, setCategoryFilter] = useState("");
  const [subcategoryFilter, setSubcategoryFilter] = useState("");
  const [typeFilter, setTypeFilter] = useState("");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadContents = async () => {
      try {
        setLoading(true);
        setError("");

        const data = await getContents();

        setAllContents(data);
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

  const categories = useMemo(() => {
    return [
      ...new Set(allContents.map((item) => item.category).filter(Boolean)),
    ];
  }, [allContents]);

  // Subcategorías disponibles según categoría seleccionada
  const subcategories = useMemo(() => {
    if (!categoryFilter) {
      return [];
    }

    return [
      ...new Set(
        allContents
          .filter((item) => item.category === categoryFilter)
          .map((item) => item.subcategory)
          .filter(Boolean),
      ),
    ];
  }, [allContents, categoryFilter]);

  // Tipos de contenido disponibles
  const contentTypes = useMemo(() => {
    return [
      ...new Set(allContents.map((item) => item.contentType).filter(Boolean)),
    ];
  }, [allContents]);

  // =========================================================
  // BÚSQUEDA EN BACKEND
  // =========================================================

  const handleSearch = async () => {
    const normalizedSearch = searchTerm.trim();

    // Si la búsqueda está vacía, mostrar nuevamente todos
    // los contenidos cargados inicialmente.
    if (!normalizedSearch) {
      setContents(allContents);
      setError("");
      return;
    }

    try {
      setLoading(true);
      setError("");

      let data;

      switch (searchType) {
        case "title":
          data = await searchByTitle(normalizedSearch);
          break;

        case "keyword":
          data = await searchByKeyword(normalizedSearch);
          break;

        case "category":
          data = await searchByCategory(normalizedSearch);
          break;

        default:
          data = await searchByTitle(normalizedSearch);
      }

      setContents(data);
    } catch (err) {
      console.error("Error al buscar contenidos:", err);
      setError("No fue posible realizar la búsqueda.");
      setContents([]);
    } finally {
      setLoading(false);
    }
  };

  const handleResetFilters = () => {
    setSearchTerm("");
    setSearchType("title");
    setCategoryFilter("");
    setSubcategoryFilter("");
    setTypeFilter("");
    setContents(allContents);
    setError("");
  };

  // Ejecutar búsqueda al presionar Enter
  const handleSearchKeyDown = (event) => {
    if (event.key === "Enter") {
      handleSearch();
    }
  };

  const handleCategoryChange = (event) => {
    setCategoryFilter(event.target.value);
    setSubcategoryFilter("");
  };

  const filteredContent = useMemo(() => {
    return contents.filter((item) => {
      const matchesCategory =
        categoryFilter === "" || item.category === categoryFilter;

      const matchesSubcategory =
        subcategoryFilter === "" || item.subcategory === subcategoryFilter;

      const matchesType = typeFilter === "" || item.contentType === typeFilter;

      return matchesCategory && matchesSubcategory && matchesType;
    });
  }, [contents, categoryFilter, subcategoryFilter, typeFilter]);

  const handleDeleteContent = async (id) => {
    try {
      setError("");

      await deleteContent(id);

      // Actualizar la lista completa
      setAllContents((prev) => prev.filter((item) => item.id !== id));

      // Actualizar los resultados que se están mostrando
      setContents((prev) => prev.filter((item) => item.id !== id));
    } catch (err) {
      console.error("Error al eliminar contenido:", err);
      setError("No fue posible eliminar el contenido.");
    }
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
        {/* ===================================================
            ENCABEZADO
        =================================================== */}

        <Box
          sx={{
            mb: 4,
            textAlign: "center",
          }}
        >
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

        {/* ===================================================
            BÚSQUEDA
        =================================================== */}

        <Box sx={{ mb: 4 }}>
          <Box
            sx={{
              display: "flex",
              gap: 2,
              flexDirection: {
                xs: "column",
                md: "row",
              },
            }}
          >
            {/* Tipo de búsqueda */}
            <FormControl
              sx={{
                minWidth: {
                  xs: "100%",
                  md: 200,
                },
              }}
            >
              <InputLabel>Buscar por</InputLabel>

              <Select
                value={searchType}
                onChange={(event) => setSearchType(event.target.value)}
                label="Buscar por"
                sx={{
                  borderRadius: 2,
                }}
              >
                <MenuItem value="title">Título</MenuItem>

                <MenuItem value="keyword">Keyword</MenuItem>

                <MenuItem value="category">Categoría</MenuItem>
              </Select>
            </FormControl>

            {/* Campo de búsqueda */}
            <TextField
              fullWidth
              placeholder={
                searchType === "title"
                  ? "Buscar por título..."
                  : searchType === "keyword"
                    ? "Buscar por keyword..."
                    : "Buscar por categoría..."
              }
              value={searchTerm}
              onChange={(event) => setSearchTerm(event.target.value)}
              onKeyDown={handleSearchKeyDown}
              variant="outlined"
              slotProps={{
                input: {
                  startAdornment: (
                    <InputAdornment position="start">
                      <SearchIcon color="action" />
                    </InputAdornment>
                  ),
                },
              }}
              sx={{
                "& .MuiOutlinedInput-root": {
                  borderRadius: 2,
                },
              }}
            />
          </Box>

          <Typography
            variant="caption"
            color="text.secondary"
            sx={{
              display: "block",
              mt: 1,
              ml: 0.5,
            }}
          >
            Presiona Enter para buscar
          </Typography>

          {/* =================================================
              FILTROS
          ================================================= */}

          <Box
            sx={{
              display: "grid",
              gridTemplateColumns: {
                xs: "1fr",
                sm: "repeat(2, 1fr)",
                md: "repeat(3, 1fr)",
              },
              gap: 2,
              mt: 3,
            }}
          >
            {/* Categoría */}
            <FormControl fullWidth>
              <InputLabel>Categoría</InputLabel>

              <Select
                value={categoryFilter}
                onChange={handleCategoryChange}
                label="Categoría"
                sx={{
                  borderRadius: 2,
                }}
              >
                <MenuItem value="">Todas las categorías</MenuItem>

                {categories.map((category) => (
                  <MenuItem key={category} value={category}>
                    {category}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            {/* Subcategoría */}
            <FormControl fullWidth disabled={!categoryFilter}>
              <InputLabel>Subcategoría</InputLabel>

              <Select
                value={subcategoryFilter}
                onChange={(event) => setSubcategoryFilter(event.target.value)}
                label="Subcategoría"
                sx={{
                  borderRadius: 2,
                }}
              >
                <MenuItem value="">Todas las subcategorías</MenuItem>

                {subcategories.map((subcategory) => (
                  <MenuItem key={subcategory} value={subcategory}>
                    {subcategory}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            {/* Tipo de contenido */}
            <FormControl fullWidth>
              <InputLabel>Tipo de contenido</InputLabel>

              <Select
                value={typeFilter}
                onChange={(event) => setTypeFilter(event.target.value)}
                label="Tipo de contenido"
                sx={{
                  borderRadius: 2,
                }}
              >
                <MenuItem value="">Todos los tipos</MenuItem>

                {contentTypes.map((type) => (
                  <MenuItem key={type} value={type}>
                    {type}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "flex-end",
              mt: 2,
            }}
          >
            <Button
              variant="outlined"
              onClick={handleResetFilters}
              disabled={
                !searchTerm &&
                !categoryFilter &&
                !subcategoryFilter &&
                !typeFilter
              }
            >
              Limpiar búsqueda y filtros
            </Button>
          </Box>
        </Box>

        {/* ===================================================
            CARGANDO
        =================================================== */}

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

        {/* ===================================================
            ERROR
        =================================================== */}

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

        {/* ===================================================
            RESULTADOS
        =================================================== */}

        {!loading && !error && filteredContent.length > 0 && (
          <Box
            sx={{
              display: "grid",
              gridTemplateColumns: {
                xs: "1fr",
                sm: "repeat(2, minmax(0, 1fr))",
                md: "repeat(3, minmax(0, 1fr))",
              },
              gap: 3,
            }}
          >
            {filteredContent.map((content) => (
              <ContentCard
                key={content.id}
                content={content}
                onDelete={handleDeleteContent}
              />
            ))}
          </Box>
        )}

        {/* ===================================================
            SIN RESULTADOS
        =================================================== */}

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
