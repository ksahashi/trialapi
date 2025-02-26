from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from routers import (
    user,
    movie
)

app = FastAPI()

router_list = [
    [user.router, "/user", ["user"]],
    [movie.router, "/movie", ["movie"]],
]
for _router in router_list:
    app.include_router(_router[0], prefix=_router[1], tags=_router[2])

app = VersionedFastAPI(
    app,
    root_path="/api",
    version_format='{major}',
    prefix_format='/v{major}',
    default_version=(0,0))
