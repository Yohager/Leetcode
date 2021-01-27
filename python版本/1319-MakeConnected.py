from collections import defaultdict
class UFS():
    def __init__(self):
        self.father = defaultdict(int)
        self.rank = []
    
    #初始化这个并查集，每个人单独作为一个部分
    def Initialize(self,n):
        for i in range(n):
            self.father[i] = i
            self.rank.append(1)
    
    def FindElem(self,x):
        if self.father[x] == x:
            return x
        else:
            return self.FindElem(self.father[x])
    
    def MergeElem(self,x,y):
        self.father[self.FindElem(x)] = self.FindElem(y)
    
    def FindElemCompressPath(self,x):
        if self.father[x] == x:
            return x
        else:
            self.father[x] = self.FindElemCompressPath(self.father[x])
            return self.father[x]
    
    def MergeElemWithRank(self,x,y):
        fa_x,fa_y = self.FindElemCompressPath(x),self.FindElemCompressPath(y)
        if self.rank[fa_x] <= self.rank[fa_y]:
            self.father[fa_x] = fa_y
        
        else:
            self.father[fa_y] = fa_x
        
        if self.rank[fa_x] == self.rank[fa_y] and fa_x != fa_y:
            self.rank[fa_y] += 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        counts = len(connections)
        #如果nodes的数量多于edges那么显然不可能连接所有nodes
        if n - counts > 1:
            return -1
        ufs1 = UFS()
        #初始化集合
        ufs1.Initialize(n)
        #将已有的连边加起来
        for i,j in connections:
            ufs1.MergeElemWithRank(i,j)
        #下面看哪些nodes可达，哪些不可达，多少不可达就表示需要改多少条edge
        res = -1
        for k in range(n):
            if ufs1.FindElemCompressPath(k) == k:
                res += 1
        return res
