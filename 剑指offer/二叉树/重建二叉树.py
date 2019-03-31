"""
Q: 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。 

思路：了解二叉树的深度优先遍历三种排序规则
    - 先序遍历： 根节点-左子树-右子树
    - 中序遍历： 左子树-根节点-右子树
    - 后序遍历： 左子树-右子树-跟结点
二叉树图片: https://i.loli.net/2019/03/31/5ca069456854a.png

解题：先序遍历的第一个元素肯定是根节点，在看中序遍历，就可以按照根节点将数组分为左右数组，左边为左子树，右边为右子树。在原来的先序遍历中就可以区别出左子树的元素和右子树的元素，再将新数组当成中序数组，与先序在进行第一步递归，直到子叶  
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pos = tin.index(pre[0])  # 中序数组中根节点的位置
            root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
            root.right = self.reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
            return root
