def MyPow(x:float,n:int)->float:
    if n == 0:
        return 1
    if n == 1:
        return x
    '''
    if n == -1:
        return 1/x
    '''
    
    result = MyPow(x,n>>1)
    result *= result
    if n & 0x1 == 1:
        result *= x

    return result

print(MyPow(2,3))