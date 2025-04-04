import pytest
from models.user import User

class TestReadUsers:

    def test_all_users(self, fastapi_client, db_session):
        db_session.delete_all_record("users")

        users = [
            User(
                user_id="tcp001",
                user_name="test user001",
                email_address="test.user001@hoge.com"
            )
        ]
        db_session.insert_record(users)

        res = fastapi_client.get("/api/v1/user")
        assert res.status_code == 200
        users = res.json()
        print(users)
        assert len(users) >= 1


    def test_read_user(self, fastapi_client, db_session):
        db_session.delete_all_record("users")

        users = [
            User(
                user_id="tcp001",
                user_name="test user001",
                email_address="test.user001@hoge.com"
            ),
            User(
                user_id="tcp002",
                user_name="test user002",
                email_address="test.user002@hoge.com"
            )
        ]
        db_session.insert_record(users)

        res = fastapi_client.get("/api/v0/user/tcp001")
        assert res.status_code == 200
        user = res.json()
        print(user)
        assert user["user_id"] == "tcp001"


    def test_read_user_v0(self, fastapi_client, db_session):
        res = fastapi_client.get("/api/v0/user")
        assert res.status_code == 200
        users = res.json()
        assert len(users) >= 3


    def test_get_version_v0(self, fastapi_client):
        res = fastapi_client.get("/api/v0/user/version")
        assert res.status_code == 200
        json = res.json()
        assert json["version"] == "v0"



    def test_get_version_v1(self, fastapi_client):
        res = fastapi_client.get("/api/v1/user/version")
        assert res.status_code == 200
        json = res.json()
        assert json["version"] == "v1"
