package com.aynikortex.backend.integration.service;

import com.aynikortex.backend.integration.client.DataScienceClient;
import com.aynikortex.backend.integration.dto.request.FileClassificationRequest;
import com.aynikortex.backend.integration.dto.request.TextClassificationRequest;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.dto.response.HealthResponse;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

@Service
public class DataScienceIntegrationService {

    private final DataScienceClient dataScienceClient;

    public DataScienceIntegrationService(DataScienceClient dataScienceClient) {
        this.dataScienceClient = dataScienceClient;
    }

    /**
     * Orquesta la clasificación de contenido basado en texto plano.
     */
    public ClassificationResponse classifyText(String title, String text, Map<String, Object> metadata) {
        TextClassificationRequest request = new TextClassificationRequest(title, text, metadata);
        return dataScienceClient.predictText(String.valueOf(request));
    }

    /**
     * Orquesta la clasificación de contenido basado en un archivo adjunto (PDF, Word, TXT, MD).
     */
    public ClassificationResponse classifyFile(MultipartFile file, Map<String, Object> metadata) {
        FileClassificationRequest request = new FileClassificationRequest(file, metadata);
        return dataScienceClient.predictFile(request);
    }

    /**
     * Verifica el estado de salud (health check) del microservicio de FastAPI.
     */
    public HealthResponse checkDataScienceHealth() {
        return dataScienceClient.checkHealth();
    }
}
