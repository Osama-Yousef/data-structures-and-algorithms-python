from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList, Node
)



""" Required Tests """

# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list


def test_str():
    ll = LinkedList()
    ll.insert('osama1')
    ll.insert('osamaosama')
    assert ll.__str__() == '{ osama1 } -> { osamaosama } -> NULL'


def test_instantiate_linked_list():
    """
    Can successfully instantiate an empty linked list
    """
    ll = LinkedList()
    assert ll.head == None





def test_insert_into_list():
    """
    Can properly insert into the linked list
    """
    ll = LinkedList()
    ll.insert('osama')
    assert ll.head.value == 'osama'




def test_head_first():
    """
    The head property will properly point to the first node in the linked list
    """
    

def test_insert_multiple_nodes():
    """
    Can properly insert multiple nodes into the linked list
    """
    ll = LinkedList()
    ll.insert('osama1')
    ll.insert('osama2')
    assert ll.head.value == 'osama1'
    assert ll.head.next.value == 'osama2'

def test_found_value_true():
    """
    Will return true when finding a value within the linked list that exists
    """
    ll = LinkedList()
    ll.insert('osama1')
    ll.insert('osama2')
    assert ll.includes('osama1')

def test_found_value_false():
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    ll = LinkedList()
    ll.insert('osama1')
    ll.insert('osama2')
    assert ll.includes('osama3') == False

def test_return_all_nodes():
    """
    Can properly return a collection of all the values that exist in the linked list
    """
    ll = LinkedList()
    ll.insert('osama1')
    ll.insert('osamaosama')
    assert ll.__str__() == '{ osama1 } -> { osamaosama } -> NULL'