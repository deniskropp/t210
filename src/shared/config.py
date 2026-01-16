from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Literal

class Settings(BaseSettings):
    """
    Global configuration for the Klipper SDK.
    Reads from environment variables and/or .env file.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # Core Settings
    ENVIRONMENT: Literal["development", "production", "testing"] = Field(
        default="development",
        description="Current runtime environment"
    )
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Logging verbosity level"
    )
    
    # API Settings (Example)
    API_TIMEOUT_SECONDS: float = Field(
        default=30.0,
        description="Default timeout for API requests"
    )

# Singleton instance
settings = Settings()
