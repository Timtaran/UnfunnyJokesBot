__all__ = ["routers"]

from .handle_joke_request import router as handle_joke_request_router
from .handle_start import router as handle_start_router

routers = [handle_joke_request_router, handle_start_router]
