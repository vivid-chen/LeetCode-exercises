# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    # 递归解法（占用内存更大)
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
            
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

    # 循环解法(最优解法)
    def Merge2(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        preNode = ListNode(-1)
        cur = preNode
        cur1 = pHead1
        cur2 = pHead2

        while (cur1 is not None and cur2 is not None):
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            
            cur = cur.next
        if cur1 is not None:
            cur.next = cur1
        else:
            cur.next = cur2
        
        return preNode.next