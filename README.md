# ARCHIVELY 📚

**Archively** is a simple yet powerful web application designed to help users archive, manage, and categorize their favorite links effortlessly. Built with Flask and PostgreSQL, Archively offers a seamless user experience with a clean and responsive interface powered by the Bootswatch Vapor Bootstrap theme.

## Features

- **Create:** Add new links with optional tags.
- **Read:** View and Search a list of all archived links with their associated tags.
- **Update:** Modify existing links and their tags.
- **Delete:** Remove links from the archive.
---

## Technologies Used

- **Backend:**
  - [Flask](https://flask.palletsprojects.com/) – A lightweight WSGI web application framework.
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) – SQLAlchemy integration for Flask.
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/) – Manage SQLAlchemy database migrations for Flask applications.
  - [PostgreSQL](https://www.postgresql.org/) – A powerful open-source object-relational database system.
  - [Psycopg2](https://www.psycopg.org/) – PostgreSQL adapter for Python.
- **Frontend:**
  - [Bootstrap 5](https://getbootstrap.com/) – Frontend component library for responsive design.
- **Others:**
  - [python-dotenv](https://github.com/theskumar/python-dotenv) – Load environment variables from `.env` file.
  - [ngrok](https://ngrok.com/) – (Optional) Secure tunnels to localhost for sharing your local app online.

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System:** macOS
- **Python:** Python 3.9 or higher. [Download Python](https://www.python.org/downloads/)
- **Homebrew:** Package manager for macOS. [Install Homebrew](https://brew.sh/)
- **PostgreSQL:** Installed and running locally (via Homebrew or otherwise).

# Setup Instructions

## Local Development Setup

1. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Set up the database
```
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
4. Run the application
```
flask run
```

## Docker Setup

0. Install Docker and Docker Compose
- Link: https://docs.docker.com/get-docker/

1. Build the Docker containers
```
docker compose build
```

2. Run the services
```
docker compose up -d
```

3.Run database migrations
```
docker compose exec web flask db init
docker compose exec web flask db migrate -m "initial migration"
docker compose exec web flask db upgrade
```

4. View logs (optional)
```
docker compose logs -f
```

5. Stop services
```
docker compose down
```

### Common Flask Commands

- Create new migration: ```flask db migrate -m "description"```
- Apply migrations: ```flask db upgrade```
- Rollback migration: ```flask db downgrade```
- Show migration history: ```flask db history```
- Show current migration: ```flask db current```

### Common Docker Commands

- Rebuild specific service: `docker compose build web`
- Restart services: docker `compose restart`
- View running containers: `docker compose ps`
- Access container shell: `docker compose exec web bash`
- View service logs: `docker compose logs web`
- Stop services: `docker compose down`


