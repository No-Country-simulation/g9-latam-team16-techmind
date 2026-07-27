package com.aynikortex.backend.exception;

public class DataScienceException extends RuntimeException {
    public DataScienceException(String message) {
        super(message);
    }

    public DataScienceException(String message, Throwable cause) {
        super(message, cause);
    }
}
