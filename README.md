![CI](https://github.com/amusteikis/devops-fullstack-starter/actions/workflows/ci.yml/badge.svg)

# 🛠 DevOps Portfolio Project: Fullstack OApp with React + Flask + Docker

**🌐 Read this in Spanish → [README.es.md](README.es.md)**

This is a professional portfolio-ready DevOps project showcasing a containerized fullstack application using **React (frontend)**, **Flask (backend)**, and **Docker**.

---

## ✨ Key Features

- 🔄 Docker Compose orchestration for frontend & backend
- 🌐 Internal network communication between services
- 🔐 Environment-based configuration (`.env`)
- 🏗 Multi-stage builds (React → Nginx)
- 🚀 Dev vs Production setup

---

## 🧰 Tech Stack

| Layer       | Tool/Service         |
|-------------|----------------------|
| Frontend    | React + Nginx        |
| Backend     | Flask (Python)       |
| Containers  | Docker               |
| Orchestration | Docker Compose     |
| Config      | `.env` files         |

---

## 🚀 Local Setup

### Prerequisites:
- Docker
- Docker Compose

### Clone & Run:

```bash
git clone https://github.com/amusteikis/devops-fullstack-starter.git
cd devops-fullstack-starter
```

### Add environment config:

Create `.env` inside the `frontend/` folder:
```
REACT_APP_API_URL=http://localhost:5000
```

### Build and launch:

```bash
docker compose up --build
```

### Access:

- Frontend → http://localhost:3000  
- Backend (ping test) → http://localhost:5000/ping

---

## 🧪 Running Tests

To run backend tests:

```bash
cd backend/
pytest
```

Tests are automatically executed on every push via GitHub Actions CI pipeline.

---

## 📦 Project Structure

```
proyecto-devops/
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
```

---

## ✅ Connectivity Test

Visit http://localhost:3000 and confirm:

- ✔ Backend status: should show “Pong!”

This confirms communication between React and Flask over HTTP.

---


## 📌 Project Status

**🟢 Ready for deployment**  
CI/CD is set up and verified. Next step: publish to a cloud platform (Render, Railway or Azure).

---

## 🙌 Author

Built by [amusteikis](https://github.com/amusteikis)
