package com.aynikortex.backend.exception;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.time.Instant;
import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ExternalServiceException.class)
    public ResponseEntity<Map<String, Object>> handleExternalServiceException(
            ExternalServiceException ex, HttpServletRequest request) {

        Map<String, Object> errorBody = new HashMap<>();
        errorBody.put("timestamp", Instant.now().toString());
        errorBody.put("status", ex.getStatusCode() != null ? ex.getStatusCode().value() : HttpStatus.SERVICE_UNAVAILABLE.value());
        errorBody.put("error", "EXTERNAL_SERVICE_ERROR");
        errorBody.put("message", ex.getMessage());
        errorBody.put("path", request.getRequestURI());

        HttpStatus status = ex.getStatusCode() instanceof HttpStatus
                ? (HttpStatus) ex.getStatusCode()
                : HttpStatus.SERVICE_UNAVAILABLE;

        return ResponseEntity.status(status).body(errorBody);
    }

    @ExceptionHandler(DataScienceException.class)
    public ResponseEntity<Map<String, Object>> handleDataScienceException(
            DataScienceException ex, HttpServletRequest request) {

        Map<String, Object> errorBody = new HashMap<>();
        errorBody.put("timestamp", Instant.now().toString());
        errorBody.put("status", HttpStatus.UNPROCESSABLE_ENTITY.value());
        errorBody.put("error", "DATA_SCIENCE_PROCESSING_ERROR");
        errorBody.put("message", ex.getMessage());
        errorBody.put("path", request.getRequestURI());

        return ResponseEntity.status(HttpStatus.UNPROCESSABLE_ENTITY).body(errorBody);
    }
}
