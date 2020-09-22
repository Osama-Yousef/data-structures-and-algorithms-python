# Blog for Code Challenge 28 - Quick Sort

## Description

Quick sort is similar to merge sort, in that it's a conquer and divide style sorting algorythm. It chooses a pivot value and partitions the input array into a left and right array. The main difference  between merge sort and quick sort is that by the time quick sort has broken up the array into sub arrays of single elements the array is sorted.

### Pseudocode

```pseudocode
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

### Python3 Implementation

```python3
def quick_sort(arr, left_idx=None, right_idx=None):
    '''Partition the array by setting the position of the pivot value '''
    if left_idx == None and right_idx == None:
        left_idx = 0
        right_idx = len(arr) - 1
    if left_idx < right_idx:
        position = partition(arr, left_idx, right_idx)
        # sort the furthest index to the left
        quick_sort(arr, left_idx, position - 1)
        # Sort the furthest index to the right
        quick_sort(arr, position + 1, right_idx)

def partition(arr, left_idx, right_idx):
    '''The point of a pivot value is to select a value, 
    find out where it belongs in the array while moving everything lower than that value
    to the left, and everything higher to the right.'''
    # set a pivot value as a point of reference
    pivot = arr[right_idx]
    # create a variable to track the largest index of numbers lower
    # than the defined pivot
    low_idx = left_idx - 1
    for current_idx in range(left_idx, right_idx):
        if arr[current_idx] <= pivot:
            low_idx += 1
            swap(arr, current_idx, low_idx)

    swap(arr, right_idx, low_idx + 1)

    return low_idx + 1

def swap(arr, current_idx, low_idx):
    '''Helper function used to shove values lower 
    than pivot value over to the left'''
    temp = arr[current_idx]
    arr[current_idx] = arr[low_idx]
    arr[low_idx] = temp
```

## Trace

`arr = [1, 8, 3, 9, 4, 5, 7]`

Indexes:  0   1   2   3   4   5   6 

low = 0,   
high =  6,  
pivot = arr[h] = 7   
###i = -1 

Traverse from `j = low` to `high-1`    
j = 0 : Since `arr[j] <= pivot`, do i++ and swap(arr[i], arr[j])
i = 0 

`arr = [1, 8, 3, 9, 4, 5, 7]`
i and j are the same so no change  

j = 1 : Since `arr[j] > pivot`, do nothing  
No change in i and arr[]

j = 2 : Since `arr[j] <= pivot`, iterate i and swap(arr[i], arr[j])  
i = 1  
`arr = [1, 3, 8, 9, 4, 5, 7]`  We swap 8 and 3

j = 3 : Since `arr[j] > pivot`, do nothing  
No change in i and arr[]

j = 4 : Since `arr[j] <= pivot`, iterate i and swap(arr[i], arr[j])  
i = 2  

`arr = [1, 3, 4, 9, 8, 5, 7]` 8 and 4 swapped
j = 5 : Since `arr[j] <= pivot`, iterate and swap arr[i] with arr[j] 
i = 3   
`arr = [1, 3, 4, 5, 8, 9, 7]` 9 and 5 Swapped 

`j == high-1`, breaking the loop  
Finally we place pivot at correct position by swapping  
arr[i+1] and arr[high] (or pivot) 

`arr = [1, 3, 4, 5, 7, 9, 8]` 8 and 7 Swapped 

