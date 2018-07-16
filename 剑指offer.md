## 剑指offer刷题
[TOC]

### 链表类
1. 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
```python
    # coding=utf-8
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            slef.next = None
    class Soulution(object):
        # 返回从尾部到头部的列表值的序列
        def printListFromTailToHead(self, listNode):
            result = []
            while listNode:
                result.insert(0, listNode.val)
                listNode = listNode.next
            return result
```
2. 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
```python
## 思路双端队列
class Deque():
    def __init__(self):
        """双端队列"""
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(int(node))

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
```


### 二叉树类
1. 剑指四：
> 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。  

思路：了解二叉树的深度优先遍历三种排序规则
- 先序遍历： 根节点-左子树-右子树
- 中序遍历： 左子树-根节点-右子树
- 后序遍历： 左子树-右子树-跟结点
![](./blogimg/binarytree.png)

解题：先序遍历的第一个元素肯定是根节点，在看中序遍历，就可以按照根节点将数组分为左右数组，左边为左子树，右边为右子树。在原来的先序遍历中就可以区别出左子树的元素和右子树的元素，再将新数组当成中序数组，与先序在进行第一步递归，直到子叶  

```python
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
```


### 数组类
1. 数组中第K大的数 (LeetCode 215 Kth Largest Element in an Array)  
思路1：先对数组进行排序，再求解第K个元素  
思路2：使用最小堆，第K大的数即len(q)-k小的元素  
二叉堆：是一棵特殊的完全二叉树，其特点：
    - 二叉树中的所有的父节点的值都不大于/不小于其子节点；
    - 根节点的值必定是所有节点中最小/最大的  
将父节点的值不大于子节点且根节点值最小的称为最小堆，反之称为最大堆。堆是一种高级的数据结构，在python中有相应的模块deapq    

```python
# 排序法
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
# 最小堆
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for i in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heapqpop(heap)
```
