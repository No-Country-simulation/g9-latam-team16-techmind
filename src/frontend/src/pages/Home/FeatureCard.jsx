import "./FeatureCard.css";
import { Card, Stack, Typography, Avatar } from "@mui/material";

function FeatureCard({ icon, title, description }) {
  return (
    <Card sx={{ borderRadius: 3, p: 2, height: "100%" }}>
      <Stack
        direction="row"
        spacing={2}
        sx={{ alignItems: "center", height: "100%" }}
      >
        <Avatar sx={{ bgcolor: "primary.main", color: "common.white" }}>
          {icon}
        </Avatar>

        <Stack spacing={0.5}>
          <Typography variant="subtitle1" sx={{ fontWeight: 700 }}>
            {title}
          </Typography>

          <Typography variant="body2" color="text.secondary">
            {description}
          </Typography>
        </Stack>
      </Stack>
    </Card>
  );
}

export default FeatureCard;
