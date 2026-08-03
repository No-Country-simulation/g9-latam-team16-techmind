package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotBlank;

public record TextContentRequest(
        @NotBlank(message = "El título es obligatorio")
        String title,
        String description,
        @NotBlank(message = "El contenido de texto es obligatorio")
        String textContent
) {}