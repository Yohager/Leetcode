class UFS():
    def __init__(self):
        self.fathers = []
        self.ranks = []
        self.counts = 0
    def initialize(self,n):
        for i in  range(n):
            self.fathers.append(i)
            self.ranks.append(1)
        self.counts = n
    def find(self,x):
        if self.fathers[x] == x:
            return x
        else:
            self.fathers[x] = self.find(self.fathers[x])
            return self.fathers[x]
    def union(self,x,y):
        fx,fy = self.find(x),self.find(y)
        if self.ranks[fx] <= self.ranks[fy]:
            self.fathers[fx] = fy
            self.counts -= 1
        else:
            self.fathers[fy] = fx
            self.counts -= 1
        if self.ranks[fx] == self.ranks[fy] and fx != fy:
            self.ranks[fy] += 1
    def connect(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        edges = []
        ufs1 = UFS()
        ufs1.initialize(total)
        for i in range(m):
            for j in range(n):
                # n * i + j
                idx = i * n + j
                if (i < n-1):
                    edges.append([i*n+j,(i+1)*n+j,max(grid[i][j],grid[i+1][j])])
                if (j < n-1):
                    edges.append([i*n+j,i*n+j+1,max(grid[i][j],grid[i][j+1])])
        edges.sort(key=lambda x:x[-1])
        for e in edges:
            ufs1.union(e[0],e[1])
            if ufs1.connect(0,n*m-1):
                return e[-1]
        return 0









