"""Simple fastapi server."""

from fastapi import FastAPI

app = FastAPI()


# TODO request ID add to logger  # pylint: disable=fixme
# TODO more function and observe context works through  # pylint: disable=fixme
# TODO have loguru take over logger  # pylint: disable=fixme
@app.get("/")
async def root():
    """Server root router."""
    return {"message": "Hello World"}
