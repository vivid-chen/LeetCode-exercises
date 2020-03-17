class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        
        left, right = None, head
        for i in range(0,k-1):
            if right.next:
                right = right.next
            else:
                return None
        left = head
        while right.next:
            left = left.next
            right = right.next
        return left