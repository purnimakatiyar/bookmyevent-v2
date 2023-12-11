import pytest
import sqlite3
from unittest.mock import patch, MagicMock
from src.models.database import DBConnection


@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    return DBConnection(connection)

class TestDBConnection:



    def test_get_item(self, db_connection):
        query = "SELECT * FROM Events WHERE event_name = ?"
        data = ("demo",)
        with patch.object(db_connection, '__enter__', return_value=MagicMock()):
             with patch.object(db_connection, 'close'):
                result = db_connection.get_item(query, data)
        assert result is None

    def test_get_items(self, db_connection):
        query = "SELECT * FROM Events WHERE category = ?"
        data = ('sports',)
        with patch.object(db_connection, '__enter__', return_value=MagicMock()):
            with patch.object(db_connection, 'close'):
                result = db_connection.get_items(query, data)
        assert result == []

    def test_get_all_events(self, db_connection):
        query = " "
        with patch.object(db_connection, '__enter__', return_value=MagicMock()):
            with patch.object(db_connection, 'close'):
                result = db_connection.get_all_events(query)
        assert result == []

    def test_insert_item(self, db_connection):
        query = "INSERT INTO Events (event_name, rating) VALUES (?, ?)"
        data = ('item_name', 10)
        with patch.object(db_connection, '__enter__', return_value=MagicMock()):
            with patch.object(db_connection, 'close'):
                db_connection.insert_item(query, data)


    def test_update_item(self, db_connection):
        query = "UPDATE Events SET rating = ? WHERE event_id = ?"
        data = (5, 1)
        with patch.object(db_connection, '__enter__', return_value=MagicMock()):
            with patch.object(db_connection, 'close'):
                db_connection.update_item(query, data)


    def test_delete_item(self, db_connection):
        query = "DELETE FROM Events WHERE event_id = ?"
        data = (1,)
        with patch.object(db_connection, '__enter__', return_value=MagicMock()):
            with patch.object(db_connection, 'close'):
                db_connection.delete_item(query, data)



