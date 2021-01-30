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
        if self.fathers[x] != x:
            self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]
    
    def union(self,x,y):
        fax,fay = self.find(x), self.find(y)
        if self.ranks[fax] <= self.ranks[fay]:
            self.fathers[fax] = fay
        else:
            self.fathers[fay] = fax 
        if self.ranks[fax] == self.ranks[fay] and fax != fay:
            self.ranks[fay] += 1
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        total = m * n
        edges = []
        for i in range(m):
            for j in range(n):
                nx = i + 1
                ny = j
                if 0 <= nx < m and 0 <= ny < n:
                    d = abs(heights[i][j]-heights[nx][ny])
                    edges.append([i*n+j,nx*n+ny,d])
                nx = i
                ny = j + 1
                if 0 <= nx < m and 0 <= ny < n:
                    d = abs(heights[i][j] - heights[nx][ny])
                    edges.append([i*n+j,nx*n+ny,d])
        edges.sort(key=lambda x:x[-1])
        ans = 0
        ufs1 = UFS()
        ufs1.initialize(total)
        for edge in edges:
            if ufs1.find(0) == ufs1.find(m*n-1):
                break
            x,y,d = edge
            if ufs1.find(x) != ufs1.find(y):
                ufs1.union(x,y)
                ans = max(ans,d)
        return ans
