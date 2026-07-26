package com.aynikortex.backend.content.controller;

import com.aynikortex.backend.content.dto.ContentRequestDTO;
import com.aynikortex.backend.content.dto.ContentResponseDTO;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/contents")
public class ContentController {

    @PostMapping
    public ResponseEntity<String> createContent(@Valid @RequestBody ContentRequestDTO requestDTO) {
        return ResponseEntity.ok("¡Petición recibida! El título es: " + requestDTO.getTitle());
    }

    @GetMapping
    public ResponseEntity<List<ContentResponseDTO>> getAllContents() {
        return ResponseEntity.ok(List.of());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ContentResponseDTO> getContentById(@PathVariable UUID id) {
        return ResponseEntity.ok(new ContentResponseDTO());
    }

    @GetMapping("/search")
    public ResponseEntity<List<ContentResponseDTO>> searchContents(
            @RequestParam(required = false) String category,
            @RequestParam(required = false) String keywords) {
        return ResponseEntity.ok(List.of());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteContent(@PathVariable UUID id) {
        return ResponseEntity.ok("Contenido eliminado con el ID: " + id);
    }
}