"""
剑指offer：p107
Q: 输入一个链表，输出该链表中倒数第k个结点。
主要要考虑代码的鲁棒性，需要判断传入参数的合法性。

思路：我们可以定义两个指针。第一个指针从链表的头指针开始遍历向前走k-1，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1，当第一个（走在前面的）指针到达链表的尾结点时，第二个指针（走在后面的）指针正好是倒数第k个结点。

正常思维就是循环求链表的长度，在循环走n-k+1步
如果第一个指针从k-1开始，另一个指针也开始循环的话, 正好走的就是n-k+1步
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        aPoint, bPoint = head, head
        for _ in range(k - 1):
            if aPoint.next:
                aPoint = aPoint.next
            else:
                return None
        while aPoint.next != None:
            aPoint = apaPoint.next
            bPoint = bPoint.next
        return bPoint


# 遍历单向链表再将元素存入 列表中在返回 倒数第k 个元素也可，但是开辟了新空间，不是很好。