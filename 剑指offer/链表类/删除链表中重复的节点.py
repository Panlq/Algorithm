"""
Q:在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
"""


class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


def remove_dups(head):
    """
    已空间换时间
    Time Complexity: O(n)
    space COmplexity: O(n)
    """
    hashset = set()
    prev = Node()
    while head:
        if head.val in hashset:
            prev.next = head.next
        else:
            hashset.add(head.val)
            prev = head
        head = head.next


def remove_dups_without_set(head):
    """
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


def print_linked_list(head):
    string = ""
    while head.next:
        string += head.val + " -> "
        head = head.next
    string += head.val
    print(string)


if __name__ == '__main__':
    a1 = Node("A")
    a2 = Node("A")
    b = Node("B")
    c1 = Node("C")
    d = Node("D")
    c2 = Node("C")
    f = Node("F")
    g = Node("G")

    a1.next = a2
    a2.next = b
    b.next = c1
    c1.next = d
    d.next = c2
    c2.next = f
    f.next = g

    remove_dups(a1)
    print_linked_list(a1)
    remove_dups_wothout_set(a1)
    print_linked_list(a1)