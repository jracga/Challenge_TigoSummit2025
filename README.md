# Challenge_TigoSummit2025
API para Mocks de Servicios REST

# Mock API REST - Proyecto Challenge Tigo Summit 2025

Este proyecto es una API para configurar y gestionar mocks de endpoints REST.  
Permite simular servicios externos devolviendo respuestas personalizadas.

---

## Requisitos

- Python 3.8 o superior
- Entorno virtual (recomendado)
- Paquetes listados en `requirements.txt`

---

## Instalación

1. Clona el repositorio  
    ```
        git clone <url-del-repositorio>
        cd <nombre-del-proyecto>  
   ```

2. Crea y activa el entorno virtual  
    ```
        python -m venv venv
        # Windows
        .\venv\Scripts\activate
        # Linux/Mac
        source venv/bin/activate
    ```

3. Instala las dependencias  

    ```
        pip install -r requirements.txt
    ```

4. USO:
Ejecuta la aplicación:  

    ```
        python app.py
    ```


5. Endpoints principales  
    * POST /mocks - Registrar una configuración de mock

    * GET /mocks - Listar mocks registrados

    * GET|POST|PUT|DELETE /mock/<path> - Endpoint genérico para simular la respuesta configurada