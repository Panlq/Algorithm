
"""
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

思路: 二叉树深度优先遍历+替换左右节点
递归退出条件 root is None
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # 替换当前节点的左右子树
        root.left, root.right = root.right, root.left
        # 递归替换当前节点的左子树
        self.invertTree(root.left)
        # 递归替换当前节点的右子树
        self.invertTree(root.right)
        # 返回当前节点
        return root
        