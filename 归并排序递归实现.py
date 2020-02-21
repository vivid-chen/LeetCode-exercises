def merge(s1,s2,s):
    """将两个列表是s1，s2按顺序融合为一个列表s,s为原列表"""
    # j和i就相当于两个指向的位置，i指s1，j指s2
    i = j = 0
    while i+j<len(s):
        # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(s):
    """归并排序"""
    n = len(s)
    # 剩一个或没有直接返回，不用排序
    if n < 2:
        return
    # 拆分
    mid = n // 2 # mid = n >> 1
    s1 = s[0:mid]
    s2 = s[mid:n]
    # 子序列递归调用排序
    merge_sort(s1)
    merge_sort(s2)
    # 合并
    merge(s1,s2,s)


if __name__ == '__main__':
    s = [1,7,3,5,4]
    merge_sort(s)
    print(s)
