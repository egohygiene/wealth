# UI App

This is a React application bootstrapped with Vite and TypeScript. It uses pnpm to manage dependencies. Major features include:

- React Router
- Tailwind CSS
- Redux Toolkit with RTK Query
- Keycloak and Google authentication stubs
- Unovis for charting
- Vite dev server proxy to the FastAPI backend
- Path aliases via `vite-tsconfig-paths`
- Type checking with `vite-plugin-checker`
- SVG imports with `vite-plugin-svgr`
- Optional PWA support via `vite-plugin-pwa`

## Getting Started

Install dependencies with pnpm:

```sh
pnpm install
```

Run the development server:

```sh
pnpm dev
```

Build for production:

```sh
pnpm build
```

### Configuration

Runtime options are provided via environment variables. Set them in a `.env`
file or pass them through your container runtime.

- `VITE_API_BASE_URL` - base URL for the API service
- `VITE_KEYCLOAK_URL` - Keycloak server URL
- `VITE_KEYCLOAK_REALM` - authentication realm
- `VITE_KEYCLOAK_CLIENT_ID` - Keycloak client id

The Docker Compose setups load these variables from their respective `.env.*`
files so the UI automatically points at the correct services.


