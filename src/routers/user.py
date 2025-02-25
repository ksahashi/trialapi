from fastapi import APIRouter, Depends

router_v0 = APIRouter()
router = APIRouter()

@router.get("/")
async def get_users() -> list:
    response = [
        "user1",
        "user2",
        "user3",
    ]

    return response

@router.get("/version")
async def get_version() -> dict:
    response = {
        'version': 'v1',
    }

    return response

@router_v0.get("/")
async def get_users_v0(users: list = Depends(get_users)) -> list:
    return users

@router_v0.get("/version")
async def get_version_v0() -> dict:
    response = {
        'version': 'v0',
    }

    return response
