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