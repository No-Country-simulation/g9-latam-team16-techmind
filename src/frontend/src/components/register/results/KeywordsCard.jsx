import { Card, CardContent, Chip, Stack, Typography } from "@mui/material";

function KeywordsCard({ keywords }) {
  if (!keywords?.length) {
    return null;
  }

  return (
    <Card variant="outlined" sx={{ borderRadius: 3 }}>
      <CardContent>
        <Typography variant="subtitle2" color="text.secondary" gutterBottom>
          Palabras Clave
        </Typography>

        <Stack direction="row" spacing={1} useFlexGap flexWrap="wrap">
          {keywords.map((keyword, index) => (
            <Chip
              key={`${keyword}-${index}`}
              label={keyword}
              variant="outlined"
              size="small"
            />
          ))}
        </Stack>
      </CardContent>
    </Card>
  );
}

export default KeywordsCard;
