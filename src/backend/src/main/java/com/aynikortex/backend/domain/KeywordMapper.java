package com.aynikortex.backend.domain;

import org.springframework.stereotype.Component;
import java.util.List;

@Component
public interface KeywordMapper {

    // Métodos de mapeo para Keywords
    List<Keyword> keywordsToKeywordDTOs(List<Keyword> keywords);
    List<Keyword> keywordDTOsToKeywords(List<Keyword> keywordDTOs);
}