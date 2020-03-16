def MyPow(x:float,n:int)->float:
    if n == 0:
        return 1
    if n == 1:
        return x
    
    if n == -1:
        return 1/x
    
    
    # 这里用移位代替/2
    result = MyPow(x,n>>1)
    result *= result # 这里自己乘自己，为了不重复运算
    # n为奇数才运行if，相当于最后一个乘一次
    if n & 0x1 == 1:
        result *= x

    return result

print(MyPow(2,-10))