from typing import Dict
from schemas.user import UserUpdate
from schemas.item import ItemCreate
from tests.test_app import client
from tests.utils import util


def test_read_users() -> None:
    """
    Return a list of users
    """
    response = client.get("/users")
    assert response.status_code == 200
    assert response.text


def test_read_user() -> None:
    """
    Return a user
    """
    response = util.create_user(client)
    assert response.status_code == 200, response.text
    data = response.json()
    user_id = data["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    existing_user = response.json()
    assert data["email"] == existing_user["email"]


def test_create_user() -> None:
    """
    Create user
    """
    response = util.create_user(client)
    assert response.status_code == 200


def test_update_user() -> None:
    """
    Update a user
    """
    response = util.create_user(client)
    assert response.status_code == 200, response.text
    data = response.json()
    user_id = data["id"]
    user_update = UserUpdate(
        name=util.random_lower_string(),
        surname=util.random_lower_string(),
        is_active=False,
    )
    response = client.put(f"/users/{user_id}", json=user_update.dict())
    assert response.status_code == 200, response.text
    user_update = response.json()
    assert data["email"] == user_update["email"] and not user_update["is_active"]


def test_delete_user() -> None:
    """
    Delete a user
    """
    response = util.create_user(client)
    assert response.status_code == 200, response.text
    data = response.json()
    user_id = data["id"]
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200


def test_user_me(user_token_headers: Dict[str, str]) -> None:
    """
    Return current logged user
    """
    response = client.get("/users/me/", headers=user_token_headers)
    current_user = response.json()
    assert current_user
    assert current_user["is_active"] is True
    assert current_user["email"] == "test@test.it"


def test_add_user_item(user_token_headers: Dict[str, str]) -> None:
    """
    Create a user item
    """
    current_user = util.logged_current_user(client, user_token_headers)
    user_id = current_user["id"]
    item = ItemCreate(title="Computer-test", description="Pc test")
    response = client.post(
        f"/users/{user_id}/items", headers=user_token_headers, json=item.dict()
    )
    assert response.status_code == 200
    item_data = response.json()
    assert item_data["title"] == item.title
