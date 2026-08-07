package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.entity.Contenido;
import org.springframework.stereotype.Component;

@Component
public class ContentMapper {

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