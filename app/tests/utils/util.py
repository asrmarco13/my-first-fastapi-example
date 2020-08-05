import string
import random
from typing import Dict
from fastapi.testclient import TestClient
from fastapi import Response
from schemas.user import UserCreate
from schemas.item import ItemCreate


def random_lower_string() -> str:
    """
    Return a randomic lower string
    """
    return "".join(random.choices(string.ascii_lowercase, k=16))


def random_user_email() -> str:
    """
    Return a randomic user email
    """
    return f"{random_lower_string()}@{random_lower_string()}.it"


def random_user_password() -> str:
    """
    Return a randomic user password
    """
    return random_lower_string()


def get_token_headers(client: TestClient) -> Dict[str, str]:
    """
    Return an access token
    """
    login_data = {"username": "test@test.it", "password": "testtest"}
    response = client.post("/token/", data=login_data)
    tokens = response.json()
    print(tokens)
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


def create_user(client: TestClient) -> TestClient:
    """
    Return an user create response
    """
    email = random_user_email()
    password = random_user_password()
    user = UserCreate(email=email, password=password)
    return client.post("/users/", json=user.dict())


def logged_current_user(client: TestClient, user_token_headers: Dict[str, str]) -> Dict:
    """
    Return a current user
    """
    response = client.get("/users/me/", headers=user_token_headers)
    return response.json()


def create_item(
    client: TestClient, user_token_headers: Dict[str, str], title: str, description: str
) -> TestClient:
    """
    Create an item
    """
    current_user = logged_current_user(client, user_token_headers)
    user_id = current_user["id"]
    item = ItemCreate(title=title, description=description)
    return client.post(
        f"/users/{user_id}/items", headers=user_token_headers, json=item.dict()
    )


def get_item_id(response: Response) -> int:
    """
    Return an item id
    """
    item_data = response.json()
    return item_data["id"]
