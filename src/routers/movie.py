from fastapi import APIRouter, Depends

from cruds.movie import get_movies
from database import get_db

router = APIRouter()

@router.get("/")
async def get_movie(db=Depends(get_db)) -> list:
    movies = get_movies(db)
    response = ({
        'movie_code': m.movie_code,
        'title': m.title,
        'release_date': m.release_date,
        'recommendation': m.recommendation,
        'is_deleted': m.is_deleted,
        'deleted_at': m.deleted_at
    } for m in movies)
    return response
