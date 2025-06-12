# 🛠 Proyecto DevOps: App Fullstack con React + Flask + Docker

Este proyecto es una aplicación web fullstack desarrollada como práctica para integrar herramientas modernas del ecosistema DevOps. Utiliza un frontend en **React**, un backend en **Flask** y ambos se ejecutan en contenedores Docker orquestados con **Docker Compose**.

Sirve como base para comprender y aplicar principios clave como:

- Construcción y despliegue de imágenes Docker
- Separación de entornos frontend/backend
- Comunicación entre servicios a través de red interna Docker
- Uso de variables de entorno para configuración flexible
- Gestión de puertos y exposición de servicios
- Resolución de CORS para permitir interacción entre FE y BE

El objetivo final es crear un entorno replicable, profesional y listo para ser desplegado en cualquier plataforma compatible con contenedores.

---

## 🧰 Tecnologías utilizadas

- **Frontend:** [React](https://reactjs.org/) (modo desarrollo)
- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Contenedores:** [Docker](https://www.docker.com/)
- **Orquestación:** [Docker Compose](https://docs.docker.com/compose/)
- **Servidor HTTP:** Nginx (modo producción opcional)
- **Variables de entorno:** `.env` para React y Flask
- **Red interna:** Docker Network

---

## 📁 Estructura del proyecto

proyecto-devops/
├── backend/ # Aplicación Flask (API REST)
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/ # Aplicación React
│ ├── src/
│ ├── public/
│ ├── Dockerfile
│ ├── package.json
│ └── .env
│
├── nginx/ # (opcional, para servir en producción)
│ └── default.conf
│
├── docker-compose.yml # Orquestación de servicios
└── README.md # Documentación del proyecto

---

## 🚀 Cómo levantar el entorno local

### Requisitos

- Docker
- Docker Compose

### Pasos:

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/proyecto-devops.git
cd proyecto-devops

2. Configurar variables de entorno:

Crear un archivo .env dentro de la carpeta frontend/ con el siguiente contenido:
REACT_APP_API_URL=http://localhost:5000
Este valor debe coincidir con la URL del backend Flask.

3. Levantar los servicios:
docker compose up --build

Esto hará lo siguiente:

Construirá las imágenes del frontend y backend.

Levantará los contenedores necesarios.

Expondrá los puertos: 3000 (frontend), 5000 (backend).

🌐 Acceso
Frontend (React): http://localhost:3000

Backend (ping): http://localhost:5000/ping


### PRUEBAS DE CONECTIVIDAD
Una vez levantado el entorno, accedé al frontend en http://localhost:3000.
Deberías ver el mensaje:

**Prueba de conexión al backend:**
**Hola desde el backend Flask!**

Esto indica que el frontend pudo conectarse correctamente al backend mediante fetch.

También podés testear el backend directamente desde:
http://localhost:5000/ping

### Desarrollo y Mantenimiento
Para modificar el frontend, trabajá dentro de frontend/src/

Para modificar el backend, trabajá dentro de backend/

Si modificás dependencias o Dockerfiles, recordá reconstruir:

docker compose up --build

Para detener y eliminar los contenedores:

docker compose down


📌 Próximos pasos
Integrar base de datos PostgreSQL como servicio adicional

Conectar Flask con SQLAlchemy

Agregar endpoints reales y persistencia

Integrar pipeline de CI/CD con GitHub Actions o Jenkins

Agregar monitoreo con Grafana + Prometheus (opcional)


 
