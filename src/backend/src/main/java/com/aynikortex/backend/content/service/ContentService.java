package com.aynikortex.backend.content.service;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.content.mapper.ContentMapper;
import com.aynikortex.backend.content.repository.ContentRepository;
import com.aynikortex.backend.entity.Contenido;
import com.aynikortex.backend.entity.ContentType;
import com.aynikortex.backend.integration.dto.response.Classification;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.service.DataScienceIntegrationService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ContentService {

    private final ContentRepository contentRepository;
    private final ContentMapper contentMapper;
    private final DataScienceIntegrationService dataScienceService;

    public ContentService(ContentRepository contentRepository,
                          ContentMapper contentMapper,
                          DataScienceIntegrationService dataScienceService) {
        this.contentRepository = contentRepository;
        this.contentMapper = contentMapper;
        this.dataScienceService = dataScienceService;
    }

    @Transactional
    public ContentResponseDTO createContent(ContentRequestDTO requestDTO) {
        if (requestDTO.contentType() == ContentType.TEXT){
            if (requestDTO.textContent() == null || requestDTO.textContent().trim().isEmpty()){
                throw new IllegalArgumentException("Text content is required for TEXT type");
            }
        } else if (requestDTO.contentType() == ContentType.FILE) {
            if (requestDTO.file() == null && (requestDTO.fileName() == null || requestDTO.filePath() == null)){
                throw new IllegalArgumentException("File content is required for FILE type");
            }
        } else {
            throw new IllegalArgumentException("Invalid content type");
        }

        Contenido contenido = contentMapper.toEntity(requestDTO);
        contenido.setCreatedAt(LocalDateTime.now());
        Contenido savedContenido = contentRepository.save(contenido);

        try {
            ClassificationResponse dsResponse;

            if (requestDTO.contentType() == ContentType.TEXT) {
                Map<String, Object> textData = Map.of("text", requestDTO.textContent());

                dsResponse = dataScienceService.classifyText(
                        savedContenido.getId().toString(),
                        requestDTO.title(),
                        textData
                );
            } else {
                Map<String, Object> fileMetadata = Map.of(
                        "id", savedContenido.getId().toString(),
                        "title", requestDTO.title() != null ? requestDTO.title() : "Sin título"
                );

                dsResponse = dataScienceService.classifyFile(
                        requestDTO.file(),
                        fileMetadata
                );
            }

            if (dsResponse != null && "SUCCESS".equalsIgnoreCase(dsResponse.status())) {
                var classification = dsResponse.classification();

                if (classification != null) {
                    savedContenido.setCategory(classification.category());
                    savedContenido.setSubCategory(classification.subcategory());

                    if (classification.confidence() != null) {
                        savedContenido.setConfidence(classification.confidence().doubleValue());
                    }
                }

                savedContenido.setModelVersion(dsResponse.modelVersion());
                savedContenido.setUpdatedAt(LocalDateTime.now());

                savedContenido = contentRepository.save(savedContenido);
            }

        } catch (Exception e) {
            throw new RuntimeException("Error al comunicarse con el servicio de Ciencia de Datos: " + e.getMessage(), e);
        }

        return contentMapper.toResponseDTO(savedContenido);
    }

    @Transactional(readOnly = true)
    public List<ContentResponseDTO> getAllContents() {
        return contentRepository.findAll().stream()
                .map(contentMapper::toResponseDTO)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public ContentResponseDTO getContentById(UUID id) {
        Contenido contenido = contentRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Contenido no encontrado con ID: " + id));
        return contentMapper.toResponseDTO(contenido);
    }

    @Transactional
    public void deleteContent(UUID id) {
        if (!contentRepository.existsById(id)) {
            throw new RuntimeException("No se puede eliminar, contenido no encontrado con ID: " + id);
        }
        contentRepository.deleteById(id);
    }
}