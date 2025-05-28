import { useKeycloak } from '@react-keycloak/web'

export default function AuthStatus() {
  const { keycloak } = useKeycloak()

  if (keycloak.authenticated) {
    const roles = (keycloak.tokenParsed as any)?.realm_access?.roles || []
    return (
      <div className="flex gap-2 items-center">
        <span className="font-semibold">
          {keycloak.tokenParsed?.preferred_username}
        </span>
        {roles.length > 0 && <span>Roles: {roles.join(', ')}</span>}
        <button
          className="px-2 py-1 bg-gray-200 rounded"
          onClick={() => keycloak.logout()}
        >
          Logout
        </button>
      </div>
    )
  }

  return (
    <button
      className="px-2 py-1 bg-gray-200 rounded"
      onClick={() => keycloak.login()}
    >
      Login
    </button>
  )
}
