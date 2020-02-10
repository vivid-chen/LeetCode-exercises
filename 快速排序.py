def quicksort(array):
    if len(array) < 2:
        # if array[0] > array[1]:
        #     temp = array[1]
        #     array[1] = array[0]
        #     array[0] = temp
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        # print(less)
        greater = [i for i in array[1:] if i > pivot]
        # print(greater)
        return quicksort(less) + [pivot] + quicksort(greater)

a = [1, 7, 5, 9]
print(quicksort(a))
