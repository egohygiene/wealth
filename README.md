# Wealth

_Part of the Ego Hygiene ecosystem_

Wealth is a small personal finance "operating system." It brings your income, spending and savings into one place so you can focus on decisions rather than spreadsheets. The goal is to reduce money stress and help you learn by doing.

It might be useful if you:

- want a clear overview of where your money goes
- deal with gig work or other unpredictable income
- are moving through a big life transition and need a simple plan

The project is still evolving, but the aim is to make budgeting approachable and to give you tools that grow with your situation.

---

## Tech overview

This repository contains utilities, a minimal API and a starter UI. Below is the main stack.

| Layer     | Technology                      |
|-----------|---------------------------------|
| Frontend  | React (Vite)                    |
| Backend   | FastAPI                         |
| Auth      | Keycloak or Google OAuth2       |
| Database  | Postgres                        |
| CLI       | Click-powered tools             |
| Schema    | Pydantic financial models       |

### API

The FastAPI service lives under `services/api`. It uses Keycloak for authentication and also supports Google OAuth2 login.

Set the following environment variables with your Google credentials:

```
GOOGLE_CLIENT_ID=<client id>
GOOGLE_CLIENT_SECRET=<client secret>
```

Start the API for development with:

```
uvicorn services.api.main:app --reload
```

### UI

A Vite + React application is located in `apps/ui`. Install dependencies with pnpm:

```sh
cd apps/ui
pnpm install
```

Run the development server:

```sh
pnpm dev
```

### Docker Compose

Several compose files make it easy to run the API and UI in different environments. The base configuration lives in `docker-compose.base.yml`, with environment-specific overrides for development, staging, demo and production.

Example usage for development:

```bash
docker-compose -f docker-compose.base.yml -f docker-compose.development.yml up --build
```

To use a different environment replace `development` with `production`, `staging` or `demo` and provide the matching `.env.*` file.
