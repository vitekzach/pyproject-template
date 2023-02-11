"""General app settings necessary for its run."""

from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Basic application settings."""

    prod_environment: bool | None = Field(
        default=True,
        env="PROD_ENV",
        description="Whether application runs in a production or a non-production environment.",
    )
