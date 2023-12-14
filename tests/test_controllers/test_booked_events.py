import pytest
from controllers.booked_events import BookedEvents
from unittest.mock import MagicMock
@pytest.fixture
def setup(monkeypatch):
    booked_event_details = {
        'booking_id': 'booking_id',
        'user_id': 'user_id',
        'event_id': 'event_id',
        'ticket_quantity': 'ticket_quantity'
    }
    return BookedEvents(**booked_event_details)

class TestBookedEvents:

    def test_view_booked_events(self, setup, monkeypatch):
        mock_get_item = MagicMock(return_value=[])
        monkeypatch.setattr(setup.db, "get_item", mock_get_item)
        assert setup.view_booked_events('user_id') == []