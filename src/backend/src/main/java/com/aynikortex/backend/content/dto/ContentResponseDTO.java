package com.aynikortex.backend.content.dto;

<<<<<<< HEAD
import com.aynikortex.backend.domain.ContentType;

import java.time.LocalDateTime;
import java.util.UUID;

public class ContentResponseDTO {

    private UUID id;
    private String title;
    private ContentType contentType;
    private String category;
    private LocalDateTime createdAt;

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

    public ContentType getContentType() {
        return contentType;
    }

    public void setContentType(ContentType contentType) {
        this.contentType = contentType;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }
}
=======
import com.aynikortex.backend.content.model.ContentType;
import java.time.LocalDateTime;
import java.util.UUID;

public record ContentResponseDTO(
        UUID id,
        String title,
        ContentType contentType,
        String category,
        LocalDateTime createdAt
) {}
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
