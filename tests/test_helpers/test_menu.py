import pytest
from unittest.mock import patch
from helpers.menu import Menu
from helpers.authentication_helper import AuthenticateHelper
from helpers.user_helper import UserHelper
from helpers.event_helper import EventHelper

@pytest.fixture
def setup(monkeypatch):
    return Menu()

class TestMenu:

    @pytest.mark.parametrize("user_input", ["1", "2", "3"])
    def test_start_view(self, setup, monkeypatch, user_input):
        choice = iter(user_input)
        constants = {"ONE": "1", "TWO": "2", "THREE": "3", "CUSTOMER": "Customer"}
        prompts = {"WRONG_INPUT": "\nWrong Input", "WRONG_CREDENTIALS": "\nWrong Credentials! User doesn't exist."}

        menu = {"START_VIEW": "-------Welcome to Book My Event application-------\n1.Login \n2.Signup \n3.Exit"}
        monkeypatch.setattr("helpers.menu.constants", constants)
        monkeypatch.setattr("helpers.menu.prompts", prompts)
        monkeypatch.setattr("helpers.menu.menu", menu)
        monkeypatch.setattr("builtins.input", lambda : next(choice, "3"))
        monkeypatch.setattr(AuthenticateHelper, "login", lambda *args, **kwargs: None)
        monkeypatch.setattr(UserHelper, "signup", lambda *args, **kwargs: None)
        result = setup.start_view()
        assert result is None

    @pytest.mark.parametrize("user_input", ["1", "2", "3", "4", "5"])
    def test_admin_menu(self, setup, monkeypatch, user_input):
        choice = iter(user_input)
        constants = {"ONE": "1", "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5", "MANAGER": "Manager"}
        prompts = {"WRONG_INPUT": "\nWrong Input", "DELETE_MANAGER": "\nEnter the username of the manager you want to delete: ", "USERNAME": "\nEnter username of your choice: "}
        menu = {"ADMIN_MENU": "Enter your choice: 1. To add Manager 2. To remove Manager 3. To update Account 4. To login as customer 5. Exit"}
        monkeypatch.setattr("helpers.menu.constants", constants)
        monkeypatch.setattr("helpers.menu.prompts", prompts)
        monkeypatch.setattr("helpers.menu.menu", menu)
        monkeypatch.setattr("builtins.input", lambda : next(choice, "5"))
        monkeypatch.setattr(Menu, "update_account_menu", lambda *args, **kwargs: None)
        monkeypatch.setattr(Menu, "customer_menu", lambda *args, **kwargs: None)
        monkeypatch.setattr(UserHelper, "signup", lambda *args, **kwargs: None)
        monkeypatch.setattr(UserHelper, "remove_manager", lambda *args, **kwargs: None)
        result = setup.admin_menu('username')
        assert result is None



    @pytest.mark.parametrize("user_input", ["1", "2", "3", "4", "5", "6"])
    def test_manager_menu(self, setup, monkeypatch, user_input):
        choice = iter(user_input)
        constants = {"ONE": "1", "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5", "SIX": "6"}
        prompts = {"WRONG_INPUT": "\nWrong Input"}
        menu = {
            "MANAGER_MENU": "\nEnter your choice: \n1. To add Event \n2. To remove Event \n3. List Events \n4. To update Event \n5. To update Account \n6. Exit"}
        monkeypatch.setattr("helpers.menu.constants", constants)
        monkeypatch.setattr("helpers.menu.prompts", prompts)
        monkeypatch.setattr("helpers.menu.menu", menu)
        monkeypatch.setattr("builtins.input", lambda : next(choice, "6"))
        monkeypatch.setattr(Menu, "update_event_menu", lambda *args, **kwargs: None)
        monkeypatch.setattr(Menu, "update_account_menu", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "add_event", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "remove_event", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "list_events", lambda *args, **kwargs: None)
        result = setup.manager_menu('username')
        assert result is None

    @pytest.mark.parametrize("user_input", ["1", "2", "3", "4", "5", "6", "7", "8"])
    def test_customer_menu(self, setup, monkeypatch, user_input):
        choice = iter(user_input)
        constants = {"ONE": "1", "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5", "SIX": "6", "SEVEN": "7", "EIGHT": "8"}
        prompts = {"WRONG_INPUT": "\nWrong Input"}
        menu = {
            "CUSTOMER_MENU": "\nEnter your choice: \n1. To add Event \n2. To remove Event \n3. List Events \n4. To update Event \n5. To update Account \n6. Exit"}
        monkeypatch.setattr("helpers.menu.constants", constants)
        monkeypatch.setattr("helpers.menu.prompts", prompts)
        monkeypatch.setattr("helpers.menu.menu", menu)
        monkeypatch.setattr("builtins.input", lambda : next(choice, "8"))
        monkeypatch.setattr(EventHelper, "view_booked_event", lambda *args, **kwargs: None)
        monkeypatch.setattr(Menu, "update_account_menu", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "list_all_events", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "view_event", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "book_event", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "filter_event", lambda *args, **kwargs: None)
        monkeypatch.setattr(EventHelper, "search_event", lambda *args, **kwargs: None)
        result = setup.customer_menu('username')
        assert result is None
