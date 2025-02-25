from fastapi import APIRouter
from fastapi_versioning import version

router = APIRouter()

@router.get("/")
@version(0)
async def get_users_v0() -> list:
    response = [
        "user1",
        "user2",
        "user3",
    ]

    return response

@router.get("/")
@version(1)
async def get_users() -> list:
    response = [
        "user1",
        "user2",
        "user3",
        "user4",
        "user5",
    ]

    return response

@router.post("/")
async def create_user() -> str:
    return "OK"

@router.patch("/")
@version(1)
async def update_user() -> str:
    return "OK"

@router.get("/version")
@version(0)
async def get_version_v0() -> dict:
    response = {
        'version': 'v0',
    }

    return response

@router.get("/version")
@version(1)
async def get_version() -> dict:
    response = {
        'version': 'v1',
    }

    return response
