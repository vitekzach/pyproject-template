"""General app settings necessary for its run."""
from dataclasses import dataclass

from pydantic import BaseSettings, Field


@dataclass()
class AppSettings(BaseSettings):
    """Basic application settings."""

    prod_environment: bool = Field(
        default=True,
        env="PROD_ENV",
        description="Whether application runs in a production or a non-production environment.",
    )
