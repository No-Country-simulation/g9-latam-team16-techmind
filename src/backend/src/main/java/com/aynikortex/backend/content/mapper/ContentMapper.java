package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.domain.Contenido;
import org.springframework.stereotype.Component;

@Component
public class ContentMapper {

    public Contenido toEntity(ContentRequestDTO requestDTO) {
        Contenido contenido = new Contenido();

        contenido.setTitle(requestDTO.getTitle());
        contenido.setContentType(requestDTO.getContentType());
        contenido.setTextContent(requestDTO.getTextContent());
        contenido.setFileName(requestDTO.getFileName());
        contenido.setFilePath(requestDTO.getFilePath());

        return contenido;
    }

    public ContentResponseDTO toResponseDTO(Contenido contenido) {
        ContentResponseDTO responseDTO = new ContentResponseDTO();

        responseDTO.setId(contenido.getId());
        responseDTO.setTitle(contenido.getTitle());
        responseDTO.setContentType(contenido.getContentType());
        responseDTO.setCategory(contenido.getCategory());
        responseDTO.setCreatedAt(contenido.getCreatedAt());

        return responseDTO;
    }
}