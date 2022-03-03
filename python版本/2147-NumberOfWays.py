class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007
        idxs = []
        n = len(corridor)
        for i in range(n):
            if corridor[i] == 'S':
                idxs.append(i)
        if len(idxs) == 2:
            return 1
        elif len(idxs) == 0:
            return 0
        elif len(idxs) % 2 != 0:
            return 0 
        else:
            # nums = len(idxs) // 2 # 需要放入共计nums个屏风
            res = 1
            for j in range(1,len(idxs)-1,2):
                res *= (idxs[j+1]-idxs[j])
            return int(res % MOD)
            
            
            