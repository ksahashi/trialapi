from fastapi import APIRouter
from fastapi_versioning import version

router = APIRouter()

@router.get("/")
async def get_movie() -> list:
    response = [
        "movie1",
        "movie2",
        "movie3",
    ]

    return response
