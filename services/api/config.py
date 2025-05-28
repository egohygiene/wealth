from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application configuration loaded from environment."""

    db_host: str = Field("localhost", env="API_DB_HOST")
    db_port: int = Field(5432, env="API_DB_PORT")
    db_user: str = Field("wealth", env="API_DB_USER")
    db_password: str = Field("wealthpass", env="API_DB_PASSWORD")
    db_name: str = Field("wealth", env="API_DB_NAME")

    google_client_id: str = Field("CHANGE_ME", env="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field("CHANGE_ME", env="GOOGLE_CLIENT_SECRET")

    keycloak_server_url: str = Field(
        "http://localhost:8080/auth/", env="KEYCLOAK_SERVER_URL"
    )
    keycloak_client_id: str = Field("wealth-api", env="KEYCLOAK_CLIENT_ID")
    keycloak_client_secret: str = Field(
        "CHANGE_ME", env="KEYCLOAK_CLIENT_SECRET"
    )
    keycloak_admin_client_secret: str = Field(
        "CHANGE_ME", env="KEYCLOAK_ADMIN_CLIENT_SECRET"
    )
    keycloak_realm: str = Field("wealth", env="KEYCLOAK_REALM")
    keycloak_redirect_uri: str = Field(
        "http://localhost:8000/callback", env="KEYCLOAK_REDIRECT_URI"
    )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_config() -> Config:
    """Return a cached Config instance."""
    return Config()
