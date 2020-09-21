# Blog for Code Challenge 27 - Merge Sort

## Description

Merge sort is a divide and conquer sorting algorithm. It recursiveley splits each portion of the origin array until it's comparing only two arrays with a single element each. It then merges the sorted subarrays back together.

### Pseudocode

```pseudocode
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

### Python3 Implementation

```python3
def merge_sort(arr):
    '''Takes in a list and sorts list in place'''
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

def merge(left, right, arr):
    '''
    Functions as helper function for merge_sort(), doing the actual
    sorting.
    '''
    left_idx, right_idx, arr_idx = 0, 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            arr[arr_idx] = left[left_idx]
            left_idx += 1
        else:
            arr[arr_idx] = right[right_idx]
            right_idx += 1

        arr_idx += 1

    if left_idx == len(left):
        for item in right[right_idx:]:
            arr[arr_idx] = item
            arr_idx += 1
    else:
        for item in left[left_idx:]:
            arr[arr_idx] = item
            arr_idx += 1
```

## Trace


ints: `[5, 2, 32, 4, 17, 1, 18, 12]` 


Split `ints` into 2 halves: L and R  

`L [5, 2, 32, 4]`   
`R [17, 1, 18, 12]`


Call mergesort on L, which will continue to split the lists in half until only 1 element remains                                                                                                                                                                                                                                        
  `[5, 2, 32, 4]`  
  `[5, 2,]`  
  `[5], [2]`  

Once the left most pair has been split, stitch back together in order.
  `[5], [2]` becomes `[2, 5]`

Now the same process repeats for the right half of L, not to be confused with R
`[32, 4]`
`[32], [4]` becomes `[4, 32]`

Stitch L backtogether in order
  `[2, 4, 5, 32]`

Repeat the entire process for R `[17, 1, 18, 12]`  

`[17, 1, 18, 12]`  

`[17, 1] `  

`[17], [1]` becomes `[1, 17]`  

`[18, 12]`  
`[18], [12]` becomes `[12, 18]`

Merge R back together in order
  `[1, 12, 17, 18]`

Merge L `[2, 4, 5, 32]` and R `[1, 12, 17, 18]` to get  
 `[1, 2, 4, 5, 12, 17, 18, 32]`

