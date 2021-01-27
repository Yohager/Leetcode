class UFS():
    def __init__(self):
        self.fathers = []
        self.ranks = []
        self.counts = 0
        self.nums = 0
    
    def getcounts(self):
        return self.counts
    
    def initialize(self,n):
        for i in range(n):
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
        fax,fay = self.find(x),self.find(y)
        if fax == fay:
            self.nums += 1  
            return False
        else:        
            if self.ranks[fax] < self.ranks[fay]:
                self.fathers[fax] = fay
            elif self.ranks[fay] > self.ranks[fax]:
                self.fathers[fay] = fax
            else:
                self.fathers[fax] = fay
                self.ranks[fay] += 1
            self.counts -= 1
    # def union(self,x,y):
    #     fx,fy = self.find(x),self.find(y)
    #     if fx == fy:
    #         return 
    #     self.fathers[fy] = fx
    #     self.counts -= 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        edgeset1 = []
        edgeset2 = []
        #修改nodes的编号使得其从0开始进行编号
        # for tmp in edges:
        #     tmp[1] -= 1
        #     tmp[2] -= 1
        n = n + 1
        ufs1 = UFS()
        ufs2 = UFS()
        ufs1.initialize(n)
        ufs2.initialize(n)
        #对应于Alice和Bob构建他们对应的边集
        for edge in edges:
            if edge[0] == 1:
                edgeset1.append(edge)
            elif edge[0] == 2:
                edgeset2.append(edge)
            else:
                ufs1.union(edge[1],edge[2])
                ufs2.union(edge[1],edge[2])
        
        x = ufs1.nums

        for j in edgeset1:
            ufs1.union(j[1],j[2])
        for k in edgeset2:
            ufs2.union(k[1],k[2])
        
        # if ufs1.getcounts() > 2 or ufs2.getcounts() > 2:
        #     return -1

        print(ufs1.counts,ufs2.getcounts())
        
        return ufs1.nums + ufs2.nums - x


n = 4
arr = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

print(Solution.maxNumEdgesToRemove(Solution,n,arr))