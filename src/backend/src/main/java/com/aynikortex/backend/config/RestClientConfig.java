package com.aynikortex.backend.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestClient;

@Configuration
public class RestClientConfig {
    private final DataScienceProperties dataScienceProperties;

    public RestClientConfig(DataScienceProperties dataScienceProperties) {
        this.dataScienceProperties = dataScienceProperties;
    }

    @Bean
    public RestClient dataScienceRestClient(RestClient.Builder builder) {
        return builder
                .baseUrl(dataScienceProperties.getBaseUrl())
                .defaultHeader(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON_VALUE)
                .build();
    }
}
