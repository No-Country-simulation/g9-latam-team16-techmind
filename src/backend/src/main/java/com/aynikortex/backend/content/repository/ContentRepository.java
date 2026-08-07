package com.aynikortex.backend.content.repository;

import com.aynikortex.backend.entity.Contenido;
import com.aynikortex.backend.entity.ContentType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface ContentRepository extends JpaRepository<Contenido, UUID> {

    List<Contenido> findByCategory(String category);

    List<Contenido> findByCategoryContainingIgnoreCaseOrSubcategoryContainingIgnoreCase(String category, String subcategory);

    List<Contenido> findByContentType(ContentType contentType);

    List<Contenido> findByTitleContainingIgnoreCase(String title);


}