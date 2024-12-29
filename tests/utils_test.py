import pytest
from utils import get_percentage_increment, format_number


def test_get_percentage_increment():
    base_price = 100000
    percentage = 5.0
    incremented_price, increment = get_percentage_increment(base_price, percentage)
    assert incremented_price == 105000
    assert increment == 5000


def test_format_number():
    assert format_number(123456.789) == "123 456,79"