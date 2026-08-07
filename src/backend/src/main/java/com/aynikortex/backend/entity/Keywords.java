package com.aynikortex.backend.entity;

import java.io.Serializable;

public class Keywords implements Serializable {
    private String word;
    private Double relevance;

    public void KeywordDTO() {}

    public void KeywordDTO(String word, Double relevance) {
        this.word = word;
        this.relevance = relevance;
    }

    public String getWord() { return word; }
    public void setWord(String word) { this.word = word; }

    public Double getRelevance() { return relevance; }
    public void setRelevance(Double relevance) { this.relevance = relevance; }

}
