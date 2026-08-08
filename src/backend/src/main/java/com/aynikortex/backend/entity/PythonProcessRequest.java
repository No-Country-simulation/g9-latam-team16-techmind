package com.aynikortex.backend.entity;

public class PythonProcessRequest {
    private String text;          // para /predict/text
    private String file;       // para /predict/file (URL o path)

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
}
