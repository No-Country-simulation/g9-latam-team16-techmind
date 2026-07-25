package com.aynikortex.backend.domain;

import jakarta.validation.constraints.NotBlank;

import java.time.LocalDateTime;
import java.util.UUID;

public record DatosContentDto(
        @NotBlank
        UUID id,
        String title,
        String description,
        @NotBlank
        String contentType,
        @NotBlank
        String textContent,
        String fileName,
        String filePath,
        String category,
        String subCategory,
        Double confidence,
        String modelVersion,
        String keywords,
        LocalDateTime createdAt,
        LocalDateTime updateAt) {
}
