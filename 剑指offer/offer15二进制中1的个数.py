'''
一个数-1与自己求与运算
结果赋值给原数字
能进行多少次就是几个1
（没考虑负数）
'''

def CountOne(n:int)->int:
    count = 0
    while n:
        count += 1
        n = n & (n-1)

    return count