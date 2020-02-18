'''
长度为n的绳子，把绳子剪成m段，m，n都是整数并且都大于1
问每一段的最大乘积是多少？
'''
# 动态规划
def maxProductAfterCutting_Solution1(length:int)->int:
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length ==3:
        return 2
    
    products = [0,1,2,3]+[0]*(length-3)
    for i in range(4,length+1):
        max = 0
        for j in range(1,i//2+1):
            result = products[j] * products[i-j]
            if max < result:
                max = result
        products[i] = max

    return products[-1]

# 贪婪算法
def maxProductAfterCutting_Solution2(length:int)->int:
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length ==3:
        return 2
    
    TimesOfThree = length//3
    rest = length%3

    if rest == 1:
        TimesOfThree -= 1
        rest = 4
    return (3**TimesOfThree)*rest


print(maxProductAfterCutting_Solution1(8))
print(maxProductAfterCutting_Solution2(8))