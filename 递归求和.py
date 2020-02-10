# 递归求和
def sum(list):
    # 这里设置递归退出条件
    if len(list)==1:
        return list[0]

    x = list.pop(0)
    return x + sum(list)

list = [1, 11, 3]
# print(sum(list))

# 递归求元素数
def count(list):
    # 设置递归退出条件
    if len(list)==1:
        return 1
    list.pop(0)
    return 1+count(list)

# print(count(list))

# 递归找最大数
def Find_Max(list):
    # 设置退出条件
    if len(list) == 1:
        return list[0]
    else:
        if list[0] > list[1]:
            list.pop(1)
        else:
            list.pop(0)
        return Find_Max(list)

    
print(Find_Max(list))