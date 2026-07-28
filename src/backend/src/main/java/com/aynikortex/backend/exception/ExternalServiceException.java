package com.aynikortex.backend.exception;

import org.springframework.http.HttpStatusCode;

public class ExternalServiceException extends RuntimeException {

    private final HttpStatusCode statusCode;
    private final String error;
    private final String errorCode;
    private final String requestId;

    public ExternalServiceException(String message) {
        super(message);
        this.statusCode = null;
        this.error = null;
        this.errorCode = null;
        this.requestId = null;
    }

    public ExternalServiceException(
            String message,
            HttpStatusCode statusCode,
            String error,
            String errorCode,
            String requestId
    ) {
        super(message);
        this.statusCode = statusCode;
        this.error = error;
        this.errorCode = errorCode;
        this.requestId = requestId;
    }

    public HttpStatusCode getStatusCode() {
        return statusCode;
    }

    public String getError() {
        return error;
    }

    public String getErrorCode() {
        return errorCode;
    }

    public String getRequestId() {
        return requestId;
    }
}