package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public record TextContentRequest(
        @Size(max = 255, message = "El título no puede superar los 255 caracteres")
        String title,

        @NotBlank(message = "El contenido de texto es obligatorio")
        String text,

        String metadata
) {}