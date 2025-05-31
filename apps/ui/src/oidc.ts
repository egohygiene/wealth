import type { AuthProviderProps } from 'react-oidc-context'
import { OIDC_AUTHORITY, OIDC_CLIENT_ID, OIDC_REDIRECT_URI } from './config'

export const oidcConfig: AuthProviderProps = {
  authority: OIDC_AUTHORITY,
  client_id: OIDC_CLIENT_ID,
  redirect_uri: OIDC_REDIRECT_URI,
  onSigninCallback() {
    window.history.replaceState({}, document.title, window.location.pathname)
  },
}
