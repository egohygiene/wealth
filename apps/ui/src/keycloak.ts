import Keycloak from 'keycloak-js'

const keycloak = new Keycloak({
  url: 'http://localhost:8080',
  realm: 'wealth',
  clientId: 'frontend',
})

export default keycloak
