[https://finler-portfolio.duckdns.org](https://finler-portfolio.duckdns.org)

# Gleb Litvinchuk — Personal Portfolio

This is the source code for my personal portfolio website, built with the goal of being lightweight, fully self-hosted, and automatically secured with HTTPS.

## 🛠️ Technologies Used

- **Flask (Python)** — backend routing and project structure
- **HTML + Jinja2** — dynamic rendering of project content
- **Docker** — containerized deployment of the application
- **Caddy** — production-grade web server that automatically handles:
  - HTTPS via Let's Encrypt
  - TLS certificate renewal
  - HTTP→HTTPS redirection

## 🧱 Structure Overview

```text
portfolio-site/
├── app/
│   ├── __init__.py
│   ├── data/
│   │   └── projects.json
│   ├── routes/
│   │   └── main.py
│   └── templates/
│       ├── index.html
│       └── additionally/
│           └── title.png
├── run.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── Caddyfile
└── .gitignore
```

## ✨ Highlights

- Smooth, responsive frontend with animated project gallery
- All project entries are dynamically rendered from a JSON source
- Deployed via Docker with zero external services
- HTTPS with auto-renewing certificate using Caddy and Let’s Encrypt
