import pytest
from controllers.event import Event
from unittest.mock import MagicMock


@pytest.fixture
def setup(monkeypatch):
    event_details = {
        'event_id': 'event_id',
        'user_id': 'user_id',
        'event_name': 'event_name',
        'event_date': 'event_date',
        'location': 'location',
        'rating': 'rating',
        'price': 'price',
        'category': 'category',
        'ticket_quantity': 'ticket_quantity'
    }
    return Event(**event_details)


class TestEvent:

    def test_add_event(self, setup, monkeypatch):
        mock_insert_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "insert_item", mock_insert_item)
        assert setup.add_event() is None


    def test_remove_event_not_exists(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.remove_event() is None


    def test_remove_event_exists(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.remove_event() is None


    def test_get_event_by_user(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_event_by_user() is None


    def test_get_event_not_exists(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_event() is None


    def test_get_event_exists(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_event() == []


    def test_list_all_events(self, setup, monkeypatch):
        mock_get_all_events = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_all_events", mock_get_all_events)
        assert setup.list_all_events() is None


    def test_list_events(self, setup, monkeypatch):
        mock_get_events = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_events)
        assert setup.list_events() == []


    def test_get_ticket_qty(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.get_ticket_qty() == []


    def test_book_event(self, setup, monkeypatch):
        mock_get_events = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_events)
        assert setup.book_event('booked_event_details') is True


    def test_update_ticket(self, setup, monkeypatch):
        mock_update_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "update_item", mock_update_item)
        assert setup.update_ticket('updated_ticket_qty', 'event_id') is None


    def test_filter_event(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=None)
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.filter_event('filter_type', 'filter_value') is None


    def test_filter_event_rating(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.filter_event('rating', 'filter_value') == []


    def test_filter_event_price(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.filter_event('price', 'filter_value') == []


    def test_filter_event_category(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.filter_event('category', 'filter_value') == []


    def test_filter_event_location(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.filter_event('location', 'filter_value') == []


    def test_search_event_not_exists(self, setup, monkeypatch):
        mock_get_items = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_items)
        assert setup.search_event('partial_name') == []


    def test_search_event_exists(self, setup, monkeypatch):
        mock_get_items = MagicMock(return_value=[
            ['1', 'date1', 'location1', 'rating1', 'price1', 'category1', 'quantity1', 'extra1', 'extra2']])
        monkeypatch.setattr(setup.db, "get_items", mock_get_items)
        assert setup.search_event('partial_name') == [
            ['1', 'date1', 'location1', 'rating1', 'price1', 'category1', 'quantity1', 'extra1', 'extra2']]

    # def test_update_event_name(self, setup, monkeypatch):
    #     mock_update_item = MagicMock(return_value=None)
    #     monkeypatch.setattr(setup.db, "update_item", mock_update_item)
    #     assert setup.update_event() is None

    # def test_update_event_date(self, setup, monkeypatch):
    #     mock_update_item = MagicMock(return_value=None)
    #     monkeypatch.setattr(setup.db, "update_item", mock_update_item)
    #     assert setup.update_event('2') is True

    # def test_update_event_rating(self, setup, monkeypatch):
    #     mock_update_item = MagicMock(return_value=None)
    #     monkeypatch.setattr(setup.db, "update_item", mock_update_item)
    #     assert setup.update_event('3') is True

    # def test_update_event_price(self, setup, monkeypatch):
    #     mock_update_item = MagicMock(return_value=None)
    #     monkeypatch.setattr(setup.db, "update_item", mock_update_item)
    #     assert setup.update_event('4') is True

    #     mock_update_item.assert_called_once_with(
    #         setup.queries["UPDATE_EVENT_CATEGORY"],
    #         ("new_event_category", setup.event_name, setup.user_id)
    #     )
