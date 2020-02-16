def FindMinNum(nums:list)->int:
    size = len(nums)
    if size <= 0:
        print("Parament Error")
        return None
    left, right, mid= 0, size-1, 0
    while nums[left] >= nums[right]:
        if right - left == 1:
            mid = right
            break
        mid = (right+left)//2
        # 如果左右和中间相等，无从判断最小在左边还是在右边，遍历查找最小
        if nums[left] == nums[mid] and nums[mid] == nums[right]:
            for i in range(0,size):
                if nums[i] < nums[left]:
                    left = i
            mid = left
            break
        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid
    return nums[mid]

print(FindMinNum([1]))