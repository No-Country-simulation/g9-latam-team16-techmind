package com.aynikortex.backend.integration.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotBlank;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

public record FileClassificationRequest(
        MultipartFile file,
        Map<String, Object> metadata
) {
}
