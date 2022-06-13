class Solution:
    def minPathCost(self, g: List[List[int]], mc: List[List[int]]) -> int:
        m,n = len(g[0]), len(g)
        dp = [[inf]*m for _ in range(n)]
        for i in range(m):
            dp[0][i] = g[0][i]
        for i in range(1,n):
            for j in range(m):
                for k in range(m):
                    dp[i][j] = min(dp[i][j],dp[i-1][k]+mc[g[i-1][k]][j]+g[i][j]) 
        print(dp)
        return min(dp[-1])
                    