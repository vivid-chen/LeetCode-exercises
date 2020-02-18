class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    # 尝试直接初始化链表
    l1 = ListNode(1)
    head = l1
    for i in range(2,10):
        l1.next = ListNode(i)
        l1 = l1.next

    # 打印看看
    tmp = head
    while tmp.next:
        print(tmp.val, end=' ')
        tmp = tmp.next
    print(tmp.val)
