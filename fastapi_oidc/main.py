import asyncio

from hypercorn import Config
from hypercorn.asyncio import serve

from fastapi_oidc.root import app

if __name__ == "__main__":
    config = Config()
    config.bind = ["localhost:8000"]
    config.use_reloader = True

    asyncio.run(serve(app, config))  # type: ignore
