import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import { BrowserRouter } from 'react-router-dom'
import { ReactKeycloakProvider } from '@react-keycloak/web'
import App from './App'
import { store } from './store'
import keycloak from './keycloak'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Provider store={store}>
      <ReactKeycloakProvider authClient={keycloak}>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </ReactKeycloakProvider>
    </Provider>
  </React.StrictMode>
)
