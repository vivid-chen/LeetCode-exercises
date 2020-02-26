class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
def PrintTree(root:TreeNode)->list:
    res = []
    def PrintToList(root:TreeNode):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        if root.left is None and root.right is not None:
            res.append(None)
            res.append(root.right)
        if root.left is not None and root.right is None:
            res.append(root.left)
        else:
            res.append(root.left)
            res.append(root.right)
        PrintToList(root.left)
        PrintToList(root.right)
    res.append(root.val)
    PrintToList(root)
    return res
'''
def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    # 如果 为空树
    if not n:
       return []

    def new_trees(start,end):
        if start > end:
            return [None]

        all_trees = []
        # 针对(start,end)中的每一个i进行切分，也就是求G(i),判断左右是否有节点，通过start和end比较
        for i in range(start,end+1):
            # 左子树
            left_trees = new_trees(start,i-1)
            # 右子树
            right_trees = new_trees(i+1,end)
            
            for left in left_trees:
                for right in right_trees:
                    tree = TreeNode(i)
                    tree.left = left
                    tree.right = right
                    all_trees.append(tree)


        # print(all_trees)
        # 注：每次递归进入的子树的all_trees都是不一样的。可以通过打印print()查看控制台的输出，这样更容易理解具体的思路。
        return all_trees

    return new_trees(1,n)

treelist = generateTrees(3)

'''
list1 = PrintTree(treelist[1])
print(list1)
'''
# 这里打印的是二叉树存储地址