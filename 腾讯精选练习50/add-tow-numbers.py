class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        cursor = dummyHead
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tsum = carry + x + y
            carry = tsum // 10
            cursor.next = ListNode(tsum % 10)
            cursor = cursor.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if carry > 0:
            cursor.next = ListNode(1)
        return dummyHead.next


if __name__ == "__main__":
    a = ListNode(0)
    b = a
    b.next = 45
    print(a.next)
    print(b)
    print(id(b), id(a))

    c = 35
    d = c
    print(id(d), id(c))

    t = "adfsdfsd"
    y = t
    print(id(t), id(y))
    print("-"*50)
    d = dict(name='zhangsan', age=27)
    co = d.copy()
    print(id(d), id(co))
    


    