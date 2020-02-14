# 加了Flag优化的冒泡排序
def BubbleSort(arr):
    size = len(arr)
    Flag = True
    for i in range(0,size-1):
        # 设置Flag用于遍历发现已经排序好的时候跳出
        if Flag == False:
            break
        Flag = False
        # 开始冒泡，前后判断，小的放前面
        for j in range(size-1,i,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                Flag = True
    return arr

print(BubbleSort([9,1,5,8,3,7,4,6,2]))

