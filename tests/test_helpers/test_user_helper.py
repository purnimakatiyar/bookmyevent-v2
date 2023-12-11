import pytest
from unittest.mock import patch, MagicMock
from src.helpers.user_helper import UserHelper


@pytest.fixture
def mock_user_id():
    user_id = MagicMock(return_value="userid12345")
    return user_id

class TestUserHelper:

    def test_signup_user_exists(self):
        mock_signup = MagicMock(return_value="signup_details")
        with patch('src.utils.input.Input.signup_input', mock_signup):
            with patch('src.controllers.user.User.signup', return_value="user"):
                user_helper = UserHelper()
                user_helper.signup('role')

        assert mock_signup.called is True

    def test_signup_user_not_exists(self):
        mock_signup = MagicMock(return_value="signup_details")
        with patch('src.utils.input.Input.signup_input', mock_signup):
            with patch('src.controllers.user.User.signup', return_value=None):
                user_helper = UserHelper()
                user_helper.signup('role')

        assert mock_signup.called is True


    def test_remove_manager_not_exists(self):
        mock_remove_manager = MagicMock(return_value='username')
        with patch('src.utils.input.Input.remove_manager_input', mock_remove_manager):
            with patch('src.controllers.user.User.get_user', return_value=None):
                user_helper = UserHelper()
                user_helper.remove_manager()
        assert mock_remove_manager.called is True

    def test_remove_manager_exists(self):
        mock_remove_manager = MagicMock(return_value='username')
        with patch('src.utils.input.Input.remove_manager_input', mock_remove_manager):
            with patch('src.controllers.user.User.get_user', return_value='manager'):
                user_helper = UserHelper()
                user_helper.remove_manager()
        assert mock_remove_manager.called is True

    @pytest.mark.parametrize("username, choice, update_user_details", [
        ("user1", "ONE", ("New Event Name", "2", "4", "300", "Sports", "2023-12-05", "Venue"),),
        ("user1", "TWO", ("Event Name", "New Date", "4", "300", "Sports", "2023-12-05", "Venue"),),
        ("user1", "THREE", ("Event Name", "2023-12-05", "New Rating", "300", "Sports", "2023-12-05", "Venue"),),
    ])
    def test_update_account(self, username, choice, update_user_details, mock_user_id):
        with patch('src.controllers.user.User.get_user_id', mock_user_id):
            with patch('src.utils.input.Input.update_account_input', return_value=update_user_details):
                mock_update_user = MagicMock(return_value=True)
                with patch('src.controllers.event.Event.update_event', mock_update_user):
                    event_helper = UserHelper()
                    event_helper.update_account(username, choice)

        assert mock_update_user.called is False
