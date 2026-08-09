package com.aynikortex.backend.content.repository;

import com.aynikortex.backend.entity.Contenido;
import com.aynikortex.backend.entity.ContentType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface ContentRepository extends JpaRepository<Contenido, UUID> {

    List<Contenido> findByCategory(String category);

    Optional<Contenido> findById(UUID id);

    List<Contenido> findByCategoryContainingIgnoreCaseOrSubcategoryContainingIgnoreCase(String category, String subcategory);

    List<Contenido> findByContentType(ContentType contentType);

    List<Contenido> findByTitleContainingIgnoreCase(String title);

    @Query(value = "SELECT * FROM contents WHERE JSON_CONTAINS(keywords, JSON_OBJECT('word', :word))", nativeQuery = true)
    List<Contenido> findByKeywordWord(@Param("word") String word);


}