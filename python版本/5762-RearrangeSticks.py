class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        '''
        dp的思路：以1，2，3，4，5为例子
        考虑长度为1的木棍，这个棍子能够被看到，则一定是放在第一个，然后加上后面四个的一种排列
        如果不能够被看到，那么一定是放在后面四个位置上的其中一位
        dp[i][j]表示如果共有i个棍子的情况下，能够看到j个情况的总数
        dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
        '''
        if n == k:
            return 1
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[1][1] = 1
        for i in range(2,n+1):
            tmp = min(k,i)
            for j in range(1,tmp+1):
                dp[i][j] = (dp[i-1][j-1] + (i-1) * dp[i-1][j]) % MOD
        return dp[n][k]
