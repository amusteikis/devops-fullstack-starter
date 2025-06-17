<<<<<<< HEAD
![CI](https://github.com/amusteikis/devops-fullstack-starter/actions/workflows/ci.yml/badge.svg)
# 🛠 Proyecto DevOps: App Fullstack con React + Flask + Docker
=======
[![CI](https://github.com/amusteikis/devops-fullstack-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/amusteikis/devops-fullstack-starter/actions)
>>>>>>> 60fe070 (Actualizacion de README antes de pull)

# 🛠 Proyecto DevOps de Portafolio: App Fullstack con React + Flask + Docker

**🌐 Leer esto en inglés → [README.md](README.md)**

Este es un proyecto profesional listo para portafolio que demuestra una aplicación fullstack contenedorizada usando **React (frontend)**, **Flask (backend)** y **Docker**.

---

## ✨ Funcionalidades Clave

- 🔄 Orquestación con Docker Compose para frontend y backend
- 🌐 Comunicación entre servicios usando red interna
- 🔐 Configuración basada en entornos con `.env`
- 🏗 Builds multi-etapa (React → Nginx)
- 🚀 Configuración para desarrollo y producción

---

## 🧰 Stack Tecnológico

| Capa        | Herramienta/Servicio   |
|-------------|------------------------|
| Frontend    | React + Nginx          |
| Backend     | Flask (Python)         |
| Contenedores| Docker                 |
| Orquestación| Docker Compose         |
| Configuración | Archivos `.env`      |

---

## 🚀 Configuración Local

### Requisitos Previos:
- Docker
- Docker Compose

### Clonar y Ejecutar:

```bash
git clone https://github.com/amusteikis/devops-fullstack-starter.git
cd devops-fullstack-starter
```

### Agregar archivo de entorno:

Crear un archivo `.env` dentro de la carpeta `frontend/`:
```
REACT_APP_API_URL=http://localhost:5000
```

### Construir y lanzar la app:

```bash
docker compose up --build
```

### Acceso:

- Frontend → http://localhost:3000  
- Backend (test ping) → http://localhost:5000/ping

---

## 🧪 Ejecutar Tests

Para correr los tests del backend:

```bash
cd backend/
pytest
```

Los tests se ejecutan automáticamente en cada push mediante el pipeline de CI de GitHub Actions.

---

## 📦 Estructura del Proyecto

```
proyecto-devops/
├── backend/            # App Flask
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/           # App React
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── docker-compose.yml  # Orquestación de servicios
└── README.md
```

---

## ✅ Test de Conectividad

Visitar http://localhost:3000 y confirmar:

- ✔ Estado del backend: debería mostrar “Pong!”

Esto confirma la comunicación entre React y Flask vía HTTP.

---


## 📌 Estado del Proyecto

**🟢 Listo para deployment**  
CI/CD está configurado y verificado. Siguiente paso: publicar en una plataforma cloud (Render, Railway o Azure).

---

## 🙌 Autor

Hecho por [amusteikis](https://github.com/amusteikis)
