package com.aynikortex.backend.content.dto;

import jakarta.validation.constraints.NotNull;
import org.springframework.web.multipart.MultipartFile;
import java.util.Map;

public record FileContentRequest(
        String title,

        @NotNull(message = "El archivo es obligatorio")
        MultipartFile file,

        Map<String, Object> metadata
) {
    // Constructor explícito para que Spring Boot y @ModelAttribute mapeen correctamente el multipart
    public FileContentRequest(String title, MultipartFile file, Map<String, Object> metadata) {
        this.title = title;
        this.file = file;
        this.metadata = metadata;
    }
}