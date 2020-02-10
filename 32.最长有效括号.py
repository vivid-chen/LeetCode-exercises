'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''


# 动态规划 栈
def longestValidParentheses(s):
    # 初始化栈
    stack = []
    # 如果只有一个字符就不用考虑了
    if len(s) < 2: return 0
    # 动态规划初始化dp
    dp = [0] * len(s)
    for i, ch in enumerate(s): # 枚举返回索引和对应的值
        if ch == ')':
            if stack and stack[-1][0] == '(':
                # index是对应左括号的索引
                _, index = stack.pop()
                # 当前右括号位置的配对数是右括号左边的配对数+对应左括号左边的配对数+2（2代表刚匹配到的左右括号）
                dp[i] = max(dp[i], dp[index - 1] + 2 + dp[i - 1]) 
        else: stack.append(('(', i)) # 如果是左括号就入栈 
    return max(dp)

print(longestValidParentheses("())()())"))
