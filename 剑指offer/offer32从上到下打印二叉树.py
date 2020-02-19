class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val) # print一个TreeNode类会返回val
    
class tree:
    def build_binary_tree(vals):
        """
        return the TreeNode root
        :param vals:List
        :return:tree
        """
        from queue import Queue

        root = TreeNode(vals[0])
        q = Queue()  # nodes that has been used to store a val, but its children has not been used.
        q.put(root)

        if len(vals) % 2 == 0: # 防止每次取2个数出现越界
            vals += [None]
        for val_index in range(1, len(vals), 2):  # 每次两个值添加到一个已经赋值的结点的左右结点中
            node = q.get()
            if vals[val_index] is not None:
                node.left = TreeNode(vals[val_index])
                q.put(node.left)
            if vals[val_index + 1] is not None:
                node.right = TreeNode(vals[val_index + 1])
                q.put(node.right)
        return root

# 干脆打印一下看看树
def PrintTreeFromTopToDown(root):
    from queue import Queue
    if root is None:
        return print("This Tree is Empty!")
    q = Queue()
    q.put(root)
    nextLevel = 0
    toBePrinted = 1
    while not q.empty():
        Node = q.get()
        print(Node.val,end=' ')

        if Node.left is not None:
            q.put(Node.left)
            nextLevel += 1
        if Node.right is not None:
            q.put(Node.right)
            nextLevel += 1
        
        toBePrinted -= 1
        if toBePrinted == 0:
            toBePrinted = nextLevel
            nextLevel = 0
            print('\n')

root = tree.build_binary_tree([8,6,10,5,7,9,11])
PrintTreeFromTopToDown(root)