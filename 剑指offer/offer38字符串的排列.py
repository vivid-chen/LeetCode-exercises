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


def Repeat(located,P):
    global string
    # 如果当前指到的前面出现过就不用考虑了
    for i in range(located,P):
        if string[i] == string[P]:
            return False
    return True

def SwapPermutation(n):
    global string
    size = len(string)
    if size <= 0:
        return print("Para Error")
    if n == size:
        print(string)
        res.append(string)
        return
    
    for i in range(n,size):
        if Repeat(n,i):
            # 交换
            temp = string[n]
            string[n] = string[i]
            string[i] = temp
            # 递归
            SwapPermutation(n+1)
            # 递归结束后还原
            temp = string[n]
            string[n] = string[i]
            string[i] = temp



if __name__ == "__main__":
    Permutation("1223") # 全排列回溯加标记，效率低
    
    # 方法2，将string转化为list处理，因为python中不能修改str
    # 后面如果有需要再转化为str
    string = list("1223")
    res = []
    SwapPermutation(0)
    print(len(res))


