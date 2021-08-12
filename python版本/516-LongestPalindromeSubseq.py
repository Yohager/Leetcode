class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        dp[i][j]表示s[i:j]之间的最长的回文子序列的长度
        转移方程为：
        如果i,j两个位置的值相等的话，则：
        dp[i][j] = dp[i+1][j-1] + 2
        如果不相等的话：
        dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        '''
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for x in range(n):
            dp[x][x] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]