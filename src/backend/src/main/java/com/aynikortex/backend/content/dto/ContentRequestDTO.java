package com.aynikortex.backend.content.dto;

import com.aynikortex.backend.domain.ContentType;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public record ContentRequestDTO(
        @NotBlank(message = "El título es obligatorio y no puede estar vacío")
        String title,

        @NotNull(message = "El tipo de contenido es obligatorio")
        ContentType contentType,

        String textContent,
        String fileName,
        String filePath
) {}