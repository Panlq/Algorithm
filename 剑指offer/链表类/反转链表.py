"""
剑指offer： P113
Q:输入一个链表的头结点，反转该链表并输出反转后链表的头结点
思路：
使用三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点。
在遍历的时候，做当前结点的尾结点和前一个结点的替换，当变换到最后一个节点的时候 
当前节点指向的就是尾节点，也就是翻转后的头节点
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        prevNode = None
        curNode = pHead
        nextNode = None
        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        return prevNode
