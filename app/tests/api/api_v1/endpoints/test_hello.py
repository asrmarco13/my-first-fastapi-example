from tests.test_app import client


def test_read_hello():
    """
    Test hello endpoint
    """
    response = client.get("/hello")
    assert response.status_code == 200
