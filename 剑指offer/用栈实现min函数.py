# coding=utf8
'''
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
在该栈中，调用min、push及pop的时间复杂度都是O(1)。
'''


class Stack(object):
    def __init__(self):
        self.main_stack =[]
        # 辅助栈，压入最小元素
        self.assist_stack = []
        # 记录栈中的最小元素
        self._min = None

    def min(self):
        return self._min

    def push(self, item):
        self.main_stack.append(item)
        if self._min is None:
            self._min = item
        else:
            if item < self._min:
                self._min = item
        # 将最小的元素压入辅助栈
        self.assist_stack.append(self._min)

    def pop(self):
        if len(self.main_stack) == 0:
            raise Exception("no item")
        elif len(self.main_stack) == 1:
            self.assist_stack.pop()
            self._min = None
            return self.main_stack.pop()
        else:
            self.assist_stack.pop()
            self._min = self.assist_stack[-1]
            return self.main_stack.pop()


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(4)
    s.push(2)
    s.push(1)
    print(s.main_stack)
    print(s.assist_stack)

    print(s.min())
    s.pop()
    s.pop()
    print(s.min())
    s.pop()
    print(s.min())
    s.pop()
    print(s.main_stack)

