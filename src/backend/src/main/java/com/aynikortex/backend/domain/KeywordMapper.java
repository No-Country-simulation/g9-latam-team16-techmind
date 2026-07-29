package com.aynikortex.backend.domain;

import com.aynikortex.backend.content.mapper.ContentMapper;
import io.swagger.v3.oas.annotations.media.Content;
import sun.font.CharToGlyphMapper;
import sun.font.CompositeFont;

import java.util.List;

public interface KeywordMapper {
    CompositeFont Mappers = null;
    CharToGlyphMapper INSTANCE = Mappers.getMapper();


    // Mapeo de Keywords
    List<Keyword> keywordsToKeywordDTOs(List<Keyword> keywords);
    List<Keyword> keywordDTOsToKeywords(List<Keyword> keywordDTOs);
}
