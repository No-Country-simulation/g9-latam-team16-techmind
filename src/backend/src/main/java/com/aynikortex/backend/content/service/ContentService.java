package com.aynikortex.backend.content.service;

import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.content.dto.FileContentRequest;
import com.aynikortex.backend.content.dto.KeywordDTO;
import com.aynikortex.backend.content.dto.TextContentRequest;
import com.aynikortex.backend.content.repository.ContentRepository;
import com.aynikortex.backend.entity.Contenido;
import com.aynikortex.backend.entity.ContentType;
import com.aynikortex.backend.entity.FileFormatType;
import com.aynikortex.backend.integration.dto.response.ClassificationResponse;
import com.aynikortex.backend.integration.service.DataScienceIntegrationService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ContentService {

    private final ContentRepository contentRepository;
    private final DataScienceIntegrationService dataScienceService;

    public ContentService(ContentRepository contentRepository,
                          DataScienceIntegrationService dataScienceService) {
        this.contentRepository = contentRepository;
        this.dataScienceService = dataScienceService;
    }

    @Transactional
    public ContentResponseDTO createTextContent(TextContentRequest requestDTO) {
        Contenido contenido = new Contenido();
        contenido.setTitle(requestDTO.title());
        contenido.setTextContent(requestDTO.text());
        contenido.setContentType(ContentType.TEXT);
        contenido.setCreatedAt(LocalDateTime.now());

        Contenido savedContenido = contentRepository.save(contenido);

        try {
            ClassificationResponse dsResponse = dataScienceService.classifyText(
                    requestDTO.title(),
                    requestDTO.text(),
                    requestDTO.metadata()
            );

            if (dsResponse != null && "SUCCESS".equalsIgnoreCase(dsResponse.status())) {
                updateEntityWithClassification(savedContenido, dsResponse);
                savedContenido = contentRepository.save(savedContenido);
            }

        } catch (Exception e) {
            throw new RuntimeException("Error durante la clasificación de texto: " + e.getMessage(), e);
        }

        return mapToResponseDTO(savedContenido);
    }

    @Transactional
    public ContentResponseDTO createFileContent(FileContentRequest requestDTO) {
        String originalFileName = requestDTO.file().getOriginalFilename();
        String simulatedFilePath = "/oci/storage/" + UUID.randomUUID() + "_" + originalFileName;

        Contenido contenido = new Contenido();
        contenido.setTitle(requestDTO.title() != null ? requestDTO.title() : originalFileName);
        contenido.setFileName(originalFileName);
        contenido.setFilePath(simulatedFilePath);
        contenido.setFileFormat(determineFileFormat(originalFileName));
        contenido.setContentType(ContentType.FILE);
        contenido.setCreatedAt(LocalDateTime.now());

        Contenido savedContenido = contentRepository.save(contenido);

        try {
            ClassificationResponse dsResponse = dataScienceService.classifyFile(
                    requestDTO.file(),
                    requestDTO.metadata()
            );

            System.out.println(">>> RESPUESTA COMPLETA DE DS: " + dsResponse);

            if (dsResponse != null && "SUCCESS".equalsIgnoreCase(dsResponse.status())) {
                updateEntityWithClassification(savedContenido, dsResponse);
                savedContenido = contentRepository.save(savedContenido);
            }

        } catch (Exception e) {
            throw new RuntimeException("Error durante la clasificación de archivo: " + e.getMessage(), e);
        }

        return mapToResponseDTO(savedContenido);
    }

    private void updateEntityWithClassification(Contenido entidad, ClassificationResponse response) {
        var classification = response.classification();
        if (classification != null) {
            entidad.setCategory(classification.category());
            entidad.setSubCategory(classification.subcategory());
            if (classification.confidence() != null) {
                entidad.setConfidence(classification.confidence().doubleValue());
            }

            if (classification.keywords() != null) {
                List<KeywordDTO> keywordDTOs = classification.keywords().stream()
                        .map(k -> new KeywordDTO(
                                k.term(),
                                k.score() != null ? k.score().doubleValue() : 0.0
                        ))
                        .collect(Collectors.toList());
                entidad.setKeywords(keywordDTOs);
            }

            entidad.setSummary(classification.summary());
        }
        entidad.setModelVersion(response.modelVersion());
        entidad.setUpdatedAt(LocalDateTime.now());
    }

    private FileFormatType determineFileFormat(String fileName) {
        if (fileName == null) return FileFormatType.OTHER;
        String lowerName = fileName.toLowerCase();
        if (lowerName.endsWith(".pdf")) return FileFormatType.PDF;
        if (lowerName.endsWith(".docx")) return FileFormatType.DOCX;
        if (lowerName.endsWith(".txt")) return FileFormatType.TXT;
        if (lowerName.endsWith(".md")) return FileFormatType.MARKDOWN;
        return FileFormatType.OTHER;
    }

    private ContentResponseDTO mapToResponseDTO(Contenido c) {
        List<String> keywordStrings = null;
        if (c.getKeywords() != null) {
            keywordStrings = c.getKeywords().stream()
                    .map(KeywordDTO::getWord)
                    .collect(Collectors.toList());
        }

        return new ContentResponseDTO(
                c.getId(),
                c.getTitle(),
                c.getContentType(),
                c.getTextContent(),
                c.getCategory(),
                c.getSubCategory(),
                c.getConfidence(),
                keywordStrings,
                c.getSummary(),
                c.getCreatedAt()
        );
    }

    @Transactional(readOnly = true)
    public List<ContentResponseDTO> getAllContents() {
        return contentRepository.findAll().stream()
                .map(this::mapToResponseDTO)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public ContentResponseDTO getContentById(UUID id) {
        Contenido contenido = contentRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Contenido no encontrado con ID: " + id));
        return mapToResponseDTO(contenido);
    }

    @Transactional
    public void deleteContent(UUID id) {
        if (!contentRepository.existsById(id)) {
            throw new RuntimeException("No se puede eliminar, contenido no encontrado con ID: " + id);
        }
        contentRepository.deleteById(id);
    }

    @Transactional(readOnly = true)
    public List<ContentResponseDTO> searchContentsByTitle(String title) {
        return contentRepository.findByTitleContainingIgnoreCase(title).stream()
                .map(this::mapToResponseDTO)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public List<ContentResponseDTO> getContentsByCategoryOrSubcategory(String term) {
        return contentRepository.findByCategoryContainingIgnoreCaseOrSubcategoryContainingIgnoreCase(term, term).stream()
                .map(this::mapToResponseDTO)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public List<ContentResponseDTO> searchContentsByKeyword(String keyword) {
        String queryKeyword = keyword.toLowerCase();
        return contentRepository.findAll().stream()
                .filter(content -> content.getKeywords() != null &&
                        content.getKeywords().stream()
                                .anyMatch(k -> k.getWord() != null && k.getWord().toLowerCase().contains(queryKeyword)))
                .map(this::mapToResponseDTO)
                .collect(Collectors.toList());
    }
}