# 找出list中最小的，输出其索引
def findSmallest(arr):
    # 初始化
    smallest = arr[0]
    smallest_index = 0

    # 遍历寻找最小数字的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    # 返回索引值
    return smallest_index

def selectionSort(arr):
    newArr = []

    # 这个for循环相当于找一次最小的之后在剩下的中再找一次最小的
    # 不断寻找，将找到的数放入新list的尾部
    # 最终得到的即是排序好的list
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        # pop用于移除列表中的一个元素，并返回该元素的元素值
        # append用于在列表最后添加一个元素值
        newArr.append(arr.pop(smallest))
    return newArr

# print(selectionSort([5, 3, 1, 8, 10, 2]))

# 按照大话数据结构里的写法
def selection_Sort(arr):
    size = len(arr)
    for i in range(0,size):
        min = i # 将i作为初始min值
        for j in range(i+1,size):
            if arr[min] > arr[j]: # 如果后面有比min小的就交换
                min = j
        if i != min: # 如果找到了更小的就交换i和min下标的元素
            arr[i],arr[min] = arr[min],arr[i]
    return arr

print(selection_Sort([9,1,5,8,3,7,4,6,2]))

