class Solution:
    def getMoneyAmount(self, n: int) -> int:
        d = {}
        def dfs(l,r):
            if (l,r) in d:
                return d[(l,r)]
            elif l >= r:
                # 区间不存在或者说只有一个值
                return 0 
            else:
                tmp = float('inf')
                for m in range(l,r+1):
                    tmp = min(tmp,max(dfs(l,m-1),dfs(m+1,r))+m)
            d[(l,r)] = tmp 
            return tmp 
        return dfs(1,n)