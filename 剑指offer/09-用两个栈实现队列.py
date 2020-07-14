class CQueue:
    def __init__(self):
        self.A , self.B = [], []

    def appendTail(self, value: int):
        self.A.append(value)

    def deleteHead(self):
        if self.B:
            return self.B.pop()
        elif not self.A:
            return - 1
        while self.A:
            self.B.append(self.A.pop())
        
        return self.B.pop()

    
if __name__ == '__main__':
    dq = CQueue()
    dq.appendTail(3)
    dq.appendTail(2)
    dq.appendTail(1)
    dq.deleteHead()
    dq.deleteHead()