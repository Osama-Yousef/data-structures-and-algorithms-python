from data_structures_and_algorithms.data_structures.linked_list_insertions.linked_list_insertions import (
    LinkedList, Node 
)



""" Required Tests """

# Can successfully add a node to the end of the linked list
# Can successfully add multiple nodes to the end of a linked list
# Can successfully insert a node before a node located i the middle of a linked list
# Can successfully insert a node before the first node of a linked list
# Can successfully insert after a node in the middle of the linked list
# Can successfully insert a node after the last node of the linked list



def test_str():
    ll = LinkedList()
    ll.insert('blahblah')
    ll.insert('blah1')
    assert ll.__str__() == '{ blah1 } -> { blahblah } -> NULL'

def test_insert_first():
    """
    Can properly insert into the linked list
    """
    ll = LinkedList()
    ll.insert('blah')
    assert ll.head.data == 'blah'


def test_instantiate_linked_list():
    """
    Can successfully instantiate an empty linked list
    """
    ll = LinkedList()
    assert ll.head == None

def test_insert_multiple_nodes():
    """
    Can properly insert multiple nodes into the linked list
    """
    ll = LinkedList()
    ll.insert('blah2')
    ll.insert('blah1')
    assert ll.head.data == 'blah1'
    assert ll.head.next.data == 'blah2'

def test_found_value_true():
    """
    Will return true when finding a value within the linked list that exists
    """
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blah2')
    assert ll.includes('blah1')

def test_found_value_false():
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blah2')
    assert ll.includes('blah3') == False

def test_return_all_nodes():
    """
    Can properly return a collection of all the values that exist in the linked list
    """
    ll = LinkedList()
    ll.insert('blahblah')
    ll.insert('blah1')
    assert ll.__str__() == '{ blah1 } -> { blahblah } -> NULL'

def test_append():
    """
    Can successfully add a node to the end of the linked list
    """
    ll = LinkedList()
    ll.append('blah')
    assert ll.head.data == 'blah'

def test_add_multiple_append():
    """
    Can successfully add multiple nodes to the end of a linked list
    """
    ll = LinkedList()
    ll.append('blah')
    ll.append('blah2')
    assert ll.head.data == 'blah'
    assert ll.head.next.data == 'blah2'

def test_insert_before_middle():
    """
    Can successfully insert a node before a node located in the middle of a linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.insert_before('blah2', 33)
    assert ll.head.next.data == 33
    
def test_insert_before_first_node():
    """
    Can successfully insert a node before the first node of a linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.insert_before('blah1', 22)
    assert ll.head.data == 22

def test_insert_after_after_middle():
    """
    Can successfully insert after a node in the middle of the linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.insert_after('blah2', 33)
    assert ll.head.next.next.data == 33   

def test_insert_after_last():
    """
    Can successfully insert a node after the last node of the linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.insert_after('blah3', 33)
    assert ll.head.next.next.next.data == 33
