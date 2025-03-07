import pytest

class TestReadUsers:

    def test_all_users(self, fastapi_client, db_session):
        res = fastapi_client.get("/api/v0/user")
        assert res.status_code == 200
        users = res.json()
        print(users)
        assert len(users) >= 1


    def test_read_user(self, fastapi_client, db_session):
        res = fastapi_client.get("/api/v0/user/tcp001")
        assert res.status_code == 200
        user = res.json()
        print(user)
        assert user["user_id"] == "tcp002"
