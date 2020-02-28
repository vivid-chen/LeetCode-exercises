
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

def levelOrder(root: TreeNode):
        res = []
        if not root:
            return res
        
        from collections import deque
        flat = deque()
        num_now = 1
        num_next = 0
        flat.append(root)
        temp = []
        a = len(flat)

        while flat:
            node = flat.popleft()
            num_now = num_now - 1 
            temp.append(node.val)
            if node.left:
                flat.append(node.left)
                num_next = num_next + 1
            if node.right:
                flat.append(node.right)
                num_next = num_next + 1
            if num_now == 0:
                num_now = num_next
                num_next = 0
                res.append(temp)
                temp = []
        return res


if __name__ == "__main__":
    root = tree.build_binary_tree([3,9,20,None,None,15,7])
    print(levelOrder(root))