def FindNum(nums,target):
    if len(nums) < 1:
        return False
    column = len(nums[0]) - 1
    row = 0

    while row < len(nums) and column > 0:
        # print(nums[row][column])
        if nums[row][column] == target:
            return True
        elif nums[row][column] > target:
            column -= 1
        else:
            row += 1
    return False
'''
nums = [[1, 2, 8, 9],
        [2, 4, 9,12],
        [4, 7,10,13],
        [6, 8,11,15]]
'''
nums = []
target = 7
print(FindNum(nums,target))