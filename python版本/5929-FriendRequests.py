class UFS():
    def __init__(self):
        self.father = defaultdict(int)
        self.rank = []
        self.count = 0
    
    #初始化这个并查集，每个人单独作为一个部分
    def Initialize(self,n):
        for i in range(n):
            self.father[i] = i
            self.rank.append(1)
        self.counts = n
    
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
        fx,fy = self.father[x],self.father[y]
        if fx != fy:
            if self.rank[fx] < self.rank[fy]:
                self.father[fx] = self.father[fy]
                self.rank[fy] += self.rank[fx]
            else:
                self.father[fy] = self.father[fx]
                self.rank[fx] += self.rank[fy]
            self.counts -= 1
            
class Solution:
    def friendRequests(self, n: int, rs: List[List[int]], reqs: List[List[int]]) -> List[bool]:
        ufs = UFS()
        ufs.Initialize(n)
        ans = []
        for req in reqs:
            u,v = req[0], req[1]
            fu,fv = ufs.FindElemCompressPath(u), ufs.FindElemCompressPath(v)
            if fu == fv:
                ans.append(True)
            else:
                flag = True 
                for r in rs:
                    x,y = r[0], r[1]
                    fx,fy = ufs.FindElemCompressPath(x), ufs.FindElemCompressPath(y)
                    if (fx == fu and fy == fv):
                        flag = False 
                    if (fx == fv and fy == fu):
                        flag = False 
                    if not flag:
                        break 
                if flag:
                    ufs.MergeElemWithRank(fu,fv)
                ans.append(flag)
        return ans 
        