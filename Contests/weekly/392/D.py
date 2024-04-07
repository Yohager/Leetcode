class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        a = self.parent[a]
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return False
        self.parent[pb] = pa
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ufs = UnionFind(n)
        vals = [-1] * n
        ans = []
        for x, y, w in edges:
            ufs.merge(x, y)
        
        for x, y, w in edges:
            vals[ufs.find(x)] &= w
          
        for s,t in query:
            if ufs.find(s) != ufs.find(t):
                ans.append(-1)
            else:
                ans.append(vals[ufs.find(s)] if s != t else 0)
        return ans 
                
                
