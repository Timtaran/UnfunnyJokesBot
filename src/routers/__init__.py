__all__ = ["routers"]

from .handle_joke_request import router as handle_joke_request_router

routers = [handle_joke_request_router]
