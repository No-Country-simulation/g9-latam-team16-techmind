package com.aynikortex.backend.content.mapper;

import com.aynikortex.backend.content.dto.KeywordDTO;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
public interface KeywordMapper {

    // Métodos de mapeo para Keywords
    List<KeywordDTO> keywordsToKeywordDTOs(List<KeywordDTO> keywords);
    List<KeywordDTO> keywordDTOsToKeywords(List<KeywordDTO> keywordDTOs);
}