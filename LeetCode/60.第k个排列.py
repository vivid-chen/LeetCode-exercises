'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''
def getPermutation(n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        res = ""
        s = []
        for i in range(n):
            s.append(i+1)
        # 此时s是“123...n”

        # 求阶乘函数
        def factorial(n):
            if n == 1:
                return 1
            return n*factorial(n-1)

        # 递归求头和尾
        def count(n,k,res):
            if n <= 1:
                res = str(s.pop())
                return res
            if n > 1:
                i = factorial(n-1)
                head = int(k/i)
                tar = int(k%i)
                # 这里注意特殊情况tar等于0，此时还是属于上一组，所以head-1
                if tar == 0:
                    res = str(s.pop(head-1))
                else:
                    res = str(s.pop(head))
                return res + count(n-1,tar,res)

        return count(n,k,res)


print(getPermutation(3,3))