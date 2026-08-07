package com.aynikortex.backend.integration.dto.response;

import java.math.BigDecimal;
import java.util.List;

public record Classification(
        String category,
        String subcategory,
        BigDecimal confidence,
        List<Keyword> keywords,
        String summary
) {}
