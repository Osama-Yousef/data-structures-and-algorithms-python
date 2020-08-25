from data_structures_and_algorithms.challenges.ll_zip.ll_zip import LinkedList ,Node
from data_structures_and_algorithms import __version__
import pytest


# def test_version():
#     assert __version__ == '0.1.0'


@pytest.fixture
def prepare_data():
    anime = LinkedList()
    node1 = anime.append("BLEACH")
    node2 = anime.append("God of high school")
    node3 = anime.append("Deat note")
    test1= anime.includes("BLEACH")
    test2= anime.includes("Conan")
    return {'anime':anime,"node1":node1,"node2":node2,"node3":node3,"test1":test1,"test2":test2}
# ________________________________________________________________

def test_empty_ll():
    """
    Can the function successfully instantiate an empty linked list?
    """
    expected =LinkedList().__str__()
    actual ='None'
    assert expected == actual

# ________________________________________________________________


def test_insert_ll():
    """
    Can properly insert into the linked list ?
    """
    anime = LinkedList()
    anime.insert("Slam Dunk")
    expected =anime.head.val
    actual ='Slam Dunk'
    assert expected == actual

# ________________________________________________________________
def test_head_ll():
    """
    will The head property point to the first node in the linked list ?
    """
    anime = LinkedList()
    anime.insert("test head")
    expected =anime.head.val
    actual ='test head'
    assert expected == actual

# ________________________________________________________________

def test_insert_multiple_nodes():
    """
    Can properly insert multiple nodes into the linked list ?
    """
    anime = LinkedList()
    anime.insert("Hunter")
    anime.insert("Slam Dunk")
    expected =anime.__str__()
    actual ='<Slam Dunk -><Hunter ->None'
    assert expected == actual

# ________________________________________________________________

def test_include_true(prepare_data):
    """
    Will return true when finding a value within the linked list that exists
    """
    expected =prepare_data['test1'].__str__()
    actual ='True'
    assert expected == actual

# ________________________________________________________________

def test_include_false(prepare_data):
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    expected =prepare_data['test2'].__str__()
    actual ='False'
    assert expected == actual

# ________________________________________________________________
def test_values_in_linked_list(prepare_data):
 
    expected =prepare_data['anime'].__str__()
    actual ='<BLEACH -><God of high school -><Deat note ->None'
    assert expected == actual

# ________________________________________________________________
def test_insertbefore():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertBefore("death note","one puch man")
    assert anime.__str__() == '<Slam dunk -><one puch man -><death note ->None'
# ________________________________________________________________
def test_insertbefore_first_node():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertBefore("Slam dunk","one puch man")
    assert anime.__str__() == '<one puch man -><Slam dunk -><death note ->None'
# ________________________________________________________________
def test_insertAfter_lastnode():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertAfter("death note","one puch man")
    assert anime.__str__() == '<Slam dunk -><death note -><one puch man ->None'
# ________________________________________________________________
def test_insertAfter():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.append("Naruto")
    anime.insertAfter("death note","one puch man")
    assert anime.__str__() == '<Slam dunk -><death note -><one puch man -><Naruto ->None'

# ________________________________________________________________



def test_kth_from_end1_Happy_Path():
    anime = LinkedList()
    anime.append(1)
    anime.append(3)
    anime.append(8)
    anime.append(2)
    assert anime.kth_from_end(3) == 1
    assert anime.kth_from_end(1) == 8

# ________________________________________________________________

def test_kth_from_end_greater_than_length():
    anime = LinkedList()
    anime.append(1)
    anime.append(3)
    anime.append(8)
    anime.append(2)
    assert anime.kth_from_end(5) =='value not found'
# ________________________________________________________________

def test_kth_from_end_same_length():
    anime = LinkedList()
    anime.append(1)
    anime.append(3)
    anime.append(8)
    anime.append(2)
    assert anime.kth_from_end(4) =='value not found'
# ________________________________________________________________

def test_kth_from_end_not_positive():
    anime = LinkedList()
    anime.append(1)
    anime.append(3)
    anime.append(8)
    assert anime.kth_from_end(-1) =='value not found'
# ________________________________________________________________

def test_kth_from_end_size1():
    anime = LinkedList()
    anime.append(3)
    assert anime.kth_from_end(0) ==3
# ________________________________________________________________
def test_zipLists1():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert llist.zipLists(llist1,llist2).__str__() =="<8 -><3 -><7 -><2 -><6 -><1 ->None"
# ________________________________________________________________
def test_zipLists2():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
    llist1.append(0) 
    llist1.append(0) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert llist.zipLists(llist1,llist2).__str__() =="<3 -><8 -><2 -><7 -><1 -><6 -><0 -><0 ->None"
# ________________________________________________________________
def test_zipLists3():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 

  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    llist2.append(5) 
    llist2.append(5)
    assert llist.zipLists(llist1,llist2).__str__() =="<8 -><3 -><7 -><2 -><6 -><1 -><5 -><5 ->None"