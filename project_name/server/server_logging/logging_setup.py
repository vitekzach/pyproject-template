"""Logging setup module for fastapi server."""

import logging
import sys

from loguru import logger

from project_name.project_logging.settings import LoggingSettings

logging_settings = LoggingSettings()


class InterceptHandler(logging.Handler):
    """Handler for fastapi/unicorn workers."""

    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        20: "INFO",
        10: "DEBUG",
        0: "NOTSET",
    }

    def emit(self, record):
        """Emit log."""
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        log = logger
        log.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logger.remove()
logger.add(
    sys.stdout,
    enqueue=True,
    backtrace=logging_settings.backtrace,
    diagnose=logging_settings.diagnose,
    level=logging_settings.std_logging_level,
)
logger.add(
    ".logs/log.json",
    enqueue=True,
    serialize=True,
    backtrace=logging_settings.backtrace,
    diagnose=logging_settings.diagnose,
    level=logging_settings.json_logging_level,
)
logger.add(
    ".logs/log.txt",
    enqueue=True,
    backtrace=logging_settings.backtrace,
    diagnose=logging_settings.diagnose,
    level=logging_settings.txt_logging_level,
)

logging.basicConfig(handlers=[InterceptHandler()], level=0)
logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]

for _log in ["uvicorn", "uvicorn.error", "fastapi"]:
    _logger = logging.getLogger(_log)
    _logger.handlers = [InterceptHandler()]
