def InsertSort(arr):
    size = len(arr)
    swap = 0
    for i in range(1,size):
        if arr[i]<arr[i-1]:
            # 放入交换位
            swap = arr[i]
            j = i-1
            while arr[j] > swap:
                arr[j+1] = arr[j]
                j -= 1
                if j < 0:break # 这里是只有两个元素前大后小的特殊处理

            arr[j+1] = swap

    return arr

print(InsertSort([9,1,5,8,3,7,4,6,2]))
