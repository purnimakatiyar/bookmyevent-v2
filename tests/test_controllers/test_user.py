import pytest
from controllers.user import User
from unittest.mock import MagicMock
@pytest.fixture
def setup(monkeypatch):
    user_details = {
        'uuid': 'uuid',
        'user_id': 'user_id',
        'username': 'username',
        'password': 'password',
        'name': 'name',
        'phone': 'phone',
        'role': 'role',
    }
    return User(**user_details)


class TestUser:


    def test_signup(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.signup() is None


    def test_save_info(self, setup, monkeypatch):
        mock_insert_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "insert_item", mock_insert_item)
        assert setup.save_info() is None


    @pytest.mark.parametrize('username', ['user1234','user7834'])
    def test_get_user(self, setup, monkeypatch, username):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_user(username) == []


    @pytest.mark.parametrize('username', ['user1234','user7834'])
    def test_remove_manager(self, setup, monkeypatch, username):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.remove_manager(username) is None


    @pytest.mark.parametrize('username', ['user12','user6778'])
    def test_get_user_id(self, setup, monkeypatch, username):
        mock_get_item = MagicMock(return_value=['value'])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_user_id(username) == 'value'


    @pytest.mark.parametrize('username', ['purnima12', 'userpurnima1'])
    def test_update_account_password(self, setup, monkeypatch, username):
        mock_update_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "update_item", mock_update_item)
        assert setup.update_account(username, '1') is None


    @pytest.mark.parametrize('username', ['user1234', 'user789'])
    def test_update_account_name(self, setup, monkeypatch, username):
        mock_update_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "update_item", mock_update_item)
        assert setup.update_account(username, '2') is None


    @pytest.mark.parametrize('username', ['purnima1', 'purnima2'])
    def test_update_account_phone(self, setup, monkeypatch, username):
        mock_update_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "update_item", mock_update_item)
        assert setup.update_account(username, '3') is None

