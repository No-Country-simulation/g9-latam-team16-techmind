CREATE TABLE contents (
                          id CHAR(36) PRIMARY KEY,
                          title VARCHAR(200) NOT NULL,
                          description VARCHAR(1000),
                          content_type ENUM('TEXT','FILE') NOT NULL,
                          text_content LONGTEXT,
                          file_name VARCHAR(255),
                          file_path VARCHAR(500),
                          category VARCHAR(100),
                          subcategory VARCHAR(100),
                          confidence DECIMAL(4,3),
                          model_version VARCHAR(20),
                          keywords JSON,
                          created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                          updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

)