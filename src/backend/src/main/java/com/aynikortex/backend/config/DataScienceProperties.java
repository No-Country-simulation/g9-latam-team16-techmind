package com.aynikortex.backend.config;

import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;

import java.time.Duration;

// representa configuración externa de la aplicación
@Getter
@Setter
@ConfigurationProperties(prefix = "datascience")
public class DataScienceProperties {

    private String baseUrl = "http://localhost:8000";

    private Duration connectTimeout = Duration.ofSeconds(5);

    private Duration readTimeout = Duration.ofSeconds(10);

}