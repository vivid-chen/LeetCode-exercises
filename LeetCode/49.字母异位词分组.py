'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
'''
# 相当于字典的键是字母排列，键值是满足键值组合条件的单词，这样思路简单，但是慢
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic={}
    for i in strs:
        a =tuple(sorted(i))
        if a not in dic:
            dic[a] = [i]
        else:
            dic[a].append(i)
    m=[i for i in dic.values()]
    return m

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))