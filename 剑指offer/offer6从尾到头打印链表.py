# 定义链表类
class ListNode:
    """链表类"""
    def __init__(self,x):
        self.val = x
        self.next = None
# 链表初始化函数
class LinkList:
    def __init__(self):
        self.head=None

    def initList(self, data):
        """创建头结点"""
        self.head = ListNode(data[0])
        r=self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def printlist(self,head):
        if head == None: return
        node = head
        while node != None:
            print(node.val,end='')
            node = node.next

def PrintListReversingly(head:ListNode):
    s = []
    node = head
    while node != None:
        s.append(node.val)
        node = node.next
    while s:
        print(s.pop(),end='')

if __name__ == '__main__':
    data1 = [1, 2, 3]
    l1=LinkList().initList(data1)
    LinkList().printlist(l1)
    print('\n')
    PrintListReversingly(l1)



