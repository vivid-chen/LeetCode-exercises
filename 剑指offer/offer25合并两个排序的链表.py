# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头结点为空的情况
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 此时l1和l2谁小返回谁，其next用递归求解
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        elif l2.val < l1.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2