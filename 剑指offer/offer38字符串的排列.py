'''
求取字符串的全排列
方法一：深度优先 + 标记（得到的结果有重复，需要去重复）
方法二：选定第1位与其他交换，然后第二位、、、递归

扩展题：求组合
'''

'''
深度优先+标记位置得到全排列
'''
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

'''
交换位置得到全排列
'''
def Repeat(located,P):
    # 如果当前指到的前面出现过就不用考虑了
    for i in range(located,P):
        if string[i] == string[P]:
            return False
    return True

def SwapPermutation(n):
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
            string[n],string[i] = string[i],string[n]
            # 递归
            SwapPermutation(n+1)
            # 递归结束后还原
            string[n],string[i] = string[i],string[n]

'''
字符串组合
'''
def Combination(li,total,choose,temp,res): # 得到组合
    if total < 1 or choose < 1:
        return
    if total == choose and choose != 1:
        res.append(''.join(temp)+''.join(li))
        return
    if choose == 1:
        for i in range(0,total):
            res.append(''.join(temp)+li[i])
    else:
        temp.append(li[0])
        # 弹出的属于选择
        Combination(li[1:],total-1,choose-1,temp,res)

        temp.pop() # 跳出了选择递归证明最后一个元素没选，所以弹出一个元素
        # 弹出的不属于选择
        Combination(li[1:],total-1,choose,temp,res)


if __name__ == "__main__":
    # 方法1
    Permutation("1223") # 全排列回溯加标记，效率低
    
    # 方法2，将string转化为list处理，因为python中不能修改str
    # 后面如果有需要再转化为str
    string = list("1223")
    res = []
    SwapPermutation(0)
    print(len(res))

    # 扩展题：得到全部组合
    string = "abcd"
    li = [i for i in string]
    res = []
    temp = []
    total = len(li)
    for choose in range(1,total+1):
        Combination(li,total,choose,temp,res)
    print(res)



