import pytest
from unittest.mock import MagicMock
from controllers.authentication import Authenticate
from utils import encrypt

@pytest.fixture
def setup(monkeypatch):
    return Authenticate(username='test_user', password='test_password')


class TestAuthenticate:


    def test_login_failed(self, setup, monkeypatch):
        monkeypatch.setattr(setup.db, "get_item",
                            lambda _, details: None)
        monkeypatch.setattr(encrypt, 'check_password', lambda _: False)
        assert setup.login() is None


    def test_login_success(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        mock_check_password = MagicMock(return_value=True)
        monkeypatch.setattr(encrypt, 'check_password', mock_check_password)
        assert setup.login() is None


    def test_get_role(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=['v', 'a'])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_role() is 'v'
