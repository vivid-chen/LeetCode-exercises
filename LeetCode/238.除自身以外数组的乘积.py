'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
'''


def productExceptSelf(nums: List[int]) -> List[int]:
    # 自身左边的数字乘积乘以自身右边数字乘积
    left, right = 1, 1
    result = []
    for i in range(len(nums)):
        result.append(left)
        left = left * nums[i]
    for i in range(len(nums)-1,-1,-1):
        result[i] = result[i] * right
        right = right * nums[i]
    return result