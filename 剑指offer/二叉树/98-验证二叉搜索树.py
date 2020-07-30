"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
***所有左子树和右子树自身必须也是二叉搜索树***

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree

根据二叉搜索树的性质：(中序遍历： 左子树-根节点-右子树)
思路：进行中序遍历后, 就是一个有序数组, 有序数组的前一个值小于后一个值
"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    pre = float('-inf')
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历的思路, 左子树-跟节点-右子树
        if root == None:
            return True
        # 左子树
        if not self.isValidBST(root.left):
            return False
        # 当前节点
        if root.val <= self.pre:
            return False
        self.pre = root.val

        # 右子树
        return self.isValidBST(root.right)

    def isBST(self, node, lower=float('-inf'), upper=float('inf')):
        # 考虑子树也是一个二叉搜索树，考虑上界和下界
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        return self.isBST(node.left, lower, val) and self.isBST(node.right, val, upper)


if __name__ == '__main__':
    pass