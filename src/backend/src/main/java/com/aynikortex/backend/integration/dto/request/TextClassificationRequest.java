package com.aynikortex.backend.integration.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotBlank;

import java.util.Map;

public record TextClassificationRequest(
        String title,
        String text,
        Map<String, Object> metadata
) {
}
