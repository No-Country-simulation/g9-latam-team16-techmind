package com.aynikortex.backend.content.dto;

import com.aynikortex.backend.entity.ContentType;
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
        String fileFormat,
        String category,
        String subCategory,
        Double confidence,
        String modelVersion,
        List<KeywordDTO> keywords,
        LocalDateTime createdAt,
        LocalDateTime updateAt
) {}