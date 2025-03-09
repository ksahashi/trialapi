import pytest
from cruds.user import get_user_by_id
from models.user import User

class TestGetUser:

    def test_get_user(self, db_session):
        db_session.delete_all_record("users")

        users = [
            User(
                user_id="tcp001",
                user_name="test user001",
                email_address="test.user001@hoge.com"
            ),
        ]
        db_session.insert_record(users)
        user = get_user_by_id(db_session.db, "tcp001")
        assert user.user_id == "tcp001"
