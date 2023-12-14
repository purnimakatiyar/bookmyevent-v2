import pytest
from utils.encrypt import hash_password, check_password

@pytest.fixture
def hashed_password():
    password = 'test_password'
    return hash_password(password)

def test_hash_password():
    password = 'test_password'
    hashed_password = hash_password(password)
    assert hashed_password != password

def test_check_password(hashed_password):
    password_to_check = 'test_password'
    assert check_password(password_to_check, hashed_password)
    assert not check_password('incorrect_password', hashed_password)
    assert not check_password('', hashed_password)
    assert not check_password(None, hashed_password)