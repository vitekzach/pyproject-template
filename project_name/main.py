"""Module docstring."""
from project_name.core.util import (
    outer_function,
    return_int_back,
    throwing_caught_error,
)
from project_name.project_logging.logging_setup import logger

logger.info("Application start")

# contextualizing project_logging in this function
outer_function()

# regular function that works
return_int_back(5)

# function that throws an error
throwing_caught_error("s")

logger.info("Application end")
