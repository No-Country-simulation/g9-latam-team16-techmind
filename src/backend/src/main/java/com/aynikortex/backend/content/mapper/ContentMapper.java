package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.domain.ContentType;
import com.aynikortex.backend.domain.Contenido;
import org.springframework.stereotype.Component;

@Component
public class ContentMapper {

    public Contenido toEntity(ContentRequestDTO requestDTO) {
        Contenido contenido = new Contenido();
        contenido.setTitle(requestDTO.title());
        contenido.setContentType(requestDTO.contentType());
        contenido.setTextContent(requestDTO.textContent());
        contenido.setFileName(requestDTO.fileName());
        contenido.setFilePath(requestDTO.filePath());
        return contenido;
    }

    public ContentResponseDTO toResponseDTO(Contenido contenido) {
        return new ContentResponseDTO(
                contenido.getId(),
                contenido.getTitle(),
                contenido.getContentType(),
                contenido.getCategory(),
                contenido.getCreatedAt()
        );
    }
}