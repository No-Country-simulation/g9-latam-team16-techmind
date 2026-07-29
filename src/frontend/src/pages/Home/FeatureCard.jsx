import "./FeatureCard.css";
import { Card, Stack, Typography, Avatar } from "@mui/material";

function FeatureCard({ icon, title, description }) {
  return (
    <Card className="feature-card">
      <Stack
        direction="row"
        spacing={2}
        sx={{ alignItems: "center" }}
        className="feature-card-content"
      >
        <Avatar className="feature-card-avatar">{icon}</Avatar>

        <Stack>
          <Typography className="feature-card-title">{title}</Typography>

          <Typography variant="body2" className="feature-card-description">
            {description}
          </Typography>
        </Stack>
      </Stack>
    </Card>
  );
}

export default FeatureCard;
