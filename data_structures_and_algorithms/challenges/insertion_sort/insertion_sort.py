def insertion_sort(array):
    for index in range(len(array)):
        position = index - 1
        temp = array[index]

        while position >= 0 and temp < array[position]:
            array[position + 1] = array[position]
            position -= 1

        array[position + 1] = temp
        print(array)
    return array

arr = [20,18,12,8,5,-2]

insertion_sort(arr)