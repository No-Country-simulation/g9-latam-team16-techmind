package com.aynikortex.backend.integration.dto.response;

import java.time.Instant;

public record ClassificationResponse(
        String requestId,
        String status,
        Classification classification,
        Integer processingTime,
        String modelVersion,
        Instant timestamp
) {}
