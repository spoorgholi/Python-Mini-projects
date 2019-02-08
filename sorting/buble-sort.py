#setting the array
array = [4, 12, 2, 0, 1, 22, 33, 33, 43, 19, 21, 5, 9]

def buble_sort(array):

    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            else:
                pass
    return array

#calling the soring function
print(buble_sort(array))