class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        idx2,idx3,idx5 = 0,0,0
        for i in range(1,n):
            dp[i] = min(dp[idx2]*2,dp[idx3]*3,dp[idx5]*5)
            if dp[i] == dp[idx2] * 2:
                idx2 += 1
            if dp[i] == dp[idx3] * 3:
                idx3 += 1
            if dp[i] == dp[idx5] * 5:
                idx5 += 1
        return dp[-1]