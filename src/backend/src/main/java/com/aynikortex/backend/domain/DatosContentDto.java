package com.aynikortex.backend.domain;

import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.validation.constraints.NotBlank;
import jdk.jfr.ContentType;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

public record DatosContentDto<Keyword>(
        @NotBlank
        UUID id,
        String title,
        String description,
        @NotBlank
        ContentType contentType,
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
        LocalDateTime updateAt) {
}
