from gc import collect


import collections

class MonotonicQueue:
    def __init__(self) -> None:
        self.q = collections.deque()
    
    def push(self,val):
        while self.q and val > self.q[-1]:
            self.q.pop()
        self.q.append(val)
    
    def top(self):
        return self.q[0]
    
    def pop(self,val):
        if self.top() == val:
            self.q.popleft() 
        
        