"""
Q:
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""

from collections import defaultdict


class RandomListNode(object):
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


# 时间复杂度O(N^2)
def copy_random_pointer_v1(pHead):
    dic = dict()
    m = n = pHead
    # 复制所有节点的label, 存在字典中
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    
    while n:
        # 画图有助于理解, 复制节点的next的和random
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
    
    return dic.get(pHead)


# 时间复杂度 O(N)
def copy_random_pointer_v2(head):
    copy = defaultdict(lambda: RandomListNode(0))
    copy[None] = None
    node = head
    while node:
        copy[node].label = node.Label
        copy[node].next = copy[node.next]
        copy[node].random = copy[node.random]
        node = node.next
    return copy[head]
