class ListNode:
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

def DeleteNode(l1:ListNode, TobeDelete:ListNode)->ListNode:
    if l1 is None:
        return None
    if TobeDelete is None:
        return l1
    # 只有一个头结点
    if l1 == TobeDelete and l1.next is None:
        return None
    # 待删除节点是尾节点
    if TobeDelete.next is None:
        tmpNode = l1
        while tmpNode.next is not TobeDelete:
            tmpNode = tmpNode.next
        tmpNode.next = None
        del TobeDelete
    # 待删除节点在中间
    if TobeDelete.next is not None:
        tmpNode = TobeDelete.next
        TobeDelete.val = tmpNode.val
        TobeDelete.next = tmpNode.next
        del tmpNode
    
    return l1

if __name__ == '__main__':
    
    # 初始化链表
    data1 = [1, 2, 3, 4]
    l1=LinkList().initList(data1)
    LinkList().printlist(l1)
    print('\n')
    # 开始准备删除节点
    l2 = l1.next
    DeleteNode(l1,l2)
    tmp = l1
    while tmp.next:
        print(tmp.val,end='')
        tmp = tmp.next
    print(tmp.val)
    

    '''
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
    '''