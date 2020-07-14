"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
如果 pos 是 -1，则在该链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 哈希表
        dic = {}
        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1
                head = head.next

        return False

    def hasCycle2(self, head: ListNode) -> bool:
        # 快慢指针
        slow, fast = head, head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                return False
            if slow == fast:
                return True

        return False