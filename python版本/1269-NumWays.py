class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        maxlen = min(steps // 2, arrLen - 1)
        dp = [[0] * (maxlen+1) for _ in range(steps+1)]
        dp[steps][0] = 1
        for i in range(steps-1, -1, -1):
            for j in range(min(steps-i,i,maxlen)+1):
                dp[i][j] = (dp[i][j] + dp[i+1][j]) % MOD
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i+1][j-1]) % MOD 
                if j < maxlen:
                    dp[i][j] = (dp[i][j] + dp[i+1][j+1]) % MOD 
        return dp[0][0]