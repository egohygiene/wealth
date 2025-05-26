# Wealth

This repository contains personal finance utilities and a minimal API.

## API

The FastAPI service lives under `services/api`. It uses Keycloak for
authentication and now also supports Google OAuth2 login.

Set the following environment variables with your Google credentials:

```
GOOGLE_CLIENT_ID=<client id>
GOOGLE_CLIENT_SECRET=<client secret>
```

Start the API for development with:

```
uvicorn services.api.main:app --reload
```


## UI

A Vite + React application is located in `apps/ui`. Install dependencies with pnpm:

```sh
cd apps/ui
pnpm install
```

Run the development server:

```sh
pnpm dev
```


## Docker Compose

Several compose files are provided to make running the API and UI in different environments easy. The base configuration lives in `docker-compose.base.yml` and environment specific overrides are available for development, staging, demo and production.

Example usage for development:

```bash
docker-compose -f docker-compose.base.yml -f docker-compose.development.yml up --build
```

To use a different environment replace `development` with `production`, `staging` or `demo` and provide the matching `.env.*` file.

