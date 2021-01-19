class UFS():
    def __init__(self,n):
        self.n = n
        self.ranks = [1]*n
        self.fathers = list(range(n))
    
    def find(self,x):
        if self.fathers[x] == x:
            return x
        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]
    
    def union(self,x,y):
        father_x,father_y = self.find(x),self.find(y)
        if father_x == father_y:
            return False
        if self.ranks[father_x] < self.ranks[father_y]:
            father_x,father_y = father_y, father_x
        self.ranks[father_x] += self.ranks[father_y]
        self.fathers[father_y] = father_x
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x,y : abs(points[x][0]-points[y][0]) + abs(points[x][1]-points[y][1])
        edges = []
        n = len(points)
        #构建完全图
        for i in range(n):
            for j in range(i+1,n):
                edges.append((dist(i,j),i,j))
        edges.sort()

        tmp_ufs = UFS(n)
        ans,counts = 0,0
        for l,x,y in edges:
            if tmp_ufs.union(x,y):
                ans += l
                counts += 1
            if counts == n:
                break
        return ans
