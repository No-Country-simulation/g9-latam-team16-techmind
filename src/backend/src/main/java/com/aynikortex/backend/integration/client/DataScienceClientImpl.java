package com.aynikortex.backend.integration.client;

import com.aynikortex.backend.exception.ExternalServiceException;
import com.aynikortex.backend.integration.dto.request.FileClassificationRequest;
import com.aynikortex.backend.integration.dto.request.TextClassificationRequest;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.dto.response.HealthResponse;
import org.springframework.core.io.InputStreamResource;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestClient;

@Component
public class DataScienceClientImpl implements DataScienceClient {

    private final RestClient dataScienceRestClient;

    public DataScienceClientImpl(RestClient dataScienceRestClient) {
        this.dataScienceRestClient = dataScienceRestClient;
    }

    @Override
    public ClassificationResponse predictText(TextClassificationRequest request) {
        return dataScienceRestClient.post()
                .uri("/api/v1/predict/text")
                .body(request)
                .retrieve()
                .onStatus(HttpStatusCode::isError, (req, res) -> {
                    throw new ExternalServiceException("Error al comunicarse con el servicio de IA para texto", res.getStatusCode());
                })
                .body(ClassificationResponse.class);
    }

    @Override
    public ClassificationResponse predictFile(FileClassificationRequest request) {
        try {
            // 1. Construimos el cuerpo multipart que exige FastAPI
            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();

            // Adjuntamos el archivo binario usando un InputStreamResource para eficiencia de memoria
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.parseMediaType(
                    request.file().getContentType() != null ? request.file().getContentType() : MediaType.APPLICATION_OCTET_STREAM_VALUE
            ));

            HttpEntity<InputStreamResource> fileEntity = new HttpEntity<>(
                    new InputStreamResource(request.file().getInputStream()),
                    headers
            );

            body.add("file", fileEntity);

            // Si hay metadatos opcionales, podemos agregarlos también al form
            if (request.metadata() != null) {
                body.add("metadata", request.metadata());
            }

            // 2. Ejecutamos la petición POST enviando multipart/form-data
            return dataScienceRestClient.post()
                    .uri("/api/v1/predict/file")
                    .contentType(MediaType.MULTIPART_FORM_DATA)
                    .body(body)
                    .retrieve()
                    .onStatus(HttpStatusCode::isError, (req, res) -> {
                        throw new ExternalServiceException("Error al procesar el archivo en el servicio de Ciencia de Datos", res.getStatusCode());
                    })
                    .body(ClassificationResponse.class);

        } catch (Exception e) {
            throw new ExternalServiceException("No se pudo leer el archivo adjunto para enviarlo a FastAPI: " + e.getMessage());
        }
    }

    @Override
    public HealthResponse checkHealth() {
        return dataScienceRestClient.get()
                .uri("/api/v1/health")
                .retrieve()
                .onStatus(HttpStatusCode::isError, (req, res) -> {
                    throw new ExternalServiceException("El servicio de Ciencia de Datos no responde correctamente", res.getStatusCode());
                })
                .body(HealthResponse.class);
    }
}
