package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotBlank;
import org.springframework.web.multipart.MultipartFile;

public record FileContentRequest(
        @NotBlank(message = "El título es obligatorio")
        String title,
        String description,
        MultipartFile file,
        String fileName,
        String filePath
) {}