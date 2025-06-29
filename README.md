# Dungeon Codex

Dungeon Codex is a game project that combines a Python-based backend (FastAPI + SQLAlchemy + PostgreSQL) with a Godot-based frontend, fully containerized using Docker and developed within a DevContainer-compatible environment.

---

## 🚀 Features

- Backend API built with FastAPI  
- Database powered by PostgreSQL  
- Manual database migrations via SQL scripts  
- Frontend built with Godot Engine  
- Development environment configured with DevContainers and Docker Compose  
- VS Code tasks and workspace integration  
- Testing environment and Makefile-based task automation

---

## ⚙️ Requirements

- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/)  
- [Visual Studio Code](https://code.visualstudio.com/)  
  - Dev Container extension  
- [Git](https://git-scm.com/)

---

## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dungeon-codex.git
cd dungeon-codex
```

### 2. Add Environment Variables

Create a `.env` file in the root directory:

```ini
POSTGRES_HOST=host.docker.internal
POSTGRES_DB=dungeon_codex_dev
POSTGRES_DB_TEST=dungeon_codex_test
POSTGRES_USER=dungeon
POSTGRES_PASSWORD=yourpassword
POSTGRES_PORT=5432
UID=1000
GID=1000
```

### 3. Open in VS Code

```bash
code .
```

Then select:  
**"Reopen in Container"** when prompted by the Dev Containers extension.

---

## 🐳 Running the Project

### Backend

Once inside the container, run:

```bash
make dev
```

This will apply migrations from SQL scripts and start the FastAPI backend with live reload.

The API will be available at:  
[http://localhost:8000](http://localhost:8000)  
[http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend

Open the `frontend` folder using the Godot editor inside or outside the container, and run the project.

---

## 🛠 Useful Make Commands

```bash
make dev         # Start the backend
make migrate     # Apply SQL migrations
make reset-db    # Drop and recreate the database
make test        # Run the backend tests
```

---

## 🧪 Running Tests

```bash
make test
```

Make sure your test database is configured in `.env`.

---

## ንድ Game Design

The core design documents for Dungeon Codex can be found in the `/docs/design` directory. These documents outline the game's concept, mechanics, and technical specifications.

-   [Game Concept](./docs/design/01_GAME_CONCEPT.md)
-   [Core Mechanics](./docs/design/02_CORE_MECHANICS.md)
-   [MVP Specification](./docs/design/03_MVP_SPECIFICATION.md)
-   [Technical Design](./docs/design/04_TECHNICAL_DESIGN.md)

## 🗺️ Development Roadmap

The development plan for the MVP is detailed in the following document:

-   [MVP Task List](./docs/development/MVP_TASK_LIST.md)

---

## 🗂 Project Structure (Summary)

```
dungeon-codex/
├── backend/
│   ├── app/               # FastAPI app modules
│   ├── sql_migrations/    # Manual SQL migration scripts
│   ├── apply_migrations.py# Migration runner script
│   ├── tests/             # Unit and integration tests
│   └── requirements.txt
├── docs/
│   ├── design/            # Game design documents
│   └── development/       # Development plans and tasks
├── frontend/              # Godot project files
├── .devcontainer/         # DevContainer setup
├── .vscode/               # VS Code tasks and workspace settings
├── docker-compose.yml
└── Makefile
```

---

## 📦 Development Tips

- Use VS Code tasks (`Ctrl+Shift+P → Run Task`) for quick actions.  
- Use `make` commands to manage common operations.  
- Monitor logs and backend behavior using live terminal output (`make dev` or task).

---

## 📜 License

MIT License
