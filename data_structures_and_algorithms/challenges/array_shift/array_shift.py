
def insertShiftArray(array,num):
    for x in range(len(array)):
        if array[x] > num:
            i = x
            break
    array = array[:x] + [num] + array[x:]
    return array

