import re

def repeated_word(string):
    """
    method that takes a string as a parameter ,then returns the first repeated word in the string 
    """
    string = re.sub(r'[^\w\s]', '', string)
    all_the_words = {}
    first_repeated_word = ''

    
    for word in string.split():
        word = word.lower()
        try:
            all_the_words[word] += 1
            first_repeated_word = first_repeated_word or word
        except:
            all_the_words[word] = 1

    

    # check for  matching words
    if first_repeated_word:
        return [first_repeated_word]
    return ["No repeating words found"]