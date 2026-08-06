package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotNull;
import org.springframework.web.multipart.MultipartFile;
import java.util.Map;

public record FileContentRequest(
        String title,

        @NotNull(message = "El archivo es obligatorio")
        MultipartFile file,

        Map<String, Object> metadata
) {}