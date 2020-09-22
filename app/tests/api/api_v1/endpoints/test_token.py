from tests.test_app import client
from schemas.user import UserCreate


def test_get_access_token() -> None:
    """
    Return an access token
    """
    email = "test@test.it"
    password = "testtest"
    user_login = UserCreate(email=email, password=password)
    response = client.post("/users/", json=user_login.dict())
    assert response.status_code == 200
    user_login = {"username": user_login.email, "password": user_login.password}
    response = client.post("/token/", data=user_login)
    tokens = response.json()
    assert "access_token" in tokens
    assert tokens["access_token"]
