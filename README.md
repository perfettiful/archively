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

