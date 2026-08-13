package com.aynikortex.backend.integration.dto.response;


import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;

public record HealthResponse(
        String serviceStatus,
        String service,
        String version,
        Long uptime,
        Instant timestamp
) {
}
