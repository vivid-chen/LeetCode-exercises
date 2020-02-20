# 投机取巧的方法
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

'''
a = [1, 7, 5, 9]
print(quicksort(a))
'''

# 正经方法
def Partition(array, length, start, end):
    import random
    if array is None or length <= 0 or start < 0 or end >= length:
        return print("para Error")
    index = random.randint(start,end)
    array[index], array[end] = array[end], array[index]
    small = start -1
    for i in range(start,end):
        if array[i] < array[end]:
            small += 1
            if small != i:
                array[i], array[small] = array[small], array[i]
    small += 1
    array[small],array[end] = array[end], array[small]

    return small

def QuickSort(array,length,start,end):
    index = Partition(array,length,start,end)
    if index > start:
        QuickSort(array,length,start,index-1)
    if index < end:
        QuickSort(array,length,index+1,end)

if __name__ == "__main__":
    array = [9,8,7,6,5,4,3,2,1]
    size = len(array)
    start = 0
    end = size - 1
    QuickSort(array,size,start,end)
    print(array)
