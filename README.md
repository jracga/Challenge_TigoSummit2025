# Mock API REST - Tigo Summit 2025

Este proyecto consiste en una API REST desarrollada con Flask que permite **configurar y gestionar mocks de endpoints REST**, simulando servicios externos y devolviendo respuestas personalizadas basadas en parámetros.

Es útil para pruebas, desarrollo de frontend sin backend, o simulación de microservicios en entornos desacoplados.

---

## 📌 Objetivo del Proyecto

Desarrollar una API que permita:

-  Configurar dinámicamente respuestas simuladas para rutas HTTP.
-  Simular el comportamiento de servicios externos (GET, POST, PUT, DELETE).
-  Visualizar, actualizar y eliminar configuraciones de mocks.
-  Responder de forma dinámica según los parámetros enviados por el cliente.

---

## ⚙️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.12
- **Framework:** Flask 3.1.1
- **Formato de datos:** JSON
- **Herramientas de prueba:** Postman, cURL

---

## 📁 Estructura del Proyecto

```
Challenge_TigoSummit2025/
├── app.py                  # Punto de entrada de la aplicación Flask
├── routes/
│   └── mock_routes.py      # Definición de rutas para gestión y ejecución de mocks
├── mocks/
│   ├── manager.py          # Lógica de almacenamiento y persistencia de configuraciones
│   └── mock_handler.py     # Lógica para seleccionar el mock correcto
├── data/
│   └── mocks.json          # Archivo de configuración de mocks persistente
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Este archivo
```

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/jracga/Challenge_TigoSummit2025.git
cd Challenge_TigoSummit2025
```

### 2. Crear y activar entorno virtual
  ```bash
    python -m venv venv
    # Activar en Windows
    .
    env\Scripts ctivate
    # Activar en Linux/Mac
    source venv/bin/activate
  ```
Cuando termines de trabajar, puedes salir del entorno con:
    ```
    deactivate
    ```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API
```bash
python app.py
```

La API estará corriendo en: `http://localhost:5000`

---

## 📮 Endpoints principales

### ▶️ Crear un mock
**POST /mocks**

```json
{
  "path": "/api/saludo",
  "method": "GET",
  "params": {
    "lang": "es"
  },
  "response": {
    "status": 200,
    "body": {
      "msg": "¡Hola!"
    }
  }
}
```

### 📜 Listar mocks
**GET /mocks**

---

### ✏️ Actualizar un mock
**PUT /mocks/{id}**

```json
{
  "path": "/api/saludo",
  "method": "GET",
  "params": {
    "lang": "es"
  },
  "response": {
    "status": 200,
    "body": {
      "msg": "¡Hola actualizado!"
    }
  }
}
```

### ❌ Eliminar un mock
**DELETE /mocks/{id}**

---

### 🧪 Simular petición
**GET /mock/api/saludo?lang=es**

Devuelve:

```json
{
  "msg": "¡Hola!"
}
```

---

## 🧠 Lógica del sistema

1. Todas las configuraciones de mocks se almacenan en el archivo `data/mocks.json`.
2. Cada configuración contiene:
   - La ruta (`path`)
   - El método (`method`)
   - Parámetros esperados (`params`)
   - La respuesta a devolver (`response`)
3. Cuando un cliente accede a `/mock/<ruta>`, el sistema busca una coincidencia exacta y responde según lo configurado.

---

## 📋 Buenas Prácticas Implementadas

- Código modular por responsabilidad (routes, lógica, almacenamiento)
- Validación mínima de entrada
- Buen manejo de errores básicos
- Uso de UUIDs para identificar configuraciones
- Uso de entorno virtual y archivo `requirements.txt`
- Ignora `venv/` mediante `.gitignore`

---

## 📚 Posibles mejoras futuras

- Validación de datos con `pydantic` o `marshmallow`
- Soporte para respuesta basada en cuerpo o headers
- Documentación Swagger/OpenAPI
- Almacenamiento en base de datos (SQLite, MongoDB, etc.)
- Interfaz gráfica para crear mocks

---
