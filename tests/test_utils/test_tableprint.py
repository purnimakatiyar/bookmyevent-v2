from utils.tableprint import list_event_table, booked_event_table


def test_list_event_table(capsys):
    events = [['2', '1', '3', 'date1', 'location1', 'rating1', 'price1', 'category1', 'quantity1'],
              ['2', '3', '4', 'date2', 'location2', 'rating2', 'price2', 'category2', 'quantity2']]
    list_event_table(events)
    captured = capsys.readouterr()
    assert 'EVENT_NAME' in captured.out


def test_booked_event_table(capsys):
    booked_events = [['5', '2', '3', '1', 'date1', 'quantity1'],
                     ['5', '4', '3', '2', 'date2', 'quantity2']]
    booked_event_table(booked_events)
    captured = capsys.readouterr()
    assert 'EVENT' in captured.out
