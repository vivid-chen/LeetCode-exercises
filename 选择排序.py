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

print(selectionSort([5, 3, 1, 8, 10, 2]))
