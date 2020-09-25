# Code Challenge - Hash Tables
## Overview 

* Implement a hash table with the methods listed under Challenge.

```
Hash Tables
-- Data Structure used to store data
-- Stores data that has key/value pairs
---- Maps key to value and returns an index
-- Hash table is a large empty array
-- Takes advantage of array O(1) to get data
---- Knowing the index

Hash Function
-- Hash function evaluates key/value and returns index
---- The same index every time for the same key
-- When adding to a hash table key is passed to hash function
---- also when getting a key from the hash table

Collisions
-- Occur when two or more key/values are mapped to the same index in the hash table
---- Common to make the index a linked list
---- Thought of like "buckets" that store reference to linked nodes with key/values
------ called chaining
```

## Challenge
Implement a Hashtable with the following methods:

- add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get: takes in the key and returns the value from the table.
- contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
- hash: takes in an arbitrary key and returns an index in the collection.

## Tests

- Adding a key/value to your hashtable results in the value being in the data structure
- Retrieving based on a key returns the value stored
- Successfully returns null for a key that does not exist in the hashtable
- Successfully handle a collision within the hashtable
- Successfully retrieve a value from a bucket within the hashtable that has a collision
- Successfully hash a key to an in-range value

## Approach & Efficiency

An array was the chosen data structure to use for the HashTable and a linked list was the chosen data structure for to use at each index of the Hash Table to handle collisions.

Adding key/value pairs and getting values from the Hash Table is essentially O(1) for time for both posting and getting. Big O is always looking for the worst case scenario. The worst case would be the length of the linked list at any given index.

## API

- add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get: takes in the key and returns the value from the table.
- contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
- hash: takes in an arbitrary key and returns an index in the collection.


## Big O notation

- time <- O(1)
- space <- O(1)

## WhiteBoard
 see it on this link : https://drive.google.com/file/d/1cFpyab2EMBxi3r702rCl1WZxX9jlqKDx/view?usp=sharing























