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