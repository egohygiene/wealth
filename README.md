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

