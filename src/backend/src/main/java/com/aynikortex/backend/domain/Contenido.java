package com.aynikortex.backend.domain;


import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "contents")
public class Contenido {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String title;
    private String description;
    private String contentType;
    private String textContent;
    private String fileName;
    private String filePath;
    private String category;
    private String subCategory;
    private Double confidence;
    private String modelVersion;
    private String keywords;
    private LocalDateTime createdAt;
    private LocalDateTime updateAt;


    public Contenido(){}


    public Contenido(DatosContentDto datosContentDto){

        this.id = datosContentDto.id();
        this.title = datosContentDto.title();
        this.description = datosContentDto.description();
        this.contentType = datosContentDto.contentType();
        this.textContent = datosContentDto.textContent();
        this.fileName = datosContentDto.fileName();
        this.filePath = datosContentDto.filePath();
        this.category = datosContentDto.category();
        this.subCategory = datosContentDto.subCategory();
        this.confidence = datosContentDto.confidence();
        this.modelVersion = datosContentDto.modelVersion();
        this.keywords = datosContentDto.keywords();
        this.createdAt = datosContentDto.createdAt();
        this.updateAt = datosContentDto.updateAt();

    }

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getContentType() {
        return contentType;
    }

    public void setContentType(String contentType) {
        this.contentType = contentType;
    }

    public String getTextContent() {
        return textContent;
    }

    public void setTextContent(String textContent) {
        this.textContent = textContent;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getSubCategory() {
        return subCategory;
    }

    public void setSubCategory(String subCategory) {
        this.subCategory = subCategory;
    }

    public Double getConfidence() {
        return confidence;
    }

    public void setConfidence(Double confidence) {
        this.confidence = confidence;
    }

    public String getModelVersion() {
        return modelVersion;
    }

    public void setModelVersion(String modelVersion) {
        this.modelVersion = modelVersion;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdateAt() {
        return updateAt;
    }

    public void setUpdateAt(LocalDateTime updateAt) {
        this.updateAt = updateAt;
    }

}
