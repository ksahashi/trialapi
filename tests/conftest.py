import pytest
from fastapi.testclient import TestClient
from main import app
from database import SessionLocal


class TestDB:
    def __init__(self):
        self.db = SessionLocal()


@pytest.fixture()
def fastapi_client():
    return TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    test_db = TestDB()
    yield test_db
    test_db.db.close()
