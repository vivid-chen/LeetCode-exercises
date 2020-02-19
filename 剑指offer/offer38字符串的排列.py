def Permutation(string):
    size = len(string)
    Flag = [True]*size
    temp = [0]*size
    res = []

    dfs(0,size,Flag,temp,res,string)
    res = list(set(res)) # 这句代码利用set去重复项
    for i in range(len(res)):
        print(res[i])
    print(len(res))


def dfs(Position,size,Flag,temp,res,string):
    # 结束条件
    if Position == size:
        res.append(''.join(temp))
        return
    else:
        for i in range(0,size):
            if Flag[i] == False:
                continue
            elif Flag[i] == True:
                temp[Position] = string[i]
                Flag[i] = False
                dfs(Position+1,size,Flag,temp,res,string)
                Flag[i] = True
    


Permutation("1223")
