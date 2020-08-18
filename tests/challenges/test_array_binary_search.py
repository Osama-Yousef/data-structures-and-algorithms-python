
from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import (
    binary_search)

# here's a test to get you started
def test_one():
    actual = binary_search([10, 20, 30, 40], 20)
    expected = 1
    assert actual == expected


def test_two():
    actual = binary_search([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

