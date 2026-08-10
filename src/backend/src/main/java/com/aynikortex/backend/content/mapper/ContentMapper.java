package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.content.dto.KeywordDTO;
import com.aynikortex.backend.entity.Contenido;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.stream.Collectors;

@Component
public class ContentMapper {

    public ContentResponseDTO toResponseDTO(Contenido contenido) {
        List<String> keywordStrings = null;
        if (contenido.getKeywords() != null) {
            keywordStrings = contenido.getKeywords().stream()
                    .map(KeywordDTO::getWord)
                    .collect(Collectors.toList());
        }

        return new ContentResponseDTO(
                contenido.getId(),
                contenido.getTitle(),
                contenido.getContentType(),
                contenido.getTextContent(),
                contenido.getCategory(),
                contenido.getSubCategory(), // Subcategoría
                contenido.getConfidence(),    // Confianza
                keywordStrings,               // Lista de keywords
                contenido.getSummary(),   // Resumen guardado en descripción
                contenido.getCreatedAt()
        );
    }
}