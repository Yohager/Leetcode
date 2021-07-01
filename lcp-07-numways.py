class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        dp[0][0] = 1
        #dp[i][j]表示的是第i轮到达第j个人的方案数量
        for i in range(1,k+1):
            for j in relation:
                dp[i][j[1]] += dp[i-1][j[0]]
        return dp[k][n-1]
