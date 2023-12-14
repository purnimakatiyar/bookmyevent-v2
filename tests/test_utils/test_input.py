import pytest
from utils.input import Input


@pytest.fixture
def instance():
    return Input()

class TestInput:

    def test_login_input(self,instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'user123')  # Mock username
        monkeypatch.setattr('maskpass.advpass', lambda: 'password123')  # Mock masked password input
        result = instance.login_input()
        assert result == ('user123', 'password123')

    def test_get_valid_input(self, instance, monkeypatch):
        validation_sequence = [False, True]
        def mock_validation_function(value):
            return validation_sequence.pop(0)
        input_values = ["invalid_value", "valid_value"]
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        result = instance.get_valid_input("Enter something: ", mock_validation_function)
        assert result == "valid_value"


    def test_add_event_input(self,instance, monkeypatch):
        expected_inputs = ["EventName", "2023-12-05", "EventLocation", "300", "Sports", "100"]
        def mock_input(prompt):
            print(prompt, end="")
            return expected_inputs.pop(0)
        monkeypatch.setattr('builtins.input', mock_input)
        result = instance.add_event_input()
        expected_result = ("EventName", "2023-12-05", "EventLocation", "300", "Sports", "100")
        assert result == expected_result


    def test_filter_event_input(self,instance, monkeypatch):
        expected_inputs = ["rating", "5"]
        def mock_input(prompt):
            print(prompt, end="")
            return expected_inputs.pop(0)
        monkeypatch.setattr('builtins.input', mock_input)
        result = instance.filter_event_input()
        expected_result = ("rating", "5")
        assert result == expected_result


    def test_remove_event_valid_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'Avengers')
        result = instance.remove_event_input()
        assert result == 'Avengers'

    def test_remove_event_empty_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '')
        result = instance.remove_event_input()
        assert result == ''

    def test_remove_event_whitespace_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '    ')
        result = instance.remove_event_input()
        assert result == '    '


    def test_view_event_valid_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'Avengers')
        result = instance.view_event_input()
        assert result == 'Avengers'

    def test_view_event_empty_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '')
        result = instance.view_event_input()
        assert result == ''

    def test_view_event_whitespace_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '    ')
        result = instance.view_event_input()
        assert result == '    '

    def test_search_event_valid_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'Avengers')
        result = instance.search_event_input()
        assert result == 'Avengers'

    def test_search_event_empty_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '')
        result = instance.search_event_input()
        assert result == ''

    def test_search_event_whitespace_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '    ')
        result = instance.search_event_input()
        assert result == '    '

    def test_book_event_valid_input(self, instance, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4')
        result = instance.book_event_input()
        assert result == (('4',), 4)