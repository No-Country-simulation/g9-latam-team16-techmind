package com.aynikortex.backend.domain;

import jakarta.validation.constraints.NotBlank;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

public record DatosContentDto(
        @NotBlank
        UUID id,
        String title,
        String description,
        @NotBlank
        ContentType contentType, // Asegúrate de que usa com.aynikortex.backend.domain.ContentType
        @NotBlank
        String textContent,
        String fileName,
        String filePath,
        String category,
        String subCategory,
        Double confidence,
        String modelVersion,
        List<Keyword> keywords,
        LocalDateTime createdAt,
        LocalDateTime updateAt
) {}