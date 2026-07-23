# Dependencias iniciales del proyecto

Las siguientes dependencias se incluirán desde la creación del proyecto en Spring Initializr.

| Dependencia                           | Propósito                                                                                                                                                                                                                                                                           |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Spring Web**                        | Desarrollo de la API REST mediante Spring MVC.                                                                                                                                                                                                                                      |
| **Spring Data JPA**                   | Persistencia de datos utilizando Hibernate como implementación de JPA.                                                                                                                                                                                                              |
| **MySQL Driver**                      | Driver JDBC para la conexión con la base de datos MySQL.                                                                                                                                                                                                                            |
| **Validation**                        | Validación de datos mediante anotaciones como `@NotBlank`, `@NotNull`, `@Size`, etc.                                                                                                                                                                                                |
| **Lombok**                            | Reduce código repetitivo generando automáticamente getters, setters, constructores, builders, entre otros.                                                                                                                                                                          |
| **Spring Boot DevTools**              | Facilita el desarrollo mediante reinicio automático de la aplicación y otras utilidades.                                                                                                                                                                                            |
| **Spring Boot Actuator** _(opcional)_ | Proporciona endpoints para monitoreo, métricas y estado de salud de la aplicación.                                                                                                                                                                                                  |
| **Reactive HTTP Client (WebClient)**  | Cliente HTTP moderno de Spring para consumir APIs externas. Se utilizará para la integración entre el Backend y la API REST de Ciencia de Datos (FastAPI). Permite realizar solicitudes HTTP de forma eficiente y es la alternativa recomendada por Spring frente a `RestTemplate`. |

## Dependencias agregadas manualmente

Las siguientes dependencias no aparecen en Spring Initializr y deberán agregarse manualmente.

### Springdoc OpenAPI

Permite generar automáticamente la documentación de la API REST y la interfaz gráfica de Swagger UI a partir de los controladores y anotaciones de Spring.

Ejemplo para Maven:

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.8.9</version>
</dependency>
```

> **Nota:** La versión puede actualizarse según la versión estable compatible con Spring Boot utilizada por el proyecto.
