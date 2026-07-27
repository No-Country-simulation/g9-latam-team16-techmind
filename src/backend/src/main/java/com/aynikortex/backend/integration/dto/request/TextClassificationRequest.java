package com.aynikortex.backend.integration.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotBlank;

import java.util.Map;

public record TextClassificationRequest(
        @JsonProperty("title")
        String title,

        @NotBlank(message = "El texto a clasificar no puede estar vacío")
        @JsonProperty("text")
        String text,

        @JsonProperty("metadata")
        Map<String, Object> metadata
) {
}
