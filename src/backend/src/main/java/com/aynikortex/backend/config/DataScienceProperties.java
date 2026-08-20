package com.aynikortex.backend.config;

import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;

import java.time.Duration;

@Getter
@Setter
@ConfigurationProperties(prefix = "datascience")
public class DataScienceProperties {

    private String baseUrl;

    private Duration connectTimeout;

    private Duration readTimeout;

}