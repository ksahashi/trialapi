import pytest

class TestReadMovies:
    def _call_api(self, fastapi_client):
        res = fastapi_client.get("/api/v0/movie")
        return res

    def test_all_movies(self, fastapi_client, db_session):
        res = self._call_api(fastapi_client)

        assert res.status_code == 200
        movies = res.json()
        print(movies)
        assert len(movies) >= 1
