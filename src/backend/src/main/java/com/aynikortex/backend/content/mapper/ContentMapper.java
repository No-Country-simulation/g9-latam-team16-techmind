package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
<<<<<<< HEAD
=======
import com.aynikortex.backend.content.model.ContentType;
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
import com.aynikortex.backend.domain.Contenido;
import org.springframework.stereotype.Component;

@Component
public class ContentMapper {

    public Contenido toEntity(ContentRequestDTO requestDTO) {
        Contenido contenido = new Contenido();

<<<<<<< HEAD
        contenido.setTitle(requestDTO.getTitle());
        contenido.setContentType(requestDTO.getContentType());
        contenido.setTextContent(requestDTO.getTextContent());
        contenido.setFileName(requestDTO.getFileName());
        contenido.setFilePath(requestDTO.getFilePath());
=======
        contenido.setTitle(requestDTO.title());
        contenido.setContentType(requestDTO.contentType().name());
        contenido.setTextContent(requestDTO.textContent());
        contenido.setFileName(requestDTO.fileName());
        contenido.setFilePath(requestDTO.filePath());
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213

        return contenido;
    }

    public ContentResponseDTO toResponseDTO(Contenido contenido) {
<<<<<<< HEAD
        ContentResponseDTO responseDTO = new ContentResponseDTO();

        responseDTO.setId(contenido.getId());
        responseDTO.setTitle(contenido.getTitle());
        responseDTO.setContentType(contenido.getContentType());
        responseDTO.setCategory(contenido.getCategory());
        responseDTO.setCreatedAt(contenido.getCreatedAt());

        return responseDTO;
=======
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
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
    }
}