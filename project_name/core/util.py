"""Defining some utilities for app."""

from project_name.logging.logging_setup import logger


def return_int_back(i: int) -> int:
    """
    Comment.

    Params:
    a: int
        some int
    """
    logger.bind(i=i).debug("Returning integer back")

    return i


def throwing_caught_error(j: str):
    """
    Definitely not a numpy style docstring.

    Two lines
    Params:
    j

    """
    logger.bind(j=j).debug("Error throwing incoming")

    try:
        j = "a"
        raise NameError("Some name error")
    except NameError:
        logger.exception("Exception")
    finally:
        logger.debug("After error")


def inner_function():
    """
    Inner function with logger context.

    Returns
    -------
    None
    """
    logger.debug("Inner function also with context")


def outer_function():
    """
    Outer function that sets logger context.

    Returns
    -------
    None
    """
    with logger.contextualize(context="everything"):
        logger.debug("Outer function (with context)")
        inner_function()
