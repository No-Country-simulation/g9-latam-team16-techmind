package com.aynikortex.backend.integration.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;

public record HealthResponse(
        @JsonProperty("service_status") String serviceStatus,
        @JsonProperty("service") String service,
        @JsonProperty("version") String version,
        @JsonProperty("uptime") long uptime,
        @JsonProperty("timestamp") String timestamp
) {
}
