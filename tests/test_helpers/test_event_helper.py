import pytest
from unittest.mock import patch, MagicMock
from src.helpers.event_helper import EventHelper
from src.controllers.event import Event

@pytest.fixture
def mock_user_id():
    user_id = MagicMock(return_value="userid12345")
    return user_id

class TestEventHelper:

    @pytest.mark.parametrize('username, event_details', [
        ('user1234', ["helloguys", "event_date1", "location1", 100, "category1", 1]),
        ('demouser12', ["antman", "event_date2", "location2", 100, "category2", 1]),
    ])
    def test_add_event(self, username, event_details):
        mock_add_event_input = MagicMock(return_value=event_details)
        with patch("src.utils.input.Input.add_event_input", mock_add_event_input):
            mock_user_id = MagicMock(return_value="userid12345")
            with patch("src.controllers.user.User.get_user_id", mock_user_id):
                helper = EventHelper()
                helper.add_event(username)
            assert mock_add_event_input.called
            assert mock_user_id.called

        assert mock_user_id.call_args[1] == {}


    @pytest.mark.parametrize('username, event_name', [
        ('test_user1', "event_name1"),
        ('test_user2', "event_name2"),
    ])
    def test_remove_event_with_existing_event(self, username, event_name):
        mock_remove_event_input = MagicMock(return_value=event_name)
        with patch("src.utils.input.Input.remove_event_input", mock_remove_event_input):
            mock_user_id = MagicMock(return_value="userid12345")
            with patch("src.controllers.user.User.get_user_id", mock_user_id):
                mock_get_event_by_user = MagicMock(return_value=True)
                with patch("src.controllers.event.Event.get_event_by_user", mock_get_event_by_user):
                    mock_remove_event = MagicMock()
                    with patch("src.controllers.event.Event.remove_event", mock_remove_event):
                        event_helper = EventHelper()
                        event_helper.remove_event(username)
        assert mock_remove_event.called is True


    @pytest.mark.parametrize('username, event_name', [
        ('test_user3', "event_name3"),
        ('test_user4', "event_name4"),
    ])
    def test_remove_event_with_non_existent_event(self, username, event_name):
        mock_remove_event_input = MagicMock(return_value=event_name)
        with patch("src.utils.input.Input.remove_event_input", mock_remove_event_input):
            mock_user_id = MagicMock(return_value=username)
            with patch("src.controllers.user.User.get_user_id", mock_user_id):
                mock_get_event_by_user = MagicMock(return_value=False)
                with patch("src.controllers.event.Event.get_event_by_user", mock_get_event_by_user):
                    mock_remove_event = MagicMock()
                    with patch("src.controllers.event.Event.remove_event", mock_remove_event):
                        event_helper = EventHelper()
                        event_helper.remove_event(username)

        assert mock_remove_event.called is False



    def test_view_event_with_existing_event(self):
        mock_view_event_input = MagicMock(return_value='event_name')
        with patch("src.utils.input.Input.view_event_input", mock_view_event_input):
            mock_get_event = MagicMock(return_value=["1", "2", "name12", "2023-06-12", "delhi", "6", "500", "demo"])
            with patch("src.controllers.event.Event.get_event", mock_get_event):
                event_helper = EventHelper()
                event_helper.view_event()
        assert mock_get_event.called is True



    def test_view_event_with_non_existent_event(self):
        mock_view_event_input = MagicMock(return_value="event_name")
        with patch("src.utils.input.Input.view_event_input", mock_view_event_input):
            mock_get_event = MagicMock(return_value=None)
            with patch("src.controllers.event.Event.get_event", mock_get_event):
                event_helper = EventHelper()
                event_helper.view_event()
        assert mock_get_event.called is True


    @pytest.mark.parametrize('username', [('user1234'), ('user4566')])
    def test_list_events_with_existing_events(self, username, mock_user_id):
        with patch("src.controllers.user.User.get_user_id", mock_user_id):
            mock_list_events = MagicMock(
                return_value=[["event_name1", "event_date1", "location1", 100, "category1", 1, 2, "b", "c", "d"]])
            with patch("src.controllers.event.Event.list_events", mock_list_events):
                event_helper = EventHelper()
                event_helper.list_events(username)
        assert mock_list_events.called is True


    @pytest.mark.parametrize('username', [('user1234'), ('user4566')])
    def test_list_events_with_non_existent_events(self, username, mock_user_id):
        with patch("src.controllers.user.User.get_user_id", mock_user_id):
            mock_list_events = MagicMock(return_value=None)
            with patch("src.controllers.event.Event.list_events", mock_list_events):
                event_helper = EventHelper()
                event_helper.list_events(username)
        assert mock_list_events.called is True


    def test_list_all_events(self):
        mock_list_all_events = MagicMock(
            return_value=[["event_name1", "event_date1", "location1", 100, "category1", 1, 2, "b", "c"]])
        with patch("src.controllers.event.Event.list_all_events", mock_list_all_events):
            event_helper = EventHelper()
            event_helper.list_all_events()
        assert mock_list_all_events.called is True

    # def test_filter_event_with_existing_events(self):
    #     mock_get_event = MagicMock(return_value=[["event_name1", "event_date1", "location1", 100, "category1", 1, "a", "b", "c"]])
    #     with patch("src.utils.input.Input.filter_event_input", return_value=["filter", "new"]):
    #         with patch("src.controllers.event.Event.get_event", mock_get_event):
    #             event_helper = EventHelper()
    #             event_helper.filter_event()
    #     assert mock_get_event.called is not None

    def test_filter_event_with_no_events(self):
        mock_get_event = MagicMock(return_value=[])
        with patch("src.utils.input.Input.filter_event_input", return_value="filter"):
            with patch("src.controllers.event.Event.get_event", mock_get_event):
                event_helper = EventHelper()
                event_helper.filter_event()
        assert mock_get_event.called is False


    def test_search_event_with_existing_events(self):
        mock_search_event = MagicMock(return_value=[["event_name1", "event_date1", "location1", 100, "category1", 1, 2, "b", "c"]])

        with patch("src.utils.input.Input.search_event_input", return_value="partial_name"):
            with patch("src.controllers.event.Event.search_event", mock_search_event):
                event_helper = EventHelper()
                event_helper.search_event()

        assert mock_search_event.called is True


    def test_search_event_with_non_existent_events(self):
        mock_search_event = MagicMock(return_value=None)
        with patch("src.utils.input.Input.search_event_input", return_value="partial_name"):
            with patch("src.controllers.event.Event.search_event", mock_search_event):
                event_helper = EventHelper()
                event_helper.search_event()

        assert mock_search_event.called is True


    @pytest.mark.parametrize("username, choice, update_event_details",[
        ("user1", "ONE", ("New Event Name", "2", "4", "300", "Sports", "2023-12-05", "Venue"),),
        ("user1", "TWO", ("Event Name", "New Date", "4", "300", "Sports", "2023-12-05", "Venue"),),
        ("user1", "THREE", ("Event Name", "2023-12-05", "New Rating", "300", "Sports", "2023-12-05", "Venue"),),
        ("user1", "FOUR", ("Event Name", "2023-12-05", "4", "New Price", "Sports", "2023-12-05", "Venue"),),
        ("user1", "FIVE", ("Event Name", "2023-12-05", "4", "300", "New Category", "2023-12-05", "Venue"),),
    ])
    def test_update_event(self, username, choice, update_event_details,  mock_user_id):
        with patch('src.controllers.user.User.get_user_id', mock_user_id):
            with patch('src.utils.input.Input.update_event_input', return_value=update_event_details):
                mock_update_event = MagicMock(return_value=True)
                with patch('src.controllers.event.Event.update_event', mock_update_event):
                    event_helper = EventHelper()
                    event_helper.update_event(username, choice)

        assert mock_update_event.called is True


    @pytest.mark.parametrize('username', [('user123'), ('user790')])
    def test_view_booked_event_not_exists(self, username, mock_user_id):
        with patch("src.controllers.user.User.get_user_id", mock_user_id):
            mock_view_booked_events = MagicMock(return_value=None)
            with patch("src.controllers.booked_events.BookedEvents.view_booked_events", mock_view_booked_events):
                event_helper = EventHelper()
                event_helper.view_booked_event(username)
        assert mock_view_booked_events.called is True


    @pytest.mark.parametrize('username', [('user123'), ('user790')])
    def test_view_booked_event_exists(self, username, mock_user_id):
        with patch("src.controllers.user.User.get_user_id", mock_user_id):
            mock_view_booked_events = MagicMock(return_value=[["event_name1", "event_date1", "location1", 100, "category1", 1, 2, "b", "c"]])
            with patch("src.controllers.booked_events.BookedEvents.view_booked_events", mock_view_booked_events):
                event_helper = EventHelper()
                event_helper.view_booked_event(username)
        assert mock_view_booked_events.called is True

    def test_update_ticket(self):
        mock_event_instance = MagicMock()
        mock_event_instance.get_ticket_qty.return_value = (10,)
        mock_event_class = MagicMock(return_value=mock_event_instance)
        with patch('src.controllers.event.Event', mock_event_class):
            event_helper = EventHelper()
            event_helper.update_ticket(5, "EventName")
        assert mock_event_instance.update_ticket.called is False
