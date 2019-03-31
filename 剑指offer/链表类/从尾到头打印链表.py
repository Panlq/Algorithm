"""
Q: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
思路：这种情况下，我们不希望修改原链表的结构。返回一个反序的链表，这就是经典的“后进先出”，我们可以使用栈实现这种顺序。每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后，再从栈顶开始逐个输出结点的值，给一个新的链表结构，这样链表就实现了反转。
"""


class ListNode:
    def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]