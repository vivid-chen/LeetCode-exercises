input = "HG[3|B[2|CA]]F"
s = input.strip()
stack = []

for i in s:
    if i == ']':
        temp = []
        while 1:
            letter = stack.pop()
            if letter == '[':
                break
            else:
                temp.append(letter)
        count, strs = "".join(temp[::-1]).split('|')
        for j in int(count)*strs:
            stack.append(j)
    else:
        stack.append(i)
print("".join(stack))


# 字符串去重复
input = "12ere2"

temp = ""
for i in input:
    if i not in temp:
        temp += i
print(temp)