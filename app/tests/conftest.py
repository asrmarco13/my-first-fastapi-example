from typing import Dict
import pytest
from tests.test_app import client
from tests.utils import util


@pytest.fixture(scope="module")
def user_token_headers() -> Dict[str, str]:
    """
    Method allow user access token
    """
    return util.get_token_headers(client)
