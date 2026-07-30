package com.aynikortex.backend.integration.dto.response;

import java.math.BigDecimal;

public record Keyword(
        String term,
        BigDecimal score
) {}
