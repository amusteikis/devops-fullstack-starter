
![CI](https://github.com/amusteikis/devops-fullstack-starter/actions/workflows/ci.yml/badge.svg)

# 🛠 Proyecto de Portafolio DevOps: Aplicación Fullstack con React + Flask + Docker

**🌐 Leé esto en inglés → [README.md](README.md)**

Este es un proyecto profesional listo para portafolio que demuestra una aplicación fullstack contenerizada utilizando **React (frontend)**, **Flask (backend)** y **Docker**.

---

## ✨ Características principales

- 🔄 Orquestación con Docker Compose para frontend y backend
- 🌐 Comunicación interna entre servicios
- 🔐 Configuración por entorno con archivos `.env`
- 🏗 Builds multietapa (React → Nginx)
- 🚀 Configuración diferenciada para desarrollo y producción

---

## 🧰 Stack Tecnológico

| Capa         | Herramienta/Servicio     |
|--------------|--------------------------|
| Frontend     | React + Nginx            |
| Backend      | Flask (Python)           |
| Contenedores | Docker                   |
| Orquestación | Docker Compose           |
| Configuración| Archivos `.env`          |

---

## 🚀 Cómo levantar el proyecto localmente

### Requisitos:
- Docker
- Docker Compose

### Clonar y correr:

```bash
git clone https://github.com/amusteikis/devops-fullstack-starter.git
cd devops-fullstack-starter
```

### Agregar configuración de entorno:

Crear un archivo `.env` dentro de la carpeta `frontend/`:

```
REACT_APP_API_URL=http://localhost:5000
```

### Build y levantar:

```bash
docker compose up --build
```

### Accesos:

- Frontend → http://localhost:3000  
- Backend (test de conexión) → http://localhost:5000/ping

---

## 🧪 Ejecutar tests

Para correr los tests del backend:

```bash
cd backend/
pytest
```

Los tests se ejecutan automáticamente en cada push mediante el pipeline de CI de GitHub Actions.

---

## 📦 Estructura del proyecto

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

## ✅ Test de conectividad

Visitá http://localhost:3000 y confirmá:

- ✔ Que se muestran los usuarios existentes y se puede crear/modificar.

Esto confirma la comunicación entre React y Flask a través de HTTP.

---

## 🌐 Demo en línea

Accedé a la app desplegada aquí:  
👉 https://devops-fullstack-starter.onrender.com

---

## 📌 Estado del proyecto

**🟢 Totalmente desplegado**  
El pipeline CI/CD está configurado y verificado. Frontend y backend están en línea en Render.

---

## 🙌 Autor

Desarrollado por [amusteikis](https://github.com/amusteikis)
