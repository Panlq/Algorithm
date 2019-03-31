"""
数组中第K大的数 (LeetCode 215 Kth Largest Element in an Array)  
思路1：先对数组进行排序，再求解第K个元素, 简单粗暴 
思路2：使用最小堆，第K大的数即len(q)-k小的元素  构建一个最小堆，每次pop根节点，知道堆顶是第K个最大数
二叉堆：是一棵特殊的完全二叉树，其特点：
    - 二叉树中的所有的父节点的值都不大于/不小于其子节点；
    - 根节点的值必定是所有节点中最小/最大的  
将父节点的值不大于子节点且根节点值最小的称为最小堆，反之称为最大堆。堆是一种高级的数据结构，在python中有相应的模块deapq 
"""

import heapq

def sortedFindKthLargest(nums, k):
    nums.sort()
    return nums[-k]



def findKthLargest(array, k):
    heap = []
    for item in array:
        heapq.heappush(heap, item)
    for i in range(len(array) - k):
        heapq.heappop(heap)
    return heapq.heappop(heap)


alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

# result = findKthLargest(alist, 4)
result = sortedFindKthLargest(alist, 4)
print(result)