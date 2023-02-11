"""Settings specific for application project_logging."""


from pydantic import BaseSettings

from project_name.core.settings import AppSettings

app_settings = AppSettings()


class LoggingSettings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Logging settings."""

    json_logging_level: str = "INFO" if app_settings.prod_environment else "DEBUG"
    txt_logging_level: str = "INFO" if app_settings.prod_environment else "DEBUG"
    std_logging_level: str = "INFO" if app_settings.prod_environment else "DEBUG"

    backtrace: bool = not app_settings.prod_environment
    diagnose: bool = not app_settings.prod_environment
