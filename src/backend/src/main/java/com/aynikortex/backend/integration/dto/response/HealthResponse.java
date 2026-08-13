package com.aynikortex.backend.integration.dto.response;


import com.fasterxml.jackson.annotation.JsonProperty;

public record HealthResponse(
        String message,

        @JsonProperty("model_loaded")
        Boolean modelLoaded
) {
}
