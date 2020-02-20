'''
解析
暴力
用暴力的方法，找出所有可能的子数组，然后找和最大的那个。这是可行的，但是时间复杂度为 n*n，显然是不够理想的。

动态递归
动态规划思想。状态方程：max(dp[i])= getMax(max(dp[i-1]) + arr[i], arr[i])
上面式子的意义是：我们从头开始遍历数组，遍历到数组元素arr[i]时，连续的最大的和可能为 max(dp[i-1])+arr[i]，也可能为arr[i]
做比较即可得出哪个更大，取最大值。时间复杂度为 n

非动态规划
不需要动态规划，时间复杂度也为n。我们从头开始累加数组的元素，初始值sum为0。
第一步 把1累加则sum=1,接着-2累加sum=-1，再接着3累加sum=2，但是此时我们发现sum<3
也就是说从第一个元素开始累加到第三个元素的和sum比第三个元素还要小，那么我们舍去前面的累加值，从第三个元素开始累加
此时 sum = 3。

继续上述步骤，直至遍历到数组的最后一个元素。
'''

def DynamicPlanning(array):
    size = len(array)
    max_dp = int(array[0])
    result = max_dp
    left,right,temp = 0,0,0
    for i in range(1,size):
        if int(array[i])>max_dp + int(array[i]):
            temp = i
        
        max_dp = max(max_dp + int(array[i]), int(array[i]))
        
        if max_dp > result:
            result = max_dp
            left = temp
            right = i
    return result,left,right

# 顺便改写了下打印了最大和两端的索引值
print(DynamicPlanning([1,-1]))

