"""Simple fastapi server."""

import uuid
from multiprocessing import Pool

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from project_name.server.server_logging.logging_setup import logger

app = FastAPI()
app.logger = logger  # type: ignore


@app.middleware("http")
async def request_middleware(request: Request, call_next):
    """Request middleware - Create request ID and return it."""
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    with logger.contextualize(request_id=request_id):
        logger.info("Request started")
        response = JSONResponse(content="Dummy content")

        try:
            response = await call_next(request)

        except Exception as ex:  # pylint: disable=broad-exception-caught
            logger.exception(f"Request failed: {ex}")
            response = JSONResponse(content={"message": "fail"}, status_code=500)

        finally:
            response.headers["X-Request-ID"] = request_id
            logger.info("Request ended")
            return response  # pylint: disable=lost-exception


@app.get("/")
async def root():
    """Server root router."""
    return JSONResponse(content={"message": "Hello World!"}, status_code=200)


@app.get("/multiprocess")
async def multiprocess_task(request: Request):
    """Router for multiprocessing testing purposes."""
    logger.info("Inside multiprocess endpoint function.")

    request_id = request.state.request_id
    processes = 2

    multiprocessing_args = [(i, request_id) for i in range(processes)]

    with Pool(processes) as process:
        process.starmap(multiproc_fn, multiprocessing_args)
    return JSONResponse(content={"message": "success"}, status_code=200)


def multiproc_fn(batch_id: int, request_id: str) -> None:
    """Make something in multiple processes to test logging enqueue."""
    logger.bind(batch=batch_id, request_id=request_id).info(f"Inside multiprocess {batch_id}")
