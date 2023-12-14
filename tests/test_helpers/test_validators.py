import pytest
from helpers.validators import (
    is_valid_username,
    check_valid_password,
    is_valid_password,
    is_valid_name,
    is_valid_phone,
    validate_event_name,
    validate_event_date,
    validate_event_rating,
    validate_event_price,
    validate_event_tickets
)

@pytest.mark.parametrize("validator_func, input_value, expected_result", [
    (is_valid_username, "purnima123", True),
    (is_valid_username, "purnima!@#", False),
    (is_valid_password, "ValidPassword1!", True),
    (is_valid_password, "invalidpassword", False),
    (is_valid_name, "Purnima Katiyar", True),
    (is_valid_name, "purni1", False),
    (is_valid_phone, "7378377899", True),
    (is_valid_phone, "0000", False),
    (validate_event_name, "Marvel", True),
    (validate_event_name, "", False),
    (validate_event_date, "2023-01-01", True),
    (validate_event_date, "InvalidDate", False),
    (validate_event_rating, 5, True),
    (validate_event_rating, 15, False),
    (validate_event_price, "100", True),
    (validate_event_price, "-50", False),
    (validate_event_tickets, "40", True),
    (validate_event_tickets, "-50", None)
])
def test_validators(validator_func, input_value, expected_result):
    assert validator_func(input_value) == expected_result
