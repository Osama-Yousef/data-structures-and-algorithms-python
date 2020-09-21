import pytest
from data_structures_and_algorithms.challenges.merge_sort.merge_sort import merge_sort, merge


def test_empty_list():
    '''Test that empty list is handled correctly'''
    array = []
    merge_sort([])
    expected = []
    assert array == expected
############################################################
def test_one_item_list():
    '''Test that single list item is handled correctly'''
    array = [5]
    merge_sort(array)
    expected = [5]
    assert array == expected
#########################################################
def test_two_item_list():
    '''Test that list with two items is handled correctly'''
    array = [5,2]
    merge_sort(array)
    expected = [2,5]
    assert array == expected
##########################################################
def test_many_item_list():
    '''Test that normal list is handled correctly'''
    array = [1,5,2,-4,88]
    merge_sort(array)
    expected = [-4, 1, 2, 5, 88]
    assert array == expected