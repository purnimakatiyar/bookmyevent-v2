import json


def test_load_config_data():
    with open("C:/Users/pkatiyar/OneDrive - WatchGuard Technologies Inc/Desktop/Myyyy proj/src/config.json", "r") as file:
        get_data = json.load(file)

    assert get_data["queries"] is not None
    assert get_data["menu"] is not None
    assert get_data["prompts"] is not None
    assert get_data["constants"] is not None