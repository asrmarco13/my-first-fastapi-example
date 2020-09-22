from typing import Dict
from tests.test_app import client
from tests.utils import util
from schemas.item import ItemUpdate


def test_read_items() -> None:
    """
    Return a list of items
    """
    response = client.get("/items")
    assert response.status_code == 200


def test_read_item(user_token_headers: Dict[str, str]) -> None:
    """
    Return an item
    """
    response = util.create_item(
        client, user_token_headers, "Computer-test-read-item", "Pc test"
    )
    assert response.status_code == 200
    item_data = response.json()
    item_id = item_data["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    item = response.json()
    assert item_data["title"] == item["title"]


def test_update_item(user_token_headers: Dict[str, str]) -> None:
    """
    Update an item
    """
    response = util.create_item(
        client, user_token_headers, "Computer-test-error-item", "Pc test error"
    )
    item_data = response.json()
    item_id = item_data["id"]
    item_owner_id = item_data["owner_id"]
    item_update = ItemUpdate(
        title="Computer-test-update-item", description="Pc test update"
    )
    response = client.put(f"/items/{item_id}", json=item_update.dict())
    assert response.status_code == 200, response.text
    item_update = response.json()
    assert (
        item_update["owner_id"] == item_owner_id
        and item_update["title"] == "Computer-test-update-item"
    )


def test_delete_item(user_token_headers: Dict[str, str]) -> None:
    """
    Delete an item
    """
    response = util.create_item(
        client, user_token_headers, "Computer-test-error-item", "Pc test error"
    )
    item_id = util.get_item_id(response)
    response = client.delete(f"/items/{item_id}", headers=user_token_headers)
    assert response.status_code == 200
