# https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/

# 要注意：left （right） 这个位置的值可能程序还没有读取到
# 因此“有可能”需要再对 left（right） 这个位置的值是否是目标元素的值做一次判断。

while left < right:
    mid  = left + (right-left)//2 # (left+right)>>1 右移1位 防溢出
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left

while left < right:
    mid = left + (right-left+1)//2
    if nums[mid] > target:
        right = mid - 1
    else:
        left = mid
return left