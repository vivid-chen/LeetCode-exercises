'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        如果字符为零而且前面不是1和2，就不能解码；如果是1或者2就只有一种可能了，等于前前一位
        如果前面是1则此位的解码数量等于前一位的加上前前一位的
        如果前面是2但是自身处于1~6，解码数量等于前一位的加上前前一位的，否则等于前一位的
        '''
        if s[0] == '0':
            return 0
        pre,curr = 1,1 # 此时pre索引是-1
        for i in range(1,len(s)):
            tmp = curr # 暂存，后续用来更新pre
            if s[i] == '0':
                if s[i-1]=='1' or s[i-1]== '2':
                    curr = pre
                else:
                    return 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] >= '1' and s[i] <= '6'):
                curr = curr + pre
            pre = tmp
        return curr