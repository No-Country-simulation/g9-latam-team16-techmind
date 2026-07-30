package com.aynikortex.backend.content.controller;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import com.aynikortex.backend.content.service.ContentService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/api/v1/contents")
public class ContentController {

    private final ContentService contentService;

    public ContentController(ContentService contentService) {
        this.contentService = contentService;
    }

    @PostMapping
    public ResponseEntity<ContentResponseDTO> createContent(@Valid @RequestBody ContentRequestDTO requestDTO) {
        ContentResponseDTO responseDTO = contentService.createContent(requestDTO);
        return ResponseEntity.ok(responseDTO);
    }

    @GetMapping
    public ResponseEntity<List<ContentResponseDTO>> getAllContents() {
        return ResponseEntity.ok(contentService.getAllContents());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ContentResponseDTO> getContentById(@PathVariable UUID id) {
        return ResponseEntity.ok(contentService.getContentById(id));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteContent(@PathVariable UUID id) {
        contentService.deleteContent(id);
        return ResponseEntity.ok("Contenido eliminado correctamente con el ID: " + id);
    }
}