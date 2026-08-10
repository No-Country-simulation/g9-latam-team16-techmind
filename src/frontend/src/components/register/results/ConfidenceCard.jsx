import {
  Box,
  Card,
  CardContent,
  LinearProgress,
  Typography,
} from "@mui/material";

function ConfidenceCard({ confidence }) {
  if (confidence === undefined || confidence === null) {
    return null;
  }

  const percentage = Math.round(confidence * 100);

  return (
    <Card variant="outlined" sx={{ borderRadius: 3 }}>
      <CardContent>
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            mb: 1,
          }}
        >
          <Typography variant="subtitle2" color="text.secondary">
            Confianza
          </Typography>

          <Typography variant="h6" sx={{ fontWeight: 700 }}>
            {percentage}%
          </Typography>
        </Box>

        <LinearProgress
          variant="determinate"
          value={percentage}
          sx={{
            height: 8,
            borderRadius: 4,
          }}
        />
      </CardContent>
    </Card>
  );
}

export default ConfidenceCard;
