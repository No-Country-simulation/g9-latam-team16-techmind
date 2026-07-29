package com.aynikortex.backend.content.service;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.content.mapper.ContentMapper;
import com.aynikortex.backend.content.repository.ContentRepository;
import com.aynikortex.backend.domain.Contenido;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ContentService {

    private final ContentRepository contentRepository;
    private final ContentMapper contentMapper;

    public ContentService(ContentRepository contentRepository, ContentMapper contentMapper) {
        this.contentRepository = contentRepository;
        this.contentMapper = contentMapper;
    }

    @Transactional
    public ContentResponseDTO createContent(ContentRequestDTO requestDTO) {
        Contenido contenido = contentMapper.toEntity(requestDTO);

        contenido.setCreatedAt(LocalDateTime.now());
        contenido.setCategory("PENDIENTE_CLASIFICACION");

        Contenido savedContenido = contentRepository.save(contenido);
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