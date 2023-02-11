"""Loggers for whole application."""

import sys

from loguru import logger

from project_name.logging.settings import LoggingSettings, app_settings

logging_settings = LoggingSettings()

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "backtrace": logging_settings.backtrace,
            "diagnose": logging_settings.diagnose,
            "level": logging_settings.json_logging_level,
        },
        {
            "sink": ".logs/log.json",
            "serialize": True,
            "backtrace": logging_settings.backtrace,
            "diagnose": logging_settings.diagnose,
            "level": logging_settings.json_logging_level,
        },
        {
            "sink": ".logs/log.txt",
            "backtrace": logging_settings.backtrace,
            "diagnose": logging_settings.diagnose,
            "level": logging_settings.txt_logging_level,
        },
    ]
)

if app_settings.prod_environment:
    logger.info("Application running in production state")
else:
    logger.warning("Application running in non-production state, sensitive data can be leaked via log diagnosis!")
