# CHALLENGE 31: Repeated Word

## Challenge 
- Write a function that accepts a lengthy string parameter.
- Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

## Approach 
- We are using re - Python's regular expression package to substitue any punctuation with a null string. When the string is just words and spaces we can split the string using the String.split method.

- We are returned a list of all of the words and can begin keeping track of what words we have seen and when we hit that first repeated word.s

## Efficiency

- O(N) for time and O(N) for space.

## White-Board
- see it on this link : https://drive.google.com/file/d/1e4TK89diNqA22EwgwDxFV76Oqn9HW6xf/view?usp=sharing
