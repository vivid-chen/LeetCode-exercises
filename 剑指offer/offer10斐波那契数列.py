def Fibonacci(n):
    result = [0,1]
    if n < 2:
        return result[n]
    NumOne = 0
    NumTwo = 1
    i = 2
    while i<= n:
        NumThree = NumOne + NumTwo

        NumOne = NumTwo
        NumTwo = NumThree
        i += 1
    return NumThree 
for i in range(1,10):
    print(Fibonacci(i),end = ' ')