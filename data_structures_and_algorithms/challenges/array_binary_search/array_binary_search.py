

def binary_search(alist, key):
    if len(alist) > 0:
        mid = len(alist) // 2

        if alist[mid] == key:
            return mid

        if key < alist[mid]:
            return binary_search(alist[:mid], key)

        if key > alist[mid]:
            return binary_search(alist[mid + 1:], key)

    else:
        return -1






