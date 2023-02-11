"""Settings specific for application logging."""

from dataclasses import dataclass

from pydantic import BaseSettings

from project_name.core.settings import AppSettings

app_settings = AppSettings()


@dataclass()
class LoggingSettings(BaseSettings):
    """Logging settings."""

    json_logging_level: str = "INFO" if app_settings.prod_environment else "DEBUG"
    txt_logging_level: str = "INFO" if app_settings.prod_environment else "DEBUG"
    std_logging_level: str = "INFO" if app_settings.prod_environment else "DEBUG"

    backtrace: bool = not app_settings.prod_environment
    diagnose: bool = not app_settings.prod_environment
