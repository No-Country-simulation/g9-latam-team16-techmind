package com.aynikortex.backend.domain;


import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.JdbcTypeCode;
import org.hibernate.annotations.UpdateTimestamp;
import org.hibernate.type.SqlTypes;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "contents")
@Data
@AllArgsConstructor
public class Contenido {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String title;
    private String description;
    @Enumerated(EnumType.STRING)
    private ContentType contentType;
    private String textContent;
    private String fileName;
    private String filePath;
    private String category;
    private String subcategory;
    private Double confidence;
    private String modelVersion;
    @JdbcTypeCode(SqlTypes.JSON)
    @Column(columnDefinition = "json")
    private List<Keyword> keywords; // Usamos la clase Keyword (no DTO)

    @CreationTimestamp
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;


    public Contenido(){}


    public Contenido(DatosContentDto datosContentDto){

        this.id = datosContentDto.id();
        this.title = datosContentDto.title();
        this.description = datosContentDto.description();
        this.contentType = ContentType.valueOf(String.valueOf(datosContentDto.contentType()));
        this.textContent = datosContentDto.textContent();
        this.fileName = datosContentDto.fileName();
        this.filePath = datosContentDto.filePath();
        this.category = datosContentDto.category();
        this.subcategory = datosContentDto.subCategory();
        this.confidence = datosContentDto.confidence();
        this.modelVersion = datosContentDto.modelVersion();
        this.keywords = datosContentDto.keywords();
        this.createdAt = datosContentDto.createdAt();
        this.updatedAt = LocalDateTime.now();

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

    public ContentType getContentType() {
        return contentType;
    }

    public void setContentType(ContentType contentType) {
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

    public String getSubCategory(){return subcategory;}
    public void setSubCategory(String subCategory){this.subcategory = subCategory;}

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
        return keywords.toString();
    }

    public void setKeywords(List<Keyword> keywords) {
        this.keywords = keywords;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {this.createdAt = createdAt;}

    public LocalDateTime getUpdatedAt() {this.updatedAt = LocalDateTime.now();return this.updatedAt;}

    public void setUpdateAt(LocalDateTime updateAt) {
        this.updatedAt = updateAt;
    }

}
