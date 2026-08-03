package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotNull;
import org.springframework.web.multipart.MultipartFile;

public record FileContentRequest(
        String title,

        @NotNull(message = "El archivo es obligatorio")
        MultipartFile file,

        String metadata
) {}