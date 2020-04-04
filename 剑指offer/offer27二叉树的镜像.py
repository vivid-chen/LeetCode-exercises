# 递归解法
def MirrorRecursively(pNode):
    if pNode is None:
        return
    
    if pNode.left is None and pNode.right is None:
        return

    temp = pNode.left
    pNode.left = pNode.right
    pNode.right = temp

    if pNode.left is not None:
        MirrorRecursively(pNode.left)
    if pNode.right is not None:
        MirrorRecursively(pNode.right)

# 循环解法
# 层序遍历，每一层的每一个结点交换左右子树
def MirrorRecursively2(pNode):
    if pNode is None:
        return
    if pNode.left is None and pNode.right is None:
        return
    
    # 利用层序遍历，队列交换结点，产生镜像
    from queue import Queue
    q = Queue()  # nodes that has been used to store a val, but its children has not been used.
    q.put(pNode)

    while q is not None:
        Node = q.get()
        temp = Node.left
        Node.left = Node.right
        Node.right = temp

        if Node.left is not None:
            q.put(Node.left)
        if Node.right is not None:
            q.put(Node.right)

    return pNode
