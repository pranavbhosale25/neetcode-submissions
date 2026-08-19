class MinStack:
    def __init__(self):
        self.dq = deque()
        self.minq = deque()
        
    def push(self, val: int) -> None:
        self.dq.append(val)
        if not self.minq:
            self.minq.append(val)
        elif val <= self.minq[-1]:
            self.minq.append(val)
        

    def pop(self) -> None:
        top = self.dq[-1]
        if self.dq:
            self.dq.pop()
        if top == self.minq[-1]:
            self.minq.pop()

    def top(self) -> int:
        if self.dq:
            return self.dq[-1]
        else:
            return None
        

    def getMin(self) -> int:
        return self.minq[-1]
        
