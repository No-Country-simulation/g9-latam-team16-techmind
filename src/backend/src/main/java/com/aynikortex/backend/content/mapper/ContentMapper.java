package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.content.model.ContentType;
import com.aynikortex.backend.domain.Contenido;
import org.springframework.stereotype.Component;

@Component
public class ContentMapper {

    public Contenido toEntity(ContentRequestDTO requestDTO) {
        Contenido contenido = new Contenido();

        contenido.setTitle(requestDTO.title());
        contenido.setContentType(requestDTO.contentType().name());
        contenido.setTextContent(requestDTO.textContent());
        contenido.setFileName(requestDTO.fileName());
        contenido.setFilePath(requestDTO.filePath());

        return contenido;
    }

    public ContentResponseDTO toResponseDTO(Contenido contenido) {
        ContentType type = contenido.getContentType() != null
                ? ContentType.valueOf(contenido.getContentType())
                : null;

        return new ContentResponseDTO(
                contenido.getId(),
                contenido.getTitle(),
                type,
                contenido.getCategory(),
                contenido.getCreatedAt()
        );
    }
}