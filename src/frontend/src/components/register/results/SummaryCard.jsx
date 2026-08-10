import { Card, CardContent, Typography } from "@mui/material";

function SummaryCard({ summary }) {
  if (!summary) {
    return null;
  }

  return (
    <Card variant="outlined" sx={{ borderRadius: 3 }}>
      <CardContent>
        <Typography variant="subtitle2" color="text.secondary" gutterBottom>
          Resumen
        </Typography>

        <Typography variant="body2" color="text.secondary">
          {summary}
        </Typography>
      </CardContent>
    </Card>
  );
}

export default SummaryCard;
