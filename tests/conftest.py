import pytest
from fastapi.testclient import TestClient
from main import app
from database import SessionLocal
from sqlalchemy.sql import text


class TestDB:
    def __init__(self):
        self.db = SessionLocal()

    def insert_record(self, data: list):
        for elem in data:
            self.db.add(elem)
        self.db.commit()

    def delete_all_record(self, table_name: str):
        self.db.execute(text(f"DELETE FROM {table_name}"))
        self.db.commit()


@pytest.fixture(scope="session")
def fastapi_client():
    return TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    test_db = TestDB()
    yield test_db
    test_db.db.close()
