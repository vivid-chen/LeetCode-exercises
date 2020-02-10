'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 如果字符串s为空，返回0
        if not s:return 0
        # 保存窗口内字符串
        lookup = list()
        n = len(s)
        # 最大子串长度
        max_len = 0
        # 当前窗口长度
        cur_len = 0
        # 遍历字符串s
        for i in range(n):
            val = s[i]
            # 如果该值不在窗口中
            if not val in lookup:
                # 添加到窗口内
                lookup.append(val)
                # 当前长度+1
                cur_len+=1
            # 如果该值在窗口中已存在
            else:
                # 获取其在窗口中的位置
                index = lookup.index(val)
                # 移除该位置及之前的字符，相当于上图中的图3到图4
                lookup = lookup[index+1:]
                lookup.append(val)
                # 当前长度更新为窗口长度
                cur_len = len(lookup)
            # 如果当前长度大于最大长度，更新最大长度值
            if cur_len > max_len:max_len = cur_len
        # 返回最大子串长度
        return max_len


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 如果是空字符串，返回0;一个字符，返回1
        if not s:
            return 0

        # 滑动窗口，左边为i，右边为j
        lookup = list()
        j = 0
        # 最大子串长度
        max_len = 0
        # 当前窗口长度
        lookup_len = 0

        while j < len(s):
            # 如果窗口中没有正在放入的字符
            if not s[j] in lookup:
                lookup.append(s[j])
                lookup_len = len(lookup)
            else:
                lookup = lookup[lookup.index(s[j])+1:]
                lookup.append(s[j])
                lookup_len = len(lookup)

            j = j + 1
            if max_len < lookup_len:
                max_len = lookup_len

        return max_len


            
