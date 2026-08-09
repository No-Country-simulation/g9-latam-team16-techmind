package com.aynikortex.backend.integration.dto.request;

import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

public record FileClassificationRequest(
        MultipartFile file,
        Map<String, Object> metadata
) {

}
