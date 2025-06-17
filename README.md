![CI](https://github.com/amusteikis/devops-fullstack-starter/actions/workflows/ci.yml/badge.svg)

# 🛠 DevOps Portfolio Project: Fullstack OApp with React + Flask + Docker

**🌐 Read this in Spanish → [README.es.md](README.es.md)**

This is a professional portfolio-ready DevOps project showcasing a containerized fullstack application using **React (frontend)**, **Flask (backend)**, and **Docker**.

It was built to demonstrate:
- Docker container orchestration with Docker Compose
- API communication across services using internal networking
- Use of environment variables
- Multi-stage Docker builds (React + Nginx)
- Dev vs Production mode configuration

---

## 🧰 Technologies Used

- **Frontend:** React (served with Nginx)
- **Backend:** Flask (Python)
- **Containers:** Docker
- **Orchestration:** Docker Compose
- **Static server:** Nginx
- **Env config:** `.env` files

---

## 🚀 Local Setup

### Prerequisites:
- Docker
- Docker Compose

### Steps:

```bash
git clone https://github.com/your-user/devops-fullstack-starter.git
cd devops-fullstack-starter

Create .env file inside the frontend/ folder:
REACT_APP_API_URL=http://localhost:5000

Then, build and run the stack:
sudo docker compose up --build

App will be available at:

Frontend: http://localhost:3000

Backend: http://localhost:5000/ping

📦 Project Structure

proyecto-devops/
│
├── backend/            # Flask app
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/           # React app
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── docker-compose.yml  # Service orchestration
└── README.md

✅ Connectivity Test
Access http://localhost:3000 and verify:

Test connection to backend: Pong!

This confirms React can communicate with Flask via HTTP.

🧠 Notes
To edit React: frontend/src/

To edit Flask: backend/

Rebuild images if you change Dockerfiles or dependencies

Use docker compose down to stop services
