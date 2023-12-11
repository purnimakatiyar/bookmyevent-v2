import pytest
from src.utils.uuid_generator import generate_uuid

def test_generate_uuid():
    for _ in range(10):
        uuid = generate_uuid()
        assert len(uuid) == 8
        assert all(c.isalnum() for c in uuid)