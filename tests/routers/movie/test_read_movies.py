import pytest
from datetime import datetime
from models.movie import Movie

class TestReadMovies:
    def _call_api(self, fastapi_client):
        res = fastapi_client.get("/api/v0/movie")
        return res

    def test_all_movies(self, fastapi_client, db_session):
        db_session.delete_all_record("movies")

        movies = [
            Movie(
                movie_code="000001",
                title="title1",
                release_date=datetime.now(),
                recommendation=1,
                is_deleted=False,
                deleted_at=None
            ),
            Movie(
                movie_code="000002",
                title="title2",
                release_date=datetime.now(),
                recommendation=2,
                is_deleted=False,
                deleted_at=None
            ),
            Movie(
                movie_code="000003",
                title="title3",
                release_date=datetime.now(),
                recommendation=0,
                is_deleted=True,
                deleted_at=datetime.now()
            ),
        ]
        db_session.insert_record(movies)

        res = self._call_api(fastapi_client)

        assert res.status_code == 200
        movies = res.json()
        print(movies)
        assert len(movies) >= 2
