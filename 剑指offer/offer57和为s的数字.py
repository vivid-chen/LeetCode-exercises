def SumOfTwo(array,s):
    # find Two num sum is s
    # array from low to high
    size = len(array)
    if size < 2:
        return print("para error")
    if s < array[0] + array[1] or s > array[-1] + array[-2]:
        return print("can not find")
    
    left, right = 0, size-1
    while left <= right:
        if array[left] + array[right] == s:
            return array[left],array[right]
        if array[left] + array[right] > s:
            right = right -1
        else:
            left = left + 1
    return print("can not find")

print(SumOfTwo([1,2,3,4,8,9], 11))