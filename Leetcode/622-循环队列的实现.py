"""
https://leetcode-cn.com/problems/design-circular-queue/

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

"""

class BaseCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int):
        if self.count == self.capacity:
            return False 
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True
    
    def deQueue(self):
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        reutrn True

    def Front(self):
        """
        Get the front item from the queue
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self):
        """
        Get the last item from the queue
        """
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self):
        """
        Check whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity



class ThreadSafeCQueue(BaseCircularQueue):
    def __init__(self, k: int):
        self.queueLock = Lock()
        super(ThreadSafeCQueue, self).__init__(k)

    def enQueue(self, val: int):
        with self.queueLock:
            if self.count == self.capacity:
                return False

            self.queue[(self.headIndex + self.count) % self.capacity] = val
            self.count += 1

        return True

    def deQueue(self):
        with self.queueLock:
            if self.count == 0:
                return False
            self.headIndex = (self.headIndex + 1) % self.capacity
            self.count -= 1
        
        return True


    
class Node:
    def __init__(self, value, nextNode=None):
        self.val = value
        self.next = nextNode


class BaseCirQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int):
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True
    
    def deQueue(self):
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True
    
    def Front(self):
        """
        Get the front item from the queue
        """
        if self.count == 0:
            return -1
        return self.head.val
    
    def Rear:
        """
        Get the last item from the queue.
        """
        if self.count == 0:
            return -1

        return self.tail.value

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


