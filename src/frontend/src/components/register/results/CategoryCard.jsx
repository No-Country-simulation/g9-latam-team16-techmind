import { Card, CardContent, Chip, Stack, Typography } from "@mui/material";

function CategoryCard({ category, subcategory }) {
  return (
    <Card variant="outlined" sx={{ borderRadius: 3 }}>
      <CardContent>
        <Typography variant="subtitle2" color="text.secondary" gutterBottom>
          Categoría
        </Typography>

        <Stack spacing={1}>
          <Chip
            label={category || "Sin categoría"}
            color="primary"
            sx={{ alignSelf: "flex-start", fontWeight: 600 }}
          />

          {subcategory && (
            <Typography variant="body2" color="text.secondary">
              Subcategoría: <strong>{subcategory}</strong>
            </Typography>
          )}
        </Stack>
      </CardContent>
    </Card>
  );
}

export default CategoryCard;
