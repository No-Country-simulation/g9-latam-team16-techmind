package com.aynikortex.backend.content.dto;

import com.aynikortex.backend.entity.ContentType;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

public record ContentResponseDTO(
        UUID id,
        String title,
        ContentType contentType,
        String category,
        String subcategory,
        Double confidence,
        List<String> keywords,
        String summary,
        LocalDateTime createdAt
) {}