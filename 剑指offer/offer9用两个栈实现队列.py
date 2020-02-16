"""增加数据进入栈1"""
def AppendTail(stack1,value):
    stack1.append(value)

"""从栈2弹出数据"""
def PopHead(stack1,stack2):
    if stack2:
        return stack2.pop()
    else:
        if not stack1:
            return None
        while stack1:
            stack2.append(stack1.pop())
        return stack2.pop()
stack1 = []
stack2 = []
AppendTail(stack1,5)
a = PopHead(stack1,stack2)
print(a)
