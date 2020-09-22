from fastapi.testclient import TestClient
from app import app
from tests.api import test_deps
from api import deps


app.dependency_overrides[deps.get_db] = test_deps.override_get_db
client = TestClient(app)
