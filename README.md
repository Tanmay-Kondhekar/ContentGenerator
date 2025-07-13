# 📝 Content Generator

A lightweight, containerized web application built using **FastAPI**, **Jinja2 templates**, and **PostgreSQL** — designed to generate dynamic content with speed and flexibility.

## 🚀 Features

- ⚡ FastAPI backend with async route support
- 🎨 Jinja2 templating for dynamic HTML rendering
- 🐘 PostgreSQL database for persistent storage
- 🐳 Dockerized for easy deployment
- 🔁 Docker Compose integration for multi-service orchestration
- 🤗 Hugging face Inference API
---

## To Run the project!

- create a .env file having 
    `1.postgre_url_key=postgresql://tammy:tammy@db:5432/aigen` 
    2.Hugging_face_token, get it from settings of HF

- Build and Start Containers
    `docker compose up --build`