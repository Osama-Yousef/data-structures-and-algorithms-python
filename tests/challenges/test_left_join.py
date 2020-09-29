import pytest
from data_structures_and_algorithms.challenges.left_join.hash_table import HashTable
from data_structures_and_algorithms.challenges.left_join.left_join import left_join


def test_get():
    one = HashTable()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')

    assert one.get('fond') == 'enamored'

def test_contains():
    one = HashTable()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')

    assert one.contains('fond') == True

def test_left_join():
    one = HashTable()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')           

    two = HashTable()
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')

    assert left_join(one, two) == [['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse'], ['outfit', 'garb', None]]

def test_left_join_if_no_any_matching():
    one = HashTable()
    one.add('pond','enamored')        
    one.add('rath', 'anger')          
    one.add('adiligent', 'employed')    
    one.add('poutfit', 'garb')           
    one.add('hangguide', 'usher')           

    two = HashTable()
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')

    assert left_join(one, two) == [['poutfit', 'garb', None], ['hangguide', 'usher', None], ['rath', 'anger', None], ['pond', 'enamored', None], ['adiligent', 'employed', None]]
