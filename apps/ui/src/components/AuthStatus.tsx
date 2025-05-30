import { useAuth } from 'react-oidc-context'

export default function AuthStatus() {
  const auth = useAuth()

  if (auth.isAuthenticated && auth.user) {
    const roles = (auth.user.profile as any)?.realm_access?.roles || []
    return (
      <div className="flex gap-2 items-center">
        <span className="font-semibold">
          {auth.user.profile?.preferred_username}
        </span>
        {roles.length > 0 && <span>Roles: {roles.join(', ')}</span>}
        <button
          className="px-2 py-1 bg-gray-200 rounded"
          onClick={() => auth.signoutRedirect()}
        >
          Logout
        </button>
      </div>
    )
  }

  return (
    <button
      className="px-2 py-1 bg-gray-200 rounded"
      onClick={() => auth.signinRedirect()}
    >
      Login
    </button>
  )
}
