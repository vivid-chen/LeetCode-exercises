# 问题一：求二叉树深度
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

# 求取树的最大深度
def TreeDepth(root:TreeNode)->int:
    if root is None:
        return 0
    left = TreeDepth(root.left)
    right = TreeDepth(root.right)

    return max(left,right)+1

# 判断二叉树是否平衡，遍历一次
def IsBalance(root:TreeNode):
    # 输入定义一个hight暂时用一下，最后不输出
    def IsBalance_Solution(root:TreeNode,hight = 0):
        if root is None:
            hight = 0
            return True,hight
        # 后序遍历
        balanced_left, left_hight = IsBalance_Solution(root.left)
        balanced_right, right_hight = IsBalance_Solution(root.right)
        # 如果左右树都平衡，再判断左右树的深度差，看当前节点是否平衡
        if balanced_left and balanced_right:
            if abs(left_hight-right_hight) <= 1:
                hight = (left_hight + 1) if left_hight > right_hight else (right_hight + 1)
                return True,hight
            else:
                return False,hight
        else:
            return False,hight
    
    result,hight = IsBalance_Solution(root,0)
    return result

# 二叉树的前序遍历（非递归）
def preorder(root:TreeNode):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
# 二叉树的中序遍历（非递归）
def inorder(root:TreeNode):
    res = []
    stack = []
    pos = root
    while pos is not None or len(stack) > 0:
        if pos is not None:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            res.append(pos.val)
            pos = pos.right
    return res


if __name__ == "__main__":
    root = tree.build_binary_tree([1,2,3,4,5,6,7])
    print(preorder(root))
    print(inorder(root))

    print(TreeDepth(root))
    print(IsBalance(root))



