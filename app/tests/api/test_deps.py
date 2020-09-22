from typing import Generator
from tests.core.test_database import TestingSessionLocal


def override_get_db() -> Generator:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
