package com.aynikortex.backend.integration.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;

public record ClassificationResponse(
        @JsonProperty("category") String category,
        @JsonProperty("subcategory") String subcategory,
        @JsonProperty("confidence") BigDecimal confidence,
        @JsonProperty("keywords") Object keywords, // Puede ajustarse a List<String> según el contrato exacto de FastAPI
        @JsonProperty("model_version") String modelVersion
) {
}
