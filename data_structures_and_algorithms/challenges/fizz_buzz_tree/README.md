# Code Challenge 18 : Fizz Buzz
* Conduct “FizzBuzz” on a tree while traversing through it. Change the values of each of the nodes dependent on the current node’s value.
* Write a function fizzbuzz_tree which takes a tree and returns a new tree with values fizzbuzzed.

## Challenge
* Write a function fizzbuzz_tree which takes a tree and returns a new tree with values fizzbuzzed.
* Write a function called FizzBuzzTree which takes a tree as an argument. Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

  * If the value is divisible by 3, replace the value with “Fizz”
  * If the value is divisible by 5, replace the value with “Buzz”
  * If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
  * If the value is not divisible by 3 or 5, simply turn the number into a String.

## Tests
  * test_empty_tree, return valueexception when an empty tree is given as an argument.
  * test_node_divisible_by_three, if value of each node is divisible by 3, replace the value with "Fizz".
  * test_node_divisible_by_five, if value of each node is divisible by 5, replace the value with "Buzz".
  * test_node_divisible_by_either, if value of each node is divisible by 3 or 5, replace the value with “FizzBuzz”.
  * test_node_not_divisible, if value of each node is not divisible by 3 or 5, replace by stringifying the value present

## Big O notation
* time <- O(n)
* space <- O(n)

## White Board 
* see it on this link : https://drive.google.com/file/d/1RT1cYI6z6OylPoQzyoa1PZ5AAJ_efdSI/view?usp=sharing