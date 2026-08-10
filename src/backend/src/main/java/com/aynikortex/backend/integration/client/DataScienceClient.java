package com.aynikortex.backend.integration.client;

import com.aynikortex.backend.integration.dto.request.FileClassificationRequest;
import com.aynikortex.backend.integration.dto.request.TextClassificationRequest;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.dto.response.HealthResponse;

public interface DataScienceClient {
    ClassificationResponse predictText(TextClassificationRequest request);

    ClassificationResponse predictFile(FileClassificationRequest request);

    HealthResponse checkHealth();
}
