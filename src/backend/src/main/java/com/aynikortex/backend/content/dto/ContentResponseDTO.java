package com.aynikortex.backend.content.dto;

import com.aynikortex.backend.content.model.ContentType;
import java.time.LocalDateTime;
import java.util.UUID;

public record ContentResponseDTO(
        UUID id,
        String title,
        ContentType contentType,
        String category,
        LocalDateTime createdAt
) {}