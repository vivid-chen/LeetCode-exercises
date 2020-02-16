'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000
示例 2:
输入: 2.10000, 3
输出: 9.26100
示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''
def myPow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:return 1
        if n == 1:return x
        if n ==-1:return 1/x
        # 这里用尾递归的写法会超出时间限制
        '''
        rest = int(n%2)
        half = int(n/2)
        return myPow(x, rest)*myPow(x, half)*myPow(x, half)
        '''
        # 老老实实不写成尾递归形式
        rest = self.myPow(x, int(n%2))
        half = self.myPow(x, int(n//2))
        return rest*half*half


print(myPow())