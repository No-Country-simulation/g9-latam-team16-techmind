package com.aynikortex.backend.integration.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;

public record DataScienceErrorResponse(
        @JsonProperty("request_id") String requestId,
        @JsonProperty("timestamp") String timestamp,
        @JsonProperty("status") int status,
        @JsonProperty("error") String error,
        @JsonProperty("code") String code,
        @JsonProperty("message") String message,
        @JsonProperty("path") String path
) {
}
