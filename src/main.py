from fastapi import FastAPI
from routers import (
    user,
    movie
)

app = FastAPI()

router_list = [
    [[user.router_v0, user.router], "/user", ["user"]],
    [[movie.router, movie.router], "/movie", ["movie"]],
]
for _router in router_list:
    for index, _version in enumerate([0, 1]):
        app.include_router(
            _router[0][index],
            prefix="/api/v" + str(_version) + _router[1],
            tags=_router[2])

@app.get("/")
async def root():
    return {"message": "Hello World"}
