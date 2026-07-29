package com.aynikortex.backend.content.controller;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
<<<<<<< HEAD
=======
import com.aynikortex.backend.content.service.ContentService;
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/api/v1/contents")
public class ContentController {

<<<<<<< HEAD
    @PostMapping
    public ResponseEntity<String> createContent(@Valid @RequestBody ContentRequestDTO requestDTO) {
        return ResponseEntity.ok("¡Petición recibida! El título es: " + requestDTO.getTitle());
=======
    private final ContentService contentService;

    public ContentController(ContentService contentService) {
        this.contentService = contentService;
    }

    @PostMapping
    public ResponseEntity<ContentResponseDTO> createContent(@Valid @RequestBody ContentRequestDTO requestDTO) {
        ContentResponseDTO responseDTO = contentService.createContent(requestDTO);
        return ResponseEntity.ok(responseDTO);
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
    }

    @GetMapping
    public ResponseEntity<List<ContentResponseDTO>> getAllContents() {
<<<<<<< HEAD
        return ResponseEntity.ok(List.of());
=======
        return ResponseEntity.ok(contentService.getAllContents());
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
    }

    @GetMapping("/{id}")
    public ResponseEntity<ContentResponseDTO> getContentById(@PathVariable UUID id) {
<<<<<<< HEAD
        return ResponseEntity.ok(new ContentResponseDTO());
    }

    @GetMapping("/search")
    public ResponseEntity<List<ContentResponseDTO>> searchContents(
            @RequestParam(required = false) String category,
            @RequestParam(required = false) String keywords) {
        return ResponseEntity.ok(List.of());
=======
        return ResponseEntity.ok(contentService.getContentById(id));
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteContent(@PathVariable UUID id) {
<<<<<<< HEAD
        return ResponseEntity.ok("Contenido eliminado con el ID: " + id);
=======
        contentService.deleteContent(id);
        return ResponseEntity.ok("Contenido eliminado correctamente con el ID: " + id);
>>>>>>> dd93825b68edbdc4a9e7ff7d6e6aad1d874a6213
    }
}