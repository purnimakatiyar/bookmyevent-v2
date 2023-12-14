import logging
from unittest.mock import patch
from utils import logs

def test_start_app(caplog):
    logs.start_app()
    assert '' in caplog.text

def test_exit_app(caplog):
    logs.exit_app()
    assert '' in caplog.text

def test_wrong_credential(caplog):
    logs.wrong_credential()
    assert '' in caplog.text

def test_remove_event(caplog):
    event_name = "Test Event"
    logs.remove_event(event_name)
    assert f"An event named {event_name!r} has been removed" in caplog.text

def test_remove_manager(caplog):
    username = "test_manager"
    logs.remove_manager(username)
    assert f"The manager with username {username!r} has been removed" in caplog.text


