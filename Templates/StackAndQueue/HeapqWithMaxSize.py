import heapq
from collections import *
import bisect 

class MaxHeap():
    def __init__(self,size) -> None:
        self.q = []
        self.length = size 
        heapq.heapify(self.q)
    
    def add(self,val):
        if len(self.q) < self.length:
            heapq.heappush(self.q,val)
        else:
            heapq.heappushpop(self.q,val)
    
    def getTop(self):
        return heapq.nlargest(self.length,self.q)

class MaxHeap2():
    def __init__(self,size):
        self.q = deque([],maxlen=size)
        self.length = len(self.q)
    
    def add(self,val):
        if self.length < self.q.maxlen or val < self.q[-1]:
            if self.length == self.q.maxlen:
                self.q.popleft()
            bisect.insort_left(self.q,val)
            self.length += 1
    
    