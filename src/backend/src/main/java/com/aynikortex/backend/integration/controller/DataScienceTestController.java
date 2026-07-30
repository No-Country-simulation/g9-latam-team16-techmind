package com.aynikortex.backend.integration.controller;

import com.aynikortex.backend.integration.dto.request.TextClassificationRequest;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.dto.response.HealthResponse;
import com.aynikortex.backend.integration.service.DataScienceIntegrationService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

@RestController
@RequestMapping("/api/test/datascience")
public class DataScienceTestController {

    private final DataScienceIntegrationService integrationService;
    private final ObjectMapper objectMapper;

    public DataScienceTestController(
            DataScienceIntegrationService integrationService,
            ObjectMapper objectMapper
    ) {
        this.integrationService = integrationService;
        this.objectMapper = objectMapper;
    }


    @PostMapping("/text")
    public ClassificationResponse classifyText(
            @RequestBody TextClassificationRequest request) {

        return integrationService.classifyText(
                request.title(),
                request.text(),
                request.metadata()
        );
    }


    @GetMapping("/health")
    public HealthResponse health() {
        return integrationService.checkDataScienceHealth();
    }


    @PostMapping(
            value = "/file",
            consumes = MediaType.MULTIPART_FORM_DATA_VALUE
    )
    public ClassificationResponse classifyFile(
            @RequestPart("file") MultipartFile file,
            @RequestPart(value = "metadata", required = false) String metadata
    ) throws JsonProcessingException {

        Map<String, Object> metadataMap = metadata != null
                ? objectMapper.readValue(
                metadata,
                new TypeReference<Map<String, Object>>() {}
        )
                : null;

        return integrationService.classifyFile(
                file,
                metadataMap
        );
    }
}