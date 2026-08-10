import { Stack } from "@mui/material";

import ResultHeader from "./ResultHeader";
import CategoryCard from "./CategoryCard";
import ConfidenceCard from "./ConfidenceCard";
import SummaryCard from "./SummaryCard";
import KeywordsCard from "./KeywordsCard";

function ClassificationResult({ classification }) {
  if (!classification) {
    return null;
  }

  return (
    <Stack spacing={2}>
      <ResultHeader title={classification.title} />

      <CategoryCard
        category={classification.category}
        subcategory={classification.subcategory}
      />

      <ConfidenceCard confidence={classification.confidence} />

      <SummaryCard summary={classification.summary} />

      <KeywordsCard keywords={classification.keywords} />
    </Stack>
  );
}

export default ClassificationResult;
