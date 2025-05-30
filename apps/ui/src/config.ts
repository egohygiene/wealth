export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'
export const KEYCLOAK_URL = import.meta.env.VITE_KEYCLOAK_URL || 'http://localhost:8080'
export const KEYCLOAK_REALM = import.meta.env.VITE_KEYCLOAK_REALM || 'wealth'
export const KEYCLOAK_CLIENT_ID = import.meta.env.VITE_KEYCLOAK_CLIENT_ID || 'frontend'

export const OIDC_AUTHORITY = `${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}`
export const OIDC_CLIENT_ID = KEYCLOAK_CLIENT_ID
export const OIDC_REDIRECT_URI =
  import.meta.env.VITE_OIDC_REDIRECT_URI || window.location.origin
