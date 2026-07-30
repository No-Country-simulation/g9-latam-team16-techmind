# 🚀 Guía de Despliegue e Integración en Oracle Cloud Infrastructure (OCI)

**Proyecto:** TechMind – Organización Inteligente del Conocimiento Técnico  
**Versión:** 1.0  
**Clasificación:** Documentación de Infraestructura y CI/CD  
**Estado:** Aprobado  

---

## 1. Visión General del Despliegue

Este documento describe la arquitectura, configuración e instrucciones paso a paso para el despliegue e integración del proyecto **TechMind** en **Oracle Cloud Infrastructure (OCI)**.

De acuerdo a los requerimientos oficiales del Hackathon ONE y las decisiones de arquitectura del proyecto (**ADR-004**), se implementó un pipeline automatizado de **Integración y Despliegue Continuo (CI/CD)** utilizando **GitHub Actions** conectado directamente con **OCI Object Storage**.

```mermaid
flowchart LR
    Developer["Desarrollador"]
    GitHubRepo["GitHub Repository<br/>(main)"]
    GitHubActions["GitHub Actions<br/>(oci-sync.yml)"]
    OCIObjectStorage["OCI Object Storage<br/>(techmind-bucket)"]
    MasterDataset["datasets/master_dataset_v1.csv"]
    Artifacts["artifacts/ (*.joblib)"]

    Developer -->|"git push"| GitHubRepo
    GitHubRepo -->|"Trigger on Push / Dispatch"| GitHubActions
    GitHubActions -->|"Subida segura (OCI CLI)"| OCIObjectStorage
    OCIObjectStorage --> MasterDataset
    OCIObjectStorage --> Artifacts
```

---

## 2. Requisitos Previos y Recursos de OCI

Para replicar o mantener el despliegue se requiere:

1. **Cuenta activa en Oracle Cloud Infrastructure (OCI)**.
2. **Bucket de Object Storage**:
   - **Nombre del Bucket:** `techmind-bucket`
   - **Región:** `mx-queretaro-1` (México Central - Querétaro)
   - **Nivel de Almacenamiento:** Standard
   - **Visibilidad:** Privada (Private)

---

## 3. Configuración de Credenciales de Seguridad (GitHub Secrets)

La autenticación entre GitHub Actions y la API de Oracle Cloud se realiza mediante cifrado asymmetric RSA sin exponer claves en el código fuente.

En el repositorio de GitHub (**Settings ➔ Secrets and variables ➔ Actions**) se encuentran configurados los siguientes **5 secretos de repositorio**:

| Nombre del Secret | Descripción | Ejemplo de Valor |
| :--- | :--- | :--- |
| `OCI_CLI_USER` | OCID del usuario en OCI | `ocid1.user.oc1..aaaaaaa...` |
| `OCI_CLI_TENANCY` | OCID de la Tenancy (Cuenta) en OCI | `ocid1.tenancy.oc1..aaaaaaa...` |
| `OCI_CLI_FINGERPRINT` | Huella digital de la API Key | `a7:45:33:a9:49:...` |
| `OCI_CLI_REGION` | Código de la región de OCI | `mx-queretaro-1` |
| `OCI_CLI_KEY_CONTENT` | Contenido completo de la clave privada `.pem` | `-----BEGIN RSA PRIVATE KEY----- ...` |

---

## 4. Pipeline de Automatización CI/CD (`.github/workflows/oci-sync.yml`)

El pipeline se encuentra definido en el archivo [oci-sync.yml](file:///c:/Users/josue/OneDrive/Escritorio/Hakathon%20Nocountry/g9-latam-team16-techmind/.github/workflows/oci-sync.yml).

### Disparadores (Triggers)
- **Automático (`push`)**: Se ejecuta automáticamente cuando se detectan cambios en las rutas `datasets/**` o `artifacts/**` en la rama `main`.
- **Manual (`workflow_dispatch`)**: Permite la ejecución manual a través de la interfaz de GitHub Actions.

### Definición del Workflow

```yaml
name: Sync Data and Models to OCI Object Storage

on:
  push:
    branches:
      - main
    paths:
      - 'datasets/**'
      - 'artifacts/**'
  workflow_dispatch:

jobs:
  upload-to-oci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Instalar OCI CLI
        run: |
          python -m pip install --upgrade pip
          pip install oci-cli

      - name: Subir Dataset Maestro a OCI Object Storage
        env:
          OCI_CLI_USER: ${{ secrets.OCI_CLI_USER }}
          OCI_CLI_TENANCY: ${{ secrets.OCI_CLI_TENANCY }}
          OCI_CLI_FINGERPRINT: ${{ secrets.OCI_CLI_FINGERPRINT }}
          OCI_CLI_REGION: ${{ secrets.OCI_CLI_REGION }}
          OCI_CLI_KEY_CONTENT: ${{ secrets.OCI_CLI_KEY_CONTENT }}
        run: |
          if [ -f "datasets/raw/master_dataset_v1.csv" ]; then
            echo "Subiendo master_dataset_v1.csv a OCI Object Storage..."
            oci os object put \
              --bucket-name techmind-bucket \
              --file datasets/raw/master_dataset_v1.csv \
              --name datasets/master_dataset_v1.csv \
              --force
          elif [ -f "datasets/processed/master_dataset_v1.csv" ]; then
            echo "Subiendo master_dataset_v1.csv a OCI Object Storage..."
            oci os object put \
              --bucket-name techmind-bucket \
              --file datasets/processed/master_dataset_v1.csv \
              --name datasets/master_dataset_v1.csv \
              --force
          fi

      - name: Subir Artefactos y Modelos a OCI Object Storage
        env:
          OCI_CLI_USER: ${{ secrets.OCI_CLI_USER }}
          OCI_CLI_TENANCY: ${{ secrets.OCI_CLI_TENANCY }}
          OCI_CLI_FINGERPRINT: ${{ secrets.OCI_CLI_FINGERPRINT }}
          OCI_CLI_REGION: ${{ secrets.OCI_CLI_REGION }}
          OCI_CLI_KEY_CONTENT: ${{ secrets.OCI_CLI_KEY_CONTENT }}
        run: |
          if [ -d "artifacts" ] && [ "$(ls -A artifacts)" ]; then
            echo "Subiendo artefactos a OCI Object Storage..."
            oci os object bulk-upload \
              --bucket-name techmind-bucket \
              --src-dir artifacts/ \
              --prefix artifacts/ \
              --overwrite
          fi
```

---

## 5. Instrucciones para Ejecutar y Verificar el Despliegue

### Ejecución Manual desde GitHub
1. Ingresar al repositorio en GitHub.
2. Navegar a la pestaña **Actions**.
3. En el menú lateral izquierdo, seleccionar **`Sync Data and Models to OCI Object Storage`**.
4. Hacer clic en el botón desplegable **`Run workflow`** ➔ Seleccionar la rama `main` ➔ Hacer clic en **`Run workflow`**.

### Verificación del Almacenamiento en OCI
1. Iniciar sesión en la consola de [Oracle Cloud (OCI)](https://cloud.oracle.com/).
2. Navegar a **Storage ➔ Buckets**.
3. Seleccionar el compartimento y hacer clic en **`techmind-bucket`**.
4. Verificar la presencia del objeto:
   - `datasets/master_dataset_v1.csv`

---

## 6. Evolución del Despliegue (Futuras Fases)

- **Fase 2 (Despliegue del Backend):** Creación de una instancia **OCI Compute (VM)** para alojar la aplicación Backend en Java Spring Boot / FastAPI y exponer la API públicamente a través de la IP de la VM.
