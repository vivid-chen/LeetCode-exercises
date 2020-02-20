# 这一题需要找规律
# https://www.cnblogs.com/aimi-cn/p/11510770.html

def CountOne(num):
    if num <= 0:
        return print("para error")
    locate, count = 1, 0
    while num//locate:
        high_div,high_mod = divmod(num,locate*10) # high_div是高位数字
        low_div,low_mod = divmod(high_mod,locate) # low_div是当前位数字，low_mod是当前位后面的数字

        if low_div > 1: # 当前位大于1
            count += high_div*locate + locate
        if low_div == 1: # 当前位等于1
            count += high_div*locate + low_mod + 1
        if low_div < 1: # 当前位小于1,当前位即为0，仅考虑高位即可
            count += high_div*locate
        
        locate = locate * 10
    return count

print(CountOne(2134))




