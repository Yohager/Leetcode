from collections import defaultdict
import faulthandler
from math import ceil
from re import L 

class UFS:
    def __init__(self) -> None:
        self.fathers = defaultdict(int)
        self.rank = []
        self.count = 0 
    
    def Initialize(self,n):
        for i in range(n):
            self.fathers[i] = i 
            self.rank.append(1)
        self.counts = n 
    
    def FindElem(self,x):
        if self.fathers[x] == x:
            return x 
        else:
            return self.FindElem(self.fathers[x])
        
    def MergeElem(self,x,y):
        self.fathers[self.FindElem(x)] = self.FindElem(y)
    
    '''
    带路径压缩的寻找元素优化
    带按秩合并的合并优化
    '''
    def FindElemCompressPath(self,x):
        if self.fathers[x] == x:
            return x 
        else:
            self.fathers[x] = self.FindElemCompressPath(self.fathers[x])
            return self.fathers[x]
    
    def MergeElemWithRank(self,x,y):
        fx,fy = self.fathers[x], self.fathers[y]
        if fx != fy:
            if self.rank[fx] < self.rank[fy]:
                self.fathers[fx] = self.fathers[fy]
                self.rank[fy] += self.rank[fx]
            else:
                self.fathers[fy] = self.fathers[fx]
                self.rank[fx] += self.rank[fy]
            self.count += 1
    

if __name__ == "__main__":
    n = 5 # there are four nodes 
    des = [[1,2],[3,4],[1,4]]
    checklist = [[1,4],[1,3],[2,3]]
    ufs1 = UFS()
    ufs1.Initialize(n)
    for x,y in des:
        ufs1.MergeElem(x,y)
    for p,q in checklist:
        if ufs1.FindElem(p) == ufs1.FindElem(q):
            print(True)
        else:
            print(False)
    