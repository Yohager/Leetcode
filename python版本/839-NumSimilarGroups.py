class UFS():
    def __init__(self):
        self.fathers = []
        self.ranks = []
        self.counts = 0
    
    def initialize(self,n):
        for i in range(n):
            self.fathers.append(i)
            self.ranks.append(1)
        self.counts = n
     
    def find(self,x):
        if self.fathers[x] == x:
            return x
        else:
            return self.find(self.fathers[x])
    def union(self,x,y):
        fx,fy = self.find(x), self.find(y)
        if fx != fy:
            if self.ranks[fx] < self.ranks[fy]:
                self.fathers[fx] = fy
                self.ranks[fy] += self.ranks[fx]
            else:
                self.fathers[fy] = fx
                self.ranks[fx] += self.ranks[fy]
            self.counts -= 1
    def getcounts(self):
        return self.counts
    def Isconnected(self,x,y):
        return self.fathers[x] == self.fathers[y]
        
class Solution:
    def isSimilar(self,x,y):
        nums = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                nums += 1
            if nums > 2:
                return False
        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        ufs1 = UFS()
        ufs1.initialize(n)
        for i in range(n-1):
            for j in range(i+1,n):
                if self.isSimilar(strs[i],strs[j]):
                    ufs1.union(i,j)
        return ufs1.getcounts()
            
