'''
'''

class MinStack:

    def __init__(self):
        self.s = []
        self.smin = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.smin or val<= self.smin[-1]:
            self.smin.append(val)

    def pop(self) -> None:
        x = self.s.pop()
        if x==self.smin[-1]:
            self.smin.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.smin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()