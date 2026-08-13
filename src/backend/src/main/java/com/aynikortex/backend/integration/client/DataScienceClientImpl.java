package com.aynikortex.backend.integration.client;

import com.aynikortex.backend.exception.DataScienceException;
import com.aynikortex.backend.exception.ExternalServiceException;
import com.aynikortex.backend.integration.dto.request.FileClassificationRequest;
import com.aynikortex.backend.integration.dto.request.TextClassificationRequest;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.dto.response.DataScienceErrorResponse;
import com.aynikortex.backend.integration.dto.response.HealthResponse;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.MediaType;
import org.springframework.http.client.ClientHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestClient;

import java.io.IOException;

@Component
public class DataScienceClientImpl implements DataScienceClient {

    private final RestClient dataScienceRestClient;
    private final ObjectMapper objectMapper;

    public DataScienceClientImpl(
            RestClient dataScienceRestClient,
            ObjectMapper objectMapper
    ) {
        this.dataScienceRestClient = dataScienceRestClient;
        this.objectMapper = objectMapper;
    }

    @Override
    public ClassificationResponse predictText(
            TextClassificationRequest request
    ) {
        return dataScienceRestClient.post()
                .uri("/api/v1/predict/text")
                .body(request)
                .retrieve()
                .onStatus(
                        HttpStatusCode::isError,
                        (req, res) -> {
                            throw handleHttpError(res);
                        }
                )
                .body(ClassificationResponse.class);
    }

    @Override
    public ClassificationResponse predictFile(
            FileClassificationRequest request
    ) {
        try {
            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();

            HttpHeaders fileHeaders = new HttpHeaders();
            fileHeaders.setContentType(
                    MediaType.parseMediaType(
                            request.file().getContentType() != null
                                    ? request.file().getContentType()
                                    : MediaType.APPLICATION_OCTET_STREAM_VALUE
                    )
            );

            ByteArrayResource resource =
                    new ByteArrayResource(
                            request.file().getBytes()
                    ) {
                        @Override
                        public String getFilename() {
                            return request.file().getOriginalFilename();
                        }
                    };

            HttpEntity<ByteArrayResource> fileEntity =
                    new HttpEntity<>(resource, fileHeaders);

            body.add("file", fileEntity);

            if (request.metadata() != null) {
                body.add("metadata", request.metadata());
            }

            return dataScienceRestClient.post()
                    .uri("/api/v1/predict/file")
                    .contentType(MediaType.MULTIPART_FORM_DATA)
                    .body(body)
                    .retrieve()
                    .onStatus(
                            HttpStatusCode::isError,
                            (req, res) -> {
                                throw handleHttpError(res);
                            }
                    )
                    .body(ClassificationResponse.class);

        } catch (IOException e) {
            throw new DataScienceException(
                    "No se pudo preparar el archivo para Data Science",
                    e
            );
        }
    }

    @Override
    public HealthResponse checkHealth() {
        return dataScienceRestClient.get()
                .uri("/")
                .retrieve()
                .onStatus(
                        HttpStatusCode::isError,
                        (req, res) -> {
                            throw handleHttpError(res);
                        }
                )
                .body(HealthResponse.class);
    }

    private ExternalServiceException handleHttpError(
            ClientHttpResponse response
    ) {
        try {
            DataScienceErrorResponse error =
                    objectMapper.readValue(
                            response.getBody(),
                            DataScienceErrorResponse.class
                    );

            return new ExternalServiceException(
                    error.message(),
                    response.getStatusCode(),
                    error.error(),
                    error.code(),
                    error.requestId()
            );

        } catch (IOException e) {
            try {
                return new ExternalServiceException(
                        "Error comunicando con Data Science",
                        response.getStatusCode(),
                        null,
                        null,
                        null
                );
            } catch (Exception statusException) {
                return new ExternalServiceException(
                        "Error desconocido comunicando con Data Science"
                );
            }
        }
    }
}