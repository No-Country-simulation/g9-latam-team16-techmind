"""
==========================================================
TechMind
Data Science Component

Module:
    test_summary_generator

Description:
    Genera un resumen extractivo a partir del contenido de un documento.

Sprint:
    
==========================================================
"""

from sklearn.feature_extraction.text import TfidfVectorizer

from data_science.ml.inference.summary_generator import SummaryGenerator


def test_generate_empty_text_returns_empty_summary() -> None:
    generator = SummaryGenerator()
    vectorizer = TfidfVectorizer()

    result = generator.generate("", vectorizer)

    assert result == ""


def test_generate_short_text_returns_original_text() -> None:
    text = (
        "Este documento describe una API REST. "
        "La API permite clasificar documentos."
    )

    vectorizer = TfidfVectorizer()
    vectorizer.fit([text])

    generator = SummaryGenerator(max_sentences=3)

    result = generator.generate(text, vectorizer)

    assert result == text


def test_generate_limits_summary_to_max_sentences() -> None:
    text = (
        "La arquitectura utiliza microservicios. "
        "Los servicios exponen APIs REST. "
        "Docker permite contenerizar las aplicaciones. "
        "Kubernetes permite desplegar los servicios. "
        "El sistema utiliza autenticación."
    )

    vectorizer = TfidfVectorizer()
    vectorizer.fit([text])

    generator = SummaryGenerator(max_sentences=3)

    result = generator.generate(text, vectorizer)

    sentences = [
        sentence.strip()
        for sentence in result.split(".")
        if sentence.strip()
    ]

    assert len(sentences) <= 3


def test_generate_summary_uses_only_original_content() -> None:
    text = (
        "El backend utiliza Spring Boot. "
        "La aplicación expone una API REST. "
        "El sistema utiliza Docker para su despliegue. "
        "Los servicios procesan documentos técnicos."
    )

    vectorizer = TfidfVectorizer()
    vectorizer.fit([text])

    generator = SummaryGenerator(max_sentences=3)

    result = generator.generate(text, vectorizer)

    assert result
    assert result in text or all(
        sentence.strip() in text
        for sentence in result.split(".")
        if sentence.strip()
    )


def test_generate_removes_basic_markdown_formatting() -> None:
    text = (
        "El componente **Data Science** utiliza `Python` y FastAPI. "
        "La API procesa documentos técnicos."
    )

    vectorizer = TfidfVectorizer()
    vectorizer.fit([text])

    generator = SummaryGenerator(max_sentences=3)

    result = generator.generate(text, vectorizer)

    assert "**" not in result
    assert "`" not in result
    assert "Data Science" in result
    assert "Python" in result


def test_generate_limits_summary_to_max_characters() -> None:
    text = (
        "La arquitectura del sistema utiliza una API REST para "
        "permitir la comunicación entre diferentes componentes. "
        "El backend procesa documentos técnicos y ejecuta modelos "
        "de Machine Learning. "
        "Docker permite contenerizar los servicios de la aplicación. "
        "Kubernetes permite desplegar los servicios de manera "
        "escalable."
    )

    vectorizer = TfidfVectorizer()
    vectorizer.fit([text])

    generator = SummaryGenerator(
        max_sentences=3,
        max_characters=200,
    )

    result = generator.generate(text, vectorizer)

    assert len(result) <= 203