package com.aynikortex.backend.integration.dto.response;

import java.time.Instant;

public record HealthResponse(
        String serviceStatus,
        String service,
        String version,
        Long uptime,
        Instant timestamp
) {
}
