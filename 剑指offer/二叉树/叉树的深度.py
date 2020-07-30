"""
剑指 Offer 55 - I. 二叉树的深度
leetcode 104


输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof

思路, 递归+深度优先 (先序遍历，中序遍历，后序遍历)  
    递归+广度优先

"""

# 递归+先序遍历
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 后序遍历
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def bfs_maxDepth(root):
    if not root:
        return 0
    queue, res = deque(), 0
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res += 1
    
    return res

def bfs_maxDepth2(root):
    if not root:
        return 0
    queue, depths = deque(), 0
    count, nextCount = 0, 1
    queue.append(root)

    while queue:
        count += 1
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if count == nextCount:
            nextCount = len(queue)
            count = 0
            depths += 1
