import pytest
from unittest.mock import patch, MagicMock
from helpers.authentication_helper import AuthenticateHelper
from settings.config import prompts

class TestAuthenticationHelper:


    @pytest.fixture
    def mock_authenticate(self):
        mock_auth = MagicMock()
        mock_auth.login.return_value = None
        with patch("controllers.authentication.Authenticate", new=mock_auth) as mock_auth_class:
            yield mock_auth_class.return_value

    @pytest.fixture
    def mock_input(self):
        with patch("utils.input.Input.login_input", return_value=("existing_user", "password")) as mock_input_class:
            yield mock_input_class.return_value

    @pytest.fixture
    def mock_check_password(self):
        with patch("utils.encrypt.check_password", return_value=True) as mock_check_password_func:
            yield mock_check_password_func

    def test_login_successful(self, mock_input, mock_check_password):
        mock_auth = MagicMock(return_value = 'hello')
        with patch("controllers.authentication.Authenticate.login", mock_auth):
            helper = AuthenticateHelper()
            helper.login()
        assert mock_auth.called is True

    def test_login_username_not_exist(self, mock_authenticate, mock_input, mock_check_password):
        mock_authenticate.login.return_value = None  # Simulate username not existing
        helper = AuthenticateHelper()
        with patch("builtins.print") as mock_print:
            result = helper.login()
            assert result is None
            mock_print.assert_called_once_with(prompts["USERNAME_NOT_EXIST"])

    def test_login_wrong_password(self, mock_authenticate, mock_input, mock_check_password):
        mock_check_password.return_value = False
        helper = AuthenticateHelper()
        with patch("builtins.print") as mock_print:
            result = helper.login()
            assert result is None
            mock_print.assert_called_once_with(prompts["USERNAME_NOT_EXIST"])

