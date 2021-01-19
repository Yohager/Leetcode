'''
并查集算法实现
'''
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

if __name__ == "__main__":
    n = 6
    m = 5
    p =3
    relatives = [[1,2],[1,5],[3,4],[5,2],[1,3]]
    judge = [[1,4],[2,3],[5,6]]
    ufs_test = UFS()
    ufs_test.Initialize(n)
    for x,y in relatives:
        ufs_test.MergeElem(x,y)
    
    ans = []
    for j,k in  judge:
        if ufs_test.FindElem(j) == ufs_test.FindElem(k):
            ans.append(True)
        else:
            ans.append(False)

    print(ans)