from fastapi import APIRouter, Depends
from fastapi_versioning import version

from cruds.user import get_users, get_user_by_id
from database import get_db

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
async def get_users_v1(db=Depends(get_db)) -> list:
    users = get_users(db)
    response = ({
        "user_id": u.user_id,
        "user_name": u.user_name,
        "email_address": u.email_address,
    } for u in users)
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

@router.get("/{user_id}")
async def get_user(user_id: str, db=Depends(get_db)):
    user = get_user_by_id(db, user_id)
    response = {
        'user_id': user.user_id,
        'name': user.user_name,
        'email_address': user.email_address
    }
    return response
