package com.aynikortex.backend.integration.dto.response;

import java.time.Instant;

public record DataScienceErrorResponse(
       String requestId,
       Instant timestamp,
       Integer status,
       String error,
       String code,
       String message,
       String path
) {
}
