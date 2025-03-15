import pytest

from my_lib.calc import add, sub


@pytest.mark.parametrize(
    "value1,value2,expected", [pytest.param(1, 1, 2), pytest.param(1, 2, 3)]
)
def test_add(value1: int, value2: int, expected: int):
    assert add(value1, value2) == expected


@pytest.mark.parametrize(
    "value1,value2,expected", [pytest.param(1, 1, 0), pytest.param(3, 1, 2)]
)
def test_sub(value1: int, value2: int, expected: int):
    assert sub(value1, value2) == expected
