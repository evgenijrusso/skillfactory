import pytest


@pytest.fixture
def input_value():
    _input = 39
    return _input


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0