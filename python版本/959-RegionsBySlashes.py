class UFS():
    def __init__(self):
        self.fathers = []
        self.counts = 0
    def getcounts(self):
        return self.counts
    #初始化并查集
    def initialize(self,n):
        for i in range(n):
            self.fathers.append(i)
        self.counts = n
    #find函数
    def find(self,x):
        if self.fathers[x] == x:
            return x
        else:
            self.fathers[x] = self.find(self.fathers[x])
            return self.fathers[x]
    #union函数
    def union(self,x,y):
        fx,fy = self.find(x),self.find(y)
        if fx == fy:
            return 
        self.fathers[fy] = fx
        self.counts -= 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = 4 * n * n
        ufs1 = UFS()
        ufs1.initialize(size)
        for i in range(n):
            for j in range(n):
                idx = 4 * (i * n + j)
                if grid[i][j] == '/':
                    #此时合并03和12
                    ufs1.union(idx,idx+3)
                    ufs1.union(idx+1,idx+2)
                elif grid[i][j] == '\\':
                    ufs1.union(idx,idx+1)
                    ufs1.union(idx+2,idx+3)
                else:
                    ufs1.union(idx,idx+1)
                    ufs1.union(idx+1,idx+2)
                    ufs1.union(idx+2,idx+3)
                #下面还需要考虑单元格之间的合并性
                #可以向下或者向右合并
                if (j+1 < n):
                    ufs1.union(idx+1,4*(i*n+j+1)+3)
                if (i+1 < n):
                    ufs1.union(idx+2,4*((i+1)*n+j))
        return ufs1.getcounts()