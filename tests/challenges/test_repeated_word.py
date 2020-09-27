import pytest
from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeated_word

# repeated_word returns a list && the index of 0 = the first_repeated_word

def test_short_string():
    string = "Once upon a time, there was a brave princess who.."
    lst = repeated_word(string)
    assert lst[0] == 'a'

def test_no_repeats():
    string = "The sky is looking beautiful today"
    lst = repeated_word(string)
    assert lst[0] == 'No repeating words found'

def test_for_capitalize_words():
    string = "Osama coding osama coding"
    lst = repeated_word(string)
    assert lst[0] == 'osama'

def test_for_long_string():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."	
    lst = repeated_word(string)
    assert lst[0] == 'it'

def test_when_punctuation():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    lst = repeated_word(string)
    assert lst[0] == 'summer'

