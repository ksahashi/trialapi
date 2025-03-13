import pytest
from models.user import User

class TestUpdateUsers:

    def test_create_user(self, fastapi_client, db_session):
        res = fastapi_client.post("/api/v0/user", content=None)
        assert res.status_code == 200
        assert res.json() == "OK"


    def test_update_user(self, fastapi_client, db_session):
        res = fastapi_client.patch("/api/v1/user")
        assert res.status_code == 200
        assert res.json() == "OK"
