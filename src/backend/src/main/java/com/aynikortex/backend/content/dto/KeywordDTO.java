package com.aynikortex.backend.content.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class KeywordDTO {
    private String word;
    private Double relevance;
}
