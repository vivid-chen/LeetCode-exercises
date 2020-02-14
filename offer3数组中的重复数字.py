def FindSameNum(arr):
    '''
    # 哈希表,时间复杂度O(n),空间复杂度O(n)
    if len(arr)<=1: # 异常条件判断
        return False
    for i in range(0,len(arr)):
        if arr[i]<0 or arr[i]>len(arr)-1:
            return False
    hashmap = {}
    res = [] # 为了找全部的重复数字设置的存储变量
    for i in range(0,len(arr)):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = i
        else:
            # return arr[i]
            res.append(arr[i])
    return res
    '''
    # 时间复杂度O(n)空间复杂度O(1)的方法
    if len(arr)<=1: # 异常条件判断
        return False
    for i in range(0,len(arr)):
        if arr[i]<0 or arr[i]>len(arr)-1:
            return False
    res = []
    for i in range(0,len(arr)):
        while arr[i] != i:
            if arr[i] == arr[arr[i]]:
                # return arr[i]
                res.append(arr[i])
                break
            # 交换
            temp = arr[i]
            arr[i] = arr[temp]
            arr[temp] = temp
    if res == []:
        return False
    else:
        return res


print(FindSameNum([2,3,1,0,2,5,3]))