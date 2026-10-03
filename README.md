# TestPilot AI

An AI-assisted test automation starter project. TestPilot AI includes a React dashboard, a FastAPI service for generating test cases, and a Playwright-powered browser smoke test.

## Public demo

[Open TestPilot AI dashboard](https://basukumar56258-cpu.github.io/AI-Test-Automation-Agent-new/)

The public demo hosts the frontend dashboard. API-powered test generation and browser smoke-test execution require the backend to be hosted separately; locally, use the setup steps below.

## Features

- Generate starter test cases from a written requirement.
- Run a browser smoke test against a supplied URL.
- Review generated cases and smoke-test results in the dashboard.
- Expose backend endpoints and interactive API documentation.
- Use SQLite by default for local development, with a MySQL service defined in docker-compose.yml.

> **Current scope:** Test-case generation uses built-in templates; it does not call an LLM yet. Database models are present, but generated cases and run results are not currently persisted.

## Technology

| Area | Technologies |
| --- | --- |
| Frontend | React, Vite, Axios |
| Backend | Python, FastAPI, SQLAlchemy |
| Browser automation | Playwright |
| Tests | Pytest |
| Database | SQLite by default; MySQL configuration is included |

## Project structure

~~~text
.
├── backend/
│   ├── app/
│   │   ├── agents/       # Test-case generation
│   │   ├── api/          # FastAPI routes
│   │   ├── core/         # Application settings
│   │   ├── models/       # SQLAlchemy models
│   │   └── services/     # Playwright smoke-test runner
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/              # React app and styles
│   └── package.json
├── playwright/           # Playwright example test
├── tests/                # Pytest tests
├── docker-compose.yml
└── README.md
~~~

## Requirements

- Python 3.10 or newer
- Node.js and npm
- Chromium for Playwright browser tests

## Run locally

Start the backend from the repository root:

~~~powershell
cd backend
python -m venv .venv
..venvScriptsActivate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m uvicorn app.main:app --reload
~~~

In a second terminal, start the frontend:

~~~powershell
cd frontend
npm install
npm run dev
~~~

Open <http://localhost:5173> for the dashboard. The API is available at <http://localhost:8000>, with interactive documentation at <http://localhost:8000/docs>.

The backend defaults to a local SQLite database. Settings such as DATABASE_URL, CORS_ORIGINS, and the optional LLM provider values can be supplied as environment variables. backend/.env.example lists the available settings; configure them for your environment before using a non-default database or an LLM provider.

### Optional: Docker Compose

The Compose setup uses MySQL. Set MYSQL_ROOT_PASSWORD and MYSQL_PASSWORD in your environment or in an untracked root .env file before starting it. MYSQL_DATABASE and MYSQL_USER default to testpilot.

~~~powershell
docker compose up --build
~~~

## API

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | /api/health | Check backend health |
| POST | /api/test-cases/generate | Generate test cases from a requirement |
| POST | /api/tests/run | Run a Playwright smoke test against a URL |

Example test-case request:

~~~json
{
  "requirement": "Test a login page with valid and invalid credentials"
}
~~~

Example smoke-test request:

~~~json
{
  "url": "https://example.com"
}
~~~

## Run tests

From the repository root, after installing the backend requirements:

~~~powershell
python -m pytest
~~~

The Playwright example test also requires Chromium, installed with python -m playwright install chromium.
