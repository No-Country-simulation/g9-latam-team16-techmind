package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotBlank;
import java.util.Map;

public record TextContentRequest(
        String title,

        @NotBlank(message = "El contenido de texto es obligatorio")
        String text,

        Map<String, Object> metadata
) {}