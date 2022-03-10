from fixture_and_parametrize_22Modul_PyTest_API.api import PetFriends
from fixture_and_parametrize_22Modul_PyTest_API.settings import valid_password, valid_email, invalid_email, invalid_age, invalid_name
import pytest


@pytest.fixture(autouse=True)
def get_key():
    pf = PetFriends()
    status, key = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in key
    return key