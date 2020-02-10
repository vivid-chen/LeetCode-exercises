'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 建立字典用来匹配对应括号
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        # 不符合条件的定义为？ 这里巧妙地用来异常检测
        stack = ['?']
        for c in s:
            # 遍历，遇到左括号入栈
            if c in dic: stack.append(c)
            # 遇到非左括号，弹出一个左括号，用字典转换成对应的右括号
            # 然后进行比较，如果不相等就返回False
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1